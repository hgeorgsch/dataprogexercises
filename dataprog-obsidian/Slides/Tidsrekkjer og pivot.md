---
tags:
  - lecture/video
css:
  - css/templates.css
---

<!-- slide template="[[tpl-quote-header]]" -->
# Tidsrekkjer og *pivot*

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

Dette systemet med flere overskrifter per søyle kalles for *multiindeks*, og det er et resultat av at tabellen konseptuelt sett har fire dimensjoner som skal presses inn i to dimensjoner på skjermen.  Den første dimensjonen er tiden, de andre tre er en for kommunen, en for regnskapsbegrepet og en for måleenheten som er enten kroner eller prosentandel.

---
<!-- slide template="[[tpl-flex]]" -->

![[statbank2.png]]

::: credit
:::

note:
SSB lar oss rotere tabellen, og da får vi årstallet nedover, som er det vi vanligvis ønsker når vi skal jobbe med tidsserier, men vi har fremdeles multiindekser, og totalt seks variabler per år.

Hvis vi skal arbeide med en tidsserie, er vi nødt til å filtrere ut én variabel per år.

Den enkleste måten å gjøre det på, er gjerne å filtrere datasettet slik at vi bare tar med én variabel, men hvis vi ønsker å ha med alle mulige tidssrekker i tabellen, kan vi prøve med *pivot*.

---
<!-- slide template="[[tpl-flex]]" -->

![[prepivot.png]]

note:
Hvis vi laster ned datasettet direkte fra SSB får vi tre søyler som egentlig hører til indeksen.

---
<!-- slide template="[[tpl-flex]]" -->

![[pivot.png]]

::: credit
Resultat av `pivot`
::: 

note:
Metoden `pivot` lar oss brette ut tabellen i bredt format.

Vi kan fortelle `pivot` at «år» skal være radindeks, mens de to dimensjonene «statistikkvariabel» og  «regnskapsbegrep» flyttes til å bli søyleindekser.
Dermed blir de ekstra søyler under kommunene, i stedet for ekstra rader under årene.

Resultatet er at vi står igjen med bare én radindeks, for år.  Vi har uhorvelig mange søyler, for ulike variabler og ulike kommuner, og hver eneste søyle er en tidsrekke.

---

- *pivot* og *melt*
- transponering

note:
Vi kan også gjøre den motsatte operasjonen, som heter *melt*.

Hvis vi skulle ha et datasett med årstallene bortover, kan vi transponere en *DataFrame*
på samme måte som vi transponerer matriser.  Dvs. tabellen blir rotert nitti grader.
Bare søk efter *transpose* for å finne eksempler.

---

# Slutt

note:
Jeg håper dette gir mening, men vi laver også en demonstrasjonsvideo som viser detaljene når vi koder operasjonene i python.