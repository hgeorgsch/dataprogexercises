---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.17.0
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---
*Førelesingsnotat frå veke 41/2024.  Sjå nokre andre notat og oppslagstabellar i [[Pandas-Series-DataFrames-JH]]*

+ #primitives/pickle

```{code-cell} ipython3
import pandas as pd
import numpy as np
import pickle

with open("HPcharacters.pickle", "rb") as file:
    HPdata = pickle.load(file)

df = pd.DataFrame(HPdata)
df
```

```{code-cell} ipython3
df = df.drop(columns=["id", "alternate_names", "gender", "wand", "actor", "alternate_actors", "image"])
df
```


# Introduksjon til *pan*el *da*ta: Pandas

Nyttig ressurs: [https://pandas.pydata.org/docs/user_guide/](https://pandas.pydata.org/docs/user_guide/)

* Pandas er et bibliotek for python for å manipulere og analysere data
* Vi bruker pandas til å laste inn eller lage datasett
    - Rydde opp i data
    - Få det over på annet format
    - Gjøre statistikk
    - Plotte data
    

+++ {"slideshow": {"slide_type": "subslide"}}

* Vi importerer pandas med som regel med `import pandas as pd`
* Pandas er bygd på numpy, så man trenger ofte også å bruke numpy

```{code-cell} ipython3
---
slideshow:
  slide_type: subslide
---
#EKSEMPEL

import pandas as pd
import numpy as np
import pickle

with open("HPcharacters.pickle", "rb") as file:
    HPdata = pickle.load(file)

df = pd.DataFrame(HPdata)
df
```

```{code-cell} ipython3
---
slideshow:
  slide_type: skip
---
sdata = {"frukt": ["epler", "pærer", "moreller", "rips"], "produksjon": [12,23,1,9], "subsidiert": [True, False, True, False], "pris": [10, 25, 40, 5]}
df_bilde = pd.DataFrame(sdata)
df_bilde
```

```{code-cell} ipython3
---
slideshow:
  slide_type: skip
---
sdata2 = { "produksjon": [12,23,1,9], "subsidiert": [True, False, True, False], "pris": [10, 25, 40, 5]}
df_bilde2 = pd.DataFrame(sdata2, index = ["epler", "pærer", "moreller", "rips"])
df_bilde2
```

+++ {"slideshow": {"slide_type": "slide"}}

* Pandas er bygd opp av objekter kalt *DataFrames* og *Series*
* Vi jobber for det meste med DataFrames
* DataFrames likner litt på hvordan man strukturerer data i feks excel
* De består av rader, og kolonner kalt *Series*
<img src="img/dfnavn1.jpg" width="550">


+++ {"slideshow": {"slide_type": "subslide"}}

* Hvert rad har en index
* Ut av boksen har radene indeks med heltall 0,1,2,3...
* Man kan også ha navn på radene (indeks er liste med strenger) slik som kolonnenavnene
![dataframe_indeksnavn](img/dfnavn2.png)

+++ {"slideshow": {"slide_type": "slide"}}

## Pandas Series
* Pandas series er som kolonnene i en tabell
* Dataserier har en *index*, et *navn* og *data* av en eller annen datatype (`dtype`)
* Vi lager serier med `pd.Series( ... )`

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
dataserie = pd.Series([1,2,3,4,5])
dataserie_2 = pd.Series(["Bil", "Båt", "Sykkel", "Tog", "Fly"])
dataserie
```

+++ {"slideshow": {"slide_type": "fragment"}}

* Her mangler vi navn på serien

+++ {"slideshow": {"slide_type": "subslide"}}

* Vi kan navngi serien ved å gi *keyword* argumentet "name"
* `pd.Series(data, name="Navnet")`

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
dataserie = pd.Series([1,2,3,4,5], name="Heltall")
dataserie
```

+++ {"slideshow": {"slide_type": "subslide"}}

* Vi kan gi en annen indeks med *keyword* argumentet "index"
* `pd.Series(data, name="Navnet", index = [ .... ])`

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
dataserie = pd.Series([1,2,3,4,5], name="Heltall", index=["en", "to", "tre", "fire", "fem"])
dataserie
```

+++ {"slideshow": {"slide_type": "subslide"}}

* Tidligere eksempel gir lister til `pd.Series()`
* Det kan være lurt å lage variabler med listene som skal bruke
* Når det passer seg bør listene være numpy *arrays*

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
data = np.array([1,2,3,4,5], dtype="int64")
navn = "heltall"
indeks = np.array(["en", "to", "tre", "fire", "fem"])
dataserie = pd.Series(data, name=navn, index=indeks)
#data[2] = 55
dataserie
```

+++ {"slideshow": {"slide_type": "subslide"}}

* Merk at dersom vi forandrer datavariabelen, forandres også pandas serien
* Dersom dette ikke er ønskelig kan vi bruke `copy=True` når vi lager serien

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
dataserie = pd.Series(data, name=navn, index=indeks, copy=True)
print(dataserie)
data[2]=66
dataserie
```

+++ {"slideshow": {"slide_type": "subslide"}}

### Oppgave 1:

* Lag dataserien under i pandas:
![oppg1](img/series_oppg1.png)

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
data = np.array([187,177,195,159], dtype="float64")
indeks = ["Per", "Pål", "Espen", "Askeladd"]
navn = "EventyrfigurHøyde"
dataserie = pd.Series(data, name=navn, index=indeks, copy=True)
dataserie
```

+++ {"slideshow": {"slide_type": "subslide"}}

* Vi kan lage serier også med dictionaries `{indeks0: data0, indeks1: data1}`
* Da blir indeksen satt til nøklene i dictionary'en

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
transport_data = {"land": "bil", "sjø": "båt", "luft": "fly"}
serie = pd.Series(transport_data, name="transportmetoder")
serie
```

+++ {"slideshow": {"slide_type": "subslide"}}

### Oppgave 2:

* Lag samme dataserie som tidligere i pandas
* Denne gangen bruk en dictionary til å sette data/indeks
![oppg1](img/series_oppg1.png)

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
data =  {"Per": 187, "Pål": 177, "Espen": 195, "Askeladd": 159}
navn = "EventyrfigurHøyde"
dataserie = pd.Series(data, name=navn, dtype="float64")
dataserie
```

+++ {"slideshow": {"slide_type": "subslide"}}

* Dersom vi mangler noe data for en indeks bruker vi `np.NaN`som data

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
data =  {"Per": 187, "Pål": 177, "Espen": np.NaN, "England": 159}
navn = "EventyrfigurHøyde"
dataserie = pd.Series(data, name=navn, dtype="float64")
dataserie
```

+++ {"slideshow": {"slide_type": "slide"}}

## Pandas DataFrame

* Vi er som regel interessert i å jobbe med DataFrames, en samling av serier
* Vi lager de med `pd.DataFrames(data, index=None, columns=None, dtype=None, copy=None)`
* Vi har de samme feltene som serier, men dataen er nå *todimensjonal*

+++ {"slideshow": {"slide_type": "subslide"}}

* `data` variabelen vi fyller dataframen vår med kan ha flere former:
 - 2d-array
 - dictionary -> `{col0: [data0], col1: [data1], ...}`
 - pandas Series

```{code-cell} ipython3
---
slideshow:
  slide_type: subslide
---
import pandas as pd
import numpy as np
data1 = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])
print(data1)
df1 = pd.DataFrame(data1, columns=["høyde", "vekt", "omkrets"], index=range(2,5))
df1
```

```{code-cell} ipython3
---
slideshow:
  slide_type: subslide
---
data2 = {"BNP": [1,2,3,4], "levealder": [88,88,99,102], 
         "styresett": ["demokrati", "diktatur", "demokrati", "monarki"]}
df2 = pd.DataFrame(data2, index=["Norge", "Uganda", "Sverige", "England"])
df2
```

```{code-cell} ipython3
---
slideshow:
  slide_type: subslide
---
indeks = ["BNP", "levealder", "styresett"]
serie1 = pd.Series([1,88,"demokrati"], name="Norge", index =indeks )
serie2 = pd.Series([2,88,"diktatur"], name="UGanda", index=indeks)
df3 = pd.DataFrame([serie1, serie2])
df3
```

+++ {"slideshow": {"slide_type": "slide"}}

### Oppgave 3:


Under har vi et lite pandas dataframe.
![oppg1](img/dataframe_oppg3.png)

Prøv å lage tabellen ved å bruke metodene over

```{code-cell} ipython3
---
slideshow:
  slide_type: subslide
---
testdat = {"Arbeidsledighet": ["2.0%","2.3%","2.6%","3.1%"],
           "Konkurser": [100,120,250,180],
           "BNP": [2e6,3e6,1.8e6,1.5e6]
          }
testdf = pd.DataFrame(testdat, index=range(2010,2014))
testdf
```

+++ {"slideshow": {"slide_type": "slide"}}

## Slå opp i Frame/Series

### Series
* Vi kan slå opp verdi nr. $i$ med serie[$i$]
* Eller vi kan bruke indeks: serie["indeks"]

### Dataframes
* Vi får tak i kolonne med `df["kolonnenavn"]`
* Vi får tak i rad med df.loc["rad_indeks"]
* Vi kan få tak i rad med df.iloc[i] hvor i er mellom 0 og antall rader i tabellen
* Vi får tak i et datapunkt med df.loc["rad", "kolonne"]

```{code-cell} ipython3
---
slideshow:
  slide_type: subslide
---
print(f"Levealder i {serie1.name} er {serie1['levealder']}")
print(f"Levealder i {serie2.name} er {serie2[1]}")
```

```{code-cell} ipython3
---
slideshow:
  slide_type: subslide
---
#kolonne BNP:
print("Kolonne 'BNP':\n", df2['BNP'])

#Rad med indeks
print("\nRad 'Sverige':\n", df2.loc['Sverige'])

#Rad med radnummer
print("\nRad nr. 3:\n", df2.iloc[2])

#Levalder i England:
print("\nLevealder i England er:", df2.loc["England", "levealder"])
df2
```

+++ {"slideshow": {"slide_type": "slide"}}

### Oppg 4

Se at du kan slå opp fra oppgave 3 og hente ut en gitt kolonne, rad eller datapunkt

+++ {"slideshow": {"slide_type": "slide"}}

## Manipulere Frame/Series

Vi vil kanskje kunne trenge å:
* Forandre indeks, navn på serie, eller navn på kolonner
* Legge til rad, eller kolonne til dataframe
* Bytte om på rad/kolonne
* Fjerne rad eller kolonne

```{code-cell} ipython3
---
slideshow:
  slide_type: subslide
---
data_land = ["England", "Norge", "Sverige"]
land = pd.Series(data_land)

#Forandre/hente navn på serie med min_serie.name
land.name = "land"

indeks = ["GB", "NO", "SE"]

#Hent eller sett en series index med min_sere.index
land.index= indeks
land["NO"] = "Danmark"

#land.index[1] = "DK" Vi må skifte hele indeksen
indeks = ["GB", "DK", "SE"]
land.index = indeks

#Vi legger til nye element på samme måte som i dictionaries
land["NOO"]= "Norge" # Legg til nytt element.

land = land.rename({"NOO": "NU"}) #Skift navn 
#Merk at .rename() ikke skifter navnet, men returnerer en ny Serie med skiftet
land.rename({"NU": "NO"}, inplace=True) #inplace=True gjør "fikser" på dette
land
```

```{code-cell} ipython3
---
slideshow:
  slide_type: subslide
---
data_innbyggere = [56, 6, 10]
land_innbyggere = pd.Series(data_innbyggere, name="innbyggere", index=indeks)

df_land = pd.DataFrame([land, land_innbyggere])
df_land = df_land.T # Bytter om på kolonner/rader (Transponerer)
df_land = df_land.rename(columns=({'land': 'navn'})) #Nytt navn til kolonne
df_land.loc['DK', 'navn'] = "Island" #Skifter landenavn til island
df_land.loc['DK', 'innbyggere'] = 0.4 #antall innbyggere til 0.4
df_land.rename(index={'DK': 'IS'}, inplace=True) #Nytt navn på indeks "DK"
df_land.loc["NO", "innbyggere"] = 5 # Oppdaterer data

df_land.loc["DK"] = ["Danmark", 6] #Legg til ny rad
df_land.loc["DE"] = {"navn": "Tyskland"} #Legg til rad med manglende data
df_land.loc["DE", "innbyggere"] = 80 #Oppdater data
df_land
```

+++ {"slideshow": {"slide_type": "slide"}}

### Oppg 5:
Ta utgangpunkt i tabellen over for å lage tabellen under
![oppg5](img/df_oppg5v2.png)

les [her](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.insert.html) for å finne ut hvordan du legger til en kolonne med `insert`

```{code-cell} ipython3
---
slideshow:
  slide_type: subslide
---
df_land.rename(columns=({"innbyggere": "populasjonsstørrelse"}), inplace=True)
df_land.drop(index=['NO'], inplace=True)
df_land.insert(2,"arbeidsledighet", ["1.0%","4.9%","3.2%","1.6%","12.5%" ])
df_land.loc["DE", "populasjonsstørrelse"]  = 83
df_land.loc["US"] = ["USA", 300, "50%"]
df_land
```

+++ {"slideshow": {"slide_type": "slide"}}

### Oppg 6
Hva er gjennomsnittlig arbeidsledighet til landene over?

```{code-cell} ipython3
---
slideshow:
  slide_type: subslide
---
arbeids_ledighet = df_land["arbeidsledighet"]
arbeidsledighet_formatert = [float(s[:-1]) for s in arbeids_ledighet]
gjennomsnitt = sum(arbeidsledighet_formatert)/len(arbeidsledighet_formatert)
print(f"Gjennomsnittlig arbeidsledighet er {round(gjennomsnitt,1)}%")
```

```{code-cell} ipython3

```
