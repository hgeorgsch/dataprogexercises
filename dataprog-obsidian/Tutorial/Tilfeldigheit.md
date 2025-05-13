---
title: Slumptal
tags:
  - lecture/video
---

# Simulering og modellering

## Pseudotilfeldig tallgenerator


* Når man skal kjøre simuleringer på datamaskin trenger man ofte å bruke tilfeldige tall
* Vi trenger elementer av tilfeldighet i simuleringene våres for å beskrive prossesser vi ikke kan forklare analytisk/matematisk
* Dette gjelder både i ingeniørfagene, men spesielt når man skal modellere *mennesklig adferd*

![newton](https://pbs.twimg.com/media/D2EZ4DwVAAApNdd?format=jpg&name=900x900)


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
