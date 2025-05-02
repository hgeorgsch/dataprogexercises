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

# API eksempel:ChatGPT

```{code-cell} ipython3
import requests
```

## Kommentarfelt fra reddit (se eget eksempel)

```{code-cell} ipython3
secret = "2qamP2_KAEG7eNkXMwrJPhbb6jxzKw"
client = "v2uZeXUHIszhF2K4hNOksQ"
auth_reddit = requests.auth.HTTPBasicAuth(client, secret)

url_auth  = "https://www.reddit.com/api/v1/access_token"

with open("passord.txt", "r") as file:
    passord = file.read()

data = {
    "grant_type": "password", "username": "jonajh", "password": passord
}
headers={"User-Agent": "IIRA2001 demo"}

response = requests.post(url_auth, data=data, auth=auth_reddit)
response.json()
```

```{code-cell} ipython3
access_token = response.json()["access_token"]
headers["Authorization"] = f"bearer {access_token}"
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

# ChatGPT -- sentimentanalyse av redditkommentarer

```{code-cell} ipython3
import os

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"] #Lim inn din API-nøkkel om du vil sjekke
openai_url = "https://api.openai.com/v1/chat/completions"

headers = { "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
          }


chat_rolle ="""You do sentiment analysis.
People give you a list that contains lists of comments on reddit about a person. 
Each sublist represent a post in hot, the entries of the sublist is a comment on the post.
You respond with a corresponding list of lists that contains -1 if the comment is negative,
0 if it is neutral and 1 if it is positive"""

data = {"model": "gpt-4o",
        "messages": [{"role": "system", 
                          "content": chat_rolle
                     },
                     {"role": "user", "content": f"{artikkel_kommentarer}"}]
       }

response = requests.post(openai_url, headers=headers, json=data)
response.json()
```

```{code-cell} ipython3
sentiment_analyse = response.json()["choices"][0]["message"]["content"]
sentiment_analyse_conv =eval(sentiment_analyse)
sentiment_analyse_conv

artikkel_kommentarer[1]
```

```{code-cell} ipython3
sentiment_analyse_conv
```

```{code-cell} ipython3

```
