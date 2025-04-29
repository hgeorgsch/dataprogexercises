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

df = pd.read_csv("teina010_linear.csv", sep=",", encoding="utf-8")
df
```

```{code-cell} ipython3
import requests

url = "https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data"
dataset_kode = "teina010"

request_url = f"{url}/{dataset_kode}"
params = {"format": "JSON", "lang": "EN"}

response = requests.get(request_url, params=params)
```

```{code-cell} ipython3
from pyjstat import pyjstat
import matplotlib.pyplot as plt

dataset = pyjstat.Dataset.read(response.text)
df = dataset.write('dataframe')
df_id = dataset.write('dataframe', naming='id')
df = df.drop(["Time frequency",
             "National accounts indicator (ESA 2010)",
             "Seasonal adjustment", "Unit of measure"], axis=1)
df["Time"] = df["Time"].map(lambda x: pd.Period(x.replace("-", ""), freq='Q'))
df = df.set_index(["Geopolitical entity (reporting)", "Time"])
df.sort_index(level=[0,1])
df_total = df.groupby(by="Geopolitical entity (reporting)").sum()
df_total = df_total.reset_index()
df_total = df_total[~df_total["Geopolitical entity (reporting)"].str.contains("Euro")]
df_total = df_total.set_index("Geopolitical entity (reporting)")
minimum = df_total.drop("United Kingdom")["value"].min()
df_total[df_total["value"] > 20*minimum].plot.pie(subplots=True, legend=False)
print("minium", minimum)
df_total.index.str.contains("a")
```

```{code-cell} ipython3
from pyjstat import pyjstat
import matplotlib.pyplot as plt

dataset = pyjstat.Dataset.read(response.text)
df = dataset.write('dataframe')
df_id = dataset.write('dataframe', naming='id')
df = df.drop(["Time frequency",
             "National accounts indicator (ESA 2010)",
             "Seasonal adjustment", "Unit of measure"], axis=1)
df["Time"] = df["Time"].map(lambda x: pd.Period(x.replace("-", ""), freq='Q'))
df.to_csv("eu_GDP.csv", index=False)
```
