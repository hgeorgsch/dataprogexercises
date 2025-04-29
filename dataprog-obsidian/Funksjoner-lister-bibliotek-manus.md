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

# Kjapp inføring i littavhvert:
 * Moduler
 * Løkker
 * Datastrukturer (lister)

+++

# Først mer om funksjoner:
* Vi lager egne funksjoner når:
    - Vi gjør samme «ting» mange ganger
    - For å dele programmet inn i deler som har sine egne spesialoppgaver (Programstruktur)
    - Når vi har funksjonalitet som kan være nyttig i andre sammenhenger (Gjenbrukbarhet)

+++

## Eksempel: Populasjonsvekst

La oss si at vi ønsker å sammenligne populasjonsveksten i for to områder, feks Norge og Sverige.
Vi vil se på vekst over $t = 10$ år, og sammenligne sluttpopulasjonen for forskjellige parametre eller omstendigheter.
La:

$$
\begin{align*}
P_{0,N} &= 5,000,000 \\
P_{0,S} &= 9,000,000 \\
K_N &= 20,000,000 \\
K_S &= 25,000,000 \\
r_N &= 0.02 \\
r_S &= 0.01
\end{align*}
$$

Logistisk vekst er fortsatt:
$$
\begin{align*}
P(t) &= \frac{K}{1+A\mathrm{e}^{-rt}} \\
A &= \frac{K-P_0}{P_0}
\end{align*}
$$

```{code-cell} ipython3
import math

e = math.exp(1) # = e^1
P0_norge = 5e6
P0_sverige = 9e6
K_norge = 20e6
K_sverige = 25e6
r_norge = 0.02
r_sverige = 0.01
A_norge = (K_norge-P0_norge)/P0_norge
A_sverige = (K_norge-P0_sverige)/P0_sverige

t = 10

P_slutt_norge = K_norge/(1+A_norge*e**(-r_norge*t))
P_slutt_sverige = K_sverige/(1+A_sverige*e**(-r_sverige*t))
print("Sluttpopulasjonen i sverige: ", int(round(P_slutt_sverige,-4)))
print("Sluttpopulasjonen i Norge: ", int(round(P_slutt_norge, -4)))
```

# Funksjoner?

* Programmet under gjør samme regneoperasjon flere ganger
* Samme utregning for $A$ for de to landene
* Samme utregning for sluttpopulasjon til de to landene
* Den eneste forskjellen er parameterene vi bruker
* I tillegg kan den logistiske ligningnen brukes til å modellere mer enn bare disse to populasjonene
* Det vil si at her kanskje er funksjonalitet vi kan bruke igjen senere

+++

### Lag funksjoner 1
* Vi kan putte utregningen til norges og sveriges sluttpopulasjoner inn i en funksjon
* Da kan vi lett regne ut populasjonen på mange tidspunkt for de to uten å skrive inn utregningene hver gang

```{code-cell} ipython3
import math

e = math.exp(1) # = e^1
P0_norge = 5e6
P0_sverige = 9e6
K_norge = 20e6
K_sverige = 25e6
r_norge = 0.02
r_sverige = 0.01


t = 10

def pop_vekst_norge(t): # Merk at variabelen «t» i funksjonsdefinisjonen, har ingenting med variabelen «t» på linjen over
    A_norge = (K_norge-P0_norge)/P0_norge
    P = K_norge/(1+A_norge*e**(-r_norge*t))
    return int(round(P,-4))

def pop_vekst_sverige(t):
    A_sverige = (K_norge-P0_sverige)/P0_sverige
    P = K_sverige/(1+A_sverige*e**(-r_sverige*t))
    return int(round(P,-4))
    
P_slutt_norge = pop_vekst_norge(t)
P_slutt_sverige = pop_vekst_sverige(t)
print("Sluttpopulasjonen i sverige: ", P_slutt_sverige)
print("Sluttpopulasjonen i Norge: ", P_slutt_norge)

print("Når halve tiden er gått er det i Norge", pop_vekst_norge(t/2))
print("Når halve tiden er gått er det i Sverige", pop_vekst_sverige(t/2))
```

* Her har vi lagt populasjonsutregningene til de to landene i egne funksjoner
* Dersom vi hadde mange slike funksjoner kunne vi også lagt utregningen av $A$ i en egen funksjon:

```{code-cell} ipython3
# Prøv selv å lage en egen funksjon for utregningen av A
```

### Lag funksjoner 2
* Denne fremgangsmåten letter programmeringen vår
* Men den tar ikke hensyn til at vi kanskje skal modellere lignende problem senere
* Funksjonene funker stort sett kun for dette programmet
* Et annet problem er at avrundingen er "hardkodet" i funksjonene -- det gjør de også mindre fleksible

+++

* *Merk at jeg limer inn hele koden på nytt -- det er så man kan se helheten*
* *Variabler vi definerte lenger oppe kan brukes i hele resten av notebooken*

```{code-cell} ipython3
import math

e = math.exp(1) # = e^1
P0_norge = 5e6
P0_sverige = 9e6
K_norge = 20e6
K_sverige = 25e6
r_norge = 0.02
r_sverige = 0.01


t = 10

def logistisk_vekst(P0,K,r,t):
    A = (K-P0)/P0
    P = K/(1+A*math.exp(-r*t))
    return P
    
P_slutt_norge = logistisk_vekst(P0_norge, K_norge,r_norge,t)
P_slutt_sverige = logistisk_vekst(P0_sverige, K_sverige, r_sverige,t)
print("Sluttpopulasjonen i sverige: ", P_slutt_sverige)
print("Sluttpopulasjonen i Norge: ", P_slutt_norge)

#print("Når halve tiden er gått er det i Norge", pop_vekst_norge(t/2))
#print("Når halve tiden er gått er det i Sverige", pop_vekst_sverige(t/2))
```

* I dette tilfelle kan vi gjenbruke funksjonen vår i andre sammenhenger
* Det er imidlertid ikke like lettvint å kalle funksjonen i resten av programmet
* Vi kan lage flere funksjonen slik at vi får både gjenbrukbarhet, og lettvint bruk

```{code-cell} ipython3
import math

e = math.exp(1) # = e^1
P0_norge = 5e6
P0_sverige = 9e6
K_norge = 20e6
K_sverige = 25e6
r_norge = 0.02
r_sverige = 0.01


t = 10

def logistisk_vekst(P0,K,r,t):
    A = (K-P0)/P0
    P = K/(1+A*math.exp(-r*t))
    return P

def lag_pop_funk(P0,K,r,t):
    def slutt_populasjon(t):
        P = logistisk_vekst(P0,K,r,t)
        return P
    return slutt_populasjon #Vi returnerer funksjonen vi laget inne i funksjonen!

def format_pop(P):
    return int(round(P,-5))

pop_norge = lag_pop_funk(P0_norge,K_norge,r_norge,t)
pop_sverige = lag_pop_funk(P0_sverige,K_sverige,r_sverige, t)

#print(type(pop_norge))
P_slutt_norge = pop_norge(t)
P_slutt_sverige = pop_sverige(t)
print("Sluttpopulasjonen i sverige: ", format_pop(P_slutt_sverige))
print("Sluttpopulasjonen i Norge: ", format_pop(P_slutt_norge))

print("Når halve tiden er gått er det i Norge", format_pop(pop_norge(t/2)))
print("Når halve tiden er gått er det i Sverige", format_pop(pop_sverige(t/2)))
```

* Her har vi laget en funksjon som lager populasjonsfunksjoner for oss!
* Tidligere måtte vi skrive:
  ```python
  def pop_vekst_«land»(....):
      ....
      ....
  ```
* For alle land som skulle ha egen vekstfunksjon -- vi gjentok oss!
* Funksjonene er som små program -- alt vi kan gjøre utenfor en funksjon kan vi gjøre inne i funksjonen
* Når man skal returnere funksjoner passer vi på å ikke ha med `...(arg1,arg2)` etter funksjonsnavn

+++

* Vi laget også en egen funksjon til å formattere output
* Slike kjappe småfunksjoner kan være greie å lage med et *lambdauttrykk* (anonym funksjon)
* Man kan lage en slik funksjon "navnløs" funksjon uten bruk av `def` slik:
  ```python
  summefunksjon = lambda arg1, arg2: arg1+arg2
  ```

```{code-cell} ipython3
summefunksjon = lambda x,y: x+y
print(summefunksjon(1,2))
```

* For å lage en ny populasjonsvekstfunksjon for et område som også gjør formatering, kunne vi skrevet:

```{code-cell} ipython3
pop_norge_formatert = lambda t: int(round(pop_norge(t),-5))
#pop_norge funksjonen laget vi tidligere
print("populasjonen i norge etter 12 år er", pop_norge_formatert(12))
```

# Moduler, biblioteker og pakker
* Vi kan importere ny funksjonalitet ved å hente inn pakker/moduler/bibliotek
* Her er noen formelle definisjoner, men vi kan kalle disse for biblioteker
* Vi har allerede så vidt sett på `datetime` og `math`

+++

## Hente inn biblioteker
* Vi kan hente inn, eller importere et bibliotek ved å skrive `import «navn»`
  

```{code-cell} ipython3
import math
```

* Her importerer vi hele matematikkbiblioteket
* Vi kan se hva det inneholder ved å bruke `dir()`

```{code-cell} ipython3
dir(math)
```

* Deretter kan vi bruke `help()` til å få litt info

```{code-cell} ipython3
help(math.sin)
```

* Når vi skal bruke deler av en modul eller pakke, får vi tak i den ved:
```python
modul.navn #For variabel
modul.funksjon(arg1,...) #for funksjonskall
```

```{code-cell} ipython3
pi = math.pi
print("Pi har verdien ca.:", pi)
sinus_test = math.sin(2*pi)
print("sin(2*pi) = ", sinus_test) #Merk at sin(2*pi) skal være lik 0
print (sinus_test == 0) #Her skulle det vært printet ut 0
print(math.isclose(sinus_test,0,abs_tol=0.00001))
print(help(math.isclose))
```

* NÅr help() og dir() er for tungtvint å bruke, sjekker man dokumentasjonen på nett
* [python.org](http://www.python.org) for innebygde moduler som `math`
* Andre bibliotek ar dokumentasjon på egen hjemmeside feks [matplotlib](https://matplotlib.org/)

```{code-cell} ipython3
#Let med help og dir og forsøk å importere biblioteket datetime og printe ut dagens dato
import datetime
print(dir(datetime.date))
help(datetime.date.today)
datetime_objekt = datetime.date.today()
dir(datetime_objekt)
print(datetime_objekt.isoformat())
```

* Moralen:
  - Vanskelig å bruke help() og dir()
  - Ofte vanskelig å lese dokumentasjon (Men prøv alltid)
* Finn tutorials på nettet som forklarer hvordan man bruker python-biblioteket du jobber med

+++

## Hente deler av bibliotek
* Av og til vil man ikke importere et helt bibliotek
* Man trenger bare å bruke en del av det

```{code-cell} ipython3
from math import exp
e = exp(1)
print(e)
```

## Synonym for bibliotek
* Dersom navnet på biblioteket er langt kan det være plagsomt å oppgi hele stien ved bruk
* Da kan man gi det et synonym når man importerer

```{code-cell} ipython3
import matplotlib.pyplot as plt
#help(plt)
```

```{code-cell} ipython3
import numpy as np
#help(np)
```

```{code-cell} ipython3
a = np.eye(10)
a
```

# Datastrukturer: Lister

+++

* Hva om vi i populasjonsveksteksempelet ikke bare så på 2 land, men kanskje alle i Europa
* Alle parametre måtte ha en egen variabel for hvert land
* Det fungerer dårlig -- i praksis må vi ha like mange variabler som datapunkt
* Det kan dreie seg om millioner av variabler å lage navn til å holde styr på
* **NEI TAKK**

+++

## Lister
* Vi trenger en annen måte å organisere og *strukturere* datapunktene våre på
* Python har flere ulike typer **datastrukturer** som kan hjelpe oss med det
* Den første vi skal se på er *lister*

```{code-cell} ipython3
a = [1,2,3]
print(a)
```

* Vi lager lister med ting ved å «liste de opp» inne i klammeparanteser (alt + shift 8 og 9 på mac ?)
* Listene kan inneholde alle hva som helst, til og med funksjoner, og vi kan blande datatyper

```{code-cell} ipython3
a = ["hei", 22, 4e6, print]
print(a)
```

* For å hente ut et element i listen bruker oppgir vi *indeksen* til elementet i klammeparanteser

```{code-cell} ipython3
a[2] #Element 3
```

```{code-cell} ipython3
a[0] #Element 1
```

* Merk at listene er «0-indeksert», vi teller altså fra og med 0 og oppover
* Noen datatyper er det ulovlig å endre innholdet av, men med lister kan vi det

```{code-cell} ipython3
a[3] = 2+2
a[0] = 42
a
```

* Vi kan bruke dir() for å se nyttige innebygde funksjoner av listen
* Disse kan kalles med '.' feks `min_liste.sort()` for å finne det største elementet i listen

```{code-cell} ipython3
dir(a)
a.sort()
len(a)
```

Noen viktige funksjoner:
* `min_liste.append(«noe»)` legger til «noe» på slutten av listen (listen blir større)
* `len(min_liste)` -- oppgir lengden på listen
* `max(min_liste)` -- oppgir største element i listen (`min()` gir minste)

+++

## Populasjonsvekst -- skandinavia
* Vi ser nok en gang på populasjonsvekst
* Denne gangen for skandinavia

```{code-cell} ipython3

land = ["Norge", "Sverige", "Danmark"]
K = [20e6, 25e6, 15e6]
r = [0.01, 0.02, 0.03]
P0 = [4e6, 8e6, 6e6]
t = 20


def logistisk_vekst(P0,K,r,t):
    A = (K-P0)/P0
    P = K/(1+A*math.exp(-r*t))
    return P

def lag_pop_funk(P0,K,r):
    def slutt_populasjon(t):
        P = logistisk_vekst(P0,K,r,t)
        return P
    return slutt_populasjon #Vi returnerer funksjonen vi laget inne i funksjonen!

def format_pop(P):
    return int(round(P,-3))

pop_funksjoner = []
pop_funksjoner.append( lag_pop_funk(P0[0], K[0], r[0]))
pop_funksjoner.append(lag_pop_funk(P0[1], K[1], r[1]))
pop_funksjoner.append(lag_pop_funk(P0[2], K[2], r[2]))
#Vi kunne også lagret disse funksjonene i en liste.. :)

#print(type(pop_norge))
P_slutt = []
P_slutt.append(pop_funksjoner[0](t))
P_slutt.append(pop_funksjoner[1](t))
P_slutt.append(pop_funksjoner[2](t))

print("Sluttpopulasjonen i", land[0], "er:", format_pop(P_slutt[0]))
print("Sluttpopulasjonen i", land[1], "er:", format_pop(P_slutt[1]))
print("Sluttpopulasjonen i", land[2], "er:", format_pop(P_slutt[2]))
```

# Fortsatt problemer?
* Vi har samlet dataene vår i lister -- det er bra
* Men vi må fortsatt gå igjennom disse listene for hånd -- ikke bra
* Vi trenger en måte å gå gjennom lister og andre datastrukturer *automatisk*
* Dette blir stoff til neste time
