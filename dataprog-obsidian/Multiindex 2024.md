---
tags:
   - pandas
   - legacy/iif
---

Materiale frå 44/2024
# Multiindex dataframes

* Multiindex har «tupler» som index: `[(Alta, 1991), (Alta, 1992), .... , (Ålesund, 1991), (Ålesund,  1992)]`
* Vi kan lage en slik multiindex med feks `.set_index(["Sted", "År"])`
* Vi slår nå opp i dataframe med tupler, `df.loc[("Molde", 2001), "Fraflytning"]`
* Vi kan også slå opp i kun ytterste index, `df.loc["Molde"]`
<!-- #endregion -->

```python editable=true slideshow={"slide_type": "subslide"}
import pandas as pd
df = pd.read_csv("eu_GDP.csv") # teina010 dataset fra eurostat, (GDP and main components (output, expenditure and income))
land = df["Geopolitical entity (reporting)"].unique() #Områder som er med
df["Time"] = pd.PeriodIndex(df["Time"], freq='Q') #Gjør om til pandas.Period i stedet for "strenger"
df = df.set_index(["Geopolitical entity (reporting)", "Time"]) #Setter multiindex - område ytterst, år innerst

print("GDP (tusen euro), Norge 1. kvartal 2023", df.loc[("Norway", "2023Q1"), "value"])#Slår opp i spesifikt datapunkt
data_norge = df.loc["Norway"] #Henter data for Norge
```

<!-- #region editable=true slideshow={"slide_type": "subslide"} -->
## Slice og hente områder med data
* Dersom vi vil hente ut data litt mer komplisert enn kun fra ytterste indeks bør vi først sortere indeksen
* Det gjøres med `df.sort_index(level=...)`
* Her er `level`et heltall, eller etikette eller en liste av heltall/etiketter som forteller hvilken nivå vi skal sortere på
* Vi teller "nivåene" fra innerst=0 til ytterst=n-1, (1 dersom vi har 2 nivå)
<!-- #endregion -->

```python editable=true slideshow={"slide_type": "subslide"}
df.sort_index(level=1) # Sortere på land
df.sort_index(level=0) # Sorterer år
df = df.sort_index(level=[0,1]) #Sorterer begge

```

<!-- #region editable=true slideshow={"slide_type": "subslide"} -->
### Slice
* Det blir litt mer komplisert når man skal slice multiindex dataframes
* Mitt tips er å bruke `df.xs(key, axis=0, level=None, drop_level=True)` ("cross section") når man skal hente ut hele nivåer
* Og `pd.IndexSlice` for mer komplisert slicing
* *Også kolonnene kan ha en "multiindex" Vi bruker da de samme teknikkene*
<!-- #endregion -->

```python editable=true slideshow={"slide_type": "fragment"}
df.xs("2021Q3", level="Time", drop_level=False) # Hent ut data for 3. kvartal 2021, for alle land
```

#### pd.IndexSlice
* IndexSlice er spesialbygget for å slice over multiindekser
* Det finnes flere måter å gjøre dette på, men de er litt rare og vanskelige
* Med `IndexSlice` lager vi først en "slicer": `idx = pd.IndexSlice`
* Denne bruker vi sammen med `.loc[]` til å slice ganske intuitivt over flere indeksnivåer, (funker også lang kolonnene)
* `data = df.loc[idx["Alta":"Molde", 1950:1970], :]`

```python editable=true slideshow={"slide_type": "fragment"}
idx = pd.IndexSlice
df.loc[idx["Germany":"Sweden", "2022Q1":"2023Q3"], :]
```

<!-- #region editable=true slideshow={"slide_type": "subslide"} -->
