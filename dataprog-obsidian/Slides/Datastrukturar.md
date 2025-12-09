---
tags:
  - lecture/video
css:
  - custom.css
---
# Datastrukturar

note:
Når vi skal håndtere store datamengder, enten det er komplekse simuleringer med mange variabler eller datasett med mange observasjoner av de samme variabler, trenger vi datastrukturer for å systematisere dem.

---

`x`

note:
Én variabel i python kan representere alt fra ett enkelt tall til en tabell med flere milliarder verdier.
Dette er ulike datatyper.
Noen datatyper er primitive, mens andre er sammensatt av flere verdier.
De primitive datatypene er dem som ikke kan deles opp.

---

## Primitive datatypar

- `int` : $\ldots, -1, 0, +1, +2, \ldots$
- `float` :  t.d. $-50.1$, $0$, $0.1$, $2.4$,  $10.0$
- `bool` : `True` eller `False`
- `str` : t.d. `"Hello World!"`

note:
De primitive datatypene håper jeg du kjenner.
De representerer enkeltverdier, som tall, sann/usann, eller
tegnstrenger.

Det kan diskuteres om tegnstrenger egentlig er en primitiv
datatype.
Mange andre sprog har en datatype for ett enkelt tegn, og da er strenger en sammensatt datatype av flere slike tegn.
Ett enkelt tegn i python er derimot også en streng, og der er ingen mindre datatype å dele strengene opp i.

---
## Samansette datatypar

- `tuple` : t.d. `(1,0.5)`
- `list` (liste) : t.d.  `[ 2, 3, 11, 3, 11, 11 ]`
- `set` (mengd) :  `{ 1, 2, 3, 5, 7, 11, 13 }`
- `dict` for *dictionary* (oppslag)  `{` nykel : verdi, $\ldots$ `}`
- egendefinerte klasser 
- klasser fra biblioteker 

note:
Der er mange sammensatte datatyper. 
Noen er bygd inn i python, og andre finnes i biblioteker.
Vi kan også definere våre egne datatyper som kalles klasser.

De to viktigste, sammensatte datatypene er `dict`  og `list`

---
## *Record*

|        kunde |                |
| -----------: | :------------- |
|    `fornamn` | "Ola"          |
|  `etternamn` | "Normann"      |
| `postnummer` | 6016           |
|       `gate` | "Borgundvegen" |
|     `nummer` | 666            |

note:
En typisk utfordring er når vi trenger en variabel for å representere ett fenomen, f.eks. en kunde, og dette fenomenet har mange egenskaper som krever hver sin datatype, f.eks. navn, adresse og fødselsdato.

Tradisjonelt har vi gjerne kalt dette for en *record*.  Jeg har ikke et godt norsk ord, men vi kan tenke på et arkivkort.
En *record* har flere felter, der hvert felt har et navn og en verdi.

---

## `dict`

```pythoh
kunde = { 
    "fornamn" : "Ola",
    "etternamn" : "Normann",
    "postnummer" : 6016,
    "gate" : "Borgundvegen",
    "nummer" : 666,
  }
```

note:
*Record* er ikke et begrep i python, men vi kan bruke datatypen `dict`.
Vi laver et `dict`-objekt med krøllparanteser og lister alle feltene som nøgle-kolon-verdi.
Rekkefølgen på feltene spiller ingen rolle.

---
## Indeksering

```
In [3]: print( kunde["fornamn"] )
Ola

In [4]: print( kunde["gate"], kunde["nummer"]  )
Borgundvegen 666

In [5]: kunde["postnummer"] = 6060

In [6]: kunde["fødselsdato"] = "2001-04-23"
```

note:
Mange sammensatte datatyper har et system for indeksering, eller *subscripting*.
Her bruker vi hakeparenteser og feltnavn for å se, endre eller legge til spesifikke felter.

---
## Samlinger

- `kundeliste = [ kunde1, kunde2, ... ]`
- `talliste = [ 2, 3, 5, 7, 11, 13 ]`

note:
Et andet typisk problem er samlinger av verdier, som regel av samme type.
Det enkleste eksempelet på en samling er en liste.
Elementene i en liste eller i en `dict` kan være både primitive datatyper og andre sammensatte datatyper.

---

## Indeksering

---
## Liste

+ Raske operasjoner
	+ `append()`
	+ 

---


Læringsutbyte
+ Konseptuell forståing av samansettet datatypar t.d. *record* eller `dict`
+ Datastrukturar som liste, *map*
+ Kompleksitet
+ Operasjonar på datastrukturar
	+ oppslag
	+ iterasjon
+ numpy 
+ Listekomprehensjon
+ JSON og `dict`

---

```python
a = (1,2)
b = [1,2]
```

```
In [3]: print( a[0], b[0] )
1 1

In [4]: b[0] = 2

In [5]: a[0] = 2
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[5], line 1
----> 1 a[0] = 2

TypeError: 'tuple' object does not support item assignment

```
<!-- element class="fragment" -->

---

```python
liste = [ "Ola", "Kari", "Mons" ]
```

---

# Listekomprehension

Snarvei til å lage lister, set og dictionaries

---

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



---

## Dynamiske datatypar

+ iterator
+ klasser

---

## numpy


---

# Slutt
