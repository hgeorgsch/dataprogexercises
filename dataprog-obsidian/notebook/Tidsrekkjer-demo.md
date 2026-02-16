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

# Tidsrekkjer og pivot

Datafile: [12143_20260209-154116.csv](12143_20260209-154116.csv)

```{code-cell} ipython3
import pandas as pd
df = pd.read_csv( "12143_20260209-154116.csv", encoding="latin1", sep=";", header=1 )
display(df)
```

```{code-cell} ipython3
df1 = df.pivot( index="år", columns=["statistikkvariabel","regnskapsbegrep"] )
display( df1 )
```

```{code-cell} ipython3

```
