---
jupytext:
  formats: md:myst,ipynb
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.18.1
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
# TEST Metadata ssb
import requests
from pyjstat import pyjstat

tabell = "08484"
url = f"https://data.ssb.no/api/v0/no/table/{tabell}"
#url = f"https://data.ssb.no/api/v0/no/console/meta/table/{tabell}"
print(url)
respons = requests.get(url)
```

```{code-cell} ipython3
import pandas as pd
meta_data = respons.json()
variabler = meta_data["variables"]
"""
for var in variabler:
    print(var.keys())
    print("kode", var["text"])
    print("Verditekst", var["valueTexts"])

"""
meta_data2 = {"Variabelkode": variabler[0]["values"], "Variabelnavn": variabler[0]["valueTexts"]}


df = pd.DataFrame(data=meta_data2)
df
```

```{code-cell} ipython3
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
items = df.query("Variabelnavn.str.contains('tyveri', case=False)")["Variabelkode"].values
```

```{code-cell} ipython3

```

```{code-cell} ipython3

```

```{code-cell} ipython3
meta_data
```

```{code-cell} ipython3
import json

ssb_query_str = """
{
  "query": [
    {
      "code": "LovbruddKrim",
      "selection": {
        "filter": "item",
        "values": [
          "1AAAAA-9ZZZZz",
          "1AAAAA-1ZZZZz",
          "2AAAAA-2ZZZZz",
          "BIZZZ",
          "BZZZZ"
        ]
      }
    },
    {
      "code": "ContentsCode",
      "selection": {
        "filter": "item",
        "values": [
          "AnmeldteLovbrudd",
          "AnmLovbrPer1000"
        ]
      }
    },
    {
      "code": "Tid",
      "selection": {
        "filter": "item",
        "values": [
          "1993",
          "1994",
          "1995",
          "2022",
          "2023"
        ]
      }
    }
  ],
  "response": {
    "format": "json-stat2"
  }
}
"""
ssb_query = json.loads(ssb_query_str)
ssb_query["query"][0]["selection"]["values"] = list(set(items))
ssb_query
```

```{code-cell} ipython3
respons_query = requests.post(url, json=ssb_query)
respons_query.status_code
```

```{code-cell} ipython3
ds = pyjstat.Dataset.read(respons_query.text)
df = ds.write('dataframe')
df_id = ds.write('dataframe', naming='id')
df =df.set_index(["statistikkvariabel", "lovbruddstype", "år"])
df[~df.duplicated()]
df
```

```{code-cell} ipython3

```
