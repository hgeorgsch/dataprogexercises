---
tags:
  - lecture/video/perspective
---

<!-- slide template="[[tpl-quote-header]]" -->

# Filbehandling

![[1328101950_Network-Folder.png|480]]

::: credit
Bilete frå VistaICO.com - VistaICO Toolbar Icons, CC BY 3.0,
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=18244879)
:::

note:
Dere er helt sikkert vant til å arbeide med filer.
Dere har Word-filer som dere kan åpne med MS-Word, Excel-filer som dere kan åpne med MS-Excel, og kanskje bilder som dere åpner med et høvelig billedprogram.
Mange filtyper er uløselig knyttet til et bestemt program.
Andre programmer kan ikke lese den samme filen, og det eneste vi vet om innholdet i filen, er det som programmet viser oss.

Det vi skal snakke om her er filer som er lavet for å deles mellom ulike programmer som gjør ulike ting; om filer der vi har selv trenger å se hva filen faktisk inneholder, og hvordan vi kan manipulere innholdet i programkode som vi skriver selv.

---

<!-- slide template="[[tpl-quote-header]]" -->

![[DDR2_ram_mounted.jpg|400]]

| Primærminne | Langtidsminne |
| ----------- | ------------- |
| RAM         | Disk          |
| Variabler   | Filer         |


::: credit
Bilete frå 
[Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=1403981)
under GFDL 1.2, 
:::

note:
Vi skiller gjerne mellom primærminne og sekundærminne i maskinen.

Primærminnet er raskt med plass til mange milliarder tegn.
Sekundærminnet er tregere, men har gjerne plass til hundrede eller tusen
ganger mer data.

Vi har sett hvordan vi kan arbeide med variabler som er lagret i primærminnet,
men denne informasjonen er tapt når strømmen går.
Informasjon som vi skal spare over tid, må lagres i sekundærminnet eller langtidsminnet,
og her er informasjonen organisert i filer, og ikke i variabler.

Hver fil er et objekt som vi stort sett behandler samlet som en enhet.


---

<!-- slide template="[[tpl-twocolumn]]" -->


::: leftimage

**Tekstfiler**

```
Den glade vandrer kalles jeg,
for sorgløs går jeg på,
den endeløse landevei,
der liker jeg å gå.
```
:::

::: leftcredit
:::

::: rightimage

 **... og binærfiler**
```
6544 206e 6c67 6461 2065 6176 646e 6572
2072 616b 6c6c 7365 6a20 6765 0a2c 6f66
2072 6f73 6772 c36c 73b8 6720 a5c3 2072
656a 2067 c370 2ca5 640a 6e65 6520 646e
6c65 b8c3 6573 6c20 6e61 6564 6576 2c69
```
:::

::: rightcredit
:::




note:
Filer kommer som sagt i ulike filtyper:
Word- og Excel-filer, Jupyter notebook-filer, billedfiler som kan være JPEG, PNG, TIFF, GIF, eller andre typer.

Det første skillet vi skal dra er mellom tekst- og binærfiler.
Tekstfiler er de enkleste å arbeide med, fordi de er kodet med vanlige tegn og bokstaver.
Ofte er de kodet slik at vi kan forstå hva de betyr, dersom vi åpner dem i en teksteditor.
Binærfiler er vilkårlige kombinasjoner av 0 og 1. Uten ytterligere informasjon om filformatet, har vi ikke håp om å forstå innholdet.

Foilen viser binærfilen som heksadesimaler, som er vanlig fordi er mer kompakt.  Heksadesimaler bruker 16 sifre: 0-9 og A-F, slik at fire *bits* blir skrevet sammen som ett tegn med verdier fra 0-15, men det er en digresjon. Poenget er at disse symbolene kan bety hva som helst og de er ikke ment for menneskelige lesere.

---

```csv
dato,DKK,GBP
2020-04-01,150.97,12.7385
2020-04-02,150.47,12.8046
2020-04-03,150.8,12.8205
2020-04-06,152.52,12.9698
2020-04-07,148.57,12.5941
2020-04-08,149.97,12.728
2020-04-14,151.59,12.9644
2020-04-15,153.41,13.1033
2020-04-16,152.97,13.0956
2020-04-17,151.26,12.974
2020-04-20,151.1,12.9029
```

note:
CSV-filene som vi skal arbeide mye med, er tekstfiler. De inneholder data som kan være vanskelig eller stundom umulig å forstå uten kontekst, men grunnelementet er bokstaver og tall som gir oss en mulighet.  Søyleoverskriftene forteller oss at vi ser på datoer, danske kroner og britiske pund, og i resten av linjene kan vi ganske riktig kjenne igjen både datoer og desimaltall som kan være valutakurser.

Jeg sier *kan være* for litt kontekst trenger vi for å være sikre, men vi har en god hypotese bare ved å se på filen. Det hadde vi ikke hatt med det samme datasettet i binærformat.

---
	
visa nautilus
- csv
- jpeg
- ipynb
- md
- katalog
- docx

note:
Uansett hva slags maskin du har, kan du sikkert finne en filbehandler.
Denne maskinen kjører Gnome, og filbehandleren heter nautilus.
Her vises *hele* filnavnet, som er nyttig informasjon for oss.
Det kan tenkes at din maskin skjuler den delen av filnavnet markerer filtypen.
I så fall vil jeg anbefale å bla i instillingene og se om du kan skru den funksjonen av, slik at du ser hva vi jobber med.

La oss se på CSV-filen først.  Hvis vi dobbelklikker vil maskinen åpne den i et regneark.
Den spør om noen konfigureringsalternativ, men det skal vi komme tilbake til.  Hvis vi
bare klikker videre så ser det vel ok ut.

---

Teksteditor

note:
Det jeg hadde lyst til å vise er at vi kan åpne samme fil med andre programmer.  Tilbake i filbehandleren kan vi høyreklikke.  Vi ser at førstevalget er å åpne i regnearket, men vi kan også velge *open with* og velge program, f.eks. *Text Editor*.
Fordi CSV er et tekstformat, kan *Text Editor* vise oss nøyaktig hva som står i filen. 
Hvis vi ser på en enkelt linje, ser vi at den er én observasjon av en valutakurs.  Linjen inneholder mange variabler, som her er skilt med semikolon.  Navn på valutaen, danske kroner; valutaen som kursen er oppgitt i, norske kroner, tidspunktet 14:15 CET, datoen og selve kursen, samt en del verdier som sikkert er viktige for dem som driver med valutahandel.

Vi leser denne filen som en tabell, der søylene er skilt med semikolon.
Den første linjen, ser vi, inneholder søyleoverskrifter.
Dette formatet er så enkelt at det er ganske enkelt å lese det inn i våre egne
python-programmer.
Det er også så utbredd at der finnes ferdiglavede funksjoner for å gjøre det.

Likevel er det lett å gjøre feil.  
Søylene er her skilt med semikolon, selv om CSV står for *comma-separated values*.
Som regel er det komma og ikke semikolon som brukes som skilletegn.
I denne filen ser vi derimot at komma brukes som desimaltegn i kursen.
Det er vanlig i de fleste land, men som vi vet bruker engelsktalende land punktum i stedet.

---

Rekneark

note:
Hvis vi går tilbake til regnearket, ser vi at vi gjorde en feil.  Her har vi delt opp kronebeløpet og ørebeløpet i hver sin søyle.  Hvis vi lukker ned og prøver en gang til, ser vi hvorfor.
Fordi ulike skilletegn blir brukt, lar programmet oss velge, og i utgangspunktet leses både semikolon, komma og tabulator som skilletegn, men vi kan ta vekk de som ikke passer.

Når vi åpner filen uten komma som skilletegn, ser vi også at desimalkomma er tolket riktig,
og vises som punktum.

Ulike programmer gjør dette forskjellig.  I Excel kan det være at du ikke får opp konfigurasjonsdialogen når du åpner en CSV-fil fra filbehandleren.  I så fall kan du prøve å starte Excel med en ny og tom fil, og så bruke «åpne» eller «import» i Fil-menyen.

Når vi vet å lese og studere filen i en teksteditor, er det ofte lett å skjønne hva
som er gått galt hvis filen ikke gir mening i andre programmer.  Der er et utall ting
som kan gå galt.  Noen er lette å forstå, andre forstår man med mer erfaring.

---

```
genuttrykk_mus_data.txt
```

note:
Vi skal se på en datafil til. Den heter `.txt` og filbehandleren vil helst åpne den i teksteditoren.
VI ser dog at prinsippet her er det samme som i CSV-filen.  Det er en tabell, med en observasjon per linje, men skilletegnet denne gangen er mellomrom.  Datasettet er genuttrykk for ulike vevstyper i mus.  Dere ser at den siste søylen er bokstaver og ikke en tallverdi.  Det er navnet på det observerte genet.

Vi kan åpne denne filen også i regnearket.  Vi må bare velge mellomrom som skilletegn.

---

note:
Teksteditoren kan også åpne JPEG-filen, men den liker det ikke.
Dette ser helt fælt ut fordi JPEG er et binærformat, 

Vi ser bare nogen få strenger innimellom.  JFIF er navnet på filformatet, som inneholder en del metadata i tillegg til selve bildet som er kodet som JPEG.

Hvis du er usikker på om en fil er binær eller i tekstformat, så er der ingen
fare i åpne den i teksteditoren for å se.  Bare pass på at du ikke lagrer den ...

---

note:
La oss til slutt se på ipynb-filen.
Dette er også en tekst-fil, strukturert i et format som heter JSON og som vi skal møte igjen senere.

Det går an å kjenne igjen strukturen, med en liste av celler, der hver celle har type, metadata, *input* og stundom *output*.

---

::: credit
By YASHAR.Y.A.M.6.T.B - Own work, CC BY-SA 4.0, 
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=148507118)
:::

Identifikasjon av filtype

- Magic bytes
- file extension
- MIME
- Koding i filsystemet

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
<!-- slide template="[[tpl-smalltext]]" -->

| MIME                                                                    | *Extensions*         | Format             |
| :---------------------------------------------------------------------- | -------------------- | :----------------- |
| image/jpeg                                                              | jpeg jpg jpe jfif    | JFIF               |
| text/csv                                                                | csv                  | CSV                |
| text/plain                                                              | txt text pot brf srt | Ren tekst          |
| application/msword                                                      | .doc                 | MS-Word            |
| application/vnd.openxmlformats-officedocument.wordprocessingml.document | docx                 | MS-Word            |
| application/octet-stream                                                | .bin *m.fl.*         | Vilkårlig Binærfil |
::: credit
:::

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
## Teiknkoding

note:
+ Teiknkoding
	+ ASCII  128 teikn inkl. kontrollteikn
	+ Latin 1  $\sim$ 230 teikn, nok til norsk, svensk, samisk og islandsk
	+ Latin 15  €, œ, Œ, mfl. men manglar ¼, ½, fransk og finsk
	+ UTF-8 millionar av teikn, og høve til utviding
	+ Windows-1252

---



* CSV-filer er som sagt vanlig tekst, men:
    - Tekst kan representeres på forkjellige måter i en datamaskin
    - Måten kalles tegnkodingen (character-coding)
    - Vi må ofte sørge for riktig inputkoding (input-encoding) for å få ut riktig tekst
* Enkleste mulige tegnkoding er ASCII
* Unicode sørger for at vi kan bruke æ,ø,å $\Delta$, $\Gamma$ osv. Feks UTF-8 og UTF-16

---

<img src="https://upload.wikimedia.org/wikipedia/commons/1/1b/ASCII-Table-wide.svg">

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

## Unicode
* Unicode er et tegnsett/tegnkoding som har som formål å støtte alle språk
* Alle tegn som brukes må da få sin egen kode
* Til og med [emojis](https://unicode.org/emoji/charts/full-emoji-list.html)
* U+1f911, CLDR Short name: money-mouth-face, 🤑

---

## Vanlige tegnkodinger:
* Unicode har flere måter å gi tegnkodingene på:
  * 'utf-8'
  * 'utf-16'
  * 'utf-32'
* I tillegg har vi en annen standard litt på siden av  unicode: *ISO-8859-1*
  * Kalles ofte "Latin-1"
  * Koder for det latinske alfabetet
  * Vanlig i bruk i Amerika, Vest-Europa, Oceania og store deler av Afrika

---

### SSB

* SSB bruker 'UTF-8' for .XML og JSON formater (mer om JSON senere)
* SSB bruker 'ISO-8859-1' for .csv formatene sine


---

+ Lineskiftkonvensjonar
