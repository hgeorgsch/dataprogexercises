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

## Agent-baserte modeller


<!-- slide template="[[tpl-diagram]]" -->

## Bytte-/Rovdyr

![[lynxhare.jpeg]]

::: credit
frå Brady RM and Butler JS (2021):
[The Circle of Life: The Mathematics of Predator-Prey Relationships](https://kids.frontiersin.org/articles/10.3389/frym.2021.651131). *Frontiers. Young Minds.* 9:651131. doi: 10.3389/frym.2021.651131
CC-BY 4.0
:::


---
<!-- slide template="[[tpl-diagram]]" -->

## Arv 

![[inheritance.svg]]

::: credit
:::

note:

---

## Polymorfi 


---

## Python


---
<!-- slide template="[[tpl-diagram]]" -->

## Innkapsling


![[object.svg]]

::: credit
:::

---

# Slutt

note:
Objekt-orientert programmering er et stort felt med mange muligheter, og
vi har bare skrapt i overflaten.
