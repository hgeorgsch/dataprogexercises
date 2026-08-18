---
jupytext:
  formats: md:myst,ipynb
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.19.1
kernelspec:
  display_name: dataprog
  language: python
  name: dataprog
---

# Reformatering med pivot

Datafile: [12143_20260209-154116.csv](12143_20260209-154116.csv)

Her har tidsaksen mange ulike variabler med hver sin rad på samme tidsperiode.
Vi ønsker heller å ha variablene bortover, med egne søyler,
slik at vi får én og bare én rad per periode.

```{code-cell} ipython3
import pandas as pd
from IPython.display import display
df = pd.read_csv( "12143_20260209-154116.csv", encoding="latin1", sep=";", header=1 )
display(df)
```

Funksjonen vi trenger er `pivot`, slik.

```{code-cell} ipython3
df1 = df.pivot( index="år", columns=["statistikkvariabel","regnskapsbegrep"] )
display( df1 )
```

Til slutt er det greit å lagre den nye *DataFrame* i en ny fil.

```{code-cell} ipython3
df1.to_csv( "pivot.csv" )
```
