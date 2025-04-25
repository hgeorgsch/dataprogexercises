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

+++ {"slideshow": {"slide_type": "slide"}}

# Simulering og modellering

+++ {"slideshow": {"slide_type": "fragment"}}

## Pseudotilfeldig tallgenerator

+++ {"slideshow": {"slide_type": "fragment"}}

* Når man skal kjøre simuleringer på datamaskin trenger man ofte å bruke tilfeldige tall
* Vi trenger elementer av tilfeldighet i simuleringene våres for å beskrive prossesser vi ikke kan forklare analytisk/matematisk
* Dette gjelder både i ingeniørfagene, men spesielt når man skal modellere *mennesklig adferd*

+++ {"slideshow": {"slide_type": "subslide"}}

![newton](https://pbs.twimg.com/media/D2EZ4DwVAAApNdd?format=jpg&name=900x900)

+++ {"slideshow": {"slide_type": "subslide"}}

* Faktisk tilfeldighet er vanskelig å oppdrive på kommando
* På datamaskinen gjør vi «mattetriks» til å generere tall som ser tilsynelatende tilfeldige ut
* I python finner vi metoder vi kan bruke i `random`biblioteket

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
import random
tilfeldig_tall = random.random()
#random() gir et "tilfeldig" flyttall mellom 0 og 1
print(f"Mitt tilfeldige tall er {tilfeldig_tall:.4f}")
```

+++ {"slideshow": {"slide_type": "subslide"}}

* De tilfeldige tallene regnes ut -- de bruker da en såkalt «*seed*» til å begynne utregningen
* Default er systemklokken på dataen -- men vi kan gi vår egen med `random.seed(«tall»)`

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
random.seed(10)
```

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
tilfeldig_tall = random.random()
#random() gir et "tilfeldig" flyttall mellom 0 og 1
print(f"Mitt tilfeldige tall er {tilfeldig_tall:.4f}")
```

+++ {"slideshow": {"slide_type": "subslide"}}

* Dersom man kan trekke et tilfeldig tall mellom 0 og 1, har man egentlig alt man trenger

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
import matplotlib.pyplot as plt
#EKs terningkast
def kast_terning():
    kast = int(random.random()*6)+1
    return kast

def kast_to():
    return kast_terning()+kast_terning()
print(kast_to())

mange_kast = []
for _ in range(10000):
    mange_kast.append(kast_to())

plt.hist(mange_kast, bins=11)
```

```{code-cell} ipython3
---
slideshow:
  slide_type: subslide
---
# Trekk tilfeldig element fra liste
def trekk_tilfeldig(liste):
    n = len(mange_kast)
    tilfeldig_indeks = int(random.random()*n)
    return liste[tilfeldig_indeks]

print(f"Tilfeldig element i listen er {trekk_tilfeldig(mange_kast)}")
```

+++ {"slideshow": {"slide_type": "subslide"}}

* Av og til må man lage egne rutiner slik som dette
* Andre ganger kan vi bruke en av de mange innebygde funksjonene i `random` biblioteket
* [Dokumentasjon, random](https://docs.python.org/3/library/random.html)

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
frukt = ["Epler", "Pærer", "Mango", "Dragefrukt", "Fruktdrage"] 
#Velg et utvalg av 10 frukter
fruktkurv = random.choices(frukt, k=10)
print(f"Fruktkurven vår består av: {fruktkurv}")

#Velg et tilfeldig heltall mellom 10 og 100
tilfeldig_heltall = random.randint(10,100)
print(f"Tilfeldig heltall er: ", tilfeldig_heltall)
```

```{code-cell} ipython3
---
slideshow:
  slide_type: subslide
---
# Trekk et tilfeldig tall fra en normalfordeling:
tall = random.gauss(mu=3, sigma=1.5)
mange_tall = []
for _ in range(10000):
    tilf_trekk = random.gauss(mu=3, sigma=1.5) 
    mange_tall.append(tilf_trekk)
plt.hist(mange_tall, bins=40)
plt.show()
```

+++ {"slideshow": {"slide_type": "slide"}}

# Simulere med `While`
* Vi har blitt ganske godt kjent med `for`-løkken
* Den bruker vi når vi skal gjøre noe «for» alle elementene i en samling
* Vi vet altså på forhånd hvor mange ganger løkken skal iterere

+++ {"slideshow": {"slide_type": "subslide"}}

* Dersom vi undersøker feks kundeadferd og bruker tilfeldige tall til å simulere avgjørelser vet man typisk ikke hvor mange ganger en løkke trenger å kjøre
* Da kan vi bruke `while` løkken


+++ {"slideshow": {"slide_type": "fragment"}}

```python
while «boolsk uttrykk»:
    #Koded
    #Kode
    #Kode
```
* Løkken kjører så lenge det "boolske uttrykket" evalueres til `True`

+++ {"slideshow": {"slide_type": "subslide"}}

* Dersom vi trenger å avbryte en løkke midt i en iterasjon kan vi bruke `break`
* Dersom vi trenger å starte løkken på nytt midt i en iterasjon kan vi bruke `continue`

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
sjekkevariabel = True
while sjekkevariabel:
    tilfeldig_tall = random.random()
    if tilfeldig_tall < 0.2:
        print("Vi avbryter")
        break
    else:
        print("Vi fortsetter")
        continue
    print("Her kommer vi aldri")
    
```

+++ {"slideshow": {"slide_type": "slide"}}

# EKS:
* Vi simulerer en kunde som handler
* Den fyller handlekurven med varer helt til budsjettet er tomt
* Eller kunden har fått det den trenger

* Vi sier at etter hver vare kunden handler, er det 10% sjanse for at den er ferdig å handle
* Kunden trekker en tilfeldig vare hver gang

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
---
varer = {"Epler": 10.0,
         "Pærer": 15.0,
         "Bleier": 35.0,
         "Sjokolade": 6.0,
         "Melk": 20.0,
         "Rundstykker": 13.0
        }

def simuler_handling():
    handlekurv = []
    budsjett = 200
    sluttsjanse = 0.1
    total_pris = 0.0

    varenavn = list(varer.keys())

    shopper = True
    while shopper:
        vare = random.choice(varenavn)
        varepris = varer[vare]
        if budsjett > varepris:
            handlekurv.append(vare)
            total_pris += varepris
            budsjett -= varepris
        else:
            shopper = False
    
        if random.random()<sluttsjanse:
            shopper = False
    return total_pris

#print(f"""Kunden handlet følgende varer {handlekurv}
#Det koster kroner {total_pris:.1f}
#Da er det igjen {budsjett} kroner i budsjettet
#""")
```

# Oppg: 
* Simuler voldsomt mange kunder som handler slik som i eksempelt over
* Regn ut gjennomsnittlig pris kundene handler for
* Plott hvordan fordelingen av pengebruk i butikken er

```{code-cell} ipython3
pengebruk = []
n = 10000
for _ in range(n):
    kundens_pengebruk = simuler_handling()
    pengebruk.append(kundens_pengebruk)

snitt = sum(pengebruk)/n
print(f"Kunder legger i snitt igjen {snitt:.2f} kroner per handletur")

plt.hist(pengebruk, 20)
plt.show()
```
