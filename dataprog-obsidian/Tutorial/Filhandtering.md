---
tags:
  - lecture/video/perspective
---
# Filhandtering

note:
Dere er helt sikkert vant til å arbeide med filer.
Dere har Word-filer som dere kan åpne med MS-Word, Excel-filer som dere kan åpne med MS-Excel, og kanskje bilder som dere åpner med et høvelig billedprogram.
Mange filtyper er uløselig knyttet til et bestemt program.
Andre programmer kan ikke lese den samme filen, og det eneste vi vet om innholdet i filen, er det som programmet viser oss.

Det vi skal snakke om her er filer som er lavet for å deles mellom ulike programmer som gjør ulike ting; om filer der vi har selv trenger å se hva filen faktisk inneholder, og hvordan vi kan manipulere innholdet i programkode som vi skriver selv.

---

| Primærminne | Langtidsminne |
| ----------- | ------------- |
| RAM         | Disk          |
| Variabler   | Filer         |

note:
Vi skiller gjerne mellom primærminne og sekundærminne i maskinen.
Vi har sett hvordan vi kan arbeide med variabler som er lagret i primærminnet, men denne informasjonen er tapt når strømmen går.
Informasjon som vi skal spare over tid, må lagres i sekundærminnet eller langtidsminnet, og her er informasjonen organisert i filer, og ikke i variabler.

Hver fil er et objekt som vi stort sett behandler samlet som en enhet.

---

+ Binær- og tekstfiler

note:
Filer kommer som sagt i ulike filtyper:
Word- og Excel-filer, Jupyter notebook-filer, billedfiler som kan være JPEG, PNG, TIFF, GIF, eller andre typer.

Det første skillet vi skal dra er mellom tekst- og binærfiler.
Tekstfiler er de enkleste å arbeide med, fordi de er kodet med vanlige tegn og bokstaver.
Ofte er de kodet slik at vi kan forstå hva de betyr, dersom vi åpner dem i en teksteditor.
Binærfiler er vilkårlige kombinasjoner av 0 og 1. Uten ytterligere informasjon om filformatet, har vi ikke håp om å forstå innholdet.

---
	
visa nautilus
+ csv
+ jpeg
+ ipynb
+ md
+ katalog
+ docx

---

Identifikasjon av filtype

+ Magic bytes
+ file extension
+ MIME
+ Koding i filsystemet

note:
Maskinen vil ofte prøve å identifisere filtypen og åpne den i et egnet program.
Av og til er det meget brukervennlig.
Andre ganger tar maskinen feil av formatet, og skaper masse problemer for oss.

Det skjer ofte når vi arbeider med et relativt sjeldne format, og vi ikke har installert et program som kjenner det.
Det kan òg skje fordi ulike systemer kategoriserer filtypene forskjellig.

Der er minst fire forskjellige måter å identifisere filtypen på.

---

.docx   .doc  .jpg .jpeg

note:
Den mest kjente måten å vise filtypen er gjennom filnavnet, dvs. den delen som kommer efter siste punktum, gjerne kalt *file extension*.
Efter gammelt utviklet det seg som en konvensjon, for å gjøre det enklere for brukeren å se hvilket program som kunne åpne en gitt fil.
Efter hvert har noen programmer og operativsystemer forsøkt å standardisere dette, med programmer som automatisk åpner filer i riktig program, basert på filnavnet.

Det er likevel slik at dette fremdeles er en konvensjon og ikke en universell begrensning.
Der er mange programmer som lar brukeren kalle filene akkurat det de vil, og der finnes eksempler på *file extensions* som brukes på ulike typer av forskjellige programmer. 
Dessuten er det slik at en fil først og fremst får et navn når den lagres på lokal disk.
En fil som overføres over epost eller på andre måter, trenger ikke å ha et navn i det hele tatt.

---

| MIME | *Extensions* | Format |
| :--- | ----------- | :- |
| image/jpeg | jpeg jpg jpe jfif | JFIF |
| application/msword | .doc | MS-Word |
| application/vnd.openxmlformats-officedocument.wordprocessingml.document | docx | MS-Word |
| application/octet-stream | .bin *m.fl.* | Vilkårleg Binørfil |

note:
Standarden for å definere filtype når filer overføres over nettet, f.eks. på epost eller en vevside, heter MIME.

MIME er mer detaljert og kan hende bedre standardisert enn *file extensions*,
men der er mye feil og misbruk.
Bl.a. blir `application/octet-stream` ofte brukt, i stedet for en mer informativ type.
Et anna problem er at det er programmet som sender filen, som bestemmer hvilken MIME-type
den skal ha, og det må altså gjette på filtypen.

---

note: 
*Magic bytes* er de to første *bytes* eller tegn i filen.
De fleste binærformater bruker en bestemt verdi i disse tegnene, for
å identisere seg selv.
Dette er den sikreste måten å identifisere en binær filtype, fordi 
*magic bytes* blir en uadskillelig del av selve filen, selv om den skulle
bytte navn.
Likevel er ikke det den vanligste måten å identifisere filtyper i dag.

Der finnes også andre metoder.
F.eks. brukte gamle versjoner av MacOS å registrere hvilket program som hadde
opprettet hver fil i filsystemet, slik at maskinen kunne være helt sikkert på
å bruke samme program neste gang brukeren åpner filen.
Fordelen er at man unngår mange menneskelige feil, ved å ta typeidentifikasjonen
ut av brukerens kontroll.
Ulempen er at brukeren mister kontroll, og det blir vanskeligere å behandle
samme fil på flere ulike måter.

---

note:


+ Filtransformasjonar og orden
	+ kjeldefiler
	+ programkode
	+ genererte filer
+ Filformat
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
