---
title: Datastrukturar
author: Hans Georg Schaathun
date: December 2025
tags:
  - lecture/video/perspective
css:
  - css/templates.css
---

# Datastrukturar

note:
Når vi skal håndtere store datamengder, enten det er komplekse simuleringer
med mange variabler eller datasett med mange observasjoner av de samme variabler,
trenger vi datastrukturer for å systematisere dem.

---

`x`
<!-- element class="r-fit-text" -->

note:
Én variabel i python kan representere alt fra ett enkelt tall til en 
tabell med flere milliarder verdier.
Dette er ulike datatyper.
Noen datatyper er primitive, mens andre typer kan inneholde flere verdier
som har sine egne datatyper.
De primitive datatypene er dem som ikke kan deles opp.

---

## Primitive datatypar

- heiltal (`int`) $\ldots, -1, 0, +1, +2, \ldots$
- flyttal (`float`) t.d. $-50{,}1$, $0$, $0{,}1$, $2{,}4$,  $10{,}0$
- bolsk (`bool`) : `True` eller `False`
- teikn : t.d. `'a'`, `'z'`, `'!'`, `'7'`
- strengar (`str`) : t.d. `"Hello World!"`

note:
De primitive datatypene håper jeg du kjenner.
De representerer enkeltverdier, som tall, sann/usann, eller
tegnstrenger.

Det kan diskuteres om tegnstrenger egentlig er en primitiv datatype.
Mange programmeringssprog behandler strenger som en sammensatt type som
består av en liste med tegn.
Python skiller derimot ikke mellom tegn og strenger.
Et tegn er blott en streng med lengde én.
Dermed kan vi ikke dele opp strengtypen i mindre typer, og vi blir nødt til
å se på det som en primitiv type.

---
## Samansette datatypar

- tupler : t.d. `(1,0.5)`, `("Oskar", 83)`
- liste : t.d.  `[ 2, 3, 11, 3, 11, 11 ]`
- avbilding (*map*) eller `dict`
- klasser 

note:
Der er mange sammensatte datatyper, og det kan være vanskelig
å skille dem fra hverandre.
Vi skal først snakke litt om hvordan vi modellerer data
uavhengig av python.

Datastrukturar er ikke bare en teknisk finesse i python.
Det er òg nyttig å bruke datastrukturer for å forklare hvordan
våre data ser ut og hvordan vi ønsker å behandle dem.

---

## *Record*

|        kunde | verdi          |
| -----------: | :------------- |
|    `fornamn` | "Ola"          |
|  `etternamn` | "Normann"      |
| `postnummer` | 6016           |
|       `gate` | "Borgundvegen" |
|     `nummer` | 666            |

note:
En typisk utfordring er når vi trenger en variabel for å representere ett fenomen,
f.eks. en kunde, og dette fenomenet har mange egenskaper som krever hver sin datatype,
f.eks. navn, adresse og fødselsdato.

Tradisjonelt har vi gjerne kalt dette for en *record*.
Jeg har ikke et godt norsk ord, men vi kan tenke på et arkivkort.
En *record* har flere felter, der hvert felt har et navn og en verdi.

---

# Tuplar

- (0,1, 2,5)
- `("Oskar", 83)`
- ( $x$, $y$ )
- `( "Ola Nordmann", "Borgundvegen 666", "6060 Ålesund", 2012-10-14)

note:
Dersom vi ikke setter navn på feltene i en *record*, får vi det som
vi kaller en tuppel.

I python og mange andre sprog skriver vi en tuppel som en kommaseparert 
liste i *runde* parenteser.
Tupler med to eller tre elementer, kaller vi gjerne for par og tripler.

Tupler er den raskeste måten å sette sammen flere primitive typer,
f.eks. i en funksjon som skal returnere flere verdier, men resultatet 
er ofte kode som er vanskelig å forstå.  
Det lønner seg ofte å definere mer omstendelige typer, for at koden
skal bli lettere å lese.

---
<!-- slide template="[[tpl-diagram]]" -->

## Avbilding (*map*)

![[map.svg|480]]

::: credit
:::

note:
Et andet typisk problem er samlinger av objekter, f.eks. et kunderegister,
som er en samling av kunderkort.
Der er mange ulike datastrukturer som organiserer samlinger.
Noen er lavet for at det skal gå raskt å søke, mens andre for at det skal gå raskt å sette inn eller fjerne elementer.

La oss begynne med avbildninger eller *maps*.
Her har hvert objekt en nøgle som vi kan bruke for å slå det opp.
I kunderegisteret kan vi f.eks. bruke navn, slik at datastrukturen avbilder navn på kundekort.

Den vanligste formen for avbildninger kalles *hashmap*, og ofte er dette ordet dere finner brukt.
Poenget med en *hashmap* er at det skal være raskt å slå opp en gitt nøgle, uansett hvor stor samlingen er.  Normalt er det også raskt å sette inn eller slette objekter. For å få det til, bruker  datastrukturen som regel ekstra minne, som er holdt av til ubrukte nøgler.  Det er dog sjelden et problem på dagens maskiner.

*Dictionaries* eller `dict` i python er et eksempel på *hashmaps*.

---
<!-- slide template="[[tpl-smalltext]]" -->

## Liste

```python
[ "Ola Nordmann", "Kari Nordmann", "John Smith", "Jane Doe", ... ]
```
<!-- element class="widecode" -->

::: credit
:::

note:
Lister lagrer objekter i rekkefølge.  

De er normalt lavet for at det skal være raskt å bla gjennom element for element fra starten av listen.
Det skal også være raskt å legge til eller fjerne et element fra enden av listen.
I python vil det si slutten av listen, men i andre sprog kan det være i
starten av listen at det går raskt å gjøre endringer.

---

## Tabell (*array*)

| # | Verdi |
| :- | :- |
| 0  | `"Ola Nordmann"` |
| 1 | `"Kari Nordmann"` |
| 2 | `"John Smith"` |
| 3 | `"Jane Doe"` |
| 4 | `"Tom"` |
| 5 | `"Dick"` |
| 6 | `"Harry"` |

note:
En *array* ligner en liste, men prioriteringene er anderledes.
Elementene har nummererte plasser, og det skal alltid være raskt å slå
opp eller bytte ut et element hvis vi kjenner plassnummeret, eller indeksen.
Det er derimot ikke alltid så enkelt å gjøre endringer hverken på starten eller
slutten av tabellen.

I utgangspunktet har en *array* et fast antall plasser, og skal man legge til
eller fjerne elementer, må man lave en ny *array* med riktig størrelse.

---
<!-- slide template="[[tpl-smalltext]]" -->

## Lister i python

```
In [2]: kunder = [ "Ola Nordmann", "Kari Nordmann", "John Smith", "Jane Doe" ]

In [3]: print( kunder[1] )
Kari Nordmann
```

::: credit
:::

note:
Lister i python er implementert som *arrays*, med litt ekstra funksjonalitet og automatikk.
Det gjør at vi kan indeksere elementer, og raskt hente elementer fra en kjent, nummerert plass i listen.

Problemet med å legge til eller fjerne elementer er løst ved at python holder av
ekstra plass og vet hvor listen slutter.
Når listen går tom for plass, vil det plutselig ta lang tid å legge til elementer, 
fordi python må allokere nytt minne og kopiere hele listen til en ny plass.
Det skjer derimot sjelden.

Det som går treigt med python sine lister er å sette inn eller fjerne
elementer midt i listen.  Da må alle efterfølgende elementer flyttes, enten for å fylle plasssen når et element blir fjernet, eller for å gi plass til nye elementer.
Hvis listen er langt kan dette gå fryktelig treigt.

---

- mengder
- sortert liste
- kø
- prioritetskø

note:
Der finnes mange andre typer samlinger.
Hver type har sine fordeler og ulemper, 
men i de fleste små prosjekter klarer man seg fint med disse to: lister og *map*, 
eller `list` og `dict` i python.

---
<!-- slide template="[[tpl-flex]]" -->

![[Pandas_dataframe.png]]

::: credit
By Lucasadvent - Own work, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=131116177
:::

note:
Vi vil støte på nogen flere datastrukturer efter hvert.
I dataanalyse trenger vi store tabeller med numeriske data.
Her kan vi bruke både `DataFrame` fra pandas-biblioteket
og numpy *arrays*.

Vi vil òg trenge en type for dato og klokkeslett.

Men det kommer vi tilbake til.  Takk for nu.

