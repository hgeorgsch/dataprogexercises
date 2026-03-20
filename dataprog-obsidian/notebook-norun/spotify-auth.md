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

# Autentisering og bruk av OAuth2: Spotify

> **Merk:** Å programmere mot et Web API med autentisering er et litt mer avansert tema, spesielt myntet på deg som trenger å kople Python opp mot eksterne plattformer og datakilder. 

Som praktisk eksempel ville **Google Analytics** kanskje vært det mest nærliggende faglig sett. Utfordringen er at Googles systemer krever omfattende oppsett i google cloud console før man kommer i gang. For å fokusere på selve læringen av *OAuth*, bruker vi derfor **Spotify** som et praktisk og lettvint eksempel. 

Prosessen vi går gjennom er standardisert. Har du først lært deg OAuth2 via Spotify, vil metodikken være tilnærmet identisk om du senere skal hente ut regnskapsdata fra [Tripletex](https://developer.tripletex.no/docs/documentation/authentication-and-tokens/), kundedata fra [Salesforce](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/intro_oauth_and_connected_apps.htm), eller trafikktall fra Google Analytics!

### Slik fungerer prosessen:

For å la Python-koden vår snakke med Spotify sitt [Web API](https://developer.spotify.com/documentation/web-api) må vi gjennom tre hovedsteg:

1. **Registrere applikasjonen:** Vi må først logge inn på [Spotify for Developers](https://developer.spotify.com/dashboard) og registrere programmet vårt. Da får vi utdelt en unik ID og en hemmelig nøkkel (`Client ID` og `Client Secret`).
2. **Autorisasjon:** Programmet vårt må be om lov til å handle på vegne av en bruker. Dette gjør vi ved hjelp av [Autorisasjonskode-flyten i OAuth](https://developer.spotify.com/documentation/web-api/tutorials/code-flow). Det er dette som skjer når du får opp et vindu som spør: *"Vil du la denne appen få tilgang til kontoen din?"*
3. **Tilgang (Access Token):** Hvis brukeren godkjenner, får Python-programmet vårt en digital nøkkel kalt *access_token*. Denne nøkkelen inneholder spesifikke tillatelser (*scopes*). Vi legger ved denne nøkkelen i alle forespørsler vi sender til Spotify for å bevise at vi har lov til å hente ut eller endre data.

::: {admonition} **Kreves det Spotify Premium?**
:class: caution
For å hente ut data (søke etter sanger, analysere artister, hente spillelister) trenger du *ikke* Premium. Du trenger kun Premium dersom du vil skrive kode som fjernstyrer avspilleren din (play, pause, bytt sang)
:::

::: {admonition} **Offisiell dokumentasjon**
:class: tip
Om denne guiden blir uklar, eller noe ikke fungerer kan du også prøve å følge den «ofisielle» [how-to guiden](https://developer.spotify.com/documentation/web-api/tutorials/getting-started). Videoene tilknyttet til dette stoffet viser også hvordan vi blar gjennom dokumentasjonen for å finne, instruksjoner og informasjon om hvordan autentiseringen foregår. 
:::

+++

## 1. Registrere en applikasjon

Vi må først logge inn på [Spotify for Developers](https://developer.spotify.com/dashboard) og registrere programmet vårt. Vi trykker på «Create app», og gir applikasjonen et navn og en beskrivelse. Vi legger også til en **`redirect_uri`**. Applikasjonen får nå også tildelt 2 koder, **`client_id`** og **`client_secret`** som vi kopierer 

::: {image} spotify-dashboard.png
:align: center
:::


::: {warning} Du må lage din egen app
Å dele *`client_secret`* slik som i denne tutorialen er ganske fy-fy.
Jeg vil derfor komme til å skifte ut denne koden i etterkant, slik at dere vil måtte følge stegene og lage deres egen applikasjon, til egen spotify-konto om dere ønsker å kjøre kode-eksemplene
:::


## 2. Hente autorisasjonskode


### Bygge lenken for brukertillatelse (Autorisasjon)

Før Python-programmet vårt kan hente ut eller endre data, må vi be brukeren (i dette tilfellet deg selv) om lov. Målet med dette første steget er å generere en spesiell lenke. Når du klikker på denne lenken, sendes du til Spotifys offisielle innloggingsside hvor du kan godkjenne at appen vår får tilgang til kontoen din.

Når vi kontakter Spotify for å bygge denne lenken, krever de at vi legger ved noen spesifikke opplysninger. Her er byggeklossene vi må definere i koden:

* **`client_id`:** Dette er applikasjonens offentlige ID, nesten som et organisasjonsnummer. Den forteller Spotify nøyaktig *hvilken* app (vår kode) som ber om tilgang.
* **`client_secret`:** Dette er applikasjonens passord. Den sendes *ikke* med i lenken vi bygger nå (det ville vært usikkert!), men vi lagrer den i koden fordi vi trenger den i neste steg for å bevise at vi faktisk eier appen.
* **`redirect_uri`:** Dette er "returadressen". Når du har logget inn og trykket "Godkjenn" inne hos Spotify, må Spotify vite hvor de skal sende deg tilbake. Du kan legge til og bruke en av returaddressene i bildet, *https://jonajh.folk.ntnu.no/tmp/authcode.html* har litt ekstra kode som henter ned autorisasjonskoden fra retur urlen, vi anbefaler å bruke denne
* **`scopes`:** Dette er selve *tillatelsene* vi ber om. Et viktig sikkerhetsprinsipp i OAuth er at man kun ber om tilgang til det man faktisk trenger (for eksempel rettighet til å lese spillelister, men ikke endre passordet ditt).

**Hva skjer i koden under?**
Vi bruker biblioteket `requests` til å samle disse variablene og pakke dem pent inn i en URL. Koden `response.url` spytter ut den ferdige lenken. Vi kan da kjøre koden, klikke på lenken som dukker opp, logge inn, og deretter kopiere koden du får i retur.

::: {admonition} Liten sjekk
:class: note

I koden under sender vi faktisk et undødvendig `GET` request, og spotify-serveren vil også «videresende oss».
`response.url` URL-en vi ser under er faktisk addressen vi blir videresendt til – Ser du hvordan den er forskjellig fra URL-en vi forventer at blir bygget?

:::

```{code-cell} ipython3
import requests, json

client_id = "fd5f36cc0ee14678ae37d086ebaf76b2"
client_secret = "152236ac370c43d2b2c4dd47e490c70d"

redir_uri = "https://jonajh.folk.ntnu.no/tmp/authcode.html"

scopes = " ".join([
    "playlist-read-private",
    "playlist-read-collaborative",
    "playlist-modify-public",
    "playlist-modify-private",
    "user-library-read",
    "user-library-modify",
    "user-read-private",
    "user-read-email",
])

auth_url = "https://accounts.spotify.com/authorize"
parametere = {"client_id": client_id,
              "response_type": "code",
              "redirect_uri": redir_uri,
              "scope": scopes
             }


response = requests.get(auth_url, params=parametere)
```

```{code-cell} ipython3
response.url
```

### Hente autorisasjonskode

Etter godkjenning og innlogging sendes du videre til `redirect_uri` addressen vi oppga i dashboard *og* i get-spørringen i forrige celle.
Om alt er i orden kan vi nå hente en kortlevd og en-gangs *`autorisasjonskode`* som fungerer som en kvittering eller hentelapp vi kan bytte inn i *API-koder* kalt *access*- og *refresh*-*tokens*. Vi kopierer denne koden og lagrer den som en tekststreng i en variabel `auth_code`. Brukte du den «anbefalte» uri-en får du bildet under, har du brukt en annen må du kanskje hente denne koden fra addressefeltet som markert (?code=«din_kode»)



::: {image} spotify_authcode.png
:align: center
:::

```{code-cell} ipython3
auth_code = "AQC9kvKMWx9B9kaRyNyB-r-dqcdmqS9JJC5Jpo26r3OFPV_NMe8RbtMxYyDAX_DT5D-sNkjKmvJipBdXIApvluerjca-5rU-x71kO8y2IC8KhzPLgV0lOMC-pgTz9W-33cjzwy-gyVXetnnRPNKg2aGf8iq7WDDAx7F-JU4zE8KNngSywIBv_NwkZ2ZAna-NTRNhcFEZQCq2VQvwG6SNsNzg-GBMSPY5iMaCUuoL_vQDh_yiy8QlHt5wti2M6xdNDL0UCA8buxPzS5EtC2golR3V1yAvAQtWvNnphn0mwXysmVJp_SfOTnBD6VUWlI2JNj0L83l5qbnX7xHlfT-ygzjHMHO7OAvgMsG7-VZpQJk-82a-jZbdVwDwY06BUL1Wak_dCcdi3hjtRIYkxFmzXWsY4cd3A1O0m2U1M71WGNLyTA"
```

## 3. Bytte autorisasjonskode mot et Access Token

Nå har du kopiert autorisasjonskoden. Tenk på denne koden som en midlertidig hentelapp. Hentelappen i seg selv gir oss ikke tilgang til Spotify-dataene, men vi kan *bytte den inn* hos Spotify for å få selve tilgangsnøkkelen: et **Access Token**.

For å gjøre dette byttet, må vi kontakte Spotify sin server igjen. Men denne gangen bruker vi ikke en `GET`-forespørsel (som vi bygget i forrige steg). Siden vi nå skal sende over hemmeligheter og be om en sensitiv digital nøkkel, bruker vi i stedet en *`POST`*-spørring. Da sendes informasjonen trygt skjult i "kroppen" av meldingen, fremfor å ligge åpent i nettadressen.

### Hva skjer i koden?

Når vi bygger denne `POST`-forespørselen med `requests`-biblioteket, sender vi med tre viktige byggeklosser:

* **`parametere` (Payload):** Vi forteller Spotify at vi ønsker å bytte inn en kode (`grant_type`), vi sender med selve hentelappen (`code`), og vi gjentar returadressen (`redirect_uri`) som en ekstra sikkerhetssjekk fra Spotifys side.
* **`header_felt` (Headers):** Dette forteller Spotify sin server *hvordan* vi har formatert dataene våre. `application/x-www-form-urlencoded` er standardmåten å sende inn web-skjemaer på.
* **`auth=(client_id, client_secret)`:** Før Spotify i det hele tatt vil vurdere hentelappen vår, må applikasjonen vår bevise hvem den er. `requests`-biblioteket har en smart innebygd funksjon (`auth`) som automatisk pakker inn og sikrer appens ID og passord for oss. Dette er en del av *OAuth* standarden

::: {admonition} Hvor lenge varer en nøkkel?
:class: note
Et Access Token varer vanligvis bare i 1 time (3600 sekunder). Dette er et viktig sikkerhetsprinsipp! Skulle nøkkelen din komme på avveie, er den ubrukelig etter kort tid. Skal man lage et program som går over lengre tid, må man også lære seg å bruke *Refresh Tokens* for å be om nye nøkler automatisk.
:::

::: {admonition} Om `Content-Type`
:class: tip dropdown
 
Dokumentasjonen spesifiserer også at vi skal sende med headerfeltet `"Content-Type"` med verdi "`application/x-www-form-urlencoded`" som forteller hvordan dataene vi sender med er formatert. Dette burde egentlig `requests`-biblioteket legge til automatisk, men vi gjør det like gjerne eksplisitt siden er beskrevet i dokumentasjonen

:::

```{code-cell} ipython3
token_url = "https://accounts.spotify.com/api/token"

parametere = {"grant_type": "authorization_code",
              "code": auth_code,
              "redirect_uri": redir_uri
             }

header_felt = {"Content-Type": "application/x-www-form-urlencoded"
}

response = requests.post(token_url, headers=header_felt, auth=(client_id, client_secret), data=parametere)

response.raise_for_status()
```

```{code-cell} ipython3
response.json()
```

## Gratulerer!

Da har vi autentisert oss og fått tak i nøkkelen vi trenger for å bruke web-APIet!
Vi lagrer disse dataene i `tokens`, og koden under viser hvordan vi kan lagre og lese de til fil med `json` biblioteket

```{code-cell} ipython3
tokens = response.json()
with open("spotify_tokens.json", "w") as file:
    json.dump(tokens, file)
```

```{code-cell} ipython3
with open("spotify_tokens.json", "r") as file:
    tokens = json.load(file)

tokens
```

## Bruk av API-et og håndtering av utgått nøkkel (Refresh Token)

Nå som vi endelig har tilgangsnøkkelen vår (`access_token`), er det på tide å bruke den! Vi prøver å gjøre et kall til Spotify sitt Web API for å hente ut informasjon om vår egen brukerprofil. Endepunktet for dette er enkelt og greit `/me`. 

For å "autentisere" oss (bevise at vi har lov til å hente dataene), må vi legge tilgangsnøkkelen vår i header-feltet `"Authorization"`. Standarden i OAuth er å sette ordet `Bearer` (bærer) foran selve nøkkelen. Vi forteller serveren: *"Jeg er bæreren av denne nøkkelen"*.

```{code-cell} ipython3
url_me = "https://api.spotify.com/v1/me"

headers = {"Authorization": f"Bearer {tokens['access_token']}"}
response = requests.get(url_me, headers=headers)
response.json()
```

::: {admonition} Vi fikk statuskode 401
:class: caution
Hvis vi kjører koden over med en gammel nøkkel, får vi en `401 Unauthorized`-feil med beskjeden *"The access token expired"*. Dette er en utrolig vanlig feilmelding når man jobber med API-er! Det betyr rett og slett at sikkerhetsvakten i døra hos Spotify sier at adgangskortet ditt har gått ut på dato.
:::

### Nytt adgangskort: Refresh Token

Heldigvis trenger vi ikke å logge inn på Spotify på nytt hver eneste time! Da vi hentet vårt `access_token` i forrige steg, fikk vi samtidig utdelt en annen nøkkel: et **`refresh_token`**. 

Vi kan se på et `refresh_token` som en *langsiktig rammeavtale* (eller en fullmakt), mens et `access_token` er et *midlertidig adgangskort*. 

Rammeavtalen (`refresh_token`) kan ikke brukes til å hente ut data direkte, men den er et kryptografisk bevis på at brukeren en gang i tiden har gitt applikasjonen vår tillatelse. Når det midlertidige adgangskortet utløper av sikkerhetsgrunner, kan programmet vårt automatisk sende inn rammeavtalen til Spotify for å få utstedt et rykende ferskt adgangskort – uten at brukeren trenger å utføre ytterligere autentiseringer. Det er dette som kalles "Refresh-flyten".

La oss bytte inn vårt `refresh_token` for å få et nytt `access_token`:

```{code-cell} ipython3
refresh_url =  "https://accounts.spotify.com/api/token"

post_body = {"grant_type": "refresh_token",
             "refresh_token": tokens["refresh_token"]}

headers = {"Content-Type": "application/x-www-form-urlencoded"}

response = requests.post(refresh_url, data=post_body, headers=headers, auth=(client_id, client_secret))
```

::: {admonition} Gjenkjennelig kode?
:class: note
Når du ser på koden i forrige celle, vil du kanskje kjenne den igjen! Å bytte inn et `refresh_token` gjøres på nøyaktig samme måte som da vi byttet inn autorisasjonskoden i Steg 3. 

Vi sender en `POST`-forespørsel til akkurat den samme webadressen, og appen vår beviser hvem den er på samme måte (`auth=(client_id, client_secret)`). Den eneste forskjellen i "bestillingsskjemaet" vårt (payloaden) er at vi endrer `grant_type` fra `"authorization_code"` til `"refresh_token"`, og sender med rammeavtalen i stedet for den midlertidige hentelappen.
:::

```{code-cell} ipython3
ny_tokens = response.json()

refresh_old = tokens["refresh_token"]
ny_tokens["refresh_token"] = refresh_old

with open("spotify_tokens.json", "w") as file:
    json.dump(ny_tokens, file)

tokens = ny_tokens
```

Vi kan nå lese inn de nye *«adgangskortene»* og lagre de til fil som koden over, og prøve å gjøre et kall til */me* på nytt


::: {admonition} Pass på rammeavtalen din! (Token Rotation)
:class: dropdown caution
En vanlig feil er å skrive kode som *alltid* gjenbruker den gamle rammeavtalen (`refresh_token`). Mange moderne API-er bruker noe som kalles *Token Rotation* av sikkerhetsgrunner. Det betyr at når du ber om et nytt adgangskort, kan serveren av og til gi deg en *helt ny* rammeavtale, og samtidig slette den gamle. 

Hvis du da blindt overskriver den nye rammeavtalen med den gamle variabelen din som i koden over, vil du låse deg selv ute neste gang du prøver å oppdatere nøkkelen! Da må du be brukeren logge inn helt på nytt. 

Vi burde alltid sjekke om API-et ga deg et nytt `refresh_token`. Hvis ja, lagre og bruk det nye. Hvis nei, behold det gamle.

```python
if "refresh_token" in ny_tokens.keys():
    #Vi har fått ny "rammeavtale"
else:
    #Vi tar med gammel rammeavtale videre   
```
:::

```{code-cell} ipython3
url_me = "https://api.spotify.com/v1/me"

headers = {"Authorization": f"Bearer {tokens['access_token']}"}
response = requests.get(url_me, headers=headers)
response.json()
```

## La oss spille musikk!

Som demonstrert i videoen til dette opplegget, kan vi nå bruke det ferske *«adgangskortet»* vårt til å faktisk gjøre noe praktisk. Vi søket opp bass-mesterverket «Dean Town» av Vulfpeck, og spiller den av på Spotify.

Dette gjøres vi i to steg:
1. Først må vi søke i Spotify for å finne sangens unike ID (som Spotify kaller en **URI**): [dokumentasjon](https://developer.spotify.com/documentation/web-api/reference/search)
2. Deretter må vi sende en beskjed til avspilleren din om å sette i gang denne spesifikke sangen: [dokumentasjon](https://developer.spotify.com/documentation/web-api/reference/start-a-users-playback)

::: {admonition} Husk Premium og en aktiv avspiller!
:class: caution
Som nevnt innledningsvis: For å hente data holder det med gratisversjonen, men for å *fjernstyre* avspillingen må kontoen din ha Spotify Premium. Du må i tillegg ha Spotify-appen åpen og aktiv (på PC-en eller mobilen din) for at koden skal ha et sted å spille av musikken.
:::

### Kode

* **Søket (`GET`):** Vi gjør et vanlig søk og sender inn sangtittel og artist i parameteren `q`, og spesifiserer at vi leter etter en sang (`"type": "track"`).
* **Navigere i JSON:** Resultatet vi får tilbake er et ganske stort og sammensatt JSON-dokument (en dictionary i Python). For å finne sangens strekkode (URI), må vi bla oss systematisk innover i resultatet: `data["tracks"]["items"][0]["uri"]`. Dette henter ut URI-en til det *første* treffet i søkelisten.
* **Spille av (`PUT`):** Nå møter vi en ny type HTTP-metode! Mens `GET` henter data og `POST` leverer skjult data, brukes **`PUT`** ofte når vi skal *endre en tilstand* på serveren. Her endrer vi tilstanden på din Spotify-klient fra "stille" til "spiller musikk". Vi pakker inn URI-en i en "body" og sender den avgårde.

Sørg for at Spotify er åpen, kjør koden under, og skru opp volumet!

```{code-cell} ipython3
url_sok = "https://api.spotify.com/v1/search"
parametre = {"q": "dean town vulfpeck", "type": "track"}
headers = {"Authorization": f"Bearer {tokens['access_token']}"}

response = requests.get(url_sok, params=parametre, headers=headers)
```

```{code-cell} ipython3
data = response.json()
dean_town_uri = data["tracks"]["items"][0]["uri"]
```

```{code-cell} ipython3
# Spill av sang
url_play = "https://api.spotify.com/v1/" + "/me/player/play"

body = {"uris": [dean_town_uri]}
headers = {"Authorization": f"Bearer {tokens['access_token']}"}

response = requests.put(url_play, json=body, headers=headers)
response.text
```

:::: {admonition} Oppgaver
:class: note

1. Viktigste oppgave her er å lese gjennom *OAuth* sin *Authorization Code*-flyt på spotify: [getting started](https://developer.spotify.com/documentation/web-api)
2. Følg dette oppsettet, og bruk eksemplene her til å få satt opp og autentisert python :)
3. Se om du kan søke opp spotify sin ID på dine top 5 artister/band
4. Bruk disse ID-ene til å hente informasjon om disse gjennom web-apiet
5. Få oversikt over strukturen og print ut info om dine top 5 

Det skulle ikke være nødvendig med spotiy-premium til disse oppgavene
::: {admonition} Trenger du et hint?
:class: tip dropdown
Koden for selve API-kallet vil se omtrent slik ut:
`sok_data = spotify_get("/search", params={"q": "Ditt Artistnavn", "type": "track", "limit": 10})`
Når du skal normalisere det, prøv: `pd.json_normalize(sok_data, record_path=["tracks", "items"])`
:::


::::
