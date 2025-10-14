---
jupytext:
  formats: ipynb,md:myst
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

# Arbeidsledigheit 14de oktober 2025

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

```{code-cell} ipython3

```
