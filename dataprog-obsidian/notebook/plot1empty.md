---
jupytext:
  formats: md:myst,ipynb
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.18.1
kernelspec:
  name: dataprog
  language: python
  display_name: dataprog
---

# Oppgåver til Demo Plott

Desse oppgåvene er utgangspunktet for ein demonstrasjonsvideo 
for plotting med pandas.  Me skal visa kurver og stolpediagram.

Eg har lasta ned eit enkle datasett frå SSB.
+ [09535fastlege.csv](09535fastlege.csv)
Datasettet viser fastlækjarkonsultasjonar per person i perioden
2010-2024, både for landet og per fylke.

::: {admonition} Oppgåve
Hent datasettet [09535fastlege.csv](09535fastlege.csv)
og last det i python.
:::

```{code-cell} ipython3
import pandas as pd
df = pd.read_csv( "09535fastlege.csv", sep=";", encoding="latin1", header=1 )
display(df)
```

```{code-cell} ipython3
df = df.set_index("år")
display(df)
```

## Kurveplot

```{code-cell} ipython3
df.columns
```

```{code-cell} ipython3
df.plot( None, "0 Hele landet Alle aldre" )
```

```{code-cell} ipython3
df.plot( )
```

## Datavask

```{code-cell} ipython3
df.dtypes
```

```{code-cell} ipython3
df = df.drop( "statistikkvariabel", axis=1 )
display( df )
```

```{code-cell} ipython3
df = df.drop( "kjønn", axis=1 )
display( df )
```

```{code-cell} ipython3
col = list(df.columns)
print( col )
```

```{code-cell} ipython3
for c in col[2:]:
    df[c] = pd.to_numeric( df[c], errors="coerce" )

display(df)
```

## Stolpediagram

