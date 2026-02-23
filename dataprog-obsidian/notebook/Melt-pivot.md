---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.18.1
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

<!-- #region -->
# Melt og Pivot

Pivot og melt er supert å bruke til å transformere eller endre formen på dataframen din: **Pivot lager kolonner, Melt lager rader.**


| Funksjon | Retning | Effekt |
| --- | --- | --- |
| **Pivot** |  | Øker antall kolonner, reduserer antall rader. |
| **Melt** |  | Reduserer antall kolonner, øker antall rader. |

---

### 1. Pivot (Bredere format)

Brukes når du vil transformere unike verdier i én kolonne til å bli **overskrifter** i nye kolonner.
```python
df.pivot(columns, index=<no_default>, values=<no_default>)
```

* **Fra:** En lang liste med gjentakende kategorier.
* **Til:** En bred matrise (f.eks. en tidsserie eller korrelasjonstabell).
* **Parametere:**
* `index`: Kolonnen som skal forbli rader.
* `columns`: Kolonnen som skal "eksplodere" ut til nye kolonneoverskrifter.
* `values`: Verdiene som skal fylle de nye cellene.



> **Merk:** Hvis du har duplikater i kombinasjonen av index/kolonne, må du bruke `df.pivot_table()` som støtter aggregering (f.eks. `aggfunc='mean'`).

---

### 2. Melt (Lengre format)

Brukes for å "av-pivotere". Det samler flere kolonner inn i to nye: én for "navnet på kolonnen" og én for "verdien".

* **Fra:** Data der informasjon ligger spredt over mange kolonner (f.eks. "Jan", "Feb", "Mar").
* **Til:** Et dataformat som er egnet for plotting og statistikk.
* **Parametere:**
* `id_vars`: Kolonnene som skal holdes som de er (identifikatorer).
* `value_vars`: Kolonnene som skal "smeltes" sammen.
* `var_name`: Navnet på den nye kolonnen for variablene.
* `value_name`: Navnet på den nye kolonnen for verdiene.

---




<!-- #endregion -->

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("05307_andel-roykere.csv", encoding="latin1",
                 sep=";", header=1, na_values=[".", ".."])
df
```

- Datasettet har et veldig bredt format
- Forutenom kolonnen `alder` er kolonneoverskriftet sammensatt av både *år*, *kjønn* og *statistikkvariabel*
- Dette gjør det vanskelig å gjøre utstnitt og utvalg i datasettet

```python
kolonner = df.columns
kolonner_valgte = (
    kolonner.str.contains("Menn")
    & kolonner.str.contains("2023")
    & kolonner.str.contains("dagligrøykere")
    | kolonner.str.contains("alder")
)
df[kolonner[kolonner_valgte]]
```

- Skal vi «fikse» opp dataene må vi:
    - Smelte kolonnenene (utenom alder) til 1 kolonne
    - SKille ut år, kjønn og statistikkvariabel
    - Eventuelt pivotere til et bredere format

```python
df_melt = df.melt(id_vars="alder", var_name="kompakt", value_name="verdi")

def get_year(kompakt_tekst):
    liste_ord = kompakt_tekst.split(' ')
    for ord_i in liste_ord:
        if ord_i.isdigit():
            return int(ord_i)

def get_gender(kompakt_tekst):
    liste_ord = kompakt_tekst.split(' ')
    for i, ord_i in enumerate(liste_ord):
        if ord_i.isdigit():
            return " ".join(liste_ord[i+1:])

def get_statvar(kompakt_tekst):
    liste_ord = kompakt_tekst.split(' ')
    for i, ord_i in enumerate(liste_ord):
        if ord_i.isdigit():
            return " ".join(liste_ord[:i])

df_melt["år"] = pd.PeriodIndex(df_melt["kompakt"].map(get_year), freq="Y")
df_melt["kjønn"] = df_melt["kompakt"].map(get_gender)
df_melt["statistikkvariabel"] = df_melt["kompakt"].map(get_statvar)

df_melt
```

```python
df_pivot = df_melt.pivot(columns=["statistikkvariabel", "alder"], index=["kjønn", "år"], values = "verdi")
df_pivot
```

```python
df_pivot.xs("Begge kjønn", level="kjønn").xs("16-24 år", level="alder", axis=1).iloc[:,0:2].plot()
plt.title("Unge røykere")
plt.show()
```

```python

```

```python
df_pivot2 = df_melt.pivot_table(columns=["statistikkvariabel", "alder"], index="år", 
                                values = "verdi", aggfunc="max")
df_pivot2.xs("35-44 år", level=1, axis=1).iloc[:, 0:2].plot()
plt.title("Andel også litt unge, røykere (største kjønnsgruppe)")
plt.show()
```
