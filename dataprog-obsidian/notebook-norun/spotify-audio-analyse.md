---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.18.1
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
import requests, json
import pandas as pd
import matplotlib.pyplot as plt
```

# WebAPI-eksempel: Audio-analyse og Pandas

## Mål for leksjonen
Nå som vi har lært å autentisere oss med *OAuth* og forstår hvordan API-et fungerer, er det på tide å samle inn ekte data.

I denne leksjonen skal vi:
1. Hente inn alle spillelister fra kontoen vår.
2. Hente inn alle sangene fra disse spillelistene.
3. Organisere all dataen i en strukturert tabell med **Pandas**.
4. Hente inn «audio features» (musikkegenskaper) for sangene via tjenesten Reccobeats.
5. Klargjøre datasettet slik at det kan brukes til maskinlæring (klyngeanalyse) senere i kurset.

::: {admonition} API-er endrer seg! (Plattformrisiko)
:class: note dropdown

Høsten 2024 stengte Spotify brått ned muligheten for å hente ut *Audio Features* fra deres offisielle API. Tusenvis av apper sluttet å fungere over natten. Dette er et klassisk eksempel på **plattformrisiko** – faren ved å gjøre forretningsmodellen sin 100 % avhengig av en annen aktør. For å omgå dette problemet gjør vi som virkelige utviklere: Vi finner en alternativ rute ("workaround") og bruker en tredjepartstjeneste for å hente akkurat disse variablene: **Reccobeats**
:::

---

## 0. Støttefunksjoner og autentisering

I forrige video lærte vi å bytte inn koder og lagre tilgangsnøklene våre i filen `"spotify_tokens.json"`. 

Når vi nå skal hente store mengder data, kommer vi til å sende *mange* spørringer til API-et. For å slippe å skrive den samme `requests`-koden om og om igjen, leser vi først inn nøklene våre, og deretter samler vi logikken vår i tre **støttefunksjoner**:

```{code-cell} ipython3
with open("spotify_tokens.json", "r") as file:
    tokens = json.load(file)


def spotify_get(endepunkt, params=None, headers=dict()):
    access_token = tokens["access_token"]
    url_base = "https://api.spotify.com/v1"
    headers["Authorization"] =  f"Bearer {access_token}"
    response = requests.get(url_base+endepunkt, params=params, headers=headers)

    if response.status_code < 300:
        return response.json()
    elif response.status_code == 401:
        print("Token utgått, henter nytt token")
        oppdater_token()
    else:
        print("oida....")
        print(response.text)


def oppdater_token():
    global tokens
    token_url = "https://accounts.spotify.com/api/token"
    header_felt = {"ContentType": "application/x-www-form-urlencoded"}
    client_id = "fd5f36cc0ee14678ae37d086ebaf76b2"
    client_secret = "152236ac370c43d2b2c4dd47e490c70d"
    data_body = {"grant_type": "refresh_token",
                "refresh_token": tokens["refresh_token"]}
    response = requests.post(token_url, headers=header_felt, auth=(client_id, client_secret), data=data_body)
    response.raise_for_status()
    refresh_old = tokens["refresh_token"]
    tokens = response.json()
    if not "refresh_token" in tokens.keys():
        tokens["refresh_token"] = refresh_old

    with open("spotify_tokens.json", "w") as file:
        json.dump(tokens, file)

    print("nye tokens:", tokens)
    
def testjson(dict_struktur):
    with open("test_file.json", "w") as file:
        json.dump(dict_struktur, file)
```

### **`oppdater_token()`** 
Dette er nøyaktig samme kode som vi brukte for "Refresh Token"-flyten i forrige leksjon, bare pakket inn i en funksjon. Kaller vi på denne, oppdateres nøklene i bakgrunnen og lagres til fil. Legg spesielt merke til
```python
    refresh_old = tokens["refresh_token"]
    tokens = response.json()
    if not "refresh_token" in tokens.keys():
        tokens["refresh_token"] = refresh_old
```
Her lagrer vi først det gamle refresh-tokenet i variabelen refresh_old. Deretter leser vi inn de nye nøklene fra Spotify og sjekker om vi faktisk fikk et nytt refresh-token. Det gjør vi ved å se om "refresh_token" finnes som en nøkkel (key) i tokens-dictionarien. Hvis den ikke finnes, legger vi rett og slett det gamle tokenet tilbake igjen.


### **`spotify_get()`** 

Er vår egen skreddersydde funksjon for å snakke med Spotify. Den baker automatisk inn `access_token` i headeren for oss.
Får vi en `401`-feil (utgått adgangskort), sier den ifra og trigger `oppdater_token()` automatisk.

### **`testjson()`** 

API-svar kan være enorme og uoversiktlige. Denne lille funksjonen dumper dataene til en lokal fil, slik at vi enkelt kan åpne den og studere datastrukturen i ro og mak. Jupyter-lab har god støtte for å lese json-filer

::: {admonition} En liten teknisk merknad til koden
:class: tip dropdown

Hvis `spotify_get` får en `401`-feil, kaller den på `oppdater_token()`. Bare vær obs på at selve funksjonen ikke *prøver på nytt* automatisk etter at tokenet er oppdatert. Hvis du får "Token utgått" når du kjører en kodecelle senere, må du bare kjøre den cellen én gang til for at spørringen skal gå gjennom med de ferske nøklene. Dette er helt vanlig og greit i Jupyter!
:::

+++

## 1: Hente spillelister


Det første vi må gjøre, er å be Spotify om en oversikt over alle spillelistene. For å gjøre dette, bruker vi endepunktet `/me/playlists`: [Offisiell dokumentasjon](https://developer.spotify.com/documentation/web-api/reference/get-a-list-of-current-users-playlists)

Vi bruker støttefunksjonen `spotify_get` for å sende spørringen. Som standard gir Spotify oss bare 20 spillelister tilbake. Siden vi ønsker et så stort datasett som mulig, legger vi med parameteren limit=50, som er det maksimale Spotify tillater per spørring. Dersom der var flere enn 50 tilgjengelige spillelister, måtte vi ha sendt flere spørringer til endepunktet og brukt parameteren `offset` til å spesifisere hvor i listen av spillelister spotify skal begynne å sende resultatene fra

```{code-cell} ipython3
# Henter spillelister og lagrer json-svaret i en variabel
playlist_data = spotify_get("/me/playlists", params={"limit": 50})

# Her lønner det seg å kikke på dataene:
testjson(playlist_data)
```

### Fra JSON-kaos til Pandas-tabell

Når vi har hentet dataene, ønsker vi å analysere dem i **Pandas**. Hvis du åpner filen `test_file.json` som vi akkurat lagret, vil du se at dataene fra Spotify er *nøstet* (nested). Det betyr at lister og dictionaries ligger inni hverandre.

Hva skjer hvis vi bare prøver å tvinge disse dataene inn i en standard Pandas DataFrame?

```{code-cell} ipython3
df = pd.DataFrame(playlist_data["items"]) # Ikke helt å anbefale
df.head()
```

::: {admonition} Ser du problemet?
:class: warning

Hvis du ser på kolonnene `owner` eller `tracks` i tabellen over, ser du at de ikke inneholder enkle verdier som tekst eller tall. De inneholder *nye* dictionaries! For eksempel står det `{'display_name': 'Jon', 'href': ...}` i owner-kolonnen. Dette er et mareritt å analysere. Vi vil at `display_name` skal ha sin *egen* kolonne!
:::

### Løsningen: `pd.json_normalize`

For å fikse dette, har Pandas en innebygd småmagisk funksjon kalt `json_normalize`. Den graver seg inn i JSON-strukturen og «flater ut» dataene for oss. Kolonnenavnene får da punktum i seg, som `owner.display_name`.

```{code-cell} ipython3
pd.json_normalize(playlist_data, record_path="items", meta="limit").head()
```

`record_path` "peker" på en liste som inneholder radene i dataframet, og `meta` angir felter "utenfor" listen vi vil ha med i radene.

I eksempelet under peker `record_path` på en listen "inne i listen", og `meta` er en liste med stier til data vi vil ha med i tillegg

```{code-cell} ipython3
pd.json_normalize(playlist_data, record_path=["items", "images"], meta=[["items", "name"], ["limit"], ["items", "id"]]).head()
```

Vi trenger egentlig bare å flate ut "hovedlisten" og velge ut kolonnene vi vil beholde.
Det kan kreve en del graving, eller man kan liste ut alle kolonnene med 
```python
print(df.columns)
```
og kopiere kolonnelisten inn igjen i en kodecelle og fjerne/beholde etter høve

```{code-cell} ipython3
df_playlist = pd.json_normalize(playlist_data, record_path="items")
df_playlist = df_playlist[['id','name','owner.display_name','items.total']]
df_playlist
```



+++

## 2. Hente sanger fra spillelistene

Nå har vi ID-ene til spillelistene våre, og vi skal bruke dem til å hente ut selve sangene. For å gjøre dette bruker vi API-endepunktet `/playlists/{playlist_id}`. Dette endepunktet gir oss all informasjon om en spesifikk spilleliste, inkludert en lang liste med alle sporene (sangene) som ligger i den.

[Spotifys dokumentasjon for dette endepunktet finner du her.](https://developer.spotify.com/documentation/web-api/reference/get-playlist)

I videoen startet vi med å teste dette på én enkelt spilleliste for å se hvordan dataene så ut. Siden informasjonen om *hvilken artist* som har laget sangen ligger utrolig dypt begravet i JSON-svaret, forsøkte vi først å bruke `json_normalize` for å grave oss helt ned i ett og samme kall:

```{code-cell} ipython3
test_param = "0f7KdfesxJoSiV9WiGwkz0"

data = spotify_get(f"/playlists/{test_param}")

#Vi må undersøke denne strukturen
testjson(data)
```

Vi kan forsøke å grave oss helt ned i "artists"-listen som ligger helt nederst. Vi må alltid ende opp i en liste, og fordi sanger ofte har flere skapere eller utøvere er dette feltet alltid en liste inne i listen med sanger i spillelisten. Vi kan deretter bruke `meta` feltet til å gi stien til alle feltene over "artist"-listen som vi vil ha med

```{code-cell} ipython3
pd.json_normalize(data, record_path=["items", "items", "item", "artists"], 
                  meta=[
                      ["name"],["items","items", "item", "album", "name"],
                      ["items", "items", "item", "album", "id"]
                  ], 
                  meta_prefix="playlist_").head()

#Kunne fortsatt -- men tungvint
```



::: {admonition} Hvorfor ikke gjøre alt på én gang?
:class: caution dropdown

Som vist i videoen, kan vi teknisk sett bruke `json_normalize` for å grave oss helt ned til artistene i ett gigantisk jafs:
`pd.json_normalize(data, record_path=["items", "items", "item", "artists"], meta=[...])`
Men dette blir utrolig uoversiktlig! Stiene blir enormt lange, det er lett å skrive feil, og koden blir umulig å lese. Vi velger heller en steg-for-steg-tilnærming med standard Pandas-verktøy.
:::

### Steg-for-steg datavask på testdataene

I stedet for å gjøre alt i `json_normalize`, graver vi oss bare "halvveis" ned til selve sangen. Deretter bruker vi to smarte Pandas-funksjoner for å rydde opp i resten:

1. **`explode()`:** Veldig ofte har en sang *flere* artister. Da ligger artistene som en liste inni en av cellene i regnearket. `.explode()` tar denne cellen og "eksploderer" den til flere rader – én ny rad for hver artist.
2. **`map(lambda x: ...)`:** Etter eksplosjonen ligger artistnavnet inni en liten ordbok (dictionary) i cellen. Vi bruker `.map()` og en lynrask, navnløs funksjon (`lambda`) for å hente ut akkurat den verdien vi vil ha.

```{code-cell} ipython3
# 1. Flater ut JSON ned til sang-nivå, og henter med navn og ID på selve spillelisten
df_test = pd.json_normalize(data, record_path=["items", "items"], meta=[["name"], ["id"]])

# 2. Kaster kolonner vi ikke trenger for å gjøre tabellen oversiktlig (bygg gjerne med df_test.columns)
kol_behold = ['item.album.id', 'item.album.name', 'item.artists', 'item.id', 'item.name', 'name', 'id']
df_test = df_test[kol_behold]

# 3. Magien! Vi 'eksploderer' sanger med flere artister til flere rader
df_test = df_test.explode("item.artists")

# 4. Plukker ut navn og ID fra artist-ordboken inni cellen
df_test["artist"] = df_test["item.artists"].map(lambda x: x["name"])
df_test["artist_id"] = df_test["item.artists"].map(lambda x: x["id"])

# 5. Rydder i kolonnerekkefølgen og fjerner den gamle ordbok-kolonnen
kol_behold = ["name", "id", "artist", "artist_id", "item.album.name", "item.album.id", "item.name", "item.id"]
df_test = df_test[kol_behold]

# 6. Gir kolonnene pene, norske og lettleselige navn
df_test = df_test.rename(columns={
    "name": "spilleliste", 
    "id": "spilleliste_id",
    "item.album.name": "album", 
    "item.album.id": "album_id", 
    "item.name": "sang", 
    "item.id": "sang_id"
})

# Sjekker at alt ser perfekt ut for test-listen vår!
df_test.head()
```

::: {admonition} Hva i all verden er en lambda-funksjon?
:class: tip dropdown

I koden over brukte vi plutselig ordet `lambda`. En lambda-funksjon er rett og slett en bitteliten, navnløs "bruk-og-kast"-funksjon som skrives på én enkelt linje. 

Vanligvis bygger vi funksjoner med `def funksjonsnavn(x):` (slik vi gjorde med `hent_sanger`), spesielt når vi skal bruke dem mange ganger. Men av og til trenger vi bare en lynkjapp operasjon akkurat her og nå – for eksempel for å rydde opp inni en Pandas-kolonne med `.map()`.

La oss bryte ned koden vår: `lambda x: x["name"]`
1. **`lambda`**: Forteller Python at "her kommer en mini-funksjon".
2. **`x`**: Er inputen (det vi dytter inn). Siden vi bruker `.map()`, vil `x` være innholdet i cellen (i vårt tilfelle en liten dictionary, f.eks. `{'id': '123', 'name': 'Vulfpeck'}`).
3. **`: x["name"]`**: Er det funksjonen skal returnere (spytte ut igjen).

Kort fortalt sier koden til Pandas: *"Gå gjennom hver eneste celle i denne kolonnen. For hver celle (x), slå opp i ordboken og gi meg kun verdien som hører til nøkkelen 'name'."*
:::


### Fra testkode til gjenbrukbar funksjon

Dette fungerte jo strålende! Tabellen vår er nå ryddig og helt perfekt for analyse. 

For å kunne gjøre nøyaktig denne operasjonen for *alle* spillelistene våre, pakker vi hele koden over inn i en funksjon som vi kaller `hent_sanger()`. Denne funksjonen tar imot en spilleliste-ID, henter dataene, vasker dem akkurat slik vi gjorde over, og returnerer den ferdige tabellen.

```{code-cell} ipython3
def hent_sanger(playlist_id):
    # Henter rådata fra API-et
    data = spotify_get(f"/playlists/{playlist_id}")
    
    # Kjører nøyaktig samme vaske-rutine som vi testet over
    df_sanger = pd.json_normalize(data, record_path=["items", "items"], meta=[["name"], ["id"]])
    
    kol_behold = ['item.album.id', 'item.album.name', 'item.artists', 'item.id', 'item.name', 'name', 'id']
    df_sanger = df_sanger[kol_behold]
    
    df_sanger = df_sanger.explode("item.artists")
    df_sanger["artist"] = df_sanger["item.artists"].map(lambda x: x["name"])
    df_sanger["artist_id"] = df_sanger["item.artists"].map(lambda x: x["id"])
    
    kol_behold = ["name", "id", "artist", "artist_id", "item.album.name", "item.album.id", "item.name", "item.id"]
    df_sanger = df_sanger[kol_behold]
    
    df_sanger = df_sanger.rename(columns={
        "name": "spilleliste", 
        "id": "spilleliste_id",
        "item.album.name": "album", 
        "item.album.id": "album_id", 
        "item.name": "sang", 
        "item.id": "sang_id"
    })
    
    return df_sanger
```

### Kjøre funksjonen for alle spillelister

Nå gjenstår bare sjarmøretappen. Vi bruker funksjonen vi nettopp bygget til å hente og vaske sangene for *hver eneste* spilleliste vi fant i Steg 1. 

Vi bruker en listekomprehensjon (en superrask Python-løkke skrevet på én linje) for å bygge en liste med mange små Pandas-tabeller (én for hver spilleliste). Til slutt bruker vi `pd.concat()` for å lime alle disse små tabellene sammen til én gigantisk master-tabell!

::: {admonition} Lær av min feil i videoen: Pass på indeksene!
:class: tip dropdown

Hvis du ser nøye på videodemonstrasjonen, vil du legge merke til at jeg glemte å skrive `ignore_index=True` inni `pd.concat()` første gang jeg kjørte koden. Det førte til litt hodebry og nøsting i etterkant! 

**Hva skjedde egentlig der?**
Når vi limer sammen mange små tabeller, har hver enkelt lille tabell sin egen rad-indeks som starter på 0 (for eksempel `0, 1, 2, 3`). Hvis vi bare limer dem blindt oppå hverandre, vil den store master-tabellen vår få en indeks som repeterer seg om og om igjen: `0, 1, 2, 0, 1, 2, 3, 0, 1...`. 

Dette skaper skikkelig trøbbel for oss senere hvis vi prøver å slå opp på "rad nummer 2", og Pandas plutselig finner *femti* forskjellige rader som alle har indeks 2! Ved å legge til `ignore_index=True` ber vi rett og slett Pandas om å kaste de gamle indeksene, og heller lage en helt ny, ren og sammenhengende tallrekke (`0, 1, 2, 3, 4...`) for den ferdige tabellen vår.
:::

```{code-cell} ipython3
# Kaller funksjonen vår for hver eneste ID vi har i spilleliste-tabellen
spillelister = [hent_sanger(pid) for pid in df_playlist["id"]]

df_sanger = pd.concat(spillelister, ignore_index=True)

df_sanger.head()
```

```{code-cell} ipython3

```

## 3. Hente Audio Features med Reccobeats

Som vi snakket om i starten, har vi lyst til å gjøre en maskinlæringsanalyse (klyngeanalyse) av musikksmaken vår. For å få til det, trenger vi dypere innsikt i *hvordan* sangene faktisk høres ut. Er de triste og akustiske? Er de kjappe, energiske og "dansbare"? 

Dette kalles **Audio Features**.  Siden Spotify stengte sitt eget API for dette, bruker vi en tredjepartstjeneste som heter [**Reccobeats**](https://reccobeats.com/docs/apis/reccobeats-api). De lar oss sende inn en liste med sang-ID-er, og returnerer disse matematiske musikkegenskapene for oss: [Get multiple audio features](https://reccobeats.com/docs/apis/get-audio-features)

### Steg 3.1: En liten test

Før vi pøser på med hele det store datasettet vårt, gjør vi et lite test-kall med tre sang-ID-er fra tabellen over for å bli kjent med strukturen til Reccobeats.

```{code-cell} ipython3
url_recco = "https://api.reccobeats.com/v1/audio-features"
params = {"ids": ["4X705JSPvEzEUuP0Oe0HoE", "6ER8plW4Mae5d5nSATWPD9", "5WGr8oEBp2RBrorc5ZEx1K"]}
response = requests.get(url_recco, params=params)
data = response.json()

pd.json_normalize(data, record_path="content").drop(columns=["id", "href"])
```

::: {admonition} Vent litt... Hvorfor fikk vi bare 2 rader tilbake?
:class: caution

Hvis du ser på tabellen vi nettopp genererte, ba vi om data for **tre** sanger, men vi fikk bare **to** rader i retur! Hva skjedde med den siste sangen?

Reccobeats er en uavhengig tjeneste. De har analysert millioner av sanger, men de har ikke *absolutt alt*. Hvis en sang er veldig ny, lokal eller litt obskur, mangler de kanskje data på den. Når API-et ikke finner sangen, hopper det bare over den i stedet for å gi en feilmelding. 

Dette betyr at når vi nå skal berike hele datasettet vårt, må vi akseptere at vi kommer til å miste noen sanger på veien fordi de rett og slett mangler analyse-data.
:::

### Steg 3.2: Hente data i porsjoner (Batching)

Nå vet vi at testen fungerer, men vi har en siste utfordring før vi kan kjøre dette på *alle* sangene våre: **Begrensninger i API-et**.

Hvis vi sjekker den offisielle API-dokumentasjonen til Reccobeats, står det svart på hvitt at parameteren for ID-er har en grense: `Possible values: >= 1, <= 40`. Vi kan altså ikke sende tusenvis av ID-er i én og samme spørring, da vil serveren avvise oss umiddelbart. 

Løsningen er å respektere dokumentasjonen og sende ID-ene i "porsjoner" (batches) på maks 40 stykker av gangen. Vi bruker en løkke til å bla oss gjennom hele listen vår, og bygger opp resultatene litt etter litt.

::: {admonition} `get_id`
:class: note
*Reccobeats gir oss en lang lenke (`href`) i stedet for en ren sang-ID i retur. For å kunne koble dataene sammen med Spotify-tabellen vår etterpå, lager vi en liten hjelpefunksjon (`get_id`) som klipper ut selve ID-en fra slutten av denne lenken.*
:::

```{code-cell} ipython3
# Hjelpefunksjon: Klipper opp lenken på hver skråstrek (/) og beholder den aller siste biten ([-1])
def get_id(href_tekst):
    return href_tekst.split("/")[-1]

# Henter ut alle sang-ID-ene fra det store datasettet vårt som en ren liste
sang_ider = list(df_sanger["sang_id"])
lengde = len(sang_ider)

# Her skal vi samle alle de små tabellene vi får tilbake
analyse = []

# Vi looper gjennom listen, og hopper 40 steg frem for hver runde
for i in range(0, lengde, 40):
    # Plukker ut 40 ID-er av gangen (fra i til i+40)
    parameter = {"ids": sang_ider[i:i+40]}
    
    # Henter data fra Reccobeats
    response = requests.get(url_recco, params=parameter)
    response.raise_for_status() # Stopper programmet hvis vi får en nettverksfeil
    data = response.json()
    
    # Flater ut porsjonen med data
    df_temp = pd.json_normalize(data, record_path="content")
    
    # Bruker hjelpefunksjonen vår til å lage en ryddig "sang_id"-kolonne
    df_temp["sang_id"] = df_temp["href"].map(get_id)
    
    # Kaster kolonner som bare skaper rot
    df_temp = df_temp.drop(columns=["id", "href", "isrc"])
    
    # Legger porsjonen til i oppsamlingslisten vår
    analyse.append(df_temp)

# Til slutt: Limer sammen alle porsjonene til én stor tabell
df_analyse = pd.concat(analyse, ignore_index=True)
df_analyse.head()
```

::: {admonition} Hvordan fungerer porsjoneringen? (Slicing)
:class: tip dropdown

I løkken vår bruker vi uttrykket `sang_ider[i:i+40]`. I Python kalles dette for **slicing** (å skjære opp en liste). Det betyr rett og slett *"gi meg alle elementene fra og med posisjon `i`, til (men ikke med) posisjon `i+40`"*.

Siden løkken vår (`range(0, lengde, 40)`) hopper 40 steg av gangen, skjer dette:
* **Første runde:** `i` er 0. Vi henter element 0 til 40 (`sang_ider[0:40]`).
* **Andre runde:** `i` er 40. Vi henter element 40 til 80 (`sang_ider[40:80]`).

**Men hva skjer på slutten?** La oss si du har 105 sanger totalt. I den siste runden vil `i` være 80, og koden ber om `sang_ider[80:120]`. I mange andre programmeringsspråk ville koden krasjet her med en stor feilmelding, siden det ikke finnes 120 sanger! Heldigvis er Python smart. Når den ser at vi ber om mer enn det som finnes, trekker den bare på skuldrene og gir oss det som er igjen (de siste 25 sangene). 
:::

### Steg 3.3: Sy alt sammen (`pd.merge`)

Nå sitter vi med to store tabeller:
1. `df_sanger`: Inneholder artist, tittel og hvilket album sangen kommer fra.
2. `df_analyse`: Inneholder maskinlærings-dataene (danceability, energy, osv.).

For å få det ultimate datasettet, må vi "lime" disse to tabellene sammen side-om-side. I SQL kalles dette en *JOIN*, og i Pandas kaller vi det **`merge`**. Vi bruker kolonnen som finnes i begge tabellene (`sang_id`) som nøkkel.

```{code-cell} ipython3
df = df_sanger.merge(df_analyse, on="sang_id", how="right").drop_duplicates("sang_id")
df.head()
```

::: {admonition} Hvorfor bruker vi `how="right"`?
:class: tip dropdown

Som vi oppdaget i testen vår, fant ikke Reccobeats data på absolutt *alle* sangene våre. Derfor er `df_analyse` kortere enn `df_sanger`. 

Når vi skriver `how="right"`, forteller vi Pandas: *"Bruk tabellen til høyre (`df_analyse`) som fasit. Hvis du finner en sang i `df_sanger` som mangler audio features, bare kast den."* Slik sikrer vi at det ferdige datasettet vårt er 100 % komplett og klart for maskinlæring, uten manglende verdier.
:::

+++

## 4. Den store finalen: Oppsummering og lagring

Nå som vi har et komplett, beriket datasett (`df`), kan vi endelig begynne å utforske dataene! En veldig vanlig måte å starte en analyse på, er å se på oppsummerende statistikk for hver gruppe. Er treningslisten min faktisk mer "energetic" enn leselisten min?

For å finne ut av dette bruker vi Pandas-funksjonen `groupby()`. Den samler alle sangene som hører til samme spilleliste i "bunker". Deretter velger vi ut de matematiske egenskapene vi vil se på, og ber Pandas om en statistisk oppsummering (`.describe()`).

*(`.describe()` gir oss automatisk gjennomsnitt, standardavvik, min- og maksverdier for hver kolonne. Siden den også gir oss en "count"-kolonne som bare viser antall sanger, fjerner vi denne med `.drop()` for å gjøre tabellen litt ryddigere).*

```{code-cell} ipython3
# Grupperer dataene våre per spilleliste
gruppering = df.groupby("spilleliste")

# Velger ut Audio Features-variablene
features = [
    'acousticness', 'danceability', 'energy',
    'instrumentalness', 'key', 'liveness', 'loudness', 'mode',
    'speechiness', 'tempo', 'valence'
]

# Regner ut statistikken, og kaster "count"-kolonnen (som ligger på nivå 1 i overskriften)
df_analyse = gruppering[features].describe().drop("count", axis=1, level=1)

# Tar en titt på spillelisteprofilene våre!
df_analyse
```

### Eksport til CSV (Klar for maskinlæring!)

Gjennom denne leksjonen har vi hentet rådata fra Spotify, vasket det, strukturert det, og beriket det via Reccobeats.

Senere i kurset skal vi bruke nøyaktig disse dataene til å trene en maskinlæringsmodell (klyngeanalyse). Vi kan la algoritmer prøve å finne skjulte mønstre og sjangere i musikksmaken vår. 

For å slippe å kjøre alle disse API-kallene på nytt, lagrer vi det ferdige, sammenslåtte datasettet (`df`) til en helt vanlig CSV-fil.

::: {admonition} Et lite lagringstips
:class: tip dropdown

Når vi eksporterer til CSV med Pandas, bør vi nesten alltid bruke parameteren `index=False`. Hvis vi glemmer denne, vil Pandas lagre radnumrene (`0, 1, 2, 3...`) som en egen, ekstra kolonne i filen. Det skaper bare rot neste gang vi skal lese filen inn igjen!
:::

```{code-cell} ipython3
# Lagrer det komplette datasettet til en lokal fil
df.to_csv("mitt_spotify_datasett.csv", index=False)

print(f"Suksess! Datasettet er lagret. Det inneholder {len(df)} sanger og er klart for maskinlæring.")
```

## 5. Treningsoppgaver: Utforsk dataene dine!

Nå har du bygget et solid datasett og har verktøyene (funksjonene) du trenger for å snakke med Spotify-API-et. Her er tre oppgaver du kan prøve deg på for å teste ferdighetene dine. Åpne en ny kodecelle under hver oppgave og prøv deg frem!

### Finn den ultimate treningslåta (Pandas-filtrering)
Du skal arrangere en treningsøkt og trenger sanger som har høyt tempo og mye energi. 
**Oppgave:** Bruk datasettet vårt (`df`). Filtrer tabellen slik at du kun sitter igjen med sanger som har `energy` større enn 0.85 og `tempo` større enn 120. Sorter deretter resultatet slik at sangen med aller høyest energi havner øverst. Hvilken sang vant?

::: {admonition} Trenger du et hint?
:class: tip dropdown
For å filtrere på flere betingelser samtidig i Pandas, må du pakke hver betingelse inn i parenteser og bruke `&` (og)-tegnet mellom dem: 
`df[(df["kolonne1"] > tall) & (df["kolonne2"] > tall)]`
For å sortere bruker du funksjonen `.sort_values(by="kolonnenavn", ascending=False)`.
:::

---

### Hvilken artist er mest populær? (Pandas GroupBy)
I leksjonen grupperte vi på `spilleliste`. Nå skal vi se på artistene i stedet!
**Oppgave:** Bruk funksjonen `groupby()` på kolonnen `artist`. Finn deretter gjennomsnittet (`.mean()`) av kolonnen `track.popularity` for hver artist. Hvem er de 5 mest populære artistene i datasettet ditt, og hvem er de 5 mest obskure (minst populære)?

::: {admonition} Trenger du et hint?
:class: tip dropdown
Når du har gruppert, kan du plukke ut én spesifikk kolonne og regne gjennomsnittet slik: 
`df.groupby("artist")["track.popularity"].mean()`
Bruk deretter `.nlargest(5)` for å finne toppen, og `.nsmallest(5)` for å finne bunnen.
:::

---
