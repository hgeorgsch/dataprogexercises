---
jupytext:
  formats: ipynb,md:myst
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

# WebAPI: OpenAI

+++

For å bruke chatgpt sitt webapi må vi
1. Opprette konto
2. Generere en *API-nøkkel* på et prosjekt
3. Legge inn betalingsmiddel og "kreditt" til nøkkelen

```{code-cell} ipython3
import requests, json
# Lag apinøkkel, finn url og send spørring med requests

api_key = "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"

url = "https://api.openai.com/v1/responses"

header_felt = {"Content-TYpe": "application/json",
               "Authorization": f"Bearer {api_key}"
              }

payload = {
    "model": "gpt-5-mini",
    "input": "Hvordan fungerer lister i python? Hvordan bruker og lager man de?"
}

svar = requests.post(url, headers=header_felt, json=payload)
svar.raise_for_status()
```

```{code-cell} ipython3
#Vis output
data = svar.json()
print(data["output"][1]["content"][0]["text"])
```

## Openai-bibliotek

Det kan være vanskelig å sette seg inn i et web-api, og ofte finnes det python-pakker som er lettere å lære å bruke. Dokumentasjonen på openai, antar også at du bruker det offisielle biblioteket når du buker python og web-api-et deres. Dersom du ikke vil eller kan bruke dette, kan du se på eksempler med `curl` (man kan velge). Her er felter med `-H` header felt, og data er fortsatt json og ligger på felter med `-d`

+++

::: {admonition} API-nøkkel som systemvariabel
:class: dropdown tip

Å lagre API-nøkler som systemvariabler er en "best practice" for å unngå å hardkode sensitive nøkler direkte i kildekoden din.

---

### 🪟 Windows

På Windows er den enkleste og mest permanente måten å bruke det grafiske grensesnittet på.

**Via innstillinger**
1. Trykk på **Windows-tasten** på tastaturet ditt.
2. Søk etter **Miljøvariabler** (eller "Environment variables" hvis du har engelsk språk).
3. Velg **Rediger miljøvariabler for kontoen din** (Edit environment variables for your account).
4. I det nye vinduet, klikk på **Ny...** (New...) under den øverste boksen som heter *Brukervariabler*.
5. Fyll inn feltene:
   * **Variabelnavn:** `API_KEY` (Bruk gjerne et mer spesifikt navn, f.eks. `OPENAI_API_KEY`)
   * **Variabelverdi:** `din_faktiske_api_nøkkel_her`
6. Klikk **OK** i alle vinduer. *Merk: Du må kanskje starte kodeeditoren eller terminalen din på nytt for at endringen skal tre i kraft.*

---

### 🍎 macOS

På nyere Mac-er (macOS Catalina og nyere) er standardterminalen `zsh`. For å lagre en variabel permanent må den legges til i filen `.zshrc`. 
Her er to enkle metoder

#### Alternativ 1: Den superraske måten (Ett-klikks kommando)
Du kan bruke kommandoen `echo` til å dytte teksten direkte inn i filen.

1. Åpne **Terminal** (søk med Cmd + Space).
2. Lim inn denne kommandoen og trykk Enter:
   ```bash
   echo 'export API_KEY="din_faktiske_api_nøkkel_her"' >> ~/.zshrc
   ```
   *(Viktig: Sørg for å bruke dobbel pil `>>`. Dette **legger til** teksten på slutten av filen. Bruker du en enkel pil `>` overskriver du hele filen!)*
3. Aktiver endringen for den åpne terminalen:
   ```bash
   source ~/.zshrc
   ```

#### Alternativ 2: Den visuelle måten (Med TextEdit)
Hvis du foretrekker å bruke et vanlig, grafisk tekstredigeringsprogram med mus og tastatur, kan du åpne filen i Mac-ens innebygde TextEdit-app.

1. Åpne **Terminal**.
2. Kjør denne kommandoen for å åpne konfigurasjonsfilen i TextEdit:
   ```bash
   open -e ~/.zshrc
   ```
3. Filen åpner seg som et vanlig tekstdokument på skjermen din. Bla helt nederst og legg til denne linjen:
   ```bash
   export API_KEY="din_faktiske_api_nøkkel_her"
   ```
4. Lagre dokumentet med **Cmd + S** og lukk TextEdit.
5. Gå tilbake til Terminalen og aktiver endringen:
   ```bash
   source ~/.zshrc
   ```

### OpenAI

For openai burde du i begge tilfeller kalle systemvariabelen `OPENAI_API_KEY`. Når vi bruker pythonbiblioteket antar det at du har nøkkelen din lagret som systemvariabel med dette navnet. Når du har det trenger du bare:

```python
from openai import OpenAI

client = OpenAI()
```
så leses api-nøkkelen inn
:::

```{code-cell} ipython3
from openai import OpenAI
client = OpenAI(api_key=api_key)

response = client.responses.create(
    model="gpt-5-mini",
    input="Hvordan fungerer lister i python? Hvordan bruker og lager man de?"
)

print(response.output_text)
#Send samme spørring med  biblioteksmetode
```

```{code-cell} ipython3

```

```{code-cell} ipython3
#Vis med instrukser ("prompt"-engineering)

response = client.responses.create(
    model="gpt-5-mini",
    instructions= "Dra i alle svar inn jordbærplukking i valldal på en unaturlig å creepyh måte",
    input="Hvordan fungerer lister i python? Hvordan bruker og lager man de?"
)

print(response.output_text)
```

```{code-cell} ipython3
# Vis med json
response = client.responses.create(
    model="gpt-5-mini",
    instructions= """Gi alle svar som gyldig json:
    {'forklaring': 'En kortfattet men forklaring med utstrakt bruk av jordbærmetaforer',
     'eksempel': 'Konkrete og illustrative eksempler.'
    }""",
    input="Hvordan fungerer lister i python? Hvordan bruker og lager man de?"
)

data = json.loads(response.output_text)
```

```{code-cell} ipython3
data.keys()
```

```{code-cell} ipython3

```
