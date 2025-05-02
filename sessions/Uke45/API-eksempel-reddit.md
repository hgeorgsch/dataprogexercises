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

# API eksempel: Reddit
* [https://www.reddit.com/prefs/apps](https://www.reddit.com/prefs/apps) -- Applikasjonsside til redditkontoen din
* (Ikke lett å finne på nett)
* Du må:
  1. Lage en redditkonto
  2. Gå inn på nettsiden over
  3. Lag en "app" og hent klientkoden (Under app-navnet) og "secret" koden
  4. url redirect kan være hva som helst

```{code-cell} ipython3
import requests
```

```{code-cell} ipython3
secret = "2qamP2_KAEG7eNkXMwrJPhbb6jxzKw" # Fra /prefs/apps
client = "v2uZeXUHIszhF2K4hNOksQ" # Fra /prefs/apps

auth_reddit = requests.auth.HTTPBasicAuth(client, secret) # Slår sammen client og secret på en spesiell måte med B64-tegnkoding

url_auth  = "https://www.reddit.com/api/v1/access_token" # URL for å hente access token

with open("passord.txt", "r") as file: #Jeg leser inn redditpassordet mitt fra fil
    passord = file.read()

# Data som skal bli med http-requesten vår
data = {
    "grant_type": "password", "username": "jonajh", "password": passord
}
# header inneholder kun user-agent nå -- skal si noe om hvem som bruker applikasjonen
headers={"User-Agent": "IIRA2001 demo"}

# Send forespørel etter access token
response = requests.post(url_auth, data=data, auth=auth_reddit)
response.json()
```

```{code-cell} ipython3
access_token = response.json()["access_token"]
headers["Authorization"] = f"bearer {access_token}" # Legg till access token i headeren
```

```{code-cell} ipython3
base_url = "https://oauth.reddit.com"
params = {"limit": 10, "q": "Donald Trump", "sort": "hot"}
res1 = requests.get(f"{base_url}/search", params=params, headers=headers)
```

```{code-cell} ipython3
qdata = res1.json()
qdata["data"]["children"][0]["data"]["id"]

post_ids = []
for post in qdata["data"]["children"]:
    post_ids.append(post["data"]["id"])

```

```{code-cell} ipython3
article = post_ids[0]

params = {"article": article, "depth": 1, "limit":10, "sort":"top"}
result2 = requests.get(f"{base_url}/comments/article", params=params, headers=headers)
```

```{code-cell} ipython3
import pprint
import json
import time

pp = pprint.PrettyPrinter(indent=2)

comments = result2.json()

def HentKommentarer(comments):

    kommentarer = []
    for comment in comments[1]["data"]["children"]:
        if comment["kind"] == "t1":
            print(comment["data"]["body"])
            kommentarer.append(comment["data"]["body"])
    return kommentarer


artikkel_kommentarer = []
for article in post_ids:
    params = {"article": article, "depth": 1, "limit":10, "sort":"top"}
    resultat = requests.get(f"{base_url}/comments/article", params=params, headers=headers)
    koms = HentKommentarer(resultat.json())
    artikkel_kommentarer.append(koms)


pp.pprint(artikkel_kommentarer)
```

```{code-cell} ipython3
comments[1]
```
