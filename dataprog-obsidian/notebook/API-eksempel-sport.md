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

# EKSEMPEL: api-sports.io

* VI går gjennom hvordan vi bruker [https://api-sports.io/](https://api-sports.io/)
* Vi forsøker å gjøre opptak siden det er mye hopping rundt i dokumentasjon på nett


```python
import pandas as pd
import requests, json
```

```python
# Logg inn, finn API-nøkkel og send spørring etter ligaider


API_key = "b9d2d72f4a09ace62c145a0b2d72bd43"
league_url = "https://v3.football.api-sports.io/leagues"

headers = {"x-apisports-key": API_key}

params = {"country": "Norway"}

response = requests.get(league_url, params=params, headers=headers)


```

```python
print("status", response.status_code)
data = response.json()
data
# Se status og data
```

```python
liga_id = 103
```

```python
# Finn lagID
team_url = "https://v3.football.api-sports.io/teams"
params = {"league": liga_id, "season": 2023}
response = requests.get(team_url, params=params, headers=headers)


```

```python
# Finn Bla igjennom data og finn LAGID

print("Status", response.status_code)
data = response.json()

for lag in data["response"]:
    print("Lag og id", lag["team"]["name"], lag["team"]["id"])
```

```python
# Hent statistikk for lag
url = "https://v3.football.api-sports.io/teams/statistics"
team_id = 757
params = {"league": liga_id, "season": 2023, "team": team_id}
response = requests.get(url, params=params, headers=headers)


```

```python
# Sjekk status -- plott noe data
print("status:", response.status_code)
data = response.json()
df = pd.DataFrame(data["response"]["fixtures"])
df.plot.bar()
```

```python

```
