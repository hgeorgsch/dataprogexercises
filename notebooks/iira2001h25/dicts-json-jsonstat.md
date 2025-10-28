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

# MÅL: Hente data programmatisk

* Vi trenger først å lære litt om nettverskprotokollen: HTTP
* Vi trenger å vite litt om JSON-formatet, og python dictionaries
* Vi trenger å vite litt om hva en URL er
* Vi må kunne bruke python-biblioteket `requests` og `pyjstat`

+++

# JSON, Python dictionaries og jsonstat

+++

## Dictionaries
- Dere har allerede brukt litt dictionaries
- Det er en meget nyttig datastruktur hvor vi lagrer data som par av "nøkler" og "verdier" i en "dictionary"
    - Nøklene er som regel tekststrenger
    - Verdiene er *data*, feks numeriske verdier, lister eller *andre dictionaries*
- Vi bygger dictionaries med klammeparanteser, fylt med `nøkkel: verdi` par skilt med komma

```{code-cell} ipython3
# Vi lager en dictionary slik:

person = {"fornavn": "jonas", "alder": 37}
print(person)
```

*Krøllparantes/klammeparanteser på mac er shift+7/8 eller shift+opt+7/8, og på windows altgr+7/8/9/0*

```{code-cell} ipython3
# Vi slår opp i dictionaries slik:

navn = person["fornavn"]
print(f"Navn på person er {navn}, alder er {person['alder']}")
```

```{code-cell} ipython3
# Vi legger til eller endrer på felter slik:

person["etternavn"] = "Hansen"
person["alder"] = 27
person
```

- Det er vanlig å bruke dictionaries til å "strukturere" sammensatt og komplisert data.
- Vi har da gjerne lister av dictionaries, underlister, eller sammensatte dictionaries

```{code-cell} ipython3
data = {
    "countries": [
        {
            "name": "Norway",
            "population": {
                "2020": 5_367_580,
                "2024": 5_550_203
            },
            "regions": ["Oslo", "Bergen", "Trondheim"]
        },
        {
            "name": "Sweden",
            "population": {
                "2020": 10_379_295,
                "2024": 10_642_122
            },
            "regions": ["Stockholm", "Göteborg", "Malmö"]
        }
    ]
}
```

- Vi kan bruke den innebygde metoden `.keys()` for å hente ut "nøklene" i en dictionary
- Vi kan bruke den innebygde metoden `.values()` for å hente ut "verdiene" i en dictionary
- Vi kan bruke `.items()`til å hente ut alle nøkkel/verdi-par i en tuple

```{code-cell} ipython3
#Vis keys/nøkler
print(list(data.keys()))
```

```{code-cell} ipython3
#Vi bruker spesielt .keys(), .values() og .items()
for land in data["countries"]:
    #print(land)
    for k, v in land.items():
        print("Nøkkel", k, "Verdi:", v)
# Når vi skal "iterere" (gå igjennom) strukturen
```

## JSON

- JSON er en forkortelse for *Javascript object notation*
- Det er en meget vanlig måte å strukturere og distrubere data på, spesielt på internett
- Heldigvis, er det nesten 100% identisk med dictionaries i python
- Det er en "liste" (klammeparanteser) med `nøkkel: verdi` par skilt med komma
- Men verdiene stammer fra javascript slik at `None` er `null` og `True` er `true`
- Vi bør alikevel alltid bruke et bibiliotek til å lese eller skrive json-data:

```{code-cell} ipython3
import json

person["gift"] = True
person["vekt"] = None

# Json til tekststreng:
print(json.dumps(person))
print(person)
```

- Vi skriver eller leser json til/fra fil med `json.dump(...)` eller `json.load(...)`
- Eller `json.dumps(...)` og `json.loads(...)` for teksstrenger

```{code-cell} ipython3
#Lagre og åpne dictionary med json.dump/load

with open("person.json", 'w') as file:
    json.dump(person, file)

with open("person.json", 'r') as fillefil:
    ny_person = json.load(fillefil)

ny_person
```

- Vi bruker gjerne en kombinasjon of `print`,  `.keys()` og `for`-løkker til å undersøke slike datastrukturer
- I json-format er et lurt triks å åpne de i nettleseren ;) 

+++

### JSON-stat
- En spesialvariant av en datastruktur er `jsonstat`
- Bla. eurostat og ssb distrubierer data i dette formatet
- Det er egentlig vanlig JSON -- men data og metadata er strukturert på en spesiell måte
- Prøv å se på dette: [https://json-stat.org/samples/oecd.json](https://json-stat.org/samples/oecd.json)

+++

- Det er som regel ikke tilrådelig å jobbe med denne strukturen direkte
- Heldigvis har vi gode innebygde biblioteker `pyjstat`


```{code-cell} ipython3
# Kommenter inn linjen under og kjør denne cellen for å hente inn pyjstat om du mangler
!pip install pyjstat
```

```{code-cell} ipython3

from pyjstat import pyjstat  # pyjstat er for behandling av JSON-stat
import pandas as pd
# Finner et dataset på ssb og lagrer som jsonstat2
with open("14406_20251027-114414.json", 'r', encoding="utf-8") as file:
    dataset = pyjstat.Dataset.read(file)
tittel = dataset.get("label")
df = dataset.write("dataframe")
df_id = dataset.write("dataframe", naming="id")

df_original = df
```

- Med jsonstat er dataene i «langt» format, eller «smeltet» format
- Vi kan bruke `df.pivot(columns=..., index=..., values=...)` til å lage en pivot-tabell

```{code-cell} ipython3
df = df_original
df = df.pivot(columns="kor ofte ein gjer aktiviteten", index="friluftslivsaktivitet", values="value")
df
```

```{code-cell} ipython3
#Kakediagram kolonne
df["Fleire gonger i veka"].plot.pie()
```

```{code-cell} ipython3
#Kakediagram rad
df.loc["Går på ski"].plot.pie()
```

# Kjapt om å finne filer
- I pausen hadde flere problemer med at filene deres ikke ble funnet på samme måte
- Vi kan bruke `os.getcwd()` til å finne ut hvor python "kjører" på datamaskinen
- Vi kan deretter gi riktig sti til filen vi vil laste inn
- Feks  `open("../Forelesning/min_fil.json")` hvis vi må gå opp en mappe/nivå (..) og inn i mappen Forelesning for å finne min_fil.json

```{code-cell} ipython3
import os
print(os.getcwd())
```
