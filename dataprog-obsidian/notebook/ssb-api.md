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

# SSB
SSB er i gang med å lage et nytt grensesnitt for sitt webapi høsten 2025.
Det ser stort sett ut til å være ferdig, men noen støtteverktøy for å bygge spørringer er borte og det hele virker litt vanskelig. Vi ville tippe at SSB vil komme til å lage nye versjoner av tidligere støtteverktøy (API-konsoll) som gjør det enklere å «skreddersy» større og mer kompliserte spørringer.

Vi skal se litt på hvordan ssb sitt webapi er satt sammen, og på noen måter å bruke det på. Vi gjør dette i økende vanskelighetsgrad:
1. Gjør utvalg/filtrer i statistikkbank og bruk ferdig lenke med `GET`
2. Gjør endringer manuelt med `GET`eller `POST` spørring
3. Bygge spørring direkte i pxweb

Ytterligere informasjon om bruk av web-apiet er å finne på ssb sin [brukerveiledning for web-api](https://www.ssb.no/api/pxwebapiv2)



### Spotpris metaller
Vi tar utgangspunkt i tabell 07199, spotpris metaller [](https://www.ssb.no/statbank/table/07199). Letteste måte å hente data programmatisk er å gjøre et utvalg i [statistikkbanken](https://www.ssb.no/statbank/table/07199) og trykke kopiere `GET`-urlen du finner under «Lagre» og «API-spørring» på venstre side. 

Dersom vi velger alle metaller unntatt aluminium, og krysser av for alle måneder, får vi denne `GET`-urlen:
```
url = "https://data.ssb.no/api/pxwebapi/v2/tables/07199/data?lang=no&outputFormat=json-stat2&valuecodes[ContentsCode]=Kopper,Nikkel,Sink,Bly,Gull,Silver&valuecodes[Tid]=*&heading=Tid&stub=ContentsCode"
```


::: {image} lagresporring2_ny.png
:align: center
:width: 500px
:::
Lagre spørring til venstre, velg json-stat, `GET` og kopier.




Denne kan vi nå ganske enkelt bruke til å hente dataene våre inn til pandas:

```python
import requests, json
import pandas as pd
import matplotlib.pyplot as plt
from pyjstat import pyjstat

url = "https://data.ssb.no/api/pxwebapi/v2/tables/07199/data?lang=no&outputFormat=json-stat2&valuecodes[ContentsCode]=Kopper,Nikkel,Sink,Bly,Gull,Silver&valuecodes[Tid]=*&heading=Tid&stub=ContentsCode"

dataset = pyjstat.Dataset.read(url)
df = dataset.write("dataframe")
df

```

::: {admonition} `pyjstat`-tips
:class: tip dropdown

Pyjstat kan hente inn og lese inn json-stat-data direkte fra url.
Du trenger altså ikke alltid å gå veien om å bygge en `GET` spørring med `requests` biblioteket.
Det samme gjelder faktisk `pd.read_csv(url)` dersom du har en direktelenke til en csv-fil.

I begge tilfeller kreves det at vi ikke må legge til egne felter i header eller body (feks. API-nøkler),
da må vi bruke `requests`biblioteket først
:::

Vi velger nå å formatere url-en litt: vi begynner hver parameter på en ny linje ved å bruke `\` som linjebrudd.
Det lar oss kikke litt på de ulike parameterene

```python
url = "https://data.ssb.no/api/pxwebapi/v2/tables/07199/data?\
lang=no&outputFormat=json-stat2\
&valuecodes[ContentsCode]=Kopper,Nikkel,Sink,Bly,Gull,Silver\
&valuecodes[Tid]=*\
&heading=Tid&stub=ContentsCode"

```

Vi har her 2 variabler: Type metall og måned. Type metall er gitt som en kommaseparert liste etter `valueCodes[ContentsCode]=`.
For tid har vi bare et stjernesymbol `*`. Disse parameterene angir filtreringen vi gjorde i statistikkbanken. Dersom vi vil gjøre et annet utvalg kan vi endre på verdiene her. Nedenfor følger en oversikt


### Oversikt over verdi-operatorer i SSB PxWebApi v2

| Operatør | Eksempel | Beskrivelse |
| :--- | :--- | :--- |
| `*` eller `??` | `valueCodes[Tid]=*` | **Alt:** Henter absolutt alle tilgjengelige verdier for variabelen. |
| `kode*` | `valueCodes[Region]=03*` | **Starter med:** Henter alle koder som begynner på spesifisert tekst (f.eks. alle i Oslo). |
| `?` | `valueCodes[Region]=030?` | **Ett tegn:** Erstatter nøyaktig ett tegn (f.eks. henter 0301, 0302). |
| `top(n)` | `valueCodes[Tid]=top(5)` | **Nyeste:** Henter de *n* nyeste (siste) verdiene i listen. |
| `bottom(n)` | `valueCodes[Tid]=bottom(1)` | **Eldste:** Henter de *n* eldste (første) verdiene i listen. |
| `from(kode)` | `valueCodes[Tid]=from(2020)` | **Fra og med:** Henter alle koder fra og med valgt verdi og utover. |
| `range(x, y)` | `valueCodes[Konto]=range(01, 05)` | **Intervall:** Henter alle verdier i et lukket intervall mellom x og y. |
| `,` | `0301, 1103` | **Liste:** Henter spesifikke koder separert med komma. |

```python
# Eksempel: Alle metaller som begynner på "S" og tidsrom fra 90-tallet:
url = "https://data.ssb.no/api/pxwebapi/v2/tables/07199/data?\
lang=no&outputFormat=json-stat2\
&valuecodes[ContentsCode]=S*\
&valuecodes[Tid]=199*\
&heading=Tid&stub=ContentsCode"

#evt &valuecodes[Tid]=199?M??

#vis
dataset = pyjstat.Dataset.read(url)
df = dataset.write("dataframe")
df

```

```python
# Eksempel: Alle metaller, spotpris siden mars 2012
# Eksempel: Alle metaller som begynner på "S" og tidsrom fra 90-tallet:
url = "https://data.ssb.no/api/pxwebapi/v2/tables/07199/data?\
lang=no&outputFormat=json-stat2\
&valuecodes[ContentsCode]=*\
&valuecodes[Tid]=from(2012M03)\
&heading=Tid&stub=ContentsCode"

#vis
dataset = pyjstat.Dataset.read(url)
df = dataset.write("dataframe")
df
```

::: {admonition} Oppgave
:class: note
Se over filtertypene i tabellen over og se om du kan:
- Hente alle metall som slutter på «l» (for Lars)
- Hente spotpris de første 10 månedene i datasettet
- Hente priser i mars på 2000-tallet ved å bruke «?»
:::


## Parse url-spørring
Det er ikke supermoro å jobbe slike lange kompliserte tekststrenger manuelt. Det kan også tenkes at vi trenger å la automatiske prosesser bygge de.
Da kan vi bruke et bibliotek som behandler url-strenger til å dele den ut i parametre og url endepunkt. Vi importerer da modulen `parse` fra `urllib`.
Det lar oss hente ut url-parametrene i en dictionary som python kan tygge på, så bygger vi opp igjen urlen med `requests` biblioteket.

```python
from urllib import parse
url = "https://data.ssb.no/api/pxwebapi/v2/tables/07199/data?\
lang=no&outputFormat=json-stat2\
&valuecodes[ContentsCode]=*\
&valuecodes[Tid]=from(2012M03)\
&heading=Tid&stub=ContentsCode"


#splitte url
url_splittet = parse.urlsplit(url)
url_splittet
```

Parse har her delt ut alle delene av url-en. Vi trenger å slå sammen alt frem til parameterene, og gjøre om parameterene til en `dict`

```python
#hente endepunkt
url_endepunkt = url_splittet.scheme + "://" +  url_splittet.netloc + url_splittet.path

#hente ut parametre med parse_qs
parametre = parse.parse_qs(url_splittet.query)
```

```python
#Endre metaller
parametre["valuecodes[ContentsCode]"] =  ["Nikkel,Sink,Bly,Gull,Silver"]

response = requests.get(url_endepunkt, params=parametre)
response.raise_for_status()
response.url
#URL ser rar ut '[' er feks blitt til %5B
#Dette er url-tegnkoding og blir gjort automatisk av requests
```

Dersom vi vil gi en liste av metaller må vi gi den slik som over. Dersom vi prøver metoden under, vil requests skille ut alle verdiene i listen bak urlparameteren valueCodes[ContentsCode]

```python
params = {"lang": "no", "outputFormat": "json-stat2",
          "valueCodes[ContentsCode]": ["Nikkel", "Sink","Bly","Gull","Silver"], #DETTE BLIR FEIL
          "valueCodes[Tid]": "*"
         }

url = "https://data.ssb.no/api/pxwebapi/v2/tables/07199/data"
response = requests.get(url, params=params)
print("URL:", response.url)
```

```python
dataset = pyjstat.Dataset.read(response.text)
df = dataset.write("dataframe")
df
```

::: {admonition} Oppgave
:class: note
Si du har følgende url:
```
url = "https://data.ssb.no/api/pxwebapi/v2/tables/07199/data?lang=no&outputFormat=json-stat2&valueCodes%5BContentsCode%5D=Nikkel&valueCodes%5BContentsCode%5D=Sink&valueCodes%5BContentsCode%5D=Bly&valueCodes%5BContentsCode%5D=Gull&valueCodes%5BContentsCode%5D=Silver&valueCodes%5BTid%5D=%2A"
```

Prøv å parse den med `urllib` slik som over og hent ut url-parameterene.
Når det er gjort har du bla en liste med metaller ["Aluminium", "Sink", ....] osv.
Prøv å gjøre dette om til en tekststreng med kommaseparerte metaller, feks ["Aluminium,Sink,Kopper"]. Dette er den «korrekte» parameteren du skulle brukt i en spørring til SSB sitt webapi. Til dette kan du lese deg opp på strengfunksjonen `"«sep»".join(«liste med tekst»)`

`.join()` og `.split()` er kjekke å bruke til strengbehandling når man sjonglerer urler og parametre. Bruk disse to funksjonene til å endre:
```
mine_tillatelser = "lese-epost skrive-til-disk hente-format fire-the-missiles"
```
til
```
mine_tillatelser = "lese-epost,skrive-til-disk,hente-format,fire-the-missiles"
```
:::


For store kompliserte spørringer (SSB foreslår over 2100 tegn) må vi bruke en `POST`-spørring – ssb støtter nemlig begge.
I statistikkbanken kan vi velge om vi vil ha get eller post

Velger vi "post" kan vi kopiere ut post-url og en data-payload med utdragene vi må legge ved som data i post-spørringen


::: {image} lagresporring3_ny.png
:align: center
:width: 500px
:::
Lagre spørring til venstre, velg json-stat, `POST` og kopier body og url.


```python
#Hent post
post_url = "https://data.ssb.no/api/pxwebapi/v2/tables/07199/data?lang=no&outputFormat=json-stat2"

#Hent post payload (md json-loads for sikkerhets skyld)
payload ="""{
  "selection": [
    {
      "variableCode": "ContentsCode",
      "valueCodes": [
        "Kopper",
        "Nikkel",
        "Sink",
        "Bly",
        "Gull",
        "Silver"
      ]
    },
    {
      "variableCode": "Tid",
      "valueCodes": [
        "*"
      ]
    }
  ],
  "placement": {
    "heading": [
      "Tid"
    ],
    "stub": [
      "ContentsCode"
    ]
  }
}"""

payload = json.loads(payload)
payload["selection" ]
```

Til en post-spørring må vi altså legge ved noe data, en payload. Denne inneholder eventuelle filtreringer og utdrag vi vil gjøre med samme formatering som tidligere.

```python
#Endre spørring til alle metall
payload["selection"][0]["valueCodes"] = ["*"]

#Endre spørring til siste 24 måneder
payload["selection"][1]["valueCodes"] = ["top(24)"]

#Merk at "*" og top(24) nå må inn i en liste

#Send spørring

```

```python
#Vis data
#response = requests.post(post_url, data = json.dumps(payload), headers={"Content-Type": "application/json"})
response = requests.post(post_url, json=payload)
print("Status", response.status_code)

```

<!-- #region -->
::: {admonition} `JSON` og requests
:class: dropdown tip

`requests`-biblioteket har egne metoder når du sender og mottar JSON-data.

Når du sender data med post brukder du funksjonsargumentet `json=data_body`, i stedet for `data=json.dumps(data_body)`.

Biblioteket tar da av seg å parse/dumpe til gyldig json, og legger automatisk ved headerfeltet:
```python
{"Content-Type": "application/json"}
```

Når du vet du får json-data tilbake, bruker du også egen metode for å lese data:
```python3
data = response.json()

#alternativt
data = json.loads(response.text)
```
requests-biblioteket vet å parse og bruke riktig tegnkoding når du bruker `response.json()` mens, å lese «råteksten» `response.text` kan by på litt problemer
:::
<!-- #endregion -->

```python
dataset = pyjstat.Dataset.read(response.text)
df = dataset.write("dataframe")
df
```

<!-- #region -->
::: {admonition} Oppgave
:class: note
SSBs webapi er spesielt kjekt å bruke for statistikk du ønsker de ferskeste dataene fra.
> Hvilke data fra ssb er mest aktuelle for deg å hente inn jevnlig?

Skriv et lite program som henter inn dette automatisk og gir deg en kjapp oversikt.
Det kan feks gjelde: Konsumprisindeks (14702), arbeidsledighetstall, sykefravær, prisutvikling på bruktboliger, byggekostnadsindekser, BNP, detaljhandelsindeksen, konkursstatistikk eller utenrikshandel.

    
:::
<!-- #endregion -->

### Gjøre alt gjennom pxweb

- Det er også mulig å holde seg helt utenom statistikkbanken på ssb sine vevsider.
- [](https://data.ssb.no/api/pxwebapi/v2/tables/) gir en oversikt over alle tabellene til ssb
- De fleste nettlesere kan faktisk åpne denne URL-en slik at en kan få en oversikt
- Ved å legge ved url-parameteren `query` kan vi søke i tabellene

```python
#Hent tabeller
url = "https://data.ssb.no/api/pxwebapi/v2/tables?lang=no"

response = requests.get(url)
data = response.json()
```

```python
# Print tabeller
for tabell in data["tables"]:
    print(tabell["label"])
```

URL til neste side med resultater finnes under "page"->"links"

```python
# Vis lenker
data["page"]["links"]
```

```python
#Hent neste side
url = data["page"]["links"][0]["href"]

response = requests.get(url)
data = response.json()
```

```python
#Vis tabeller
for tabell in data["tables"]:
    print(tabell["label"])
```

### Mer heavy metal 
Vi kan prøve å finnne og hente ut spotprisdataene våres ved å søke og bla i pxweb sitt api. Merk at lenkene her lar seg åpne i nettleseren - det er en god måte å lete i json-strukturene

```python
# Ved å legge ved en query parameter gjør vi et søk i tabellene :)

url = "https://data.ssb.no/api/pxwebapi/v2/tables?lang=no"

parametre = {"query": "spotpris"}

response = requests.get(url, params=parametre)
response.raise_for_status()
data = response.json()

```

::: {admonition} Søke i tabeller
:class: tip
Se punkt 1. i ssb sin [veiledning](https://www.ssb.no/api/pxwebapiv2) til pxweb, hvor eksempler på søk etter tabell gis.
Vi kan filtrere søket vårt, feks ved å begrense det til kun tittelen: `{"query": "title:spotpris"}`,  og der er eksempler på å begrense dato og tidsintervall bruke trunkering med `*` med flere. 
:::

```python
# Vis tabelltreff, og finn spotpris metaller

# Dersom vi ikke har lenke, men vil se på jsondata:
with open("testdata.json", "w") as file:
    json.dump(data,file)
    
```

```python
# Vi har funnet tabellen vår:
treff = data["tables"][0]
treff.keys()

```

```python
# Lagre lenker, metadata og data og hent metadata
data_url = treff["links"][-1]["href"]
metadata_url = treff["links"][-2]["href"]

response = requests.get(metadata_url)
response.raise_for_status()
metadata = response.json()
response.url
```

Nå kan vi prøve å printe ut litt aktuell metadata:

```python
#Print tittel, notater fra ssb, statistikkvariabler
print("Tittel", metadata["label"])
print("Notat", metadata["note"])
print("variabelid'er", metadata["id"])

ider = metadata["id"]
```

Vi kan hente ut alle mulige verdier for statistikkvariablene eller «dimensjonene» i datasettet:

```python
# Hent dimensjoner til dictionary
dimensjoner = dict()

for i in ider:
    dimensjoner[i] = list(metadata["dimension"][i]["category"]["index"].keys())
# Ikke lett å finne fram i json-stat for et menneske, men her må vi
```

- Vi har nå hentet frem tabellid, metadata og url for dataene vi skal hente
- Vi må nå bygge spørringen fra bunnen av ved å undersøke dimensjon/metadata
- Vi må altså velge hvilke data det er vi skal spørre etter

```python
#data_url = # funnet fram tidligere
# Lag post payload
payload = {
    "selection" : []
}
for var_name, var_values in dimensjoner.items():
    entry = {"variableCode": var_name, "valueCodes": var_values}
    payload["selection"].append(entry)


# Endre til siste 24 måneder
payload["selection"][1]["valueCodes"] = ["top(24)"]

payload
```

```python
# les data, send spørring
response = requests.post(data_url, json=payload)
response.raise_for_status()
response.url
```

```python
#vis
dataset = pyjstat.Dataset.read(response.text)
df = dataset.write("dataframe")
df
```

### Oppsummering: SSB

- Vi har hoppet over mange detaljer om hvordan spørringen er oppbygd
- Se [offisiell dokumentasjon](https://www.ssb.no/api/pxwebapiv2) dersom du trenger å gjøre aggregering, velge fra gruppering og eliminiering av valgfrie variabler
- Enkleste bruk er å gjøre filtreringer i statistikkbanken, og hente ut get-url derifra


::: {admonition} Oppgave
:class: note

1. I eksempelet over hentet vi programmatisk fram datasettet om spotpris på metaller med alle tilgjengelige statistikkvariabler. Hvor mye av koden må endres for at vi skal hente et annet dataset? Prøv deg fram.
2. Lag en funksjon som tar et tabellnummer fra ssb, og henter og leser inn all data fra tabellen til et pandas dataframe.

Til 2. vil du trenge å hente inn metadata og data slik som vi gjorde for metallene - Vi har ikke sett på datasett hvor man må velge grupperinger osv. slik at framgangsmåten vi har sett på kanskje ikke vil fungere for alle tabellnummer
    
:::
