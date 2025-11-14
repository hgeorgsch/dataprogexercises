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
tags:
   - legacy/iif
---

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

# Mer om hashmaps (dictionaries)

* Vi lagde hashmaps/dictionaries slik:


```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: fragment
---
persondata = {"navn": "Jonas", "yrke": "lærer", "lønn": False}
```

+++ {"editable": true, "slideshow": {"slide_type": "fragment"}}

* Vi bruker "keys" til å slå opp i verdiene

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: fragment
---
persondata["navn"]
```

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

Vi kan liste opp alle nøklene slik ved å bruke .keys() og alle verdiene med .values()

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: fragment
---
print(persondata.keys())
print(persondata.values())
```

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

* Vi kan legge til nye felt ved å "slå opp" med den nye nøkkelen og sette dataen vi vil ha der

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: fragment
---
persondata["enliste"] = [1,2,3,4]
print(persondata)
```

+++ {"editable": true, "slideshow": {"slide_type": "fragment"}}

* Vi sletter key/value med `del` slik

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: fragment
---
del persondata["enliste"]
print(persondata)
```

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

* Vi kan gå iterere igjennom en dictionary ved bruk av `.items()` som gir en liste med tuple-par av "nøkkel"/verdi

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: fragment
---
for key, value in persondata.items():
    print(f"Nøkkel {key} har verdi {value}")
```

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

* Hver gang vi legger til eller fjerner et felt fra hashmappet må python fikse "hashingen"
   ![tekst](https://www.boardinfinity.com/blog/content/images/2023/03/HashMap-in-Python.png)
* Dersom vi skal legge til mange felt er det derfor greit å bruke `.update({  ... })`

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: subslide
---
print(persondata)
ny_data = {"Saldo": 1003, "hobbier": {"jakt", "fiske", "fiskejakt"}}
persondata.update(ny_data)
print(persondata)
```

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

### Knep for å printe ut store dictionary litt finere

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: fragment
---
import pprint as pprint
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(persondata)
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: subslide
---
ny_data = { "studier" : {"Fysikk": ["Trondheim", "Gjøvik"], "informatikk": "Bergen", "PPU": "Bergen"}}
persondata.update(ny_data)
#print(persondata) #Vanskelig å lese
pp.pprint(persondata)
```

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

* Vi bruker `[]` flere ganger for å slå opp i nøstede dictionaries:

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: fragment
---
pp.pprint(persondata)
persondata['studier']["Fysikk"][0]
```

# EKSEMPEL Sparekalkulator

```{code-cell} ipython3
import json
with open("kundedata1.json", 'r') as file:
    kundedata = json.load(file)
info = f"""Listen inneholder data om {len(kundedata)} kunder.
For hver kunde har vi data om {list(kundedata[0].keys())}"""
print(info)
```

```{code-cell} ipython3
pp.pprint(kundedata[:10])
```

```{code-cell} ipython3
#Lag funksjon som søker opp kunde gitt et etternavn og gir tilbake en liste over kunder med gitt etternavn

def finnKunde(etternavn):
    treffliste = []
    for kunde in kundedata:
        if etternavn == kunde["etternavn"]:
            treffliste.append(kunde)
    if treffliste == []:
        print(f"Ingen kunder med etternavn '{etternavn}' funndet")
        return None
    else:
        print(f"Vi fant {len(treffliste)} kunder med etternavn '{etternavn}'")
        return treffliste

pp.pprint(finnKunde('Husøy'))


```

```{code-cell} ipython3
# Lag sparefunksjon
# Tar terminbeløp, antall terminer i året, rente og startsaldo og gir sluttsaldo
def sluttsaldo(P,r,n,startsaldo,t):
    rn=r/n
    F = P*((1+rn)**(n*t)-1)/rn
    return F + startsaldo*(1+r)**t
```

```{code-cell} ipython3
# Gå over kundelisten og legg inn sluttsaldo
# Vi sparer 1000kr/mnd, i 10 år, p.a. rente på 5%
P = 1000
r = 0.1
n=12
t_slutt = 10

for kunde in kundedata:
    startsaldo = kunde["startsaldo"]
    kunde["sluttsaldo"] = sluttsaldo(P,r,n,startsaldo,t_slutt)
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
# Iterer over listen og legg til en liste med årlig saldo fra start til sluttå for alle kunder

for kunde in kundedata:
    saldo = []
    for t in range(t_slutt+1):
        saldo_t = sluttsaldo(P,r,n,kunde["startsaldo"], t)
        saldo.append(saldo_t)
    kunde["saldo_liste"] = saldo

pp.pprint(kundedata[:5])
        
```

```{code-cell} ipython3
# Plott fordelingen av sparepenger i et histogram
import matplotlib.pyplot as plt

sluttsaldo_liste = []
startsaldo_liste = []
for kunde in kundedata:
    sluttsaldo_liste.append(kunde["sluttsaldo"])
    startsaldo_liste.append(kunde["startsaldo"])

plt.hist(sluttsaldo_liste, bins=20, label="Sluttsaldo")
plt.hist(startsaldo_liste, bins=20, label="Startsaldo")
plt.legend()
plt.show()

```

```{code-cell} ipython3
#Finn en måte å dele kundene inn i segmenter: rik, middels bemidlet, lavt bemidlet, etter hvor mye sparepenger de har
#Oppdater kundedata med klassifiseringen
#Lag et kakediagram over kundegruppen før og etter sparing

n_kunder  = len(startsaldo_liste)

snitt_start = sum(startsaldo_liste)/n_kunder
minste_start = min(startsaldo_liste)
max_start = max(startsaldo_liste)

snitt_slutt = sum(sluttsaldo_liste)/n_kunder
minste_slutt = min(sluttsaldo_liste)
max_slutt = max(sluttsaldo_liste)

print(f"""I snitt har kundene {snitt_start:.0f} kr på konto ved start
Kunden med lavest saldo har {minste_start:.0f} på konto
Kunden med høyest saldo har {max_start:.0f} på konto""")


print(f"""
I snitt har kundene {snitt_slutt:.0f} kr på konto ved slutt
Kunden med lavest saldo har {minste_slutt:.0f} på konto
Kunden med høyest saldo har {max_slutt:.0f} på konto""")

#Forslag: 50% over middelverdi er rik, 50% under middelverdi er lavt bemidlet

segmenter = {"rik": 1.3, "middels": None, "lav": 0.7}

data = {"segmenter": segmenter, "antall": n_kunder, 
        "middelsaldo": {"start": snitt_start, "slutt": snitt_slutt},
        "max": {"start": max_start, "slutt": max_slutt},
        "min": {"start": minste_start, "slutt": minste_slutt},
        "kunder": kundedata,
        "segment_storrelse": {"start": {"rik": 0, "middels": 0, "lav": 0},
                              "slutt": {"rik": 0, "middels": 0, "lav": 0}
                             }
                              
       }
def kalk_segmentstorrelse(start_slutt):
    for kunde in data["kunder"]:
        if data["middelsaldo"][start_slutt]*data["segmenter"]["rik"]<=kunde[f"{start_slutt}saldo"]:
            kunde["segment"]="rik"
            data["segment_storrelse"][f"{start_slutt}"]["rik"] += 1
        elif data["middelsaldo"][f"{start_slutt}"]*data["segmenter"]["lav"] >= kunde[f"{start_slutt}saldo"]:
            kunde["segment"]="lav"
            data["segment_storrelse"][f"{start_slutt}"]["lav"] += 1
        else:
            kunde["segment"] = "middel"
            data["segment_storrelse"][f"{start_slutt}"]["middels"] += 1
    


kalk_segmentstorrelse("start")
kalk_segmentstorrelse("slutt")

segmentstorrelse = data["segment_storrelse"]["start"].values()
segmentstorrelse_labels = data["segment_storrelse"]["start"].keys()
plt.pie(segmentstorrelse, labels=segmentstorrelse_labels)
plt.show()

segmentstorrelse = data["segment_storrelse"]["slutt"].values()
segmentstorrelse_labels = data["segment_storrelse"]["slutt"].keys()
plt.pie(segmentstorrelse, labels=segmentstorrelse_labels)
plt.show()
```

```{code-cell} ipython3

```

```{code-cell} ipython3

```
