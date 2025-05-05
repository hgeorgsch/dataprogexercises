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

```{code-cell} ipython3
import json
import requests
from pyjstat import pyjstat
import pandas as pd


with open("skaddeitrafikk.json", "r") as file:
    ssbquery_data = json.load(file)

ssbquery = ssbquery_data["queryObj"]
postUrl  = ssbquery_data["postUrl"]
tabellnummer = ssbquery_data["tableIdForQuery"]

response_ssb = requests.post(postUrl, json=ssbquery)
```

```{code-cell} ipython3
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

dataset = pyjstat.Dataset.read(response_ssb.text)
df = dataset.write("dataframe")
df_id = dataset.write("dataframe", naming="id")

df["måned"] = pd.to_datetime(df["måned"], format="%YM%m")
df=df.pivot(index=["kjønn", "måned"], columns="statistikkvariabel", values="value")

df_kvinner = df.loc["Kvinner"]
df_menn = df.loc["Menn"]
    
verdier = set(df.index.get_level_values(level=0))
verdier

fig, ax = plt.subplots(1,1)
moving_avg = []
for kj in verdier:
    df.loc[kj].rolling(window=datetime.timedelta(weeks=12*4)).mean().plot(ax=ax, label="12mnders snitt")
    moving_avg.append(df.loc[kj].rolling(window=datetime.timedelta(weeks=12*4)).mean())
    #print(list(df.loc[kj].rolling(window=datetime.timedelta(weeks=12*4))["Personer drept eller skadd"]))

moving_avg.reverse()
s = pd.concat(moving_avg)
s.index = df.index
df2 = df.copy()
df2["Glidende snitt"] = s
plt.title("12 måneders snitt")
plt.show()
df2.loc["Kvinner"].plot()
```

```{code-cell} ipython3
import numpy as np
from sklearn.linear_model import LinearRegression

ax = df2.xs("Menn", level=0).reset_index().plot.scatter(x="måned", y="Personer drept eller skadd")
display(df.xs("Menn", level=0).reset_index().corr())


df_kvinner = df.xs("Kvinner", level=0)
df_menn = df.loc["Menn"]

x = df_menn.reset_index()[["måned"]]
x["tid"] = x["måned"]-x["måned"].iloc[0]
x["tid"] = x["tid"].dt.days
x = x[["tid"]]

y = df_menn[["Personer drept eller skadd"]]

y_k = df_kvinner[["Personer drept eller skadd"]]

model = LinearRegression()
model_k = LinearRegression()

reg = model.fit(x,y)
reg_k = model_k.fit(x,y_k)
print(reg.score(x,y))

df_menn["modell"] = model.predict(x)
df_menn["modell"].plot(ax=ax, color="orange")
df2.xs("Menn", level=0).reset_index().plot.scatter(x="måned", y="Personer drept eller skadd", ax=ax)

df_kvinner["modell"] = model_k.predict(x)
df_kvinner["modell"].plot(ax=ax,color="orange")
df2.xs("Kvinner", level=0).reset_index().plot.scatter(x="måned", y="Personer drept eller skadd", ax=ax, color="red")
```

```{code-cell} ipython3

```

```{code-cell} ipython3

```

```{code-cell} ipython3
ax = df.loc["Kvinner"].plot()
df.loc["Menn"].plot(ax=ax)
plt.legend(["Kvinner", "Menn"])
```

```{code-cell} ipython3
df["tid"] = df[:, "måned"]
```

```{code-cell} ipython3
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

dataset = pyjstat.Dataset.read(response_ssb.text)
df = dataset.write("dataframe")
df_id = dataset.write("dataframe", naming="id")

df["måned"] = pd.to_datetime(df["måned"], format="%YM%m")
df=df.pivot(index=["kjønn", "måned"], columns="statistikkvariabel", values="value")

df_kvinner = df.loc["Kvinner"]
df_menn = df.loc["Menn"]
```

```{code-cell} ipython3
vindu = pd.Timedelta(12*365/12, "d")
df_kvinner.plot()
ax = plt.gca()
df_kvinner.rolling(window=vindu).mean().plot(y="Personer drept eller skadd",label="12-mnd snitt", ax = ax)
plt.legend()
plt.show()
```
