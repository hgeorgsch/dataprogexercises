### Web-APIer: Autentisering


![](Slides/slidefig/doors-keycards.jpg)




---

## Hvorfor autentisering?

<split even>

::: block

* **Identifisering**
* **Ressursstyring**
* **Personvern**
* **Betaling**

::: 

::: block

![](Slides/slidefig/robot-guard.jpg)

:::

</split>

---
###  Case 1: De åpne dataene (SSB, Eurostat)

![](Slides/slidefig/ssb-case.jpg)


---

### Case 1: De åpne dataene (SSB, Eurostat)


* **Type:** Ingen autentisering
* **Sikkerhet:** Åpent for alle
* **Eksempel:** Statistisk sentralbyrå (SSB).
* **Bruk:** Du sender bare en `GET` eller `POST` forespørsel, og får data i retur.
* **Begrensning:** Du kan bli blokkert, for ssb kan er grensen 30 spørringer per minutt (per ip-adresse)



---

```{python}
import requests
ssb_url = "https://www.ssb.no/statbank/sq/10118503"
for i in range(40):
    res = requests.get(ssb_url)
    if not res.status_code == 200:
        print("statuskode", res.status_code)
        print(res.headers)
        break
```
```bash
statuskode 429
{'Date': 'Tue, 13 Jan 2026 10:57:00 GMT', 'Server': '',
 'X-Varnish': '145346560', 'X-Ratelimit-Resource': 'SB_SQ',
 'X-Ratelimit-Limit': '10', 'X-Ratelimit-Policy': '10;w=10s',
 'Retry-After': '4.672', 'Content-Length': '0',
 'Via': '1.1 google', 
 'Alt-Svc': 'h3=":443"; ma=2592000,h3-29=":443"; ma=2592000'}
``` 


---
### Case 2: "Nøkkelen i døra" (API-nøkler)

![](Slides/slidefig/apikey-stolen.jpg)



---

### Case 2: "Nøkkelen i døra" (API-nøkler)
* **Type:** API Key / Token
* **Konsept:** En unik tekststreng du får fra leverandøren.
* **Eksempel:** OpenWeather, Google Maps, eller ChatGPT.
* **Slik virker det:**
  `headers = {"X-API-KEY": "din_hemmelige_nøkkel"}`
* **Risiko:** Hvis nøkkelen kommer på avveie, kan hvem som helst bruke din kvote/konto.

---

### Case 3: OAuth 2.0

![](Slides/slidefig/oauth-flow.jpg)


---
## Case 3: OAuth 2.0
* **Type:** Delegert autorisasjon
* **Case:** Spotify eller Google Analytics.
* **Konsept:** Appen din får *lov* av brukeren til å hente data på deres vegne, uten at appen får vite brukerens passord.
* **Nøkkelord:** `Access Token` – en midlertidig nøkkel som går ut på tid.
* `Access Token`- har begrenset *scope* (Tillatelser)

---

### Eksempel: Spotify 
#### 1: Bruker logger inn
```{python}
client_id = "fd5f36cc0ee14678ae37d086ebaf76b2"
client_secret = "«HOLD HEMMELIG»"
auth_url = "https://accounts.spotify.com/authorize"
redirect_uri = "localhost:8888"

scopes = " ".join(["playlist-read-private",
"playlist-modify-public",... ])
parametre = {"client_id": client_id,
             "response_type": "code",
             "redirect_uri": redirect_uri,
             "scope": scopes
            }
res = requests.get(auth_url, params=parametre)
print(res.url)
```

---
#### 2: Applikasjon får "kvittering"
![](Slides/slidefig/spotify-auth-code.jpg)

---

#### 3: Applikasjon bytter kvittering mot «tokens»

```{python}
import base64
token_url = "https://accounts.spotify.com/api/token"
code = "AQAkCxEaNqL4AQ7CaXffc9xH6BDWUZwud0fw"
basic = base64.b64encode(
	f"{client_id}:{client_secret}".encode()).decode()
	
headers = { "Authorization": f"Basic {basic}",
    "Content-Type": "application/x-www-form-urlencoded",}

data = { "grant_type": "authorization_code",
    "code": code, "redirect_uri": redirect_uri}
	
r = requests.post(token_url, headers=headers, data=data)
tokens = r.json()
print(tokens)
```

---

#### 4: Applikasjon bruker tokens til å styre spotify konto

```json
{'access_token': 'BQPBX5hj1....XL2RiyS032G1oQ',
 'token_type': 'Bearer',
 'expires_in': 3600,
 'refresh_token': 'AQDSCOrdtj....okhlYSfpnw',
 'scope': 'playlist-read-private ...'}
```
```{python}
#Hent info om innlogget konto
konto_info_url = "htthps://api.spotify.com/v1/me"
headers = {"Authorization": f"Bearer {tokens['access_token']}
"}
res = requests.get(konto_info_url, headers=headers)
```


---

## Oppsummering

![[Pasted image 20260113122506.png]] 