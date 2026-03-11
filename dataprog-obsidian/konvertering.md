---
jupytext:
  formats: md:myst,ipynb,py:percent
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

# Formatering av valutakursar

Dette programmet skal laga ein CSV-fil med valutakursar,
der kvar valuta har ei søyle.  Utgangspunktet er fila
frå 
[Noregs Bank](https://www.norges-bank.no/tema/Statistikk/Valutakurser/?tab=api).

Programmet fylgjer øvinga «Fyrste datasett i CSV».

Fyrst importane

```{code-cell} ipython3
import pandas as pd
```

No er det greit å definera dei filene me skal bruka, både innfil og utfil.

```{code-cell} ipython3
innfil = "EXR20250401.csv"
utfil = "EXR-formattert.csv"
```

So kjem skjølve programmet.
Eg har klipt ned koden frå den gamle øvinga.
Fyrst kan me fiksa dato- og kurssøylene.

```{code-cell} ipython3
df = pd.read_csv(innfil, sep=";")
df['dato'] = pd.to_datetime(df['TIME_PERIOD'], format='%Y-%m-%d')

df['kurs'] = df['OBS_VALUE'].str.replace(',', '.')
df['kurs'] = pd.to_numeric(df['kurs'])
```

```{code-cell} ipython3
# Neste steg er å dra ut søyler for kvar valuat.  No skal me
# berre sjå på pund og danske kroner.
```

```{code-cell} ipython3
gbp = df[ df["BASE_CUR"] == "GBP" ]
gbp = gbp.reset_index()
gbp["GBP"] = gbp["kurs"]
gbp = gbp.filter( items= [ "dato", "GBP" ] )

dkk = df[ df["BASE_CUR"] == "DKK" ]
dkk = dkk.reset_index()
dkk["DKK"] = dkk["kurs"]
dkk = dkk.filter( items= [ "dato", "DKK" ] )
```

Desse to tabellane kan me fletta.

```{code-cell} ipython3
mrg = pd.merge( dkk, gbp, on="dato" )
print(mrg)
```

```{code-cell} ipython3
# Til slutt skriv me ut CSV-fila
mrg.to_csv(utfil, index=False)
```
