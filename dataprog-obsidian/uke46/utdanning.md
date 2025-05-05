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
import pandas as pd
import numpy
import requests
import json
from pyjstat import pyjstat


with open("utdanningsnivå.json", "r") as file:
    ssbquery_data = json.load(file)

print(ssbquery_data)
postURL = ssbquery_data["postUrl"]
ssbqury = ssbquery_data["queryObj"]
response = requests.post(postURL, json=ssbqury)
response.status_code
```

```{code-cell} ipython3
dataset = pyjstat.Dataset.read(response.text)
df = dataset.write("dataframe")
df_id = dataset.write("dataframe", naming="id")

df2 = df.copy()
```

```{code-cell} ipython3
df=df2.copy()
df["år"] = pd.PeriodIndex(df["år"], freq="Y")
df = df.pivot(index=["statistikkmål", "år"], columns=["utdanningsnivå"], values="value")
df["Høyere utdanning"] = df["Universitets- og høgskoleutdanning, 1-4 år (nivå 6)"]+df["Universitets- og høgskoleutdanning, over 4 år (nivå 7-8)"]
df=df.drop(columns=["Universitets- og høgskoleutdanning, 1-4 år (nivå 6)", "Universitets- og høgskoleutdanning, over 4 år (nivå 7-8)"])
df = df.astype({"Høyere utdanning": "float64"})
snitt = df.loc["Gjennomsnitt", "Høyere utdanning"]/2
sum = df.loc["Antall arbeidsforhold med lønn", "Høyere utdanning"]
ny = pd.concat([sum, snitt])
ny.index = df.index
df["Høyere utdanning"] = ny
```

```{code-cell} ipython3
df
```

```{code-cell} ipython3
import scipy.stats as spstat
snitt = df.loc["Gjennomsnitt", "Utdanningsnivå i alt"].mean()

res = spstat.ttest_1samp(df.loc["Gjennomsnitt", "Høyere utdanning"], snitt, alternative="greater")
res.pvalue
#res = spstat.ttest_ind(df.loc["Gjennomsnitt", "Høyere utdanning"],
#                 df.loc["Gjennomsnitt", "Utdanningsnivå i alt"],
#                 alternative='greater')


#Snittlønnen snittlønnen har veldig liten varians
```

```{code-cell} ipython3
dir(dataset)
```

```{code-cell} ipython3
with open("data2.json", "r") as file:
    ssbquery_data = json.load(file)

print(ssbquery_data)
postURL = ssbquery_data["postUrl"]
ssbqury = ssbquery_data["queryObj"]
response = requests.post(postURL, json=ssbqury)
response.status_code
```

```{code-cell} ipython3
dataset = pyjstat.Dataset.read(response.text)
df = dataset.write("dataframe")
df_id = dataset.write("dataframe", naming="id")

df2 = df.copy()
```

```{code-cell} ipython3
df = df2.copy()
df = df.drop(columns="statistikkvariabel")

df["år"] = pd.PeriodIndex(df["år"], freq="Y")
df = df.pivot(index=["utdanningsnivå", "år"], columns=["statistikkmål", "fagfelt"], values="value")
df.dropna(axis=0)
```

```{code-cell} ipython3
import numpy as np

from scipy.stats import norm

import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)

x = np.linspace(norm.ppf(0.00001),

                norm.ppf(0.9), 100)

ax.plot(x, norm.pdf(x),

       'r-', lw=5, alpha=0.6, label='norm pdf')
```

```{code-cell} ipython3
with open("annet-vinningsbrudd.json", "r") as file:
    ssbquery_data = json.load(file)

print(ssbquery_data)
postURL = ssbquery_data["postUrl"]
ssbqury = ssbquery_data["queryObj"]
response = requests.post(postURL, json=ssbqury)
response.status_code
```

```{code-cell} ipython3
dataset = pyjstat.Dataset.read(response.text)
df = dataset.write("dataframe")
df_id = dataset.write("dataframe", naming="id")

df2 = df.copy()
```

```{code-cell} ipython3
df = df2.copy()
df = df.drop(columns=["lovbruddstype", "statistikkvariabel"])
df["år"] = pd.PeriodIndex(df["år"], freq="Y")
df = df.pivot(index="år", columns="kjønn", values="value")
df["Totalt"] = df["Kvinner"]+df["Menn"]
df[["Kvinner", "Menn"]].plot()

t, p = spstat.ttest_ind(df["Menn"], df["Kvinner"], alternative="greater")
print(t, p)
alpha = 0.05

if p<alpha:
    print("Nullhypotese forkastes: Menn er mer sannynlig å være offer for annen vinningskriminalitet")
else:
    print("Nullhypotese beholdes: Menn er ikke mer sannsynlig å være offer for annen vinningskriminalitet")
```

```{code-cell} ipython3
d2016 = df.loc["2023"]
p_menn = d2016["Menn"]/d2016["Totalt"]
n = d2016["Totalt"]

res = spstat.binomtest(d2016["Menn"], n, p=0.5, alternative="greater")

print(f"p-verdi = {res.pvalue}")
df["diff"] = df["Menn"]-df["Kvinner"]
df.sort_values("diff")
n_menn = df.loc["2014", "Menn"]
n = df.loc["2014", "Totalt"]
```

```{code-cell} ipython3

df
```

```{code-cell} ipython3
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

ax = df.plot.scatter(x="Menn", y="Kvinner")

model = LinearRegression()
model.fit(df[["Menn"]], df["Kvinner"])

df["Modell"] = model.predict(df[["Menn"]])
plt.plot(df["Menn"], df["Modell"])

#Gir det mening? Nei
```

```{code-cell} ipython3
import statsmodels.stats.proportion as smp

# Parameters
n = float(df.loc["2023", "Totalt"])# total number of trials
k = float(df.loc["2023", "Menn"])  # observed number of successes
confidence_level = 0.95  # 95% confidence interval

# Calculate the confidence interval for p
ci_low, ci_high = smp.proportion_confint(count=k, nobs=n, alpha=1-confidence_level, method='wilson')
print(f"Estimated p: {k/n}")
print(f"{confidence_level*100}% Confidence Interval: ({ci_low}, {ci_high})")
```

```{code-cell} ipython3

```

```{code-cell} ipython3

```
