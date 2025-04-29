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

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

# Listekomprehension

+++ {"editable": true, "slideshow": {"slide_type": "fragment"}}

### Snarvei til å lage lister, set og dictionaries

+++ {"editable": true, "slideshow": {"slide_type": "fragment"}}

* Liste:
  ```python
  [ uttrykk for element in samling if betingelse]
  ```
  * Set:
  ```python
  { uttrykk for element in samling if betingelse}
  ```
  * Dictionary:
  ```python
  { utrykk_key: uttrykk_value for element in samling if betingelse ]
  ```

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

Standard måte å lage liste på:

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: fragment
---
import matplotlib.pyplot as plt
#Plot saldo på sparekonto

def forrentning(P,r,t):
    return P*(1+r)**t

n_tid = 10
tid = list(range(n_tid))
saldo = []
start = 1000
rente = 0.05
for t in tid:
    ny_saldo = forrentning(start, rente, t)
    saldo.append(ny_saldo)

plt.plot(tid, saldo)
plt.show()
```

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

Med listekomprehensjon

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: fragment
---
import matplotlib.pyplot as plt
import numpy as np


def forrentning(P,r,t):
    return P*(1+r)**t

n_tid = 10
start = 1000
rente = 0.05

tid = [ t for t in range(n_tid)]
saldo = [forrentning(start, rente, t) for t in tid]

start_aar = 2023
tid_aar = [f"01.01.{start_aar+t}" for t in tid if t%2 == 0]
print(tid_aar)
plt.bar(tid, saldo)
plt.xticks(ticks=np.arange(0,10,2), labels=tid_aar, rotation=45) 
plt.show()

```

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

* Ofte er slike listekomprehensjoner lette og lese, skrive og forstå
* Man må passe på ikke ta av -- de kan bli kompliserte og vanskelige å forstå

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

Man lager `set` på akkura samme måte

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: fragment
---
import json
with open("kundedata1.json", 'r') as file:
    kundedata = json.load(file)


alle_etternavn = {kunde["etternavn"] for kunde in kundedata}
etternavn_H = {kunde["etternavn"] for kunde in kundedata if kunde["etternavn"][0] == 'H'}
print(etternavn)

```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: subslide
---

#Kan bli vanskelig å lese eller for komplisert
#Dictionary av alle kunder med etternavn som begynner på 'H'
H_klubben = { navn: [kunde["fornavn"] for kunde in kundedata if kunde["etternavn"] == navn] 
             for navn in etternavn_H }

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

H_klubben = { navn: finnKunde(navn) for navn in etternavn_H}

with open("kundedata_test.json", 'w') as file:
    json.dump(H_klubben, file)
```

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

## Oppg:
* Bruk komprehensjon til å lage en dictionary som inneholder allekunder med startsaldo større enn 120,000
* Dictionary skal bestå av nøkler som tilsvarer etternavnet til kundene, og verdiene skal være en liste med kundene på samme format som originalt

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: fragment
---
grense = 120e3
#lag liste med rike kunder
#lag set med etternavnene
#lag dictionary med kunder { kundensetternavn: [liste med kunder]}
rike_kunder = [ kunde for kunde in kundedata if kunde["startsaldo"] > grense]
etternavn_rik = {kunde["etternavn"] for kunde in rike_kunder}
data_rike_kunder = {navn: [kunde for kunde in rike_kunder if kunde["etternavn"] == navn] for navn in etternavn_rik}
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: fragment
---
data_rike_kunder
```

```{code-cell} ipython3

```
