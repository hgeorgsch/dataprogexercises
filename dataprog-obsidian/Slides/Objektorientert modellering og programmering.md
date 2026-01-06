---
title: Objektorientert modellering og programmering
tags:
  - lecture/video
css:
  - css/templates.css
---

# Objektorientert modellering og programmering

note:
En av de største utfordringene i programmering er at programmene
raskt blir uoversiktlige, og det er vanskelig å holde orden.
Utfordringene vokser både når datasettene blir større, når de
blir mer komplekse og varierte, og når programmene blir lengre.

---
<!-- slide template="[[tpl-twocolumn]]" -->

## Simula (1962)

::: leftimage
![[Ole-Johan_Dahl.jpg]]
:::

::: leftcredit
*Ole-Johan Dahl*,
bilete ved [ACM](https://amturing.acm.org/photo/dahl_6917600.cfm),
Fair use from
[Wikimedia Commons](https://en.wikipedia.org/w/index.php?curid=63417106)
:::

::: rightimage
![[Kristen-Nygaard-SBLP-1997-head.png]]
:::

::: rightcredit
*Kristen Nygaard*,
bilete av Jorge Stolfi - Public Domain,
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=8886807)
:::

note:
En av de mest lovende løsningene for å strukturere komplekse programmer er objekt-orientert programmering.
Denne idéen skriver vi gjerne tilbake til programmeringssproget Simula som ble utviklet ved Norsk Regnesentral i 1962.

Simula som sprog ble aldri noen stor suksess, og det tok kanskje tyve år før objekt-orientert programmering slo an.  De siste femti årene kan vi derimot se hvordan de fleste imperative sprog blir objekt-orienterte.

---
<!-- slide template="[[tpl-diagram]]" -->

## Objektet

![[object.svg]]

::: credit
:::

note:
Det sentrale konseptet i objekt-orientert programmering er sjølvsagt objektet.
Dette er litt tvetydig, siden vi ofte kaller verdien av en variabel for et obkekt,
enten det er et tall, en streng, en liste eller en *dictionary*. 

I objekt-orientert programmering er objektet ikke bare en verdi eller en tilstand.
Objektet har også metoder, eller funksjoner, som modellerer oppførsel.
Vi ser gjerne for oss at objektet kan sanse, gjerne gjennom funksjoner som tar
parametere, og at det kan handle, gjerne gjennom funksjoner med en returverdi som
forteller hva det gjør.

Objektet blir på mange måter et eget mini-program med *input* og *output* som
samhandler med andre mini-programmer som inngår i det store programmet.
Dette gir en modulær struktur som vi kan bruke for å holde orden i programmet.

---

## Klassa

```python
class Counter:
   def increase(self):
      self.state += 1
   def get(self):
      return self.state
```

note:
Siden objektet er en verdi som kan tilordnes en variabel, må det ha en type.
Objekttyper kaller vi for klasser, og vi kan definere våre egne klasser som 
definerer typen for de objekter som vi trenger.

I python er det først og fremst metodene vi definerer i klassen.
En metode er ikke noe andet enn en funksjon som er definert i en klasse.
Metodene tar alltid et argument `self` som viser til objektet selv.
Variablene i objektet blir definert når de blir tilordnet, hvilket helst skjer i metodene.

Ved å samle all kode som opererer på objektet i klassens egne metoder, blir koden ryddigere og det blir lettere å forsikre seg om at den er konsistent.

---
<!-- slide bg="white" template="[[tpl-twocolumn]]" -->

::: leftimage
## Røynda
![[Earth_-_Illustration_(5679642883).jpg|360]]
:::

::: leftcredit
By Ilya Grigorik, CC BY-SA 3.0,
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=74181523)
:::

::: rightimage
## Modellen
![[oo.svg]]
:::

::: rightcredit
<a href="https://www.flaticon.com/">Ikon frå tulpahn - Flaticon</a>
:::

note:
Objekt-orientering er et tankesett som gjennomsyrer både modellering og
programmering.
Et dataprogram er en modell av en eller anden virkelighet,
og når vi designer våre klasser og objekter gjelder det at hvert objekt
er en modell av ett eller andet gjenkjennelig objekt i den virkeligheten
som modelleres.

Skal vi simulere et marked, er objektene kanskje produksjonsbedriften, 
investoren og kunden.

Skal vi simulere et økosystem, er objektenee kanskje rever, kaniner og
det landskapet de bor i.

Hver klasse definerer egenskapene til ett konkret objekt, eller fenomen,
i virkeligheten.

---
<!-- slide template="[[tpl-diagram]]" -->

## Bytte-/Rovdyr

![[lynxhare.jpeg]]

::: credit
frå Brady RM and Butler JS (2021):
[The Circle of Life: The Mathematics of Predator-Prey Relationships](https://kids.frontiersin.org/articles/10.3389/frym.2021.651131). *Frontiers. Young Minds.* 9:651131. doi: 10.3389/frym.2021.651131
CC-BY 4.0
:::

note:
La oss ta et eksempel på en simulator.
Et klassisk eksempel fra biologi og økologi er dynamikken mellom rovdyr og byttedyr,
der populasjonene gjerne svinger i motfase.
Når der er lite byttedyr, går rovdyrpopulasjonen ned fordi der er lite mat, mens
byttedyrpopulasjonen går opp fordi der er få fiender.
Motsatt, når der er mye byttedyr har rovdyrene gode kår og blir flere, mens 
byttdyrene gjerne har mangel på mat og stagnerer, og blir der mye rovdyr,
går byttdyrpopulasjonen ned.

Der er mange måter å simulere dette på.
Den mest detaljerte er å modellere på individnivå.
Hvert dyr er en agent, som kan bevege seg, spise og formere seg.

Hver agent modellerer vi som et objekt, i tillegg til objekter for
å holde rede på verden som helhet.

---
<!-- slide template="[[tpl-diagram]]" -->

## Arv 

![[inheritance.svg]]

::: credit
<a href="https://www.flaticon.com/">Ikon frå tulpahn - Flaticon</a>
:::

note:
Objekt-orientert programmering innebærer et par viktige grunnprinsipper
som hjelper oss til å holde koden ryddig og enkel.

Det første er arv.  
Når vi modellerer økosystemet kan vi både ulver og rever, kaniner og mus,
som antangelig oppfører seg forskjellig.
Dyrene har dog mange felles egenskaper.

De danner et hierarki, der kaniner og mus er byttdyr, og ulver og rever
er rovdyr.
Både rovdyr og byttedyr er agenter i vår simulator, som har det til
felles at de har en plass i landskapet og kan handle.

Når vi programmerer klasser kan vi la en klasse arve hverandre.
Egenskaper som er felles for alle agenter kan legges til en superklasse,
Agent.
Rovdyr kan arve fellesegenskapene fra Agent, og blott definere det som
er spesielt for rovdyrene, f.eks. jakt.
Ulv og rev arver antagelig de fleste egenskapene fra Rovdyr, men noe
kan være spesielt slik at de oppfører seg forskjellig.

---

## Polymorfi 

<hr>

- `agent.act()` $\to$ ???

<hr>

- `rev.act()` $\to$ jakt
- `kanin.act()` $\to$ flykt

note:
Et objekt i objekt-orientert programmering har flere typer samtidig.
Et individ av typen Rev er også et invidid av typen Rovdyr, og dermed
også et individ av typen Agent.

Dette kaller vi polymorfi, fra gresk, poly betyr flere og morf betyr form.
Objekter har flere former.

I en agentbasert simulator har agentene gjerne en metode `act()` som
definerer hva de gjør hver gang det er deres tur til å handle.
De ulike underklassene vil derimot handle forskjellig; det eneste de har
til felles er *at* de handler.
Reven vil jakte, mens kaninen vil flykte.

Polymorfi gjør at programmet kan kalle `act()`-metoden *uten å vite* hvilken
type agenten har eller hvilken definisjon av `act()` som skal brukes.
Det er objektet som vet hvordan det skal handle når metoden blir kalt.


---
<!-- slide template="[[tpl-flex]]" -->

## Python

![[rubber-duck.png]]

::: credit
<a href="https://www.flaticon.com/free-icons/rubber-duck" title="rubber duck icons">Rubber duck icons created by Talha Dogar - Flaticon</a>
:::

note:
Det skal sies at python er ennu mer fleksibelt enn polymorfi i tradisjonelle sprog.
I python trenger vi strengt tatt ikke ha en superklasse som definere `act()` for
å få den polynorfe oppførselen.

Grunnen til dette er at python bruker det som de gjerne kalle *duck typing*.
«Hvis det ser ut som en and, og låter som en and, så er det en and.»

Python bryr seg rett og slett ikke om hvilken type objektet har.
Hvis det har en metode `act()`, så kan det handle, uansett om det er definert
som en agent eller ikke.

Det er likevel en god idé å ha det mentale bildet av arvehierarkiet og felles
egenskaper, fordi det gir et klart bilde av forholdet mellom ulike klasser og
hvordan de representerer virkeligheten.

---

# Slutt

note:
Objekt-orientert programmering er et stort felt med mange muligheter, og
vi har bare skrapt i overflaten.  

Når vi innfører objekt-orientering i dette kurset, så er det først og fremst
med tanke på agent-basert simulering.
Ved å definere hver agent for seg, som en klasse og et objekt, er det mulig å 
simulere meget komplekse modeller.  
Fordi vi bare trenger å se på en enkelt klasse ad gangen, blir modelleringen
overkommelig.
Fordi vi kan instantiere mange objekter av hver klasse, kan vi like fullt 
simulere komplekse og uoversiktlige systemer.

Det er på tide å prøve seg på en oppgave.
