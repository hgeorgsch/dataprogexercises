---
jupyter:
  jupytext:
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

```python

```

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
