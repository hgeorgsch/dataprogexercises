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

![](client-server-http.png)

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
