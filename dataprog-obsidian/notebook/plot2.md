---
jupytext:
  formats: md:myst,ipynb
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.18.1
kernelspec:
  display_name: dataprog
  language: python
  name: dataprog
---

# Løysingar frå Demo Plot Del 2 (Kakediagram)

Desse oppgåvene er utgangspunktet for den andre
demonstrasjonsvideoen om plotting med pandas.
Her skal me sjå på kakediagram.
Datasettet kjem frå den same tabellen åt SSB.
+ [09535fastlege2.csv](09535fastlege2.csv)
Dette datasettet viser andelen personar med 0, 1-2, 3-4 eller 5+ 
konsultasjonar i 2024.

Kakediagram er egna for å visa andelar.
Datasettet vårt viser prosentvis andel av folket som har konsultert
fastlækjaren eit visst tal gongar, og er dermed godt egna for kakediagram.

::: {admonition} Oppgåve
Hent datasettet [09535fastlege2.csv](09535fastlege2.csv)
og last det i python.
:::

```{code-cell} ipython3
import pandas as pd
df = pd.read_csv( "09535fastlege2.csv", sep=";", encoding="latin1", header=1 )
display(df)
```

## Kakediagram

```{code-cell} ipython3
ser = df.iloc[0]
display( ser )
```

```{code-cell} ipython3
ser = ser[3:]
display(ser)
```

```{code-cell} ipython3
ser.plot()
```

```{code-cell} ipython3
ser.plot.bar()
```

```{code-cell} ipython3
ser.plot.pie()
```

```{code-cell} ipython3

```
