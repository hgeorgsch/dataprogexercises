---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.17.2
kernelspec:
  display_name: dataprog
  language: python
  name: dataprog
---

# Arbeidsledigheit 14de oktober 2025

**NB** Dette er notata som vart skrivne *under* førelesinga 14. oktober.
Det er ikkje alt som verkar, og ingenting er forklart.

+ Datasett 1054 frå [](https://data.ssb.no/api/)

```{code-cell} ipython3
import pandas as pd

df = pd.read_csv( "1054.csv", encoding="latin1", sep=";" )
display(df)
```

```{code-cell} ipython3
type(df)
```

```{code-cell} ipython3
k = df["kjønn"]
display(k)
```

```{code-cell} ipython3
type(k)
```

```{code-cell} ipython3
r = df.iloc[1]
display(r)
```

```{code-cell} ipython3
type(r)
```

```{code-cell} ipython3
r["kjønn"]
```

```{code-cell} ipython3
df[ [ "kjønn", "alder" ] ] 
```

```{code-cell} ipython3
df.iloc[1:4]
```

```{code-cell} ipython3
utsnitt = df[1:4]
utsnitt
```

```{code-cell} ipython3
utsnitt.loc[1,"kjønn"]
```

```{code-cell} ipython3
utsnitt.loc[1,"kjønn"] = "0"
```

```{code-cell} ipython3
utsnitt.loc[1,"kjønn"]
```

```{code-cell} ipython3
df.iloc[1]
```

```{code-cell} ipython3
display(df)
```

```{code-cell} ipython3
u = utsnitt.copy()
u
```

## Filtrering

```{code-cell} ipython3
df1 = df[ df["statistikkvariabel"] == "Arbeidsledige (1000 personer)" ]
display(df1)
```

```{code-cell} ipython3
display(df1)
```

```{code-cell} ipython3
ledighet = df1.iloc[:,5]
print(ledighet)
```

```{code-cell} ipython3
import matplotlib.pyplot as plt
plt.plot( ledighet )
plt.show()
```

```{code-cell} ipython3
ledighet2 = ledighet.copy()
ledighet3 = ledighet2.reset_index()
print( ledighet3 )
```

```{code-cell} ipython3
list( ledighet3 )
```

```{code-cell} ipython3
ledighet3.plot( )
```

## Notat etter førelesing

Eitt problem me hadde er at me må filtrera på (nesten) alle søylane for å få ein tidsserie.

```{code-cell} ipython3
df = pd.read_csv( "1054.csv", encoding="latin1", sep=";", decimal="," )
df1 = df[ df["statistikkvariabel"] == "Arbeidsledige (1000 personer)" ]
df1 = df1[ df1["kjønn"] == "0 Begge kjønn" ]
df1 = df1[ df1["alder"] == "15-74 15-74 år" ]
df1 = df1[ df1["type justering"] == "T Trend" ]

display(df1)
```

Eit anna problem var å byta namn på søylen med det lange og uskikkelege namnet.
Me kan henta ut namnet direkte utan klipp og lim, for so å byta det ut, slik:

```{code-cell} ipython3
idx = list(df1.columns)[-1]
df2 = df1.rename( columns={ idx : "arbeidsledige" } ) 

print(idx)
df2
```

Neste problem er at `arbeidsledige` ikkje er ein numerisk søyle.
Det er truleg fordi nokre radar i den opprinnelege tabellen ikkje lét seg tolka som tal.
Det er truleg betre å bruka ein numpy-type, men for ikkje å importera numpy, gjer me det slik i full fart.

```{code-cell} ipython3
df2["arbeidsledige"] = df2["arbeidsledige"].astype(float)
```

Dette er nok til å kunna plotta.

```{code-cell} ipython3
df2.plot( y="arbeidsledige" )
```

```{code-cell} ipython3
list(df2["arbeidsledige"])
```

```{code-cell} ipython3

```
