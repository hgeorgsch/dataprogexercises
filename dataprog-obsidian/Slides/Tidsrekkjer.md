---
tags:
  - lecture/video
css:
  - css/templates.css
---

<!-- slide template="[[tpl-quote-header]]" -->
## Tidsrekkjer

![[arbeidsledige.svg]]

::: credit
Hans Georg Schaathun
:::

note:
Hei.

Jeg skal prate litt om tidsrekker, som er en meget vanlig for for datasett.

Der er to ting som kjennetegner en tidsrekke.  
For det første har vi numeriske data, som vi kan se for oss som en $y$-akse.
For det andre har vi *tid* som indeks, som vi kan se for oss som en $x$-akse.

Ser vi på paneldata, eller *DataFrame* i pandas, har vi en numerisk søyle og tid som indeks. En *DataFrame* kan bestå av mange tidsserier, der hver serie er en søyle.

---
<!-- slide template="[[tpl-flex]]" -->

![[statbank.png]]

::: credit
:::

note:
Mange datasett inneholder mye data, og det kan være vanskelig å trekke ut de tidsserier vi ønsker å arbeide med.

Bildet viser en tabell over kommuneøkonomi fra SSB.
Vi ser at vi har en indeksering på år bortover, men år er ikke den eneste indekseringen.
Vi har hele tre rader som er brukt til søyleindeksering.  For hvert år har vi tre forskjellige søyler som representerer tre ulike variabler, «brutto driftsresultat», «brutto investeringsutgifter» og «disposisjonsfond».  I tillegg har vi en overskrift  som vi ikke ser fordi tabellen er større enn skjermen, men på toppnivå skilles mellom to varibler, én i kronebeløp og én i andel av driftsinntekter.

Dette systemet med flere overskrifter per søyle kalles for *multiindeks*, og det er et resultat av at vi tabellen konseptuelt sett har fire dimensjoner som skal presses inn i to dimensjoner på skjermen.  Den første dimensjonen er tiden, de andre tre er en for kommunen, en for regnskapsbegrepet og en for måleenheten som er enten kroner eller prosentandel.

---
<!-- slide template="[[tpl-flex]]" -->

![[statbank2.png]]

::: credit
:::

note:
SSB lar oss rotere tabellen, og da får vi årstallet nedover, som er det vi vanligvis ønsker når vi skal jobbe med tidsserier, men vi har fremdeles multiindekser, og totalt seks variabler per år.

Hvis vi skal arbeide med en tidsserie, er vi nødt til å filtrere ut én variabel per år.

---

+ filtrering
+ pivot 
+ melt

---


## Læringsmål

- Repetisjon
	- Utdrag frå datasett: filtrering på fleire søyler.
    - Numeriske søyler
- Nytt stoff
	- Tidssøyler
	- Byte av indeks.
	- Frekvens og gruppering av radar.
	- Fletting av datasett på tid.
- Om me rekk det
	- Manglande data og NaN (not a number).

---

## Problem 1.

> Korleis handterer me ... 

1. ulik presisjon (år, kvartal, månad, dag, tidspunkt)?
2. ulik representasjon som `2025-10-20` eller `20. okt 2025`?
3. ulike tidssonar?

---

+ støy og rolling average
+ oppløysing

---
<!-- slide template="[[tpl-flex]]" -->

![[Units_of_Time_in_tabular_form.png]]

::: credit
By Vikramsurya - Own work, CC BY-SA 4.0,
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=83566382)
:::

---
<!-- slide template="[[tpl-flex]]" -->

![[Time_zones_of_the_world-UTC.svg]]

::: credit
By Goran tek-en, CC BY-SA 4.0, 
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=98591995))
:::