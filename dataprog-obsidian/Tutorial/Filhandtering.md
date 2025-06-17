---
tags:
  - lecture/perspective
---
+ Filtransformasjonar og orden
	+ kjeldefiler
	+ programkode
	+ genererte filer
+ Filformat
	+ Binær- og tekstfiler
	+ Format som me bruker
		+ CSV
		+ JSON
			+ datafiler
			+ jupyter notebook
		+ py
		+ md
	+ Syntaks og semantikk
	+ Vanlege binærformat
		+ Excel
		+ MS-Word
		+ PDF

+ Teiknkoding
	+ ASCII  128 teikn inkl. kontrollteikn
	+ Latin 1  $\sim$ 230 teikn, nok til norsk, svensk, samisk og islandsk
	+ Latin 15  €, œ, Œ, mfl. men manglar ¼, ½, fransk og finsk
	+ UTF-8 millionar av teikn, og høve til utviding
	+ Windows-1252
+ Lineskiftkonvensjonar
+ Lagring og organisering
	+ app versys filsystem
	+ versjonskontroll
	+ git og github


+ Moglege øvingar og demoar
	+ git og github

# Filformat og teiknkoding
	
## CSV 

* En vanlig måte å lagre data på er i csv-format
* csv = comma separated values
* I en csv-fil har vi data lagret som tekst i en type tabellformat
* Hver linje i filen er et datapunkt, og inneholder et eller flere felt med data (kolonner)
* Datafeltene er separert med en *separator*, ofte et komma
* Første linje i filen gir gjerne metadata (navn på kolonnene)

## Tegnkoding

* CSV-filer er som sagt vanlig tekst, men:
    - Tekst kan representeres på forkjellige måter i en datamaskin
    - Måten kalles tegnkodingen (character-coding)
    - Vi må ofte sørge for riktig inputkoding (input-encoding) for å få ut riktig tekst
* Enkleste mulige tegnkoding er ASCII
* Unicode sørger for at vi kan bruke æ,ø,å $\Delta$, $\Gamma$ osv. Feks UTF-8 og UTF-16

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

<img src="https://upload.wikimedia.org/wikipedia/commons/1/1b/ASCII-Table-wide.svg">

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

## Unicode
* Unicode er et tegnsett/tegnkoding som har som formål å støtte alle språk
* Alle tegn som brukes må da få sin egen kode
* Til og med [emojis](https://unicode.org/emoji/charts/full-emoji-list.html)
* U+1f911, CLDR Short name: money-mouth-face, 🤑

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

## Vanlige tegnkodinger:
* Unicode har flere måter å gi tegnkodingene på:
  * 'utf-8'
  * 'utf-16'
  * 'utf-32'
* I tillegg har vi en annen standard litt på siden av  unicode: *ISO-8859-1*
  * Kalles ofte "Latin-1"
  * Koder for det latinske alfabetet
  * Vanlig i bruk i Amerika, Vest-Europa, Oceania og store deler av Afrika

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

### SSB

* SSB bruker 'UTF-8' for .XML og JSON formater (mer om JSON senere)
* SSB bruker 'ISO-8859-1' for .csv formatene sine

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}
