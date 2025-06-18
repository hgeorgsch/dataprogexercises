---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.17.0
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

# Semi-avansert pandas

Vi har nå vært igjennom basics med pandas. Det er veldig mye du kan gjøre med pandas, og vi kan ikke dekke alt i dette kurset

* Filtrering
* Omforme med `.melt()`, `.pivot()`
## Filtrering

* Ofte holder det ikke å slice data -- vi trenger å filtrere de ut
* Kanskje vi vil velge ut data for land med befolkning større enn 10 millioner *OG* BNP større enn ...
* I pandas kan vi filtrere i `.loc[..]` ved bruk av boolsk aritmetikk
* Vi kan også bruke `.query("spørring")`
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": "subslide"} -->
## Boolsk filtrering

* Gjør vi noe som `df["alder"] > 25` returnerer pandas en dataserie med `True`overalt hvor "alder" er større enn 25
* Vi kan bruke denne dataserien til å slå opp i alle radene hvor serien inneholder true:

  ```python
  df.loc[df["alder"] > 25] # Returnerer alle rader hvor "alder" kolonnen inneholder et tall over 25
  ```
* Vi kan kombinere ulike boolske serier med `&` ( and ) og `|` (eller) 
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": "subslide"} -->
Tabell med ulike måter å bruke dette til å filtrere ut data:
| Beskrivelse                                                 | Eksempel                                           |
|-------------------------------------------------------------|----------------------------------------------------|
| Filter rader der `Alder` er større enn 20                   | `df[df['Alder'] > 20]`                             |
| Filter rader der `Navn` inneholder 'e' (case-insensitive)   | `df[df['Navn'].str.contains('e', case=False)]`     |
| Filter rader der `Alder` er mellom 20 og 30                 | `df[(df['Alder'] >= 20) & (df['Alder'] <= 30)]`    |
| Filter rader der `Navn` ikke inneholder 'a'                 | `df[~df['Navn'].str.contains('a', case=False)]`    |
| Filter rader der `Poeng` er større enn 50 eller `Alder` er mindre enn 25 | `df[(df['Poeng'] > 50) \| (df['Alder'] < 25)]` |
| Filter rader der `Land` er enten "Norge" eller "Sverige"    | `df[df['Land'].isin(['Norge', 'Sverige'])]`        |
| Filter rader med eksakte match i `Postnummer`               | `df[df['Postnummer'].isin([1234, 5678])]`          |
| Filter rader der `Navn` starter med 'B'                     | `df[df['Navn'].str.startswith('B')]`               |
| Filter rader der `Navn` slutter på 'e'                      | `df[df['Navn'].str.endswith('e')]`                 |

<!-- #endregion -->

```python editable=true slideshow={"slide_type": "subslide"}
import pandas as pd
import numpy as np
df = pd.read_csv("folketall.csv", encoding="ISO-8859-1", sep="\t")

df = df.replace("..", np.nan)
kolonner = list(df.columns)
kolonner.remove("region")
konvertering = {kol: "Int64" for kol in kolonner}
df = df.astype(konvertering)
df["år"] = pd.PeriodIndex(df["år"], freq="Y")

df= df.set_index(["region", "år"])
df = df.sort_index(level=["region", "år"])

#litt slicing
idx = pd.IndexSlice
df.xs("1990", level="år")
display(df.loc[idx[:, "2000":"2025"], idx["Døde":"Innflyttinger"]])

df[df["Døde"] <1000] # Slå opp alle år hvor færre enn 1000 døde (alle regioner)

display(df.loc[df["Innflyttinger"] > df["Utflyttinger"]]) #Slå opp alle rader hvor flere flyttet inn enn ut

# Alle region/år hvor nettoinnflytting er positiv og befolkning er større enn 100,000
df[(df["Nettoinnflytting"] > 0) & (df["Befolkning 1. januar"] > 100000)]

#Dersom man vil filtrere på index, kan man resette den med .reset_index() eller:
df[df.index.get_level_values("region").str.contains("Ålesund")]

#Finn kommune-funksjon
def FK(kommune):
    regioner = df.index.get_level_values("region").unique()
    for reg in regioner:
        if kommune in reg:
            return reg
    return None

df.loc[idx[FK("Molde"):FK("Halden"), "1990"], ["Døde", "Levendefødte"]]
                            
```

<!-- #region editable=true slideshow={"slide_type": "subslide"} -->
### Filtrere med `.query("streng")`
* Filtrering med query er veldig likt -- bare litt mer lesbart
* Vi gir like gjerne bare en tabell:

| Beskrivelse                                                 | Eksempel                                           |
|-------------------------------------------------------------|----------------------------------------------------|
| Filter rader der `Alder` er større enn 20                   | `df.query("Alder > 20")`                           |
| Filter rader der `Navn` er "Ola"                            | `df.query("Navn == 'Ola'")`                        |
| Filter rader der `Alder` er mellom 20 og 30                 | `df.query("20 <= Alder <= 30")`                    |
| Filter rader der `Poeng` er større enn 50 eller `Alder` er mindre enn 25 | `df.query("Poeng > 50 or Alder < 25")` |
| Filter rader der `Land` er enten "Norge" eller "Sverige"    | `df.query("Land in ['Norge', 'Sverige']")`         |
| Filter rader der `Navn` ikke er "Ola"                       | `df.query("Navn != 'Ola'")`                        |
| Filter rader der `Alder` ganger `Poeng` er større enn 1000  | `df.query("Alder * Poeng > 1000")`                 |
| Filter rader med delvis match på `Postnummer` (tekststreng) som starter med '12' | `df.query("Postnummer.str.startswith('12')", engine='python')` |
| Filter rader der `Poeng` ikke er null                       | `df.query("Poeng.notna()", engine='python')`       |

<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": "subslide"} -->
# Melt og Pivot

* Vi trenger ofte å omforme hvordan dataene er satt sammen i rader og kolonner
* Vi kan bruke `df.melt()` til å gjøre dataframen smal og lang (kolonner ned i rader)
* Vi bruker `df.pivot()` til å gjøre dataframen bred og kort (rader opp i kolonnene)
* Ofte er det greit å første gjøre dataframe så smal som mulig uten å "miste data"
* Deretter fikse datatyper og filtrere før man bestemmer seg for indeks og kolonner
<!-- #endregion -->

<!-- #region editable=true slideshow={"slide_type": "subslide"} -->
## `df.melt(...)`

Et kall til melt ser slik ut:
* `df.melt(id_vars=None, value_vars=None, var_name=None, value_name='value', col_level=None, ignore_index=True)`
* id_vars, er kolonnene vi vil beholde slik de er, en liste med kolonnenavn
* value_vars er en liste med kolonnene vi vil "smelte" (ha ned som rader).
  * Dersom den er `None` antar vi at det er alle andre kolonner enn id_vars
* var_name og value_name er kolonnenavn og verdinavn til kolonnene som blir smeltet
<!-- #endregion -->

```python editable=true slideshow={"slide_type": "subslide"}
df = pd.read_csv("helsepersonell.csv", encoding="ISO-8859-1", sep=";", header=1)
df = df.melt(id_vars=["statistikkvariabel", "fagutdanning", "alder", "kjønn"], var_name="år")
df = df.replace("..", np.nan)
df = df.query("fagutdanning == 'Sykepleier' and statistikkvariabel in ['Personer', 'Sysselsatte']")
df=df.rename(columns={"value": "antall"})
df = df.astype({"antall": "int32"})
df["år"] = pd.PeriodIndex(df["år"], freq="Y")

df
```

<!-- #region editable=true slideshow={"slide_type": "subslide"} -->
## `df.pivot()`

Et kall til pivot ser slik ut:
* `df.pivot(columns, index=<no_default>, values=<no_default>)`
* columns: forteller hvilken kolonne vi skal bruke til å lage kolonnene i pivot-tabellen
* index: er kolonnene vi vil ha som indeks (bruker eksisterende indeks om vi ikke gir noe her)
* values: Kolonnene eller kolonnen som holder verdiene/datapunktene 

<!-- #endregion -->

```python editable=true slideshow={"slide_type": "subslide"}
df = pd.read_csv("helsepersonell.csv", encoding="ISO-8859-1", sep=";", header=1)
df = df.melt(id_vars=["statistikkvariabel", "fagutdanning", "alder", "kjønn"], var_name="år")
df = df.replace("..", np.nan)
df = df.query("fagutdanning == 'Sykepleier' and statistikkvariabel in ['Personer', 'Sysselsatte']")
df=df.rename(columns={"value": "antall"})
df = df.astype({"antall": "int32"})
df["år"] = pd.PeriodIndex(df["år"], freq="Y")


df = df.pivot(index=["år", "kjønn"], columns=["statistikkvariabel", "alder"], values="antall")
df2 = df[("Personer", "Alle aldre")]
df2.xs("Kvinner", level="kjønn").plot()
df2.xs("Menn", level="kjønn").plot()
display(df)
```
