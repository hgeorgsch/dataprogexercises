---
jupytext:
  formats: md:myst,ipynb
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.18.1
kernelspec:
  display_name: dataprog
  language: python
  name: dataprog
---

+++ {"editable": true, "slideshow": {"slide_type": ""}}

# Simulering av kontantstrøm

+++ {"editable": true, "slideshow": {"slide_type": "fragment"}}

- I stor grad lærer vi grunnleggende programmering gjennom simuleringsoppgavene
- For å lage simuleringsprogrammene må vi kunne:
  - Datastrukturer: Behandle data i lister og `dictionaries`
  - Strukturere program og logikk i funksjoner
  - Iterere over datastrukturene, og kjøre simuleringer i løkker med `for` og `while`
  - Kunne styre kontrollflyt med `if` `elif` og `else`
  - Ha kontroll på begreper og saker som variabler og datatyper
  - Kunne presentere resultat med tekststrenger (f-strenger) og forskjellige plot (linje, stolpe osv)

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

Det aller viktigste læringsmålet:
> Vi skal utvikle algoritmisk tenkning: Vi kan ta en praktisk problemstilling (for eksempel nedbetaling av lån), formulere en enkel modell, og deretter implementere denne som et Python-program som simulerer ulike scenarioer.

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

I Oppgave om simulering av en kontantstrøm gjør vi det så basic som vi klarer, men vi bruker allerde funksjoner, `if`- og `while`-løkker lister, f-strenger og et enkelt plot.

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

## Lister
- Lister i python lages ved å veks putte "ting" i klammeparanteser adskilt med komma: `[1,2,"hei", print, [1,2,3]]`
- Vi kan putte og blande alle mulige datatyper vi vil i en liste, til og med andre lister og funksjoner (slik som `print` over)

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: fragment
---
#Lagrer tall, tekststreng, funksjon og liste i en liste
```

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

 - Dersom vi har tilordnet en liste til en variabel, slår vi opp i listen ved å bruke: `variabel[indeks]`
 - Her er indeksen posissjonen til listeelementet, første element har indeks `0` andre element indeks `1` osv. helt opp til `n-1` for en liste med `n`elementer

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: fragment
---
# Første og andre element
forste, andre =  # Tilordning av flere i 1 linje
print("Første elment:", forste, "\nAndre element:", andre)
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: subslide
---
# Print-funksjon i liste kan hentes ut og brukes
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: fragment
---
# 2-dimensjonale strukturer (matriser) kan beskrives som lister av lister
# (Merk at vi gjerne heller bruker "arrays"
print("2. siste element i listen som er siste element i min_liste:", )
```

+++ {"editable": true, "slideshow": {"slide_type": "fragment"}}

Ved å bruke negative indekser, slår vi opp "bakenifra"

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

# `for`-løkken
- Når vi først har en liste, eller en annen samling med elementer, trenger vi gjerne å gjøre noe med de
- `for`-løkken er en kodeblokk som "gjør noe" med alle elementene suksessivt - vi sier vi itererer over elementene
- Syntaks:
```python
for <element> in <liste>:
    # Gjør noe med elementet
    #...
    #...
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: subslide
---
# Print ut alle elementer i min_liste
```

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

`for`-løkken funker på sekvenser/samlinger elementer som er vi sier er itererbare

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: fragment
---
a = [1,2,3,4,5]
b = ["a", "B", "c", "d"]
range_objekt = range(-5, 10, 2)
zippet = zip(a,b)
opptelt = enumerate(b)
tekst = "Fire franske fruer feis full fart forover"

#Printer ut sammenzippet
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
#Printer ut nummer og element i enumerate
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
# Printer ut bokstaver i tekststreng
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
#Printer ut rangeindeks
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

### Løkketeknikker med lister
- Vi bruker ofte for-løkker til å bygge nye lister
- En litt ekkel med vanlig og viktig måte er å bruke `range()`til å iterere over *indeks*-spennet til listen
- Nyttige funksjoner er da `min_liste.append("ny_ting")` som legger "ny_ting" bakerst i listen
- og `len(min_liste)` som returnerer lengden av listen

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
a = [1,2,3,4,5]
# bygg ny liste b med elementene i a doblet:

#start med tom liste
# For alle tall i "a",
# legg til det dobbelte i listen "b"
    

#Med listekomprehensjon b =
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
# Skift fortegn på elementene i listen a, dersom den er et heltall
#Vi må iterere over indeksen til a - fordi vi skriver tilbake til listen
        
# Sum sammen 2 og 2 tall i a og lagre i liste c
# Vi må iterere over indeksen til a, fordi vi slår opp i 2 og 2 verdier samtidig
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

- Effektiv bruk av lister og løkker krever litt trening
- Vi har også mange flere listefunksjoner som kan være nyttige i forskjellige situasjoner:

+++ {"editable": true, "slideshow": {"slide_type": ""}}

| Funksjon / metode         | Hva den gjør                                | Eksempel               |
| ------------------------- | ------------------------------------------- | ---------------------- |
| `len(liste)`              | Antall elementer i lista                    | `len([1,2,3])  # 3`    |
| `liste.append(x)`         | Legger til ett element bakerst              | `navn.append("Ola")`   |
| `liste.extend(itererbar)` | Legger til flere elementer                  | `a.extend([3,4])`      |
| `liste.insert(i, x)`      | Setter inn element på indeks `i`            | `a.insert(0, "start")` |
| `liste.remove(x)`         | Fjerner første forekomst av verdi `x`       | `a.remove("Ola")`      |
| `liste.pop()`             | Fjerner og returnerer siste element         | `siste = a.pop()`      |
| `liste.pop(i)`            | Fjerner og returnerer element på indeks `i` | `første = a.pop(0)`    |
| `liste.index(x)`          | Finner indeks til første forekomst av `x`   | `a.index("Ola")`       |
| `liste.count(x)`          | Teller hvor mange ganger `x` finnes         | `a.count(0)`           |
| `liste.sort()`            | Sorterer lista **på plass**                 | `tall.sort()`          |
| `sorted(liste)`           | Returnerer **ny** sortert liste             | `ny = sorted(tall)`    |
| `liste.reverse()`         | Snur rekkefølgen **på plass**               | `a.reverse()`          |
| `reversed(liste)`         | Gir omvendt iterator (kan gjøres til liste) | `list(reversed(a))`    |
| `liste.copy()`            | Lager en kopi av lista                      | `b = a.copy()`         |
| `x in liste`              | Sjekker om verdi finnes i lista             | `"Ola" in navn`        |
| `min(liste)`              | Minste verdi                                | `min([4,1,9])  # 1`    |
| `max(liste)`              | Største verdi                               | `max([4,1,9])  # 9`    |
| `sum(liste)`              | Summerer tall i lista                       | `sum([1,2,3])  # 6`    |

+++

# `While`-løkken
- Med `for` løkken gjør vi noe "for alle elementer" i en sekvens
- Generelt sett kan vi bruke `for` løkker til å gjøre noe mange ganger -- men vi må vite hvor mange
- Av og til vet vi ikke dette på forhånd, for eksempel når en variabel når en viss grense ( `saldo > 100000`)
- I slike tilfeller kan vi bruke en `while`-løkke
```
while <betingelse>:
    #Kjør kode
    # kode
    # ....
```
- Her er betingelsen et uttrykk som evalueres til `True` eller `False` og løkken kjører omigjen og omigjen så lenge den er `True`


```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
from random import random
import matplotlib.pyplot as plt
import pandas as pd

#Simuler å kaste terninger til vi får Yatzee
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---

```

```{code-cell} ipython3

```
