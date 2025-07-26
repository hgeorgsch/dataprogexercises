---
title: CSV og Deskriptiv Statistikk
tags:
  - session
  - statistics
  - csv
---

# CSV og Deskriptiv Statistikk

+ **Læringsmål**
	+ Kunna finna, lasta ned og bruka filer frå ulike kjelder 
		+ kunna kjenna igjen og byta teiknkoding
		+ kjenna ulike filformat og dialektar av CSV
	+ Kunna bruka pandas til deskriptiv statistikk og plotting
+ *Perspektivførelesing*
	+ [[Filhandtering]]
	+  [[Konseptuell forståing av  pandas]]  veke 40-41/2024
+ Utsett til seinare
	+ Lagring og organisering
		+ app versys filsystem
		+ versjonskontroll
		+ git og github
	+ Moglege øvingar og demoar
		+ git og github

+ *Demovideo*
	+ [[Filkonvertering og -import]]
	+ [[Plot i pandas]]
	+ [[Gjennomsnitt og spreding]] 
+ Step 1.  Pandas
	+ Step 1a.  Extracting Series and making plots.
	+ Step 1b.   Gjennomsnitt og standardavvik
	+ Kombinasjon (fletting) av datasett
+ Step 2. Plott
    + Plot/subplot og eksport av figurar
    + Ulike plot: histogram/scatter/kakediagram
	+ Eksporting plots
+ Oppgåver
    + [[Jordskjelv]] demonstrerer animasjon og plotting oppå kart
    + [[Genetikk]] demonstrerer korrelasjon m.m.
	+ [[Arbeidsledige]] : Latin 1,  Kombiner arbeidsledige og konkurser
		+ Utfordring: Konverter 1980M1 til dato
		+ Oppgåve: Plott begge datasett
		+ Refleksjon: samanheng?
		+ Utfordring: aggreger kvartalsdata
		+ Oppgåve: Korrelasjonskoeffisient
		+ Oppgåve: Korrelasjonskoeffisient med forskjøvede data
	+ [[Eksportdata]] requires extensive pre-processing to extract comparable data


+ Grunnleggjande pandas
	+ index
	+ søyler og radar
	+ tabellar og seriar
	+ utdrag av tabellar
+ Plott
+ Vidaregåande
	+ snitt og union
+ ToDo
	+ [ ] Samla gode døme på CSV-filer
	+ [ ] Set saman øvingar

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
+ Oversikt of CSV-data under
	
| Topic                   | File                        | Type                | Encoding                                 | Newline                    |
| :---------------------- | :-------------------------- | ------------------- | ---------------------------------------- | -------------------------- |
|                         | arbeidsledige.csv           | Semikolon+ metadata | ASCII text                               | with CRLF line terminators |
| User data (kvalitativt) | blackboard.csv              | Tab                 | Unicode text, UTF-16, little-endian text |                            |
| GDP                     | eu_GDP.csv                  | CSV                 | Unicode text, UTF-8 text                 |                            |
|                         | folketall.csv               | Tab                 | ISO-8859 text                            | with CRLF line terminators |
|                         | helsepersonell.csv          | Semikolon+ metadata | ISO-8859 text                            | with CRLF line terminators |
|                         | konkurser.csv               | Tab                 | ISO-8859 text                            | with CRLF line terminators |
|                         | laksedata.csv               | Semikolon+ metadata | ASCII text                               | with CRLF line terminators |
|                         | namq_10_gdp_page_linear.csv | CSV                 | ASCII text                               |                            |
|                         | teina010_linear.csv         | CSV                 | ASCII text                               |                            |
| Valutalurs              | `EXR20250401.csv`           | semicolon           | UTF8                                     |                            |
