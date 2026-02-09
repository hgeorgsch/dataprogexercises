---
title: CSV og pandas
tags:
  - csv
  - topic/pandas
  - topic/statistics
---
# CSV og pandas

Dette inngår som veke 3-4 i [[IIRA6001]]

+ Veke 3. Tidsrekkjer
+ Veke 4.  
	+ [[Flyttal og NaN]]
	+ Fletting av datasett

+ Perspektivføredrag.  Del 1.
    + [[Filhandtering]]
    + [[Statistikk med pandas]]
        + [[Notar til Statistikk med pandas]]
+ Øvingar Del 1
    + [[Eksportdata]]
    + [[Tid og dato]]
+ Perspektivføredrag.  Del 2.
	+ [[Tidsrekkjer]]
	+ [[Fletting av datasett]]
	+ [[Melt og Pivot]]

## Skisser og idéar

+ Grunnleggjande pandas
	+ index
	+ søyler og radar
	+ tabellar og seriar
	+ utdrag av tabellar
+ Plott
+ Vidaregåande
	+ snitt og union
+ [[Semi-avansert-Pandas]]  veke 44/2024
	+ Filtrering (viktig)
	+ melt og pivot (?)
	+ [[example-piechart]]
	+ [[example-encoding]]
+ Relatert stoff frå tidlegare år	
	+ [[Manipulere-Dataframes]]    veke 42/2024
		+ grunnteknikkar - manuell opprettning av *Series* og *DataFrame*
		+ éi oppgåve
		+ kun for spesielt interesserte
	+ [[Pandas-Lese-Data-JH]] frå CSV veke 43/2024
		+ Bruker blackboard-data
		+ I stor grad dekt i opningsseminaret
	+ [[Multiindex]]
		+ see also [[Multiindex 2024]]


## Sjekkliste 

+ Step 1.  Pandas
	+ Step 1a.  Extracting Series and making plots.
	+ Step 1b.   Gjennomsnitt og standardavvik
	+ Kombinasjon (fletting) av datasett
+ Step 2. Plott
    + Plot/subplot og eksport av figurar
    + Ulike plot: histogram/scatter/kakediagram
	+ Eksporting plots
+ Step 3. NaN
+ Step 4. melt og pivot

## Materiale som ikkje fekk plass med valuta 

+ Sjå etter endring - differanse
    1. plott differanse
+ Korrelasjon mellom valutaar?

## Førelesingstema

+ Algoritma
    + Historie
    + Syntaks og semantikk
    + Representasjon - pseudo-kode og programkode
    + Generalisering og abstraksjon
+ Filer, format og filsystem
    + Ulike verkty for same fil
    + Kommandoline
    + Tekst versus binærformat
    + git og github - versjonskontroll

## Datasets 

| Topic                   | File                             | Type                | Encoding                       | Newline | Brukt                          |
| :---------------------- | :------------------------------- | ------------------- | ------------------------------ | ------- | ------------------------------ |
| Arbeidsledigheit        | arbeidsledige.csv                | Semikolon+ metadata | ASCII                          | CRLF    | erstatta av 1054.csv           |
| Arbeidsledigheit        | [1054.csv](/notebook/1054.csv)   | Semikolon           | Latin 1                        | CRLF    | [[Arbeidsledige]]              |
| User data (kvalitativt) | blackboard.csv                   | Tab                 | Unicode, UTF-16, little-endian |         |                                |
| GDP                     | eu_GDP.csv                       | CSV                 | Unicode, UTF-8                 |         |                                |
|                         | folketall.csv                    | Tab                 | ISO-8859                       | CRLF    |                                |
|                         | helsepersonell.csv               | Semikolon+ metadata | ISO-8859                       | CRLF    |                                |
|                         | konkurser.csv                    | Tab                 | ISO-8859                       | CRLF    | erstatta av 62495.csv          |
|                         | [62495.csv](/notebook/62495.csv) | Tab                 | ISO-8859                       | CRLF    | [[Arbeidsledige og Konkursar]] |
|                         | laksedata.csv                    | Semikolon+ metadata | ASCII                          | CRLF    |                                |
|                         | namq_10_gdp_page_linear.csv      | CSV                 | ASCII                          |         |                                |
|                         | teina010_linear.csv              | CSV                 | ASCII                          |         |                                |
| Valutalurs              | `EXR20250401.csv`                | semicolon           | UTF8                           |         | [[Fyrste datasett med CSV]]    |
| Lånesøknad | [loan_approval.csv](/notebook/loan_approval.csv) | CSV           | ASCII                           |         | [[Lånesøknad]]    |
| Customer Segmentation | [Mall_Customers.csv](/notebook/Mall_Customers.csv) | CSV           | ASCII                           |         | [[Kundesegmentering]]    |
