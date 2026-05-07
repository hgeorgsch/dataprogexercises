---
author: Hans Georg Schaathun
date: December 2025
css:
  - css/templates.css
tags:
  - topic/machinelearning
  - lecture/video/perspective
plugins:
  - scripts:
    - css/auto.js
---

<!-- slide template="[[tpl-title]]" -->
![Klyngeanalyse](Klyngeanalyse.mp4)<!-- element data-autoplay onended="Reveal.next()" -->

---
<!-- slide template="[[tpl-flex]]" -->

![[Supervised_machine_learning_in_a_nutshell.svg]]

::: credit
By EpochFail - Own work, CC BY-SA 4.0,
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=45021868)
:::

![[klynge01.mp3]]<!-- element data-autoplay onended="Reveal.next()" -->

note:
Den mest kjente formen for maskinlæring er veiledet læring,
eller *supervised learning*.
Her er vi avhengige av treningsdata som er ferdig klassifisert.  
Dvs. for hvert objekt i treningssettet har vi en kjent klasse eller målverdi.
Vi trener modellen for å kunne gjenskape akkurat denne verdien på nye andre data der den verdien er ukjent, men på treningdataene må den være kjent.

Der er mange problemer som kan løses med veiledet læring, men i mange tilfeller finnes der ikke en åbenbar klassifisering *a priori*.  Hva om vi kan identifisere interessante klasser, eller klynger, direkte fra datasettet uten å gjøre nogen forutsetninger?

---
<!-- slide template="[[tpl-flex]]" -->

![[customers.svg]]

::: credit
:::

![[klynge02.mp3]]<!-- element data-autoplay onended="Reveal.next()" -->

note:
Ett typisk eksempel er kundesegmentering, eller markedsegmentering.
Problemet er i og for seg ikke at vi har kjente kundekategorier,
men at der er så mange av dem. Vi kan tenke på sosioøkonomisk klasse,
utdannelsesnivå, bosted, men hvis vi legger like mye vekt på alt,
ser vi bare at kundene er unike.

Løsningen er det som vi gjerne kaller klyngeanalyse.
Kan vi identifisere klynger av kunder som ligner på hverandre?

---
<!-- slide template="[[tpl-flex]]" -->

![[klyngedemo-initial.svg]]

::: credit
:::

![[klynge03.mp3]]<!-- element data-autoplay onended="Reveal.next()" -->

note:
Datasettet vårt ser kanskje slik ut.
Det vil si, vi ser på kundene våre som vektorer av tall,
som vi kan visualisere som punkter i et $n$-dimensjonalt rom.
Her har vi bare plottet to verdier $(x,y)$ i planet, kanskje
inntekt og formue.  I praksis kan vi ha hundrevis av variabler.

I plottet kan vi kanskje ane tre klynger, med litt mer spredde
punkter imellom, selv om mønsteret ikke er veldig tydlig.

---

- *Supervised learning*
- *Unsupervised learning*

![[klynge04.mp3]]<!-- element data-autoplay onended="Reveal.next()" -->

note:
Spørsmålet er om vi kan identifisere disse klyngene algoritmisk.

Hvis vi hadde hatt et eksempel med en kjent klyngeinndeling, kunne
vi ha brukt Fisher-diskriminanter, SVM eller nevrale nettverk.
Alle disse algoritmene er eksempler på *supervised learning* eller
veiledet læring.

Siden vi ikke har kjente klynger, må vi trene modeleln uten veiledning,
altså *unsupervised learning*.

---

$k$-*means*
<!-- element class="[[r-fit-text]]" -->

note:
Den mest kjente algoritmen for læring uten veiledning er $k$-*means*.

Prinsippet for $k$-*means* er at hver klynge er representert med en
vektor som er gjennomsnittet, *mean*, i sin klynge.
Hvert datapunkt hører så til nærmeste klynge, målt med utgangspunkt
i denne gjennomsnittsrepresentanten.

---

![[klyngedemo00.svg]]

note:
Vi kan ta et eksempel.
La oss forutsette tre klynger.

Vi starter med tre vilkårlig valgte vektorer som representerer hver sin
klynge.

---

![[klyngedemo01a.svg]]

note:
Første steg i algoritmen er å danne klynger ved å identifisere
hvert datapunkt med nærmeste representant.  Da ser det slik ut.

---

![[klyngedemo01b.svg]]

note:
Andre steg i algoritmen er å oppdatere representantene slik at de
er gjennomsnitt i sin klynge.

I figurene har de sorte representantpunktene flyttet, men datapunktene
har ikke endret farve.

---

![[klyngedemo02a.svg]]

note:
Så gjentar vi.

Førs oppdaterer vi klyngetilordningen.

---

![[klyngedemo02b.svg]]

note:
Dernest oppdaterer vi representantene.

---

![[klyngedemo03a.svg]]

note:
Algoritmen fortsetter å iterere med disse to stegene.

---

![[klyngedemo03b.svg]]

note:
For hver gang blir klyngeinndelingen litt bedre.

---

![[klyngedemo04a.svg]]

note:
og endringene fra forrige iterasjon blir også mindre og mindre.

---

![[klyngedemo04b.svg]]

note:
før eller siden blir endringene fra iterasjon til iterasjon så
små at de ikke lenger spiller nogen rolle.

---

![[klyngedemo-final.svg]]

note:
da er det på tide å stoppe.

---

$k$-*means*
<!-- element class="[[r-fit-text]]" -->

note:
$k$-*means* er en meget enkel algoritme, faktisk så enkel at det
er en grei studentøvelse å implementere den selv, i alle fall om 
man har lest matriseregning.

Det er nyttig å se hvordan iterasjonene gradvis forbedrer løsningen,
fordi dette er grunnprinsippet for de fleste maskinlæringsalgoritmer.
Også nevrale nettverk fungerer på denne måten.  Man starter med en
tilfeldig modell, som sannsynligvis er håpløst dårlig, men så forbedrer
man den ved å se på dataene og justere modellen.

Hver gang man justerer modellen, blir den litt bedre.

Finner man nye data, kan man også fortsette å trene en eksisterende modell,
som forhåpentligvis gir en bedre start.

---

$k$
<!-- element class="[[r-fit-text]]" -->

note:
Utfordringen i $k$-means er at man må velge $k$, dvs. antallet klynger.
Som regel krever det prøving og feiling.

---

## Lykke til videre

note:
I praksis trenger du selvsagt ikke implementere $k$-means selv.
Algoritmen er implementert i SciKitLearn for python og i mange
andre biblioteker.
Du kan starte med et hvilket som helst datasett som du er interessert i, og se hva $k$-*means* gjør for deg.


