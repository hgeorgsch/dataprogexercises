---
jupytext:
  formats: md:myst,ipynb
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.19.1
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Maskinlæring med data frå WebAPI

```{code-cell} ipython3
import json
import requests
from pyjstat import pyjstat
from sklearn.linear_model import LinearRegression
import pandas as pd
```

I denne øvinga skal me bruka APIet åt SSB for å henta data til maskinlæring.
For at programmet skal vera mest mogleg gjenbrukbart, har me lagt dei kritiske funksjonane
til ein JSON-fil, som me lastar inn fyrst.

```{code-cell} ipython3
configfil = "innenlandslanegjeld.json"
```

## Konfigurasjonen

+++

Lat oss fyrst sjå korleis konfigurasjonen ser ut.

```{code-cell} ipython3
with open(configfil, 'r') as file:
        ssbAPIdata = json.load(file)
for k, v in ssbAPIdata.items():
    print( f"{k}: {v}"  )
```

Her ser me kva URL me kontaktar, kva tabell me skal be om, og kva søyler me vil ha.

+++

## Bruk av API-et

Sjølve innhentinga av datasettet har me lagt til eit API.

```{code-cell} ipython3
def hent_dataset(ssbAPIdata):
    
    postUrl = ssbAPIdata["postUrl"]
    tabellnummer = ssbAPIdata["tableIdForQuery"]
    query = ssbAPIdata["queryObj"]
    print(f"Henter data fra tabell {tabellnummer}")
    response = requests.post(postUrl, json=query)

    if response.status_code == 200:
        print("Data hentet: OK")
    else:
        print(f"""Data kunne ikke hentes, feilkode {response.status_code}
        Responstekst: response.text""")
        return None

    dataset = pyjstat.Dataset.read(response.text)
    df = dataset.write("dataframe")

    print(f"""Hentet dataset: {dataset['label']}""")
    return df, dataset
```

::: {admonition} Refleksjon
Kva gjer funksjonen `hent_dataset()`?
:::

## Datasettet

Lat oss bruka funksjonen og sjå på datasettet.
Legg merke til at funksjonen returnerer to variablar, og
det er greitt å sjekka kva type dei har.

```{code-cell} ipython3
df, ds = hent_dataset(ssbAPIdata)
print( "df", type(df), len(df) )
print( "ds", type(ds), len(ds) )
```

Altso, i funksjonen har `dataset.write()` laga ein pandas
*DataFrame* som vert returnert som den frste utvariabelen.
Den andre utvariabelen er *Dataset*-typen frå `pyjstat`.

Slik ser datasettet ut:

```{code-cell} ipython3
display(df)
```

::: {admonition} Oppgåve
Korleis ser datasettet ut i formatet frå `pyjstat`?
Bruk ein `print`- eller `display`-line for å sjekka.
:::

+++

## Formatering av datasettet

Der er nokre overflødige søyler, og periodane er formattert
som strengar.  Dette kan me fiksa opp i slik som me har gjort
før.

```{code-cell} ipython3
df = df.drop(columns=["låntakersektor", "statistikkvariabel"])
df["måned"] = pd.to_datetime(df["måned"], format="%YM%m")
df = df.rename(columns={"value": "Innenlandsk lånegjeld"})
df = df.set_index("måned")
display(df)
```

Om me plottar, kan eå sjå at dette ser ålreit ut.

```{code-cell} ipython3
df.plot()
```

## Utsnitt

Det er enkelt å plotta eit mindre utsnitt, ved å indeksera med 
`.loc`.

```{code-cell} ipython3
df_linje = df.loc["2004":]
```

Det kan verka rart at pandas les `"2004":` som eit utsnitt frå
og med 2004, men om me plottar, so ser me at det er det som skjer.

```{code-cell} ipython3
df_linje.plot()
```

I det vidare er det dette utsnittet me skal sjå på.

## Tidsakse i dagar.

Skal me få ein presis regresjonsanalyse, treng me ein konsistent
eining på tidsaksen.  Månader er dårleg, sidan dei ikkje er like
lang.  I staden kan me laga ein ny søyle som måler tida i dagar.

```{code-cell} ipython3
data = df_linje.reset_index()
data["dager"] = data["måned"] - data.loc[0,"måned"] 
data["dager"] = data["dager"].dt.days 
```

Me set indeksen tilbake slik at me tel frå null.
Definisjonen av `"dager"`-søyla skjer i to steg.
Fyrst reknar me om i tid frå fyrste periode, og deretter reknar
me tidsdifferansane om i dagar.

## Regresjonsanalyse

No kan me bruka dagane som $x$-variabel og 
lånegjelda som $y$-variabel

```{code-cell} ipython3
X = data[["dager"]] 
y = data["Innenlandsk lånegjeld"] 
```

Då har me det me treng for å laga ein lineær regresjonsmodell
slik som me har gjort før.

```{code-cell} ipython3
modell = LinearRegression() # Lager en lineær regresjonsmodell
resultat = modell.fit(X,y) #Tilpasser modell til data (læring)
data["regresjon"] = modell.predict(X) # Bruker modell til å anslå avhengig variabel
ax = data.plot(x="måned", y="regresjon")
data.plot(x="måned", y="Innenlandsk lånegjeld", ax=ax)
```

Eit vanleg mål for kor godt modellen passar er $R^2$
som me kan rekna ut slik.

```{code-cell} ipython3
Rsquared = modell.score(X,y) #Score med hvor godt linjen "passer"
```

## Avrunding

Målet med dette dømet har vore å visa korleis me kan kombinera
*WebAPI* med statistisk inferens, og skriva ein mest mogleg
gjenbrukbar *Notebook*.  Om du køyrer koden på nytt om ein månad,
vil du få ein lenger tidsrekkje frå APIet.  I alle fall om ikkje
SSB endrar grensesnittet.
