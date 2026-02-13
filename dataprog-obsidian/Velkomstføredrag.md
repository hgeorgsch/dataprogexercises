---
tags:
  - opening
  - lecture/slides
---
<!-- slide template="[[tpl-titleslide]]" -->

# Programmering til Dataanalyse

::: author
Hans Georg Schaathun
:::

::: footer
NTNU---Noregs Teknisk-Naturvitskaplege Universitet
:::

---

## Hans Georg Schaathun

- professor i datafag
- mellomfag i sosialøkonomi
- cand.scient. i industriell og anvendt matematikk og informatikk
- dr.scient. i informatikk (kodeteori)

---

- Maskinlæring i steganalyse rundt 2010
- Velferdsteknologi  rundt 2012-2015
- Optimering for datastøttet design rundt 2015
- Feltstudiar i industridesign  rundt 2015-2017
- Modellering av knær til kirurgisimulatorar  2020-2025
- Matematikkdidaktikk  sidan 2013
- Designmetode og vitskapsteori 2020-2025
- Maskinlæring i kosmologi sidan 2021
- Utdanningsfilosofi  sidan rundt 2018
- KI-filosofi sidan rundt 2020

---

## Jonas Julius Harang

---
## Programmering til Dataanalyse

note:
- Dette er fyrste gongen me held dette kurste for vaksne folk.
	- Det er ikkje sikkert at eg alltid treff, og de må gjerne fortelja meg det
	- eg lytter gjerne til kva de treng
- Dette er ikkje eit kurs der eg veit kva de skal kunna og berre kan forklara dykk korleis de skal gjera ditt og datt
	- Eg kan mykje om programmering og programutvikling og dataanalyse
	- men de skal ikkje lære å programmera som eg gjer
	- de skal læra å bruka programmering i dykkar fag og virke, uansett kva fag det er
	- dykkar fag er det de som kan, og korleis det heng saman med programmering må me finna ut saman
- Hugs det. De er autoritetar i dette faget.  De veit betre enn eg kva som er verd å læra.

---
## Runde i salen

- Kva heiter du?
- Kva arbeider du med?
- Kva er hensikta med programmering for deg?

note:
- Før me går vidare, kan me ta ei runde og høyra kva dykkar fag er.

---

**Mål for samlinga**
koma i gang med programvaren og danna seg eit bilete av kva me skal arbeida med dei neste seks vekene

---
<!-- slide template="[[tpl-twocolumn]]" -->

::: leftimage
## onsdag

- Installasjon
- 11.30-12 Lunsj
- Velkomen
- Økt 1.  Jupyter Notebook
- Briefing til Økt 2.  Dataanalyse
:::
::: leftcredit
:::

::: rightimage
## torsdag

- Økt 2.  Dataanalyse
- 11.30-12.30 Lunsj
- Velkomen
- Økt 3.  Simulering
- Seminar.  Kva vil me med kurset?
- Slutt 15.00
:::
::: rightcredit
:::


note:
Tre gjennomarbeidde døme med oppgåver, samt eit seminar om vegen vidare til slutt.
- Skriva i Jupyter Notebook
- Lasta og studera data i CSV
- Simulering av kontantstraum

Oppgåvene fylgjer det same formatet som me skal bruka gjennom mesteparten av kurset.
Det kjem eg tilbake til.

---
<!-- slide template="[[tpl-flex]]" -->

![[Helmeted_boy_on_training_wheels.jpg]]


::: credit
By Dawn Endico from Menlo Park, California - Terror on Training Wheels, CC BY-SA 2.0
via [wikimedia commons](https://commons.wikimedia.org/w/index.php?curid=7248195)
:::

note:
- Kurset byggjer på den filosofien at programmering sjelden handlar om å vita korleis ein skriv nye løysingar.  Langt oftare handlar det om å leita fram eit døme som løyser eit problem som liknar, for so å tilpassa det.  
- Dersom ein skal læra å hugsa alt ein treng til praktisk bruk, skulle me trenga mykje meir enn 7½ studiepoeng.
- Den litle tida me har er best investert på å læra seg å forstå døma, testa og vurdera kode og å prøva og feila.

---

Gjennomarbeidde døme
<!-- element class="[[r-fit-text]]" -->

note:
Den viktigste læringsaktiviteten i dette kurset er *Gjennomarbeidede eksempler*.

Det er tekster som tar for seg et mer eller mindre interessant spørsmål om økonomi og samfunn, og som bruker programmering for å regne på problemet.

Dere kan laste ned hele teksten og kjøre programkoden, og dere kan prøve dere frem med variasjoner av koden for å teste hvordan den virker.

Jeg pleier å legge med noen øvelser og spørsmål som inspirasjon til utforskning.

Hensikten med dette er selvsagt å utforske bruken av programmering på interessante problemer.

Jeg skal bli mer konkret efter pausen.

---


Spørsmål?
<!-- element class="[[r-fit-text]]" -->


---

Beinstrekk?
<!-- element class="[[r-fit-text]]" -->

---


+ https://iirevu.org.ntnu.no/iira6001/

note:
+ Forsiden 
+ Vurdering
+ Installasjon
+ Oversikt over semesteret:  Senere uker tar vi siden
+ Opningssamling
	+ foiler 
	+ øvelser
+ Økt 1. Første dokument

---

Jupyter Lab
<!-- element class="[[r-fit-text]]" -->

---

## Markdown

```text
# Hovedoverskrift

Vanlig tekst i Markdown skal være lett å naturlig å lese.

## Underoverskrift

Markering i teksten er diskret,
med stjerner for *kursiv* og **halvfet* 
skrift

Blank linje begynner nytt avsnitt.
```


note:
Markdown er det vi kaller et markup-sprog.
De brukes til å skrive tekster som mennesker skal lese, men inneholder formatteringskoder som forteller hvordan teksten skal vises, med overskrifter, kursivering osv.

Markdown er et kompromiss. Målet er at kodene skal være minst mulig forstyrrende, slik at teksten er lett å lese også i kodeformat. Til gjengjeld er formatteringsmulighetene relativt begrensede.

---

 ## $\LaTeX$


```text
\section{Hovedoverskrift}

Vanlig tekst i Markdown skal være lett å naturlig å lese.

\subsection{Underoverskrift}

Markering i teksten er diskret,
med stjerner for \emph{kursiv} og \textbf{halvfet}
skrift

Blank linje begynner nytt avsnitt.
```

note:
For  å illustrere poenget, kan vi sammenligne med $\LaTeX$, som først ble utviklet for å typesette bøker på 1970- og 80-tallet.

---
## HTML

```text
<h1>Hovedoverskrift<h1>
<p>
Vanlig tekst i Markdown skal være lett å naturlig å lese.
</p>

<h2>Underoverskrift</h2>
<p>
Markering i teksten er diskret,
med stjerner for <em>kursiv</em> og <strong>halvfet</strong>
skrift
</p>
<p>
Avsnitt har en egen kode p.
</p>
```


note:
Og HTML som ble utviklet for å lave vevsider i 1994/95.

---

## Markdown

```text
# Hovedoverskrift

Vanlig tekst i Markdown skal være lett å naturlig å lese.

## Underoverskrift

Markering i teksten er diskret,
med stjerner for *kursiv* og **halvfet* 
skrift

Blank linje begynner nytt avsnitt.
```


note:
Men vi skal holde oss til Markdown.

Markdown er et semantisk sprog.  Vi koder overskrifter på nivå 1, 2, 3 osv., og fremhevet skrift som stort sett vises som kursiv eller halvfet.  

Når vi skriver markdown, skal vi tenke på hva koding *betyr* og ikke hvordan den skal vises.
Det gjør at ulike programmer kan vise teksten litt forskjellig, slik at det passer til ulike skjermstørrelser og papirformater.

Dette er uvant for dem som er vokst opp med tekstbehandlere, og det har både fordeler og ulemper.

--- 

## Python

