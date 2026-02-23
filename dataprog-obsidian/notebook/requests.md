---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.18.1
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

# Web API

<!-- #region -->
# Hva er et API?

For å forstå hvordan moderne programvare samhandler, må vi først definere begrepet **API**, som står for *Application Programming Interface* (på norsk: programmeringsgrensesnitt). Et API fungerer som en kontrakt eller en bruksanvisning som beskriver nøyaktig hvordan en programvarekomponent skal brukes av en annen. Det definerer hvilke funksjoner som er tilgjengelige, hvilke data man må sende inn, og hva man kan forvente å få i retur.

Når vi jobber lokalt i Python, møter vi API-er hele tiden uten at vi nødvendigvis tenker over det. Når du bruker et bibliotek som `pandas` eller `numpy`, er det bibliotekets API som bestemmer hvilke kommandoer du må skrive for å for eksempel lese en CSV-fil eller beregne et gjennomsnitt.

---

## Web API:

Et **Web API** er en spesialisert form for API som gjør ressurser tilgjengelige over internett. I stedet for at koden din snakker med en pakke som ligger installert på din egen maskin, sender programmet ditt en forespørsel over nettverket til en ekstern server.


I vår kontekst dreier dette seg om en strukturert måte for kommunikasjon mellom to parter:
1. **Klienten:** Dette er din egen maskin eller Python-programmet du skriver.
2. **Serveren:** Dette er en ekstern datakilde, for eksempel hos Statistisk sentralbyrå (SSB) eller Eurostat.

Gjennom Web API-et kan klienten "be om" spesifikke datasett, og serveren svarer med å sende de forespurte dataene tilbake i et format maskinen forstår (ofte JSON eller XML). Dette gjør at vi kan automatisere henting av data uten å måtte laste ned filer manuelt via en nettleser.

---


Når en bruker Web API-er går man fra å jobbe med statiske filer på egen PC, til å kunne hente og behandle enorme mengder oppdatert data fra hele verden.
<!-- #endregion -->

<!-- #region -->
## REST API: Standardarkitekturen for datautveksling

Selv om "Web API" er et bredt begrep, vil du i de aller fleste tilfeller støte på en spesiell og svært populær variant som kalles et **REST API** (eller *RESTful API*). 

REST er et akronym for *REpresentational State Transfer*. Selv om navnet kan virke tungt og teknisk, beskriver det i bunn og grunn et sett med standardiserte kjøreregler for hvordan klienter og servere skal utveksle informasjon over internett. Når et API er bygget i henhold til disse reglene, sier vi at det er *RESTful*. 

For oss som skal skrive Python-kode for å hente data, innebærer dette at vi forholder oss til fire sentrale prinsipper:

### 1. HTTP-metoder (Verbet)
Når klienten (vårt program) ber om en ressurs, skjer dette gjennom standardiserte HTTP-metoder. Metoden fungerer som et "verb" som forteller serveren hva vi ønsker å gjøre. Den desidert vanligste for dataanalyse er **GET**, som betyr "hent disse dataene til meg". Hvis vi derimot skulle sende eller opprette ny data på serveren, ville vi brukt metoden **POST**.

### 2. Endepunkter (Substantivet)
I et REST API har hver unike ressurs sin helt egen nettadresse (URL). I API-terminologi kaller vi en slik adresse for et **endepunkt** (*endpoint*). Endepunktet fungerer som et "substantiv" i forespørselen. Vil vi for eksempel ha befolkningsstatistikk fra SSB, retter vi Python-koden vår mot det spesifikke endepunktet (URL-en) som representerer akkurat dette datasettet.

![](https://images.ctfassets.net/vwq10xzbe6iz/5sBH4Agl614xM7exeLsTo7/9e84dce01735f155911e611c42c9793f/rest-api.png)


### 3. Representasjon av data
Når vi "treffer" et endepunkt med en forespørsel, sender ikke serveren hele den underliggende databasen sin til oss. I stedet genererer den en *representasjon* av de forespurte dataene der og da. I moderne REST API-er er denne representasjonen nesten utelukkende formatert som **JSON** (JavaScript Object Notation). Dette er et strukturert tekstformat som er svært enkelt for datamaskiner å parse, og som Python elegant kan gjøre om til lister, ordbøker eller en Pandas DataFrame.

### 4. Tilstandsløshet (Statelessness)
Et av de mest fundamentale prinsippene i REST, er at kommunikasjonen er **tilstandsløs** (*stateless*). Det betyr at serveren *ikke* husker deg fra forrige forespørsel. Det finnes ingen "pågående sesjon", og du er ikke vedvarende innlogget mellom handlinger. Fordi serveren er "glemsk", må *hver eneste forespørsel* du sender inneholde absolutt alt webserveren trenger
<!-- #endregion -->

## Bruk
For å ta i bruk et REST-API bør vi altså kunne litt om:
* HTTP-protokollen
* Oppbygging av en URL
* JSON-formatet, og jsonstat-formatet med `pyjstat`
* Bruk av `requests` biblioteket til å sende http-spørringer

Når det er på plass kan man ta i bruk mange kule ressurser!
Se feks:
* [https://free-apis.github.io/#/categories](https://free-apis.github.io/#/categories)
* [https://github.com/public-apis/public-apis](https://github.com/public-apis/public-apis)


# requests, json og pyjstat


*Vi antar vi kan litt om http-protokollen og hvordan en URL er bygget opp*



### Sende http-spørring med `requests`

For å kunne sende en httpspørring må vi:
* Vite hvilken tjener vi skal sende det til (eks www.ssb.no)
* Vite *hvor* på tjeneren ressursen vi spør etter er
* Vite om det skal være en GET/PUT/POST spørring
* Vite hvilke parametre som skal være med
* Vite om vi skal sende med noe i headeren til spørringen (API-nøkler, brukernavn og passord etc)

Når vi vet dette, kan `requests` sette sammen spørringen og sende den på riktig vis



<!-- #region -->
### Bruk av `requests`

Under er typisk gang i bruk av requests -- ikke kjørbar kode, men en cheat-sheet

```python
import requests

url = #tjener OG sti på tjeneren
parametere = # Dictionary med parameternavn: verdi
headere = #Dictionary med headere felt: verdi
data_payload = #Data som skal sendes ved -- i tilfelle POST

response = requests.get(url, params = parametere, headers = headere) # GET request
response = requests.post(url, params = parametere, headers = headere, data=data_payload) # POST request

print("statuskode", response.status_code)
print("Headere (til respons)", response.headers)
print("responstype:", response.headers['content-type']) # Dersom tilgjengerlig (feks application/json)

## Data kan leses på flere måer
data = response.json() #Dersom responsdata er i jsonformat
data = response.text #Tegnkoding ordnes som regel automatisk
data = response.content.decode("latin1") # Dersom det er feil med automatisk tegnkoding
```


<!-- #endregion -->

Vi bruker altså `requests.get` eller `requests.post` til å sende spørringen,
mens headere og url-parametere lages som dictionaries og gis som argumenter (`params=`, `headers=`) til `requests.get`/`requests.post`. Biblioteket kan nå ta seg av å bygge den faktiske http-spørringer som ser noe slikt ut:


![](http-form.png)

<!-- #region -->
Etter å ha sendt spørringen ordner `requests` bibiloteket et responseobjekt til oss
som vi ofte kaller `res` eller `response`. Tabellen under gir en oversikt over attributter og metoder til dette responsobjektet



| Egenskap / Metode | Type | Beskrivelse | Eksempel på bruk |
| :--- | :--- | :--- | :--- |
| `.status_code` | Attributt | Viser HTTP-statuskoden fra serveren (f.eks. `200` for OK, eller `404` for Ikke funnet). | `print(res.status_code)` |
| `.ok` | Attributt | En praktisk snarvei som er `True` hvis forespørselen var vellykket (statuskode 200–299). | `if res.ok:` |
| `.raise_for_status()`| Metode | **Viktig for feilhåndtering!** Krasjer programmet (kaster en feil) hvis forespørselen feilet. Slik unngår du at koden kjører videre med tomme data. | `res.raise_for_status()` |
| `.url` | Attributt | Viser den endelige URL-en som ble sendt (inkludert alt du la til i `params`). Utrolig nyttig for feilsøking! | `print(res.url)` |
| `.headers` | Attributt | En dictionary med metadata som *serveren* sendte tilbake. Kan inneholde info om datamatype eller gjenværende API-kvote. | `print(res.headers["Content-Type"])` |
| `.json()` | Metode | Gjør automatisk serverens JSON-tekst om til en ferdig Python-dictionary (deserialisering). | `data = res.json()` |
| `.text` | Attributt | Returnerer serverens svar som rå, ubehandlet tekst. Veldig nyttig for feilsøking hvis `.json()` feiler! | `print(res.text)` |

<!-- #endregion -->

### Httpbin.org

- httpbin er en webressurs vi kan bruke til å teste spørringene våres
- Den tar imot GET/POST spørringer, og sender tilbake data om hva den mottok

```python
import requests
```

```python

url_httpbin = "https://httpbin.org/get" #url for å test GET-spørringer
response = requests.get(url_httpbin)
print("Statuskode", response.status_code)
print("Svarheadere", response.headers)

#Data om spørringen som ble sendt legges ved som svar
data = response.json()  #Henter ut data -- mer om json lenger nede
print("Parametre", data["args"])
print("Headere:", data["headers"])
```

::: {hint}
Dersom du lar en dictionary-variabel «henge» på slutten av en kodecelle
vil den bli vist med litt penere formatering enn om du bruker `print`
:::


Vi kan legge ved parametre og headere for å sjekke hvordan spørringer vi sender ser ut:

```python
url_httpbin = "https://httpbin.org/post" #url for å test POST-spørringer

mine_parametre = {"query": "Donald duck ruler", 
                  "lang": "EN", 
                  "min": "parameter"}
mine_headere = {"User-Agent": "Superscript-requests-tester1.1"}

data_payload = """ 
HTTP står ved døra: «Hei, er du klar?»
med metode i lomma og URI på svar.
GET henter fredelig, POST sier «jeg sender!»
PUT gjør det helt om, mens PATCH bare endrer.

En klient på tur med en socket så fin,
den banker på server’n: «Kan jeg slippe inn?»
Et request går av gårde i linje og bånd,
med headers som merkelapp, «Content-Type» på hånd.
"""

response = requests.post(url_httpbin,
                       params = mine_parametre, 
                       headers=mine_headere,
                       data = data_payload)
print("Statuskode", response.status_code)
print("Svarheadere", response.headers)

#Data om spørringen som ble sendt legges ved som svar
data = response.json() #Henter ut data -- mer om json lenger nede
print("Parametre jeg brukte", data["args"])
print("Header om user-agent:", data["headers"]["User-Agent"])
print("Data jeg sendte", data["data"])
```

::: {admonition} Oppgave
Sjekk at du kan bruke `requests`-biblioteket til å sende `GET`og `POST` spørringer til:
 - httpbin.org/get
 - httpbin.org/post

Legg ved noen egne parametere, headere og, til `POST`, legg ved noe data og sjekk:
1. Hvilken URL bygde requests? Kjenner du igjen parameterene du brukte?
2. Hvilke headere ble sendt? Finner du din egen header?
3. Hvilke data mottok httpbin? sjekk at du finner de igjen i svaret fra httpbin
:::

<!-- #region -->
# Introduksjon til JSON:

Når vi bruker et Web API til å hente data fra en server, trenger vi et felles format for å utveksle denne informasjonen. Serveren vet nemlig ingenting om Python, og klienten (vårt program) vet kanskje ikke hvordan serverens database er bygget opp. Løsningen på dette problemet er **JSON**.

JSON står for *JavaScript Object Notation*. Til tross for navnet er formatet i dag fullstendig uavhengig av programmeringsspråk. Det har blitt den absolutte standarden for datautveksling på internett, og har i stor grad erstattet eldre, mer tungvinte formater som XML. 

Grunner til at JSON er så populært i Web API-er:
* **Det er lettvektig:** Det tar minimalt med plass å sende over nettverket.
* **Det er lesbart:** Formatet består av ren tekst bygget opp av nøkkel-verdi-par (akkurat som vi er vant til), noe som gjør det lett for mennesker å lese og forstå.
* **Det er enkelt å parse:** Nærmest alle moderne programmeringsspråk har innebygde verktøy for å lynraskt konvertere JSON til brukbare datastrukturer.

---

## Den viktige forskjellen: JSON vs. Python Dictionary

Når du ser på et stykke JSON-data, vil du umiddelbart legge merke til at det ser slående likt ut som en Python *dictionary* (`dict`). Begge bruker krøllparenteser `{}` for å samle data, og begge bruker et system med nøkler og verdier: `{"navn": "Ola", "alder": 30}`. 

Likevel er det en fundamental og svært viktig forskjell du må forstå:

* **En Python `dict`** er et levende dataobjekt som eksisterer i datamaskinens minne (RAM) mens programmet ditt kjører. Den lar deg gjøre oppslag, endre verdier og kjøre metoder som `.keys()`.
* **JSON** er utelukkende et tekstformat (en *string* i Python). Det er bare en lang rekke med bokstaver og tegn som er strukturert på en spesiell måte. Du kan ikke slå opp verdier direkte i en JSON-streng.



Når data skal reise over internett, kan vi ikke sende et Python-objekt. Vi må først gjøre objektet om til ren tekst (JSON). Denne prosessen kalles *serialisering*. Når teksten kommer frem til oss fra API-et, må vi oversette teksten tilbake til en dictionary for å kunne jobbe med den. Dette kalles *deserialisering*.

---

## Bruk nettleser til å utforske JSON

Før du begynner å skrive kode for å hente data fra et ukjent API, er det lurt å undersøke hvordan dataene faktisk er strukturert. Siden JSON er ren tekst, kan du ofte bare lime inn nettadressen (API-endepunktet) direkte i adressefeltet i nettleseren din. Når du er ferdig å bygge spørringen med `requests` kan du også hente ut url med `response.url` og lime denne inn i nettleseren.

Nettlesere har ofte en innebygd, utmerket JSON-visning som automatisk fargekoder dataene og lar deg klappe sammen (kollapse) og utvide lister og objekter. Dersom det mangler, finnes det som regel utvidelser eller «plugins» hjelper deg med dette (feks JSON viewer for chrome). Poenget er å finne ut hvilke "nøkler" du skal slå opp i i python for å finne dataene du er interessert i.

---

## Slik bruker vi `json`-biblioteket i Python

Python har et innebygd bibliotek for å håndtere oversettelsen mellom tekst (JSON) og Python-objekter (dict/list). Biblioteket heter rett og slett `json`.

De to viktigste funksjonene du må kjenne til er:
* `json.loads()`: (Load String) Tar en JSON-tekststreng og gjør den om til en Python-dictionary.
* `json.dumps()`: (Dump String) Tar en Python-dictionary og gjør den om til en JSON-tekststreng.

Disse har også fil-varianter
* `json.load()`: Tar en JSON-fil og gjør den om til en Python-dictionary.
* `json.dump()`: (Dump) Tar en Python-dictionary og en fil, og «dumper» dictionary til en json-fil.

Her er et praktisk eksempel på hvordan det fungerer:
<!-- #endregion -->

```python
import json

# 1. Vi mottar litt data som ren tekst (JSON) fra et tenkt API
json_tekst = '{"navn": "Ada Lovelace", "yrke": "Programmerer", "alder": 36}'

# Sjekker vi typen nå, vil Python si at dette bare er en string (str)
print(type(json_tekst)) 

# 2. Vi oversetter (deserialiserer) teksten til en Python dictionary
bruker_data = json.loads(json_tekst)

# Nå er det en dict, og vi kan hente ut spesifikke verdier!
print(bruker_data["navn"])  # Output: Ada Lovelace

# 3. Motsatt vei: Hvis vi har en dict vi vil sende til en server
min_dict = {"språk": "Python", "versjon": 3.12}

# Vi gjør den om til tekst (serialisering)
ny_json_tekst = json.dumps(min_dict)
print(ny_json_tekst)

```

Dersom vi har et stort og komplisert dataobjekt vi prøver å finne fram i,
kan det være lurt å skrive det ut til en json-fil og åpne den i nettleseren:

```python
#Vi antar at "bruker_data er stor og komplisert

#Skriv til fil:
with open("test_data.json", "w") as file:
    json.dump(bruker_data, file) #Skriv bruker_data til filen "test_data.json"

#For å lese inn fra fil:
with open("test_data.json", "r") as file:
    data_lest_fra_fil = json.load(file)

print(data_lest_fra_fil)
```

<!-- #region -->
### JSON og `requests`

Siden json-formatet er såpass utbredt og vanlig, er bruken innebygd i `requests` biblioteket.
Dersom vi får tilbake data i json-format må vi «deserialisere» til et python-objekt:
```python
response = requests.get(data_url_endepunkt)
data = json.loads(response.text)
```
JSON-parsingen er også innebygd:
```python
response = requests.get(data_url_endepunkt)
data = response.json()
```
Skal vi sende data med `requests` og `POST` ville vi gjort det slik:
```python
data = {"mine_data": [1,2,3,43,5,6,7]}
data_payload = json.dumps(data)
response = requests.post(url_post, data = data_payload)
```
Her serialiserer vi dataene våre med `json.dumps()` og sender tekstrengen som data. Dette har ogås en innebygd variant:
```python
data = {"mine_data": [1,2,3,43,5,6,7]}
response = requests.post(url_post, json=data)
```


<!-- #endregion -->

### EKSEMPEL VÆR

- Vi ønsker å hente inn værmeldingen de neste 7 dagene i Ålesund
- Se også video: [Hente data programmatisk](https://ntnu.cloud.panopto.eu/Panopto/Pages/Viewer.aspx?id=631c2496-15aa-4cf8-adc5-b3ed00d06e16)
* Vi leser dokumentasjon av en gratis værtjeneste på nett: [https://open-meteo.com/en/docs#location_and_time](https://open-meteo.com/en/docs#location_and_time)
  


```python
import requests


#Lengde og breddegrad Ålesund
#https://www.latlong.net/place/lesund-norway-17299.html
lat = 62.472229
long = 6.149482

url = "https://api.open-meteo.com/v1/forecast"
parametre = {"latitude": lat, "longitude": long, "hourly": "temperature_2m"}

#Send http-spørring
response = requests.get(url, params=parametre)
print("URL bygget av requests (kan åpnes i nettleser)", response.url)
```

::: {hint}
For å få oversikt og kontroll på JSON-data kan vi:
1. Printe ut «nøkler» og gå gjennom strukturen med `data_dict.keys()` og `for` løkker
2. Skrive ut til fil med `json.dump()` og utforske med, feks, nettleser
3. Åpne url bygget av requests direkte i nettleser: `print(response.url)` 
:::

```python
import pandas as pd
import json


data = response.json()

# Les igjennom med print + keys osv .. evt skriv til fil og les i nettleser
with open("weather_data.json", 'w') as file:
    json.dump(data, file)

df = pd.DataFrame(data["hourly"])
df["time"] = pd.to_datetime(df["time"])

df.set_index("time").plot()
#Plot temperatur
```

::: {admonition} Oppgave
Les dokumentasjonen til open-meteo, og se om du klarer å gjøre et kall til web-apien etter noe data. Eksempelvis:

- Finn en lengde- breddegrad feks her: [](https://www.gps-coordinates.net/)
- Hent ut for *daglig værvariabel* (totalt regn, uv-index, solnedgang osv)
- Les ut aktuell data fra og importer til pandas

Lagre gjerne responsen fra open-meteo til en json-fil og undersøk den i nettleseren din

:::


### EKSEMPEL: Eurostat

* Det er flere måter å hente data fra eurostat programmatisk
* Vi anbefaler: [denne](https://ec.europa.eu/eurostat/web/user-guides/data-browser/api-data-access/api-detailed-guidelines/api-statistics)
* Her får vi data på jsonstat2 format

Vi henter data med en URL av følgende format:
![https://ec.europa.eu/eurostat/documents/19009692/20123432/structure-rest-request.png/0164d56d-495a-94ec-638d-1af93be0062d?t=1728057499783](https://ec.europa.eu/eurostat/documents/19009692/20123432/structure-rest-request.png/0164d56d-495a-94ec-638d-1af93be0062d?t=1728057499783)

```python
from pyjstat import pyjstat


#Vis dataset --> tec00033
url = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/tec00033"
parametre = {"format": "JSON", "lang": "EN"}

response = requests.get(url, params=parametre)
```

```python
print("Statuskode", response.status_code)
print("Headere", response.headers)
```

# JSON-stat
> Vi skal se nøyere på bruk av eurostat sitt webapi, vi konsentrerer oss nå om *formatet* på dataene.

Alt ser greit ut - og eurostat har sendt oss dataene i json_stat format.
JSON-stat er et format spesielt for statistikk hvor dataene er lagt i en flerdimensjonal «kube» i stedet for «flate tabeller». Metadata skilles fra tallverdier og vi får en komprimert plasseffektiv struktur (Vi slepper å gjenta «Ålesund kommune, K-150» e.l. for hvert datapunkt) i en maskinvennlig standard. Det at standarden er lett å lese og lagre for en datamaskin, betyr *IKKE* at det er lett for oss mennesker å lese dataene - og det er ikke tilfelle

Det anbefales på det sterkeste å bruke biblioteket `pyjstat` for å lese inn til et dataframe

```python
#!pip install pyjstat
```

<!-- #region -->
## Bruk `pyjstat`

Installer `pyjstat` med `pip install pyjstat` feks ved å kommentere inn og kjøre cellen over.
Pyjstat biblioteket har en egen dataset-type for dataene, og vi leser først inn json_stat dataene våres hit. Dette kan vi gjøre via. requests, en json-fil eller faktisk direktre fra en URL (med begresninger):
```python
url = "https://url.com/til/noe/data"
response = requests.get(url)
dataset = pyjstat.Dataset.read(response.text)
```
Eller rett fra url:
```python
url = "https://url.com/til/noe/data"
dataset = pyjstat.Dataset.read(url)
```

Deretter skriver vi til et dataframe med
```
dataframe = dataset.write("dataframe")
```

<!-- #endregion -->

Dataene fra eurostat kan vi nå lese til pandas og plotte:

```python
#data = response.json() #IKKE til jsonstat
data = response.text #Jsonstat (pyjstat) vil ha råtekst

# Les først data til et pyjstat-dataset
dataset = pyjstat.Dataset.read(data) 

#Skriv så pyjstat datasettet til pandas dataframe
df = dataset.write("dataframe")
df["Time frequency"].unique() # Kun 1 verdi
df["Statistical information"].unique()# Kun 1 verdi
df["Unit of measure"].unique()# Kun 1 verdi
df["Currency"].unique()
df["Time"] = pd.to_datetime(df["Time"])
df_pivot = df.pivot(columns="Currency", index="Time", values="value")

df_pivot[["Norwegian krone", "US dollar"]].plot()
```

`pyjstat` sin "dataset"-type lar oss hente ut noe fornuftig data som forsvinner når vi skriver det til et pandas dataframe:

```python
label = dataset["label"]
kilde = dataset["source"]
dato = dataset["updated"]

print("Data fra", kilde, "oppdatert ", dato, "med tittel: \n", label)
```

::: {admonition} Oppgave
Finn et dataset på [](https://ec.europa.eu/eurostat/web/main/data/database) og se om du får lastet det inn i pandas via `requests` og `pyjstat`. 
:::
