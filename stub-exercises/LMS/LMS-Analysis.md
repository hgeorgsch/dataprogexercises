---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.17.0
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
import pandas as pd

df_moodle = pd.read_csv("moodleres.csv")
df_bb = pd.read_csv("bb.csv")
df_bb
```

```{code-cell} ipython3
df_moodle = df_moodle.rename(columns={"First name": "Fornavn", "Last name": "Etternavn"})

df = pd.merge(df_moodle, df_bb, on=["Fornavn", "Etternavn"])
df = df.replace("-", "0.0")

df  = df.astype({"Quiz: Øving 1 - Variabler og datatyper (Real)": "float64", "Quiz: Øving 2 - Funksjoner, løkker og lister (Real)": "float64"})
df["GodkjenningB"] = (df["Quiz: Øving 1 - Variabler og datatyper (Real)"]>=7.5) & (df["Quiz: Øving 2 - Funksjoner, løkker og lister (Real)"]>=7.5)
df["Godkjenning"] = df["GodkjenningB"].map(lambda x: "Godkjent" if x else "Ikke godkjent")
df_moodle.query("Etternavn == 'Sagflaat'")
```

```{code-cell} ipython3
import numpy as np
df_fsweb = df[["Fornavn", "Etternavn", "Student-ID", "Godkjenning"]]
df_fsweb.rename(columns={"Student-ID": "Studentnr."}, inplace=True)
df_fsweb.insert(3, "Kandidatnr.", [np.nan]*99)
df_fsweb.to_excel("tilfsweb.xlsx", index=False)
df_fsweb
```

```{code-cell} ipython3
df.query("Etternavn == 'Hennøen'")
```
