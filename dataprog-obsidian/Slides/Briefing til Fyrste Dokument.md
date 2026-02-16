---
tags:
  - opening
  - lecture/slides
css:
  - css/templates.css
---
<!-- slide template="[[tpl-titleslide]]" -->

# Briefing til Fyrste Dokument

::: author
Hans Georg Schaathun
:::

::: footer
NTNU---Noregs Teknisk-Naturvitskaplege Universitet
:::

---

- **Jupyter Lab**  - verktyet
- **Python** - språket
- Anaconda er eit verkty for å installera andre verkty

note:
Opna Jupyter Lab.

Dette er én av svært mange måter å bruke python på.

Vise kodeblokk.

1. Kode-blokk

---
<!-- slide template="[[tpl-ntnu]]" -->

Eit **Dataprogram**
er ein *serie med instruksjonar*

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
2, Litt Markdown

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
