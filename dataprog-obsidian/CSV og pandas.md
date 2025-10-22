---
title: CSV og pandas
tags:
   - csv
   - pandas
   - statistics
---

# CSV og pandas

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

+ Øvingar
    + [[Tid og dato]]


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
