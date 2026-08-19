---
jupytext:
  formats: md:myst,ipynb
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

# Løysingar frå Demo Dataformatering

Desse oppgåvene er utgangspunktet for ein video der eg demonstrerer
nokre triks for å importera og formattera datafiler i python og pandas.

Me skal sjå på to filer
+ [plot01.csv](./plot01.csv)
+ [plot02.csv](./plot02.csv)

Me ynskjer å seia noko om utviklinga i bustadprisar over tid.

::: {admonition} Oppgåve
Last inn [plot01.csv](./plot01.csv) i pandas og studer filen.
Kva kan me bruka ho til?
:::

```{code-cell} ipython3
import pandas as pd
df1 = pd.read_csv( "plot01.csv", sep=";", decimal="," )
display( df1 )
```

```{code-cell} ipython3
df1bis = df1.dropna()
display( df1bis )
```

```{code-cell} ipython3
df1tri = df1bis.drop( 1 )
display( df1tri )
```

```{code-cell} ipython3
df1tri["Sesongjustert"] = pd.to_numeric( df1tri["Sesongjustert"].str.replace( ",", "." ) )
display( df1tri )
```

```{code-cell} ipython3
df1tri.plot.bar( "Unnamed: 0", "Sesongjustert" )
```

::: {admonition} Oppgåve
Last inn [plot02.csv](./plot02.csv) i pandas og studer filen.
Kva kan me bruka ho til?
:::

```{code-cell} ipython3
df2 = pd.read_csv( "plot02.csv", sep=";", decimal=",", header=2 )
display(df2)
```

```{code-cell} ipython3

```
