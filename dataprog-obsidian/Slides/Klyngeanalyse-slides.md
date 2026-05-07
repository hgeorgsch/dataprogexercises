---
author: Hans Georg Schaathun
date: December 2025
css:
  - css/templates.css
tags:
  - topic/machinelearning
  - lecture/video/perspective
enableAudioSlideshow: true
---

![Klyngeanalyse](Klyngeanalyse.mp4)<!-- element data-autoplay -->

---
<!-- slide template="[[tpl-flex]]" -->

![[Supervised_machine_learning_in_a_nutshell.svg]]

::: credit
By EpochFail - Own work, CC BY-SA 4.0,
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=45021868)
:::

note:
Den mest kjente formen for maskinlæring er veiledet læring, eller *supervised learning*.
Her er vi avhengige av treningsdata som er ferdig klassifisert.  
Dvs. for hvert objekt i treningssettet har vi en kjent klasse eller målverdi.
Vi trener modellen for å kunne gjenskape akkurat denne verdien på nye andre data der den verdien er ukjent, men på treningdataene må den være kjent.

Der er mange problemer som kan løses med veiledet læring, men i mange tilfeller finnes der ikke en åbenbar klassifisering *a priori*.  Hva om vi kan identifisere interessante klasser, eller klynger, direkte fra datasettet uten å gjøre nogen forutsetninger?

---
<!-- slide template="[[tpl-flex]]" -->

![[customers.svg]]

::: credit
:::

note:
Ett typisk eksempel er kundesegmentering, eller markedsegmentering.
Problemet er i og for seg ikke at vi har kjente kundekategorier, men at der er så mange av dem. Vi kan tenke på sosioøkonomisk klasse, utdannelsesnivå, bosted, men hvis vi legger like mye vekt på alt, ser vi bare at kundene er unike.

Løsningen er det som vi gjerne kaller klyngeanalyse.
Kan vi identifisere klynger av kunder som ligner på hverandre?

---
<!-- slide template="[[tpl-flex]]" -->

![[klyngedemo-initial.svg]]

::: credit
:::


---

+ *Supervised learning*
+ *Unsupervised learning*


---

$k$-means
<!-- element class="[[r-fit-text]]" -->


---

![[klynge-initial.svg]]

---

![[klyngedemo01a.svg]]

---

![[klyngedemo01b.svg]]

---

![[klyngedemo02a.svg]]

---

![[klyngedemo02b.svg]]

---

![[klyngedemo03a.svg]]

---

![[klyngedemo03b.svg]]

---

![[klyngedemo04a.svg]]

---

![[klyngedemo04b.svg]]

---

![[klyngedemo-final.svg]]

---

+ Kundesegmentering
