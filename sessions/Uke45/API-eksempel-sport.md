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

### API-eksempel sport


```{code-cell} ipython3
import requests
import json

API_key = "31d5cf4a12d29e845d6b08db3ede0685"
team_url = "https://v3.football.api-sports.io/teams/statistics"
aafk_id = 757
liga_id = 103
sesong = 2022

params = {
    "league" : liga_id,
    "season": sesong,
    "team": aafk_id
}
headers = {"x-apisports-key": API_key}
result = requests.get(team_url, params=params, headers = headers)
data = result.json()
```

```{code-cell} ipython3
import pprint
import matplotlib.pyplot as plt
import pandas as pd
pp = pprint.PrettyPrinter()
#pp.pprint(data["response"])

oversikt = data["response"]["fixtures"]
pp.pprint(oversikt)

df = pd.DataFrame(data=oversikt)
df

df.plot.bar()
df
```
