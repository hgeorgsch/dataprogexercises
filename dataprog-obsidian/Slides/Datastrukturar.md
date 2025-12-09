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

```
In [1]: L = [ 2, 3, 5, 7, 11, 13, 17 ]

In [2]: print( L[2] )
5

In [3]: L[2] = 3

In [4]: print( L )
[2, 3, 3, 7, 11, 13, 17]
```

note:
Lister støtter indeksering, akkurat som `dict`, men her har ikke elementene sine egne nøgler.
Det er posisjonen i listen vi bruker som indeks.
Klammeparentesene er dog de samme.

---
<!-- slide template="[[tpl-quote-twocolumn]]" -->

::: left
## Raske operasjoner

+ `append()`
+ `pop()`
+ indeksering (get/set)

:::
::: leftcredit
:::
::: right
## Trege operasjoner

+ `insert()`
+ `delete()`

:::
::: rightcredit
:::

note:
Datastrukturer og sammensatte datatyper blir alltid lavet for at noen operasjoner skal være raske og effektive, men ingenting er perfekt, og operasjoner som ikke blir prioritert går da gjerne tregere.

Det er mulig å sette inn eller fjerne elementer midt i listen, men dette går tregt.
For å sette inn et element på en vilkårlig plass, må man flytte deler av listen for å gjør plass til det nye elementet. Det tar lenger tid dess større listen er.  Det samme skjer om man sletter et element.  Man må flytte listen for å fylle hullet.

Det går derimot raskt å operere på slutten av listen.  Derfor er der egne funksjoner, `append` og `pop`, for å legge til eller fjerne et element på enden av listen.  Det går i konstant tid, uavhengig av antall elementer i listen.

Indeksering går også raskt.  Vi kan slå opp en posisjon i konstant tid.

Når vi snakker om trege operasjoner her, er det i forhold til listelengden.
Vi kaller det gjerne kompleksitet.
Om listen er kort, så spiller kompleksiteten ingen rolle.  Vi merker ikke forskjell før vi kommer opp i noen millioner eller kanskje milliarder elementer.
Raske operasjoner går i konstant tid, uansett listelengde.

Kompleksitet er mye av grunnen til at der finnes så mange forskjellige datastrukturer i literaturen og i biblioteker.
Ulike datastrukturer er utviklet for å fungere optimalt på ulike problemer.

---
## Mengde

- `kunder = { kunde1, kunde2, ... }`
- `mengd = { 2, 3, 5, 7, 11, 13 }`

```
In [5]: M = { 2, 3, 7, 5, 13 }

In [6]: print( M )
{2, 3, 5, 7, 13}

In [7]: M.add( 17 )

In [8]: print( M )
{17, 2, 3, 5, 7, 13}

In [9]: M.add( 5 )

In [10]: print( M )
{17, 2, 3, 5, 7, 13}
```

note:
Vi kan illustrere kompleksitet om vi sammenligner lister med mengder, eller *set* på engelsk.

Mengder ligner lister, men vi bruker krøllparenteser i stedet for hakeparenteser, og der elementer i listen kommer i en bestemt rekkefølge og gjerne kan dukke opp flere ganger, er elementene i en mengde alltid unike og rekkefølgen er uvesentlig.

Det er åbenbart nyttig, i mange situasjoner, å være sikker på at ingen elementer blir duplisert, men det gjør det også umulig å ha en rask `append()`-fuinksjon. Vi kan ikke legge til et element uten å sjekke at det ikke finnes fra før.  Dermed må vi bla gjennom hele listen og det tar tid.

---
## Tuplar


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

note:
En anden datatype som ligner lister er tupler.
Her bruker vi runde parenteser.

Egentlig er tupler noe helt andet enn lister.  
Lister er samlinger og mye av poenget er å kunne legge til og ta bort elementer.

Tupler er ikke muterber.  Dvs. det er umulig å legge til eller ta bort elementer.
Vi ser det raskt om vi prøver å endre et element i en tuppel.

Dette er ikke bare en ulempe.  Det er f.eks. mulig å bruke tupler som nøgler i en `dict`.
Lister kan derimot ikke brukes, fordi `dict` er avhengig av at nøglene ikke kan forandres.

Vi bruker helst tupler der vi har et lite og fast antall elementer.

---

## `dict` som samling

*map* : **oppslagsord** $\to$  verdi

note:
`dict` er også et eksempel på en samling.

Ulempen med en liste er at det er vanskelig finne et bestemt element.
Vi må bla gjennom hele listen for å finne det som vi leter efter.

`dict` er et eksempel på en datastruktur som gjerne kalles *map*, dvs. den avbilder et oppslagsord eller en nøgle, på en verdi som gjerne kan være et komplekst objekt.
Dersom elementene våre har en ID som vi kan bruke som nøgle, er det som regel bedre å bruke `dict` enn liste.


---

# Listekomprehensjon


* Liste:
```python
[ uttrykk for element in samling if betingelse]
```
* Set:
```python
{ uttrykk for element in samling if betingelse}
```
* `dict`:
```python
{ utrykk_key: uttrykk_value for element in samling if betingelse ]
```


note:
Snarvei til å lage lister, set og dictionaries


---

# Slutt

note:
Til neste gang
+ iterasjon
+ numpy 
+ JSON og `dict`