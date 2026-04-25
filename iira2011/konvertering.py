# ---
# jupyter:
#   jupytext:
#     default_lexer: ipython3
#     formats: md:myst,ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.19.1
#   kernelspec:
#     display_name: dataprog
#     language: python
#     name: dataprog
# ---

# %% [markdown]
# # Formatering av valutakursar
#
# Dette programmet skal laga ein CSV-fil med valutakursar,
# der kvar valuta har ei søyle.  Utgangspunktet er fila
# frå 
# [Noregs Bank](https://www.norges-bank.no/tema/Statistikk/Valutakurser/?tab=api).
#
# Programmet fylgjer øvinga «Fyrste datasett i CSV».
#
# Fyrst importane

# %%
import pandas as pd

# %% [markdown]
# No er det greit å definera dei filene me skal bruka, både innfil og utfil.

# %%
innfil = "EXR20250401.csv"
utfil = "EXR-formattert.csv"

# %% [markdown]
# So kjem skjølve programmet.
# Eg har klipt ned koden frå den gamle øvinga.
# Fyrst kan me fiksa dato- og kurssøylene.

# %%
df = pd.read_csv(innfil, sep=";")
df['dato'] = pd.to_datetime(df['TIME_PERIOD'], format='%Y-%m-%d')

df['kurs'] = df['OBS_VALUE'].str.replace(',', '.')
df['kurs'] = pd.to_numeric(df['kurs'])

# %%
# Neste steg er å dra ut søyler for kvar valuat.  No skal me
# berre sjå på pund og danske kroner.

# %%
gbp = df[ df["BASE_CUR"] == "GBP" ]
gbp = gbp.reset_index()
gbp["GBP"] = gbp["kurs"]
gbp = gbp.filter( items= [ "dato", "GBP" ] )

dkk = df[ df["BASE_CUR"] == "DKK" ]
dkk = dkk.reset_index()
dkk["DKK"] = dkk["kurs"]
dkk = dkk.filter( items= [ "dato", "DKK" ] )

# %% [markdown]
# Desse to tabellane kan me fletta.

# %%
mrg = pd.merge( dkk, gbp, on="dato" )
display(mrg)

# %%
# Til slutt skriv me ut CSV-fila
mrg.to_csv(utfil, index=False)
