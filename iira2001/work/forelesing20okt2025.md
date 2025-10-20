---
jupytext:
  formats: md:myst,ipynb
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.17.0
kernelspec:
  display_name: dataprog
  language: python
  name: dataprog
---

# Arbeidsledigheit 20de oktober 2025

+ Datasett 1054 frå [](https://data.ssb.no/api/)

```{code-cell} ipython3
import pandas as pd

df = pd.read_csv( "1054.csv", encoding="latin1", sep=";" )
print( type(df) )
```

## Repetisjon 1.  Filtrering

```{code-cell} ipython3
display(df)
```

```{code-cell} ipython3
df1 = df[ df["statistikkvariabel"] == "Arbeidsledige (1000 personer)" ]
display(df1)
```

Me skulle gjerne ha vist eit plott her, men me får ikkje det til før
me har løyst fleire problem nedover.


```{code-cell} ipython3
df1 = df1[ df1["kjønn"] == "0 Begge kjønn" ]
df1 = df1[ df1["alder"] == "15-74 15-74 år" ]
df1 = df1[ df1["type justering"] == "T Trend" ]
display(df1)
```

Me skal kopiera utdraget, slik at me kan endra det utan konflikt
med det underliggjande datasettet.

```{code-cell} ipython3
arbdf = df1.copy()
```

### Leselege søylenamn.

```{code-cell} ipython3
idx = list(df1.columns)[-1]
print(idx)
```

```{code-cell} ipython3
arbdf = arbdf.rename( columns={ idx : "arbeidsledige" } ) 
display(arbdf)
```

## Repetisjon 2.  Numeriske søyler

```{code-cell} ipython3
display( arbdf["arbeidsledige"] )
```

```{code-cell} ipython3
arbdf["arbeidsledige"] = arbdf["arbeidsledige"].astype(float)
```

```{code-cell} ipython3
arbdf.plot()
```

## Problem 1.  Tidssøyler

## Problem 2.  Byte av indeks.

## Problem 3.  Frekvens og gruppering av radar.

## Problem 4.  Fletting av datasett på tid.

