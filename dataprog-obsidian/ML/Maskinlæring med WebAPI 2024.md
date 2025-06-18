---
jupytext:
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

## Eksempel med lineær regresjon

```{code-cell} ipython3
import json
import requests
from pyjstat import pyjstat
def hent_dataset(filnavn):
    with open(filnavn, 'r') as file:
        ssbAPIdata = json.load(file)

    postUrl = ssbAPIdata["postUrl"]
    tabellnummer = ssbAPIdata["tableIdForQuery"]
    query = ssbAPIdata["queryObj"]
    print(f"Henter data fra tabell {tabellnummer}")
    response = requests.post(postUrl, json=query)

    if response.status_code == 200:
        print("Data hentet: OK")
    else:
        print(f"""Data kunne ikke hentes, feilkode {response.status_code}
        Responstekst: response.text""")
        return None

    dataset = pyjstat.Dataset.read(response.text)
    df = dataset.write("dataframe")
    df_id = dataset.write("dataframe", naming="id")

    print(f"""Hentet dataset: {dataset['label']}""")
    return df, df_id, dataset

df, df_id, ds = hent_dataset("innenlandslanegjeld.json")
df_copy=df.copy()
df
```

```{code-cell} ipython3
df = df_copy.copy()
df = df.drop(columns=["låntakersektor", "statistikkvariabel"])
df["måned"] = pd.to_datetime(df["måned"], format="%YM%m")
df = df.rename(columns={"value": "Innenlandsk lånegjeld"})
df=df.set_index("måned")
display(df)
df.plot()
##
df_linje = df.loc["2004":]
df_linje.plot()
```

```{code-cell} ipython3
from sklearn.linear_model import LinearRegression

data = df_linje.reset_index()
data["dager"] = data["måned"] - data.loc[0,"måned"] #Ny kolonner med dager siden "start"
data["dager"] = data["dager"].dt.days # Fikser slik at dagene er flyttall

X = data[["dager"]] #Velger uavhengige variabler (dager siden start)
y = data["Innenlandsk lånegjeld"] #Velger avhengig variabel (mål)

modell = LinearRegression() # Lager en lineær regresjonsmodell
resultat = modell.fit(X,y) #Tilpasser modell til data (læring)
data["regresjon"] = modell.predict(X) # Bruker modell til å anslå avhengig variabel
ax = data.plot(x="måned", y="regresjon")
data.plot(x="måned", y="Innenlandsk lånegjeld", ax=ax)

Rsquared = modell.score(X,y) #Score med hvor godt linjen "passer"
```
