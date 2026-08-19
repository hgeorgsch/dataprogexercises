---
tags:
  - opening
  - lecture/slides
css:
  - css/templates.css
---
<!-- slide template="[[tpl-titleslide]]" -->

# Maskinlæring i Biologiske Fag

::: author
Hans Georg Schaathun
:::

::: footer
NTNU---Noregs Teknisk-Naturvitskaplege Universitet
:::

---

## Hans Georg Schaathun

- professor i datafag, Høgskolen i Ålesund/NTNU frå 2011
- *lecturer*/*senior lecturer*, Universitetet i Surrey 2006-2010
- Post.doc. m.m., Universitetet i Bergen 2002-2006
- dr.scient. i informatikk (kodeteori) 2002
- cand.scient. i industriell og anvendt matematikk og informatikk 1999
- mellomfag i sosialøkonomi  1996

note:
Presentasjon 

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

note:
Eg har arbeidd med ganske mange forskjellige fagfelt og tema, særleg dei femten åra
som eg har vore ved NTNU og Høgskolen i Ålesund.
I staden for å reindyrka ein akademisk disiplin, er eg genuint interessert i å forstå anvendingsområda på sine eigne premissar.
Akkurat det fargar òg korleis eg ser dette kurset og oppgåvene me skal arbeida med.

---

## Snorre Bakke

- Biomarin innovasjon

note:
Med meg har eg Snorre.


---
## Runde i salen

- Kva heiter du?
- Kvifor er du her?
- Kva tenkjer du å arbeida med om 3-5 år

note:
- Før me går vidare, kan me ta ei runde og høyra kva dykkar fag er.

---
## Maskinlæring i Biologiske Fag

- Kunstig Intelligens: Korleis tenkjer maskiner?
- Kva kan me bruka det til i biologiske fag?
- Programmering: Korleis kontrollerer me maskina?
- Datahandsaming: Korleis held me styr på store data?
- Statistikk: Kor mykje kan me stola på maskina?

---
## Programvaren

- Python 
- pip
- Jupyter lab

**Mål i dag** Koma i gang med programvaren

---
<!-- slide template="[[tpl-flex]]" -->

![[Helmeted_boy_on_training_wheels.jpg|500]]


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


- https://iirevu.org.ntnu.no/iira2011/

note:
- Forsiden 
- Vurdering
- Installasjon
- Oversikt over semesteret:  Senere uker tar vi siden
- Opningssamling
	- foiler 
	- øvelser
- Økt 1. Første dokument

---

Spørsmål?
<!-- element class="[[r-fit-text]]" -->


---

- **Jupyter Lab**  - verktyet
- **Python** - språket
- **pip** - installerer tilbehør til python

$\to$ demo

note:
Demonstrasjon

1. Kommandoline
2. `python --version`
3. `pip install jupyterlab`
4. `jupyter lab`


---
<!-- slide template="[[tpl-ntnu]]" -->

## Programmering

---
<!-- slide template="[[tpl-ntnu]]" -->

Eit **Dataprogram**
er ein *serie med instruksjonar*

$\to$ *demo*

---
<!-- slide template="[[tpl-ntnu]]" -->

Ein **variabel** er en *verdi med namn*.

note:
Verdien er data i minnet på maskinen, og navnet gjør at
vi kan finne dataene igjen.

---

## Programinstruksjonar

- **Tilording:** `variabel = 17`
- **I/O:**  `print( variabel )`
- **Kontroll:** `if variabel < 20: print( variabel )`
- **Aritmetikk:** `variabel2 = 3*variabel`

---

## Python i Jupyter

note:
Tilbake i Jupyter

1. Litt kode
2.  Litt  Markdown

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
med stjerner for \emph{kursiv} og \textbf{halvfet} skrift

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
med stjerner for <em>kursiv</em> og 
<strong>halvfet</strong> skrift
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

## Fyrste Dokument

$\to$ demo

note:
Lasta ned og opna

Bruk filnavigatøren

---

## Eit par tips

- dokumentet er eit program om du køyrer frå start
- celler kan køyrast i feil rekkjefylgje
- variabelvising med og utan `print`

---

Spørsmål?
<!-- element class="[[r-fit-text]]" -->
