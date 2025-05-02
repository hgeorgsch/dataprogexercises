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

```{code-cell} ipython3
# Annuitetslån
import matplotlib.pyplot as plt

laan = 100000
rentesats = 0.05
terminbelop = float(input("Hva er ønsket terminbelop?"))
renter = laan*rentesats/12
max_nedbetalingstid = 10
```

+++ {"slideshow": {"slide_type": "slide"}}

# Datastrukturer: Tuple, set, dictionary
* Til nå har vi sett på lister og arrays (med numpy)
  - Lister kunne inneholde en blanding av data, og vi kunne gjøre listen lengre eller kortere
  - Arrays kunne kun inneholde 1 datatype om gangen, og lengden på listen lot seg ikke endres på

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
import numpy as np
numpy_array = np.array([1,23,3,4,5])
print(numpy_array[3])

vanlig_liste = ["hei", 1, 2.0, print]
vanlig_liste[-1]("heisann!") # Slår opp siste element som er print-funksjonen og gjør et kall til den 
```

+++ {"slideshow": {"slide_type": "slide"}}

* Vi har flere datastrukturer tilgjengelig:
### Tuples
* Kan inneholde en blanding av data
* Vi kan ikke endre på data, eller lengde
* Nyttig for å returnere flere verdier fra en funksjon, eller samle sammen annen data «parvis»
* Vi lager tupler med `(1,2)` i stedet for `[1,2]` for en liste 

```{code-cell} ipython3
---
slideshow:
  slide_type: subslide
---
min_tuple = ("hei",2)
print(min_tuple[0])
#min_tuple[0] = "hade" #Dette er ikke lov
n = len(min_tuple)

#Når vi returnerer flere verdier fra funksjon
#gjør vi egentlig dette i en tuple
def testfunk(a,b):
    a_return = a*2
    b_return = b//2
    return #????

#??? = testfunk(1,9)
print(f"{a} og {b}")
```

+++ {"slideshow": {"slide_type": "subslide"}}

* De hendige funksjonene `enumerate` og `zip` samler dataene i tupler om vi ber python lage lister av de

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
a = [1,2,3,4,5]
b = ["hei", "på", "deg", "så", "lenge"]
zippet = zip(a,b)
opptelt = enumerate(b)
```

+++ {"slideshow": {"slide_type": "slide"}}

# Set
* Set kan være en kjekk datastruktur i mange tilfeller
* Den er uordnet (kan ikke sorteres eller slås opp i)
* Den kan kun inneholde 1 av hvert element, ingen duplikater
* Vi lager set med `{ item1,item2, item3, ...}`
* Eller vi kan bruke funksjonen `set(«datastruktur»)`

```{code-cell} ipython3
---
slideshow:
  slide_type: subslide
---
hobby_liste = ["Lese", "Game", "Fotball", "Fotball", "Game", "Lese", "Danse", "Game","Game"]
hobbier2 = {"Lese", "Danse", "Buldre"}


# Hvilke elementer er i begge settene?
#Hvilket set får vi om vi slår de sammen?
```

+++ {"slideshow": {"slide_type": "slide"}}

# Dictionary /Hash-map / Map
* En viktig og nyttig datastruktur (en dere kommer til å bruke mye) kalles i python `dictionary`
* I andre sammenhenger kalles en slik datastruktur et "hash-map" eller et "map"
* Det er en datastruktur det hvert datalement eller verdi har en "nøkkel" (eng. key) man bruker for å slå opp verdien med
  ![tekst](https://www.boardinfinity.com/blog/content/images/2023/03/HashMap-in-Python.png)

+++ {"slideshow": {"slide_type": "subslide"}}

* Vi lager en dictionay slik:

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---

```

+++ {"slideshow": {"slide_type": "subslide"}}

* Krøllparantes på mac er shift+opt+8, shift+opt+9 (?)
* Tekstrenger før `:` er nøkkelen
* bak `:` er verdien
      - Den kan være data av hvilken som helst type
      - Heltall, flyter, lister, set, funksjoner eller **andre dictionaries**
* Vi slår opp i dictionarien på samme måte som vi slo opp i *listene*, men nå bruker vi nøkkelen i stedet for *indeksen*

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
navn1 = #???
print("Navnet er:", navn1)
```

+++ {"slideshow": {"slide_type": "subslide"}}

* Vi har lov til å endre dictionarier
* Vi fjerner et key/value-par med `del`
* Vi kan legge et et key/value-par ved å "slå opp" for den nye nøkkelen å sette dataen med `=`

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
#Legger til ny key/value

print(person)
#Sletter key/value

print(person)
```

+++ {"slideshow": {"slide_type": "subslide"}}

* Dictionaries lar oss strukturere data på en oversiktlig måte
* Tenk om vi hadde data av typen under for tusenvis av personer, og vi måtte ha alt i haugevis med lister og holde orden på hvillke indekser inneholdt hva?
* Eller enda verre: I lister inne i lister inne i lister?

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
person = {"navn": "Jonas",
          "alder": 37,
          "hobbier": hobbier2,
          "favorittfunksjon": print,
          "bosteder": {"studie": ["Trondheim", "Gjøvik", "Bergen"],
                       "Oppvekst": "Breivika",
                       "Nå": "Åse"
                      }
         }
print(person.values())
```

+++ {"slideshow": {"slide_type": "slide"}}

### Oppgave 
* Vi begynner vel å bli lei av populasjonsvekst i skandinavia -- men sist behandlet vi dataene i lister slik som under

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
---
import math
import matplotlib.pyplot as plt
land = ["Norge", "Sverige", "Danmark"]
K = [20e6, 25e6, 15e6] #Makspopulasjon
r = [0.01, 0.02, 0.03] #relativ vekstrate
P0 = [4e6, 8e6, 6e6] # Startpopulasjon
t = 20 #Hvor mange år vekst


def logistisk_vekst(P0,K,r,t):
    A = (K-P0)/P0
    P = K/(1+A*math.exp(-r*t))
    return P
    
data = []
#Iterer over indeksen til dataene våre (0,1,2) og sett sammen "datalisten"
for i in range(len(land)):
    datapunkt = [land[i], P0[i], K[i], r[i]]
    #vekst_funksjon = lambda t: logistisk_vekst(P0[0], K[0], r[0], t) # Kjapp måte å lage en funksjon på (eks fx = lambda x: 2x-x**2)
    #datapunkt.append(vekst_funksjon)
    data.append(datapunkt)

t_liste = list(range(t))
#Iterer over dataene og regn ut populasjonsvekstlisten, og legg de til bakerst i "datapunktene"
#Du trenger to løkker -- først over dataene -- deretter over årene
for d in data:
    pop_vekst = []
    for ti in t_liste:
        #populasjon = d[4](ti)
        populasjon = logistisk_vekst(d[1], d[2],d[3], ti)
        pop_vekst.append(populasjon)
    d.append(pop_vekst)

plt.title("Populasjonsvekst")
plt.xlabel("Tid/[År]")
plt.ylabel("Populasjonsstørrelse")

for d in data:
    plt.plot(t_liste, d[-1], label=d[0])
plt.legend()
plt.show()
```

+++ {"slideshow": {"slide_type": "subslide"}}

* Dersom datapunktene våre blir mer komplisert, kan det bli vanskelig å holde styr på alle indeksene
* Hvilken indeks var navnet på området? Makspopulasjon?
* Forsøk å endre datapunktene til dictionaries -- `data` variabelen kan da inneholde en liste over de forskjellige dictionariene

+++ {"slideshow": {"slide_type": "fragment"}}

```python
{
    "navn": "Norge",
    "startpopulasjon": 4e6,
    "makspopulasjon": 20e6,
    "vekstrate": 0.01
}
```

```{code-cell} ipython3
---
slideshow:
  slide_type: slide
---
import math
import matplotlib.pyplot as plt
land = ["Norge", "Sverige", "Danmark"]
K = [20e6, 25e6, 15e6] #Makspopulasjon
r = [0.01, 0.02, 0.03] #relativ vekstrate
P0 = [4e6, 8e6, 6e6] # Startpopulasjon
t = 200 #Hvor mange år vekst


def logistisk_vekst(P0,K,r,t):
    A = (K-P0)/P0
    P = K/(1+A*math.exp(-r*t))
    return P
    
data = []
#Iterer over indeksen til dataene våre (0,1,2) og sett sammen "datalisten"
for i in range(len(land)):
    datapunkt = { "navn": land[i], 
                 "makspopulasjon": K[i], 
                 "startpopulasjon": P0[i], 
                 "vekstrate": r[i] 
                }
    #datapunkt = [land[i], P0[i], K[i], r[i]]
    data.append(datapunkt)

t_liste = list(range(t))
#Iterer over dataene og regn ut populasjonsvekstlisten, og legg de til bakerst i "datapunktene"
#Du trenger to løkker -- først over dataene -- deretter over årene
for d in data:
    pop_vekst = []
    for ti in t_liste:
        #populasjon = d[4](ti)
        populasjon = logistisk_vekst(d["startpopulasjon"], 
                                     d["makspopulasjon"],
                                     d["vekstrate"], 
                                     ti)
        pop_vekst.append(populasjon)
    d["vekst"]=pop_vekst

plt.title("Populasjonsvekst")
plt.xlabel("Tid/[År]")
plt.ylabel("Populasjonsstørrelse")

for d in data:
    plt.plot(t_liste, d["vekst"], label=d["navn"])
plt.legend()
plt.show()
```

+++ {"slideshow": {"slide_type": "slide"}}

# Strengformatering

+++ {"slideshow": {"slide_type": "fragment"}}

### f-Strenger
* Til nå har vi brukt `round` til å runde av tall så de ser fornuftige ut når vi skal skrive de ut til skjerm
* Når vi har kombinert tekst og tallresultat har vi brukt print slik: `print("Resultatet er", round(resultat1,2), "prosent")`
* Når vi skal sette sammen tekst og resultat i variabler med fornuftig formatering er det bedre å bruke såkalte **f-strenger**

+++ {"slideshow": {"slide_type": "subslide"}}

* Vi gjør en vanlig tekststreng feks `"Dette er en tekstreng"` om til en f-streng ved å sette en `f` foran det første hermetegnet
```python
tekst = f"Dette er en f-streng"
```
* Da kan man «lime» inn variabler i strengen med krøllparanteser `{tall/variablel/tekst:formatering}`

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
#f-streng eksempel
dyr = "Tiger"
print(f"Dette er en f-{dyr} min venn :)")
#Flere resultat
resultat1 = math.pi
resultat2 = 1239087243587345.0
resultat_streng = f"Når man regner med {resultat1:.2f} blir resultatet ofte {resultat2:+,.0f}"
print(resultat_streng)
```

+++ {"slideshow": {"slide_type": "subslide"}}

* Tabellen under viser hvordan de forskjellige formateringene bak `:` fungerer:
| Eksempel                   | Beskrivelse                                      | Resultat (med f-string) |
|----------------------------|-------------------------------------------------|-------------------------|
| `f"{42}"`                  | Heltall                                          | `42`                    |
| `f"{42.12345:.2f}"`        | Flyttall med 2 desimaler                         | `42.12`                 |
| `f"{42.12345:.3f}"`        | Flyttall med 3 desimaler                         | `42.123`                |
| `f"{42:04}"`               | Heltall med ledende nuller (4 siffer)            | `0042`                  |
| `f"{1000000:,}"`           | Stort tall med tusenskiller                      | `1,000,000`             |
| `f"{1000000:_}"`           | Stort tall med understrek som tusenskiller       | `1_000_000`             |
| `f"{42:^10}"`              | Sentrert i et felt på 10 tegn                    | `    42    `            |
| `f"{42:<10}"`              | Venstrejustert i et felt på 10 tegn              | `42        `            |
| `f"{42:>10}"`              | Høyrejustert i et felt på 10 tegn                | `        42`            |
| `f"{0.85:.0%}"`            | Prosentformatering uten desimaler                | `85%`                   |
| `f"{0.857:.2%}"`           | Prosentformatering med 2 desimaler               | `85.70%`                |
| `f"{0.857:.1%}"`           | Prosentformatering med 1 desimal                 | `85.7%`                 |
| `f"{42:e}"`                | Eksponentialnotasjon (små bokstaver)             | `4.200000e+01`          |
| `f"{42:E}"`                | Eksponentialnotasjon (store bokstaver)           | `4.200000E+01`          |
| `f"{42.12345:.2e}"`        | Eksponentialnotasjon med 2 desimaler (små bokstaver) | `4.21e+01`          |
| `f"{42.12345:.2E}"`        | Eksponentialnotasjon med 2 desimaler (store bokstaver) | `4.21E+01`          |
| `f"{{ }}"`                 | Utskrift av krøllete parenteser `{` og `}`       | `{ }`                   |

```{code-cell} ipython3
---
slideshow:
  slide_type: subslide
---
data_norge = data[0]
sluttpopulasjon = data_norge["vekst"][-1]
print(sluttpopulasjon)
#print(data_norge)
print(f"Sluttpopulasjonen i {data_norge['navn']} er {sluttpopulasjon} som vi avrunder til {round(sluttpopulasjon,-4):,.0f}")
print(f"Det tilsvarer en vekst siden start på {sluttpopulasjon/data_norge['startpopulasjon']-1:.1%}")
```

+++ {"slideshow": {"slide_type": "slide"}}

# Slicing

+++ {"slideshow": {"slide_type": "fragment"}}

* Slicing er en nyttig teknikk som lar oss velge ut deler av en listen eller en tekststreng
* Tekststrenger kan indekseres på samme måte som lister, og derfor også "slices" på samme måte

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
tekst = "Hei hallo hade"
#Vi kan indeksere tekststrenger
forste_tegn = tekst[0]
print(f"Første tegn er '{forste_tegn}'")
print(f"Siste tegn er '{tekst[-1]}'")
forste_5_tegn = tekst[:5]
print(f"Første 5 tegn er '{forste_5_tegn}'")
```

+++ {"slideshow": {"slide_type": "subslide"}}

* Vi kan altså "slice" over indekser i en liste eller streng med [start:stop]
* Vi kan ta med feks, annet hvert element med [start:stop:step]
* Dersom man utelukker `start` eller `stop` antar vi at man mener henholdsvis fra begynnelsen eller til slutten

```{code-cell} ipython3
---
slideshow:
  slide_type: subslide
---
tekst = '11.04.1987'
liste = [1,23,4,5,67,7,8,10]
#Fra 3 element til men ikke med 7
print(liste[3:7])
#Fra begynnelsen til men ikke med 7 tegn
print(liste[:7])
#Fra 3 tegn til slutten
print(tekst[3:])
```

```{code-cell} ipython3
---
slideshow:
  slide_type: subslide
---
# Hvert tredje element fra start til slutt
print(liste[::3])
# Hvert andre element fra 2 til 9 
print(tekst[2:9:2])
#Vi kan slice med negative indekser
year =  tekst[-4:]
print(f"Året i datoen er {year}")
# Vi kan slice baklengs
reversliste = liste[-1::-1]
print(reversliste)
```

```{code-cell} ipython3
---
slideshow:
  slide_type: ''
---
# Annuitetslån
import matplotlib.pyplot as plt

laan = 100000
rentesats = 0.05
terminbelop = float(input("Hva er ønsket terminbelop?"))
renter = laan*rentesats/12
max_nedbetalingstid = 10

def sjekk_terminbelop():
    if terminbelop < renter:
        print("Terminbeløpet er for lite til å dekke rentene av lånet")
        print("Renter ved første termin er ", renter)
        return False
    else:
        return True

if sjekk_terminbelop():
    
    renter_liste = []
    avdrag_liste = []
    
    laan_rest = laan
    mnd = 0
    while laan_rest > 0:
        renter = laan_rest*rentesats/12
        avdrag = terminbelop - renter
        renter_liste.append(renter)
        avdrag_liste.append(avdrag)
        laan_rest -= avdrag
        mnd += 1

    mnd_liste = list(range(mnd))

    plt.bar(mnd_liste, avdrag_liste, label="Avdrag")
    plt.bar(mnd_liste, renter_liste, bottom=avdrag_liste, label="Renter")
    plt.xlabel("Måneder")
    plt.ylabel("Avdrag/[kr]")
    plt.legend()
    plt.show()
    #Plot ser ikke bra ut ennå...
    if mnd/12 > max_nedbetalingstid:
        print("Nedbetalingstiden på ", mnd//12, "år og", mnd%12, "måneder er for lang")

    n_aar = mnd//12
    avdrag_aarlig = []
    renter_aarlig = []
    print(avdrag_liste[12:12*2])
    years = list(range(n_aar))
    for year in years:
        avdrag_y = avdrag_liste[12*year:12*(year+1)]
        avdrag_aarlig.append(sum(avdrag_y))
        renter_aarlig.append(sum(renter_liste[12*year:12*(year+1)]))

    years_string = []
    startaar = 2024
    for year in years:
        years_string.append(f"{startaar+year:.0f}")
    
    plt.bar(years_string, avdrag_aarlig, label="Avdrag")
    plt.bar(years_string, renter_aarlig, bottom=avdrag_aarlig, label="Renter")
    plt.xlabel("År")
    plt.ylabel("Avdrag/[kr]")
    plt.legend()
    plt.show()
        
        

else:
    print("Avbryter låneutregning")
    
```

```{code-cell} ipython3

```
