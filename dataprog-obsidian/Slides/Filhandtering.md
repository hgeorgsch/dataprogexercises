---
tags:
  - lecture/video/perspective
css:
  - css/templates.css
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
Andre programmer kan ikke lese den samme filen, og det eneste vi vet om innholdet i filen, er det som programmet vil vise oss.

Det vi skal snakke om her er filer som er lavet for å deles mellom ulike programmer som gjør ulike ting; om filer der vi har selv trenger å se hva filen faktisk inneholder, og hvordan vi kan manipulere innholdet i programkode som vi skriver selv.

---

<!-- slide template="[[tpl-quote-header]]" -->


| Primærminne | Langtidsminne |
| ----------- | ------------- |
| RAM         | Disk          |
| Variabler   | Filer         |

![[DDR2_ram_mounted.jpg|400]]

::: credit
Bilete frå 
[Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=1403981)
under GFDL 1.2, 
:::

note:
Vi skiller gjerne mellom primærminne og sekundærminne i maskinen.

Vi har sett hvordan vi kan arbeide med variabler som er lagret i primærminnet,
men denne informasjonen er tapt når strømmen går.
Informasjon som vi skal spare over tid, må lagres i sekundærminnet eller langtidsminnet,
og her er informasjonen organisert i filer, og ikke i variabler.

Hver fil er et objekt som vi stort sett behandler samlet som en enhet.

---



**Tekstfiler**

```txt
Den glade vandrer kalles jeg,
for sorgløs går jeg på,
den endeløse landevei,
der liker jeg å gå.
```
 **... og binærfiler**
```txt
6544 206e 6c67 6461 2065 6176 646e 6572
2072 616b 6c6c 7365 6a20 6765 0a2c 6f66
2072 6f73 6772 c36c 73b8 6720 a5c3 2072
656a 2067 c370 2ca5 640a 6e65 6520 646e
6c65 b8c3 6573 6c20 6e61 6564 6576 2c69
```

note:
Filer kommer som sagt i ulike filtyper:
Word- og Excel-filer, Jupyter notebook-filer, billedfiler som kan være JPEG, PNG, TIFF, GIF, eller andre typer.

Det første skillet vi skal dra er mellom tekst- og binærfiler.
Tekstfiler er de enkleste å arbeide med, fordi de er kodet med vanlige tegn og bokstaver.
Ofte er de kodet slik at vi kan forstå hva de betyr, dersom vi åpner dem i en teksteditor.
Binærfiler er vilkårlige kombinasjoner av 0 og 1. Uten ytterligere informasjon om filformatet, har vi ikke håp om å forstå innholdet.

Foilen viser binærfilen som heksadesimaler, som er vanlig fordi det er mer kompakt.  Heksadesimaler bruker 16 sifre: 0-9 og A-F, slik at fire *bits* blir skrevet sammen som ett tegn med verdier fra 0-15, men det er en digresjon. Poenget er at disse symbolene kan bety hva som helst og de er ikke ment for menneskelige lesere.

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
CSV-filene som vi skal arbeide mye med, er tekstfiler. De inneholder data som kan være vanskelig eller stundom umulig å forstå uten kontekst, men grunnelementet er bokstaver og tall som gir oss en mulighet til å se og forstå hva som foregår under panseret.  

I eksempelet på skjermen ser vi søyleoverskrifter som forteller oss at vi ser på datoer, danske kroner og britiske pund, og i resten av linjene kan vi ganske riktig kjenne igjen både datoer og desimaltall som kan være valutakurser.

Jeg sier *kan være*, for litt kontekst trenger vi for å være sikre, men vi har en god hypotese bare ved å se på filen. Det hadde vi ikke hatt med det samme datasettet i binærformat.

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
Her vises *hele* filnavnet, som er nyttig informasjon for oss.  Slutten av filnavnet, som .txt eller .jpeg gir en pekepinn på hva slags fil det er.

Det kan tenkes at din maskin skjuler den delen av filnavnet markerer filtypen.
I så fall vil jeg anbefale å bla i instillingene og se om du kan skru den funksjonen av, slik at du også ser hele filnavnet.

La oss se på CSV-filen først.  Når jeg dobbelklikker, åpner maskinen filen i et regneark.
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
som er gått galt når filen ikke gir mening i andre programmer.  Der er et utall ting
som kan gå galt.  Noen er lette å forstå, andre forstår man med mer erfaring.

---

```
genuttrykk_mus_data.txt
```

note:
Vi skal se på en datafil til. Den har navn på `.txt` og filbehandleren vil helst åpne den i teksteditoren.
Vi ser dog at prinsippet her er det samme som i CSV-filen.  Det er en tabell, med en observasjon per linje, men skilletegnet denne gangen er mellomrom.  Datasettet er genuttrykk for ulike vevstyper i mus.  Dere ser at den siste søylen er bokstaver og ikke en tallverdi.  Det er navnet på det observerte genet.

Vi kan åpne denne filen også i regnearket.  Vi må bare velge mellomrom som skilletegn.

Vi velger *open with* og ser på forhåndsvisningen nederst.  Når vi endrer skilletegn, ser vi at søylene skilles riktig.

---

JPEG i teksteditor

note:
Teksteditoren kan også åpne JPEG-filen, men den liker det ikke.
Dette ser helt fælt ut fordi JPEG er et binærformat, 

Vi ser bare nogen få strenger innimellom.  JFIF er navnet på filformatet, som inneholder en del metadata i tillegg til selve bildet som er kodet som JPEG.

Hvis du er usikker på om en fil er binær eller i tekstformat, så er der ingen
fare i åpne den i teksteditoren for å se.  Bare pass på at du ikke lagrer og overskriver den ...

---

Jupyter notebook-fil i teksteditor

note:
La oss til slutt se på ipynb-filen.
Dette er også en tekst-fil, strukturert i et format som heter JSON og som vi skal møte igjen senere.

Det går an å kjenne igjen strukturen, med en liste av celler, der hver celle har type, metadata, *input* og stundom *output*.

---

<!-- slide template="[[tpl-twocolumn]]" -->

::: leftimage
![[File-extensions-list.png]]
:::

::: leftcredit
By YASHAR.Y.A.M.6.T.B - Own work, CC BY-SA 4.0, 
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=148507118)
:::

::: rightimage

Identifikasjon av filtype

- Magic bytes
- file extension (etternavn)
- MIME
- Metadata i filsystemet
:::

::: rightcredit
:::

note:
Maskinen vil ofte prøve selv å identifisere filtypen og åpne den i et egnet program.
Av og til er det meget brukervennlig.
Andre ganger tar maskinen feil av formatet, og skaper masse problemer for oss.

Det skjer ofte når vi arbeider med et relativt sjeldne format, og vi ikke har installert et program som kjenner det.
Det kan òg skje fordi ulike systemer kategoriserer filtypene forskjellig.

Der er minst fire forskjellige måter å identifisere filtypen på.

Den mest kjente måten å vise filtypen er gjennom filnavnet, dvs. den delen som kommer efter siste punktum, gjerne kalt *file extension*.
Efter gammelt utviklet det seg som en konvensjon, for å gjøre det enklere for brukeren å se hvilket program som kunne åpne en gitt fil.
Efter hvert har noen programmer og operativsystemer forsøkt å standardisere dette, med programmer som automatisk åpner filer i riktig program, basert på filnavnet.

Det er likevel slik at dette fremdeles er en konvensjon og ikke en universell begrensning.
Der er mange programmer som lar brukeren kalle filene akkurat det de vil, og der finnes eksempler på *file extensions* som brukes på ulike filtyper av forskjellige programmer. 
Dessuten er det slik at en fil først og fremst får et navn når den lagres på lokal disk.
En fil som overføres over epost eller på andre måter, trenger ikke å ha et navn i det hele tatt.

---
<!-- slide template="[[tpl-smalltext]]" -->

| MIME                                                                    | *Extensions*              | Format             |
| :---------------------------------------------------------------------- | ------------------------- | :----------------- |
| image/jpeg                                                              | .jpeg .jpg .jpe .jfif     | JFIF               |
| text/csv                                                                | .csv                      | CSV                |
| text/plain                                                              | .txt .text .pot .brf .srt | Ren tekst          |
| application/msword                                                      | .doc                      | MS-Word            |
| application/vnd.openxmlformats-officedocument.wordprocessingml.document | .docx                     | MS-Word            |
| application/octet-stream                                                | .bin *m.fl.*              | Vilkårlig Binærfil |
::: credit
:::

note:
Standarden for å definere filtype når filer overføres over nettet, f.eks. på epost eller en vevside, heter MIME.

MIME er mer detaljert og kan hende bedre standardisert enn *file extensions*,
men der er mye feil og misbruk.
Bl.a. blir `application/octet-stream` ofte brukt, selv om det ikke sier andet enn at det er en binærfil.  I de fleste tilfeller finnes der en mer presis filtype.

Et andet problem er at det er maskinen som sender filen, som bestemmer hvilken MIME-type
den skal ha, og det må altså gjette på filtypen.  Ikke så sjelden gjetter den feil.

Dessuten er det lite hjelp i korrekt filtype dersom din maskin, som mottar filen, ikke kjenner formatet.  Hvis din maskin er i overkant hjelpsom, kan mye gå galt når den prøver å få filen til å passe i et kjent format som likevel ikke passer.
Det er derfor jeg synes det er viktig at dere blir komfortable både med å åpne ukjente filer for selv å se hva det er for noe, med å endre filnavn og filtype selv, og med å velge hvilket program dere ønsker å åpne filen i.  Det er ikke alle formater vi kommer til å finne ut av, men med erfaring klarer vi flere og flere.

---

```
ÿØÿà^@^PJFIF^@^A^A^A^@H^@H^@^@ÿá èExif^@^@MM^@*^@^@^@^H^@^G^A^R^@^C^@^@^@^A^@^A^@^@^A^Z
^@^E^@^@^@^A^@^@^@b^A^[^@^E^@^@^@^A^@^@^@j^A(^@^C^@^@^@^A^@^B^@^@^
A1^@^B^@^@^@^K^@^@^@r^A2^@^B^@^@^@^T^@^@^@~<87>i^@^D^@^@^@^A^@^@^@<92>^@^@^@¼^@^@^@H^@^@^@^A^@^@^@H^@^@^@^AGIMP 2.6.6^@^@2009:08:07 09:53:10^@^@^C ^A^@^C^@^@^@^Aÿÿ^@^@ ^B^@^D^@^@^@^A^@^@^Aô 
^C^@^D^@^@^@^A^@^@^BÛ^@^@^@^@^@^F^A^C^@^C^@^@^@^A^@^F^@^@^A^Z^@^E^@^@^@^A^@^@^A
```


+ `ÿØÿ`  = `FF D8 FF` = (255, 232, 255)  $\sim$  JFIF/JPEG

note: 
*Magic bytes* eller *magic numbers* er de par første *bytes* eller tegn i filen.
De fleste binærformater bruker en bestemt verdi i disse tegnene, for
å identisere seg selv.
Dette er den sikreste måten å identifisere en binær filtype, fordi 
*magic bytes* blir en uadskillelig del av selve filen, selv om den skulle
bytte navn.
Likevel er ikke det den vanligste måten å identifisere filtyper i dag.

Foilen viser toppen av en JPEG-fil slik den ser ut i en teksteditor.
De første tre tegnene er tre *magic bytes*.  Vi ser dem som y med trema
og stor Ø. *Byte*-verdiene, eller tallverdiene, er 255, 232 og 255,
eller, i heksadesimal, slik de vanligvis blir vist, FF-D8-FF.

Der finnes også andre metoder.
F.eks. brukte gamle versjoner av MacOS å registrere hvilket program som hadde
opprettet hver fil i filsystemet, slik at maskinen kunne være helt sikkert på
å bruke samme program neste gang brukeren åpner samme fil.

Fordelen er at man unngår mange menneskelige feil, ved å ta typeidentifikasjonen
ut av brukerens kontroll.

Ulempen er at brukeren mister kontroll, og det blir vanskeligere å behandle
samme fil på flere ulike måter.

---

<!-- slide template="[[tpl-smalltext]]" -->

<table class="wikitable nounderlines nowrap" border="1" style="border-collapse:collapse;text-align:center">
<caption style="font-size:140%;line-height:1.5">ASCII (1977/1986)</caption>
<tbody><tr>
<td>
</td>
<td style="width:20pt">0</td>
<td style="width:20pt">1</td>
<td style="width:20pt">2</td>
<td style="width:20pt">3</td>
<td style="width:20pt">4</td>
<td style="width:20pt">5</td>
<td style="width:20pt">6</td>
<td style="width:20pt">7</td>
<td style="width:20pt">8</td>
<td style="width:20pt">9</td>
<td style="width:20pt">A</td>
<td style="width:20pt">B</td>
<td style="width:20pt">C</td>
<td style="width:20pt">D</td>
<td style="width:20pt">E</td>
<td style="width:20pt">F</td></tr>
<tr>
<td style="height:2em;height:22pt;line-height:1">0x</td>
<td title="0 U+0000: Control (alias NULL) (alias NUL)" style="padding:1px;"><span style="display:inline-block; border:1px dashed blue;"> <a href="/wiki/Null_character" title="Null character">NUL</a> </span>
</td>
<td title="1 U+0001: Control (alias START OF HEADING) (alias SOH)" style="padding:1px"><span style="display:inline-block; border:1px dashed blue;"> <a href="/wiki/Start_of_heading" class="mw-redirect" title="Start of heading">SOH</a> </span>
</td>
<td title="2 U+0002: Control (alias START OF TEXT) (alias STX)" style="padding:1px;"><span style="display:inline-block; border:1px dashed blue;"> <a href="/wiki/Start_of_text" class="mw-redirect" title="Start of text">STX</a> </span>
</td>
<td title="3 U+0003: Control (alias END OF TEXT) (alias ETX)" style="padding:1px;"><span style="display:inline-block; border:1px dashed blue;"> <a href="/wiki/End-of-Text_character" title="End-of-Text character">ETX</a> </span>
</td>
<td title="4 U+0004: Control (alias END OF TRANSMISSION) (alias EOT)" style="padding:1px;"><span style="display:inline-block; border:1px dashed blue;"> <a href="/wiki/End-of-Transmission_character" title="End-of-Transmission character">EOT</a> </span>
</td>
<td title="5 U+0005: Control (alias ENQUIRY) (alias ENQ)" style="padding:1px"><span style="display:inline-block; border:1px dashed blue;"> <a href="/wiki/Enquiry_character" title="Enquiry character">ENQ</a> </span>
</td>
<td title="6 U+0006: Control (alias ACKNOWLEDGE) (alias ACK)" style="padding:1px"><span style="display:inline-block; border:1px dashed blue;"> <a href="/wiki/Acknowledge_character" class="mw-redirect" title="Acknowledge character">ACK</a> </span>
</td>
<td title="7 U+0007: Control (alias ALERT) (alias BEL)" style="padding:1px;"><span style="display:inline-block; border:1px dashed blue;"> <a href="/wiki/Bell_character" title="Bell character">BEL</a> </span>
</td>
<td title="8 U+0008: Control (alias BACKSPACE) (alias BS)" style="padding:1px"><span style="display:inline-block; border:1px dashed blue;"> <a href="/wiki/Backspace" title="Backspace">&#160;BS&#160;</a> </span>
</td>
<td title="9 U+0009: Control (alias CHARACTER TABULATION) (alias HORIZONTAL TABULATION) (alias HT) (alias TAB)" style="padding:1px;"><span style="display:inline-block; border:1px dashed blue;"> <a href="/wiki/Horizontal_tabulation" class="mw-redirect" title="Horizontal tabulation">&#160;HT&#160;</a> </span>
</td>
<td title="10 U+000A: Control (alias LINE FEED) (alias NEW LINE) (alias END OF LINE) (alias LF) (alias NL) (alias EOL)" style="padding:1px;"><span style="display:inline-block; border:1px dashed blue;"> <a href="/wiki/Line_feed" class="mw-redirect" title="Line feed">&#160;LF&#160;</a> </span>
</td>
<td title="11 U+000B: Control (alias LINE TABULATION) (alias VERTICAL TABULATION) (alias VT)" style="padding:1px;"><span style="display:inline-block; border:1px dashed blue;"> <a href="/wiki/Vertical_tabulation" class="mw-redirect" title="Vertical tabulation">&#160;VT&#160;</a> </span>
</td>
<td title="12 U+000C: Control (alias FORM FEED) (alias FF)" style="padding:1px;"><span style="display:inline-block; border:1px dashed blue;"> <a href="/wiki/Form_feed" class="mw-redirect" title="Form feed">&#160;FF&#160;</a> </span>
</td>
<td title="13 U+000D: Control (alias CARRIAGE RETURN) (alias CR)" style="padding:1px;"><span style="display:inline-block; border:1px dashed blue;"> <a href="/wiki/Carriage_return" title="Carriage return">&#160;CR&#160;</a> </span>
</td>
<td title="14 U+000E: Control (alias SHIFT OUT) (alias LOCKING-SHIFT ONE) (alias SO)" style="padding:1px;"><span style="display:inline-block; border:1px dashed blue;"> <a href="/wiki/Shift_out" class="mw-redirect" title="Shift out">&#160;SO&#160;</a> </span>
</td>
<td title="15 U+000F: Control (alias SHIFT IN) (alias LOCKING-SHIFT ZERO) (alias SI)" style="padding:1px;"><span style="display:inline-block; border:1px dashed blue;"> <a href="/wiki/Shift_in" class="mw-redirect" title="Shift in">&#160;SI&#160;</a> </span>
</td></tr>
<tr>
<td style="height:2em;height:22pt;line-height:1">1x
</td>
<td title="16 U+0010: Control (alias DATA LINK ESCAPE) (alias DLE)" style="padding:1px"><span style="display:inline-block; border:1px dashed blue;"> <a href="/wiki/Data_link_escape" class="mw-redirect" title="Data link escape">DLE</a> </span>
</td>
<td title="17 U+0011: Control (alias DEVICE CONTROL ONE) (alias DC1)" style="padding:1px;"><span style="display:inline-block; border:1px dashed blue;"> <a href="/wiki/Device_Control_1" class="mw-redirect" title="Device Control 1">DC1</a> </span>
</td>
<td title="18 U+0012: Control (alias DEVICE CONTROL TWO) (alias DC2)" style="padding:1px;"><span style="display:inline-block; border:1px dashed blue;"> <a href="/wiki/Device_Control_2" class="mw-redirect" title="Device Control 2">DC2</a> </span>
</td>
<td title="19 U+0013: Control (alias DEVICE CONTROL THREE) (alias DC3)" style="padding:1px;"><span style="display:inline-block; border:1px dashed blue;"> <a href="/wiki/Device_Control_3" class="mw-redirect" title="Device Control 3">DC3</a> </span>
</td>
<td title="20 U+0014: Control (alias DEVICE CONTROL FOUR) (alias DC4)" style="padding:1px;"><span style="display:inline-block; border:1px dashed blue;"> <a href="/wiki/Device_Control_4" class="mw-redirect" title="Device Control 4">DC4</a> </span>
</td>
<td title="21 U+0015: Control (alias NEGATIVE ACKNOWLEDGE) (alias NAK)" style="padding:1px"><span style="display:inline-block; border:1px dashed blue;"> <a href="/wiki/Negative_acknowledge_character" class="mw-redirect" title="Negative acknowledge character">NAK</a> </span>
</td>
<td title="22 U+0016: Control (alias SYNCHRONOUS IDLE) (alias SYN)" style="padding:1px;"><span style="display:inline-block; border:1px dashed blue;"> <a href="/wiki/Synchronous_idle" class="mw-redirect" title="Synchronous idle">SYN</a> </span>
</td>
<td title="23 U+0017: Control (alias END OF TRANSMISSION BLOCK) (alias ETB)" style="padding:1px"><span style="display:inline-block; border:1px dashed blue;"> <a href="/wiki/End_of_transmission_block" class="mw-redirect" title="End of transmission block">ETB</a> </span>
</td>
<td title="24 U+0018: Control (alias CANCEL) (alias CAN)" style="padding:1px"><span style="display:inline-block; border:1px dashed blue;"> <a href="/wiki/Cancel_character" title="Cancel character">CAN</a> </span>
</td>
<td title="25 U+0019: Control (alias END OF MEDIUM) (alias EOM)" style="padding:1px"><span style="display:inline-block; border:1px dashed blue;"> <a href="/wiki/End_of_medium" class="mw-redirect" title="End of medium">&#160;EM&#160;</a> </span>
</td>
<td title="26 U+001A: Control (alias SUBSTITUTE) (alias SUB)" style="padding:1px"><span style="display:inline-block; border:1px dashed blue;"> <a href="/wiki/Substitute_character" title="Substitute character">SUB</a> </span>
</td>
<td title="27 U+001B: Control (alias ESCAPE) (alias ESC)" style="padding:1px"><span style="display:inline-block; border:1px dashed blue;"> <a href="/wiki/Escape_character#ASCII_escape_character" title="Escape character">ESC</a> </span>
</td>
<td title="28 U+001C: Control (alias INFORMATION SEPARATOR FOUR) (alias FILE SEPARATOR) (alias FS)" style="padding:1px"><span style="display:inline-block; border:1px dashed blue;"> <a href="/wiki/File_separator" class="mw-redirect" title="File separator">&#160;FS&#160;</a> </span>
</td>
<td title="29 U+001D: Control (alias INFORMATION SEPARATOR THREE) (alias GROUP SEPARATOR) (alias GS)" style="padding:1px"><span style="display:inline-block; border:1px dashed blue;"> <a href="/wiki/Group_separator" class="mw-redirect" title="Group separator">&#160;GS&#160;</a> </span>
</td>
<td title="30 U+001E: Control (alias INFORMATION SEPARATOR TWO) (alias RECORD SEPARATOR) (alias RS)" style="padding:1px"><span style="display:inline-block; border:1px dashed blue;"> <a href="/wiki/Record_separator" class="mw-redirect" title="Record separator">&#160;RS&#160;</a> </span>
</td>
<td title="31 U+001F: Control (alias INFORMATION SEPARATOR ONE) (alias UNIT SEPARATOR) (alias US)" style="padding:1px"><span style="display:inline-block; border:1px dashed blue;"> <a href="/wiki/Unit_separator" class="mw-redirect" title="Unit separator">&#160;US&#160;</a> </span>
</td></tr>
<tr>
<td style="height:2em;height:22pt;line-height:1">Ax
</td>
<td title="32 U+0020: SPACE (alias SP)" style="padding:1px;"><span style="display:inline-block; border:1px dashed blue;"> <a href="/wiki/Space_character" class="mw-redirect" title="Space character">&#160;SP&#160;</a> </span>
</td>
<td title="33 U+0021: EXCLAMATION MARK" style="padding:1px;"><a href="/wiki/!" class="mw-redirect" title="!">!</a>
</td>
<td title="34 U+0022: QUOTATION MARK" style="padding:1px;"><a href="/wiki/%22" class="mw-redirect" title="&quot;">"</a>
</td>
<td title="35 U+0023: NUMBER SIGN" style="padding:1px;"><a href="/wiki/Number_sign" title="Number sign">#</a>
</td>
<td title="36 U+0024: DOLLAR SIGN" style="padding:1px;"><a href="/wiki/$" class="mw-redirect" title="$">$</a>
</td>
<td title="37 U+0025: PERCENT SIGN" style="padding:1px;"><a href="/wiki/%25" class="mw-redirect" title="%">%</a>
</td>
<td title="38 U+0026: AMPERSAND" style="padding:1px;"><a href="/wiki/%26" class="mw-redirect" title="&amp;">&amp;</a>
</td>
<td title="39 U+0027: APOSTROPHE" style="padding:1px;"><a href="/wiki/%27" class="mw-redirect" title="&#39;">'</a>
</td>
<td title="40 U+0028: LEFT PARENTHESIS" style="padding:1px;"><a href="/wiki/(" class="mw-redirect" title="(">(</a>
</td>
<td title="41 U+0029: RIGHT PARENTHESIS" style="padding:1px;"><a href="/wiki/)" class="mw-redirect" title=")">)</a>
</td>
<td title="42 U+002A: ASTERISK" style="padding:1px;"><a href="/wiki/*" class="mw-redirect" title="*">*</a>
</td>
<td title="43 U+002B: PLUS SIGN" style="padding:1px;"><a href="/wiki/%2B" class="mw-redirect" title="+">+</a>
</td>
<td title="44 U+002C: COMMA" style="padding:1px;"><a href="/wiki/," class="mw-redirect" title=",">,</a>
</td>
<td title="45 U+002D: HYPHEN-MINUS" style="padding:1px;"><a href="/wiki/-" class="mw-redirect" title="-">-</a>
</td>
<td title="46 U+002E: FULL STOP" style="padding:1px;"><a href="/wiki/Full_stop" title="Full stop">.</a>
</td>
<td title="47 U+002F: SOLIDUS" style="padding:1px;"><a href="/wiki/Slash_(punctuation)" title="Slash (punctuation)">/</a>
</td></tr>
<tr>
<td style="height:2em;height:22pt;line-height:1">3x
</td>
<td title="48 U+0030: DIGIT ZERO" style="padding:1px;"><a href="/wiki/0" title="0">0</a>
</td>
<td title="49 U+0031: DIGIT ONE" style="padding:1px;"><a href="/wiki/1" title="1">1</a>
</td>
<td title="50 U+0032: DIGIT TWO" style="padding:1px;"><a href="/wiki/2" title="2">2</a>
</td>
<td title="51 U+0033: DIGIT THREE" style="padding:1px;"><a href="/wiki/3" title="3">3</a>
</td>
<td title="52 U+0034: DIGIT FOUR" style="padding:1px;"><a href="/wiki/4" title="4">4</a>
</td>
<td title="53 U+0035: DIGIT FIVE" style="padding:1px;"><a href="/wiki/5" title="5">5</a>
</td>
<td title="54 U+0036: DIGIT SIX" style="padding:1px;"><a href="/wiki/6" title="6">6</a>
</td>
<td title="55 U+0037: DIGIT SEVEN" style="padding:1px;"><a href="/wiki/7" title="7">7</a>
</td>
<td title="56 U+0038: DIGIT EIGHT" style="padding:1px;"><a href="/wiki/8" title="8">8</a>
</td>
<td title="57 U+0039: DIGIT NINE" style="padding:1px;"><a href="/wiki/9" title="9">9</a>
</td>
<td title="58 U+003A: COLON" style="padding:1px;"><a href="/wiki/Colon_(punctuation)" title="Colon (punctuation)">:</a>
</td>
<td title="59 U+003B: SEMICOLON" style="padding:1px;"><a href="/wiki/Semicolon" title="Semicolon">;</a>
</td>
<td title="60 U+003C: LESS-THAN SIGN" style="padding:1px;"><a href="/wiki/Less-than_sign" title="Less-than sign">&lt;</a>
</td>
<td title="61 U+003D: EQUALS SIGN" style="padding:1px;"><a href="/wiki/%3D" class="mw-redirect" title="=">=</a>
</td>
<td title="62 U+003E: GREATER-THAN SIGN" style="padding:1px;"><a href="/wiki/Greater-than_sign" title="Greater-than sign">&gt;</a>
</td>
<td title="63 U+003F: QUESTION MARK" style="padding:1px;"><a href="/wiki/%3F" class="mw-redirect" title="?">?</a>
</td></tr>
<tr>
<td style="height:2em;height:22pt;line-height:1">4x
</td>
<td title="64 U+0040: COMMERCIAL AT" style="padding:1px"><a href="/wiki/@" class="mw-redirect" title="@">@</a>
</td>
<td title="65 U+0041: LATIN CAPITAL LETTER A" style="padding:1px;"><a href="/wiki/A" title="A">A</a>
</td>
<td title="66 U+0042: LATIN CAPITAL LETTER B" style="padding:1px;"><a href="/wiki/B" title="B">B</a>
</td>
<td title="67 U+0043: LATIN CAPITAL LETTER C" style="padding:1px;"><a href="/wiki/C" title="C">C</a>
</td>
<td title="68 U+0044: LATIN CAPITAL LETTER D" style="padding:1px;"><a href="/wiki/D" title="D">D</a>
</td>
<td title="69 U+0045: LATIN CAPITAL LETTER E" style="padding:1px;"><a href="/wiki/E" title="E">E</a>
</td>
<td title="70 U+0046: LATIN CAPITAL LETTER F" style="padding:1px;"><a href="/wiki/F" title="F">F</a>
</td>
<td title="71 U+0047: LATIN CAPITAL LETTER G" style="padding:1px;"><a href="/wiki/G" title="G">G</a>
</td>
<td title="72 U+0048: LATIN CAPITAL LETTER H" style="padding:1px;"><a href="/wiki/H" title="H">H</a>
</td>
<td title="73 U+0049: LATIN CAPITAL LETTER I" style="padding:1px;"><a href="/wiki/I" title="I">I</a>
</td>
<td title="74 U+004A: LATIN CAPITAL LETTER J" style="padding:1px;"><a href="/wiki/J" title="J">J</a>
</td>
<td title="75 U+004B: LATIN CAPITAL LETTER K" style="padding:1px;"><a href="/wiki/K" title="K">K</a>
</td>
<td title="76 U+004C: LATIN CAPITAL LETTER L" style="padding:1px;"><a href="/wiki/L" title="L">L</a>
</td>
<td title="77 U+004D: LATIN CAPITAL LETTER M" style="padding:1px;"><a href="/wiki/M" title="M">M</a>
</td>
<td title="78 U+004E: LATIN CAPITAL LETTER N" style="padding:1px;"><a href="/wiki/N" title="N">N</a>
</td>
<td title="79 U+004F: LATIN CAPITAL LETTER O" style="padding:1px;"><a href="/wiki/O" title="O">O</a>
</td></tr>
<tr>
<td style="height:2em;height:22pt;line-height:1">5x
</td>
<td title="80 U+0050: LATIN CAPITAL LETTER P" style="padding:1px;"><a href="/wiki/P" title="P">P</a>
</td>
<td title="81 U+0051: LATIN CAPITAL LETTER Q" style="padding:1px;"><a href="/wiki/Q" title="Q">Q</a>
</td>
<td title="82 U+0052: LATIN CAPITAL LETTER R" style="padding:1px;"><a href="/wiki/R" title="R">R</a>
</td>
<td title="83 U+0053: LATIN CAPITAL LETTER S" style="padding:1px;"><a href="/wiki/S" title="S">S</a>
</td>
<td title="84 U+0054: LATIN CAPITAL LETTER T" style="padding:1px;"><a href="/wiki/T" title="T">T</a>
</td>
<td title="85 U+0055: LATIN CAPITAL LETTER U" style="padding:1px;"><a href="/wiki/U" title="U">U</a>
</td>
<td title="86 U+0056: LATIN CAPITAL LETTER V" style="padding:1px;"><a href="/wiki/V" title="V">V</a>
</td>
<td title="87 U+0057: LATIN CAPITAL LETTER W" style="padding:1px;"><a href="/wiki/W" title="W">W</a>
</td>
<td title="88 U+0058: LATIN CAPITAL LETTER X" style="padding:1px;"><a href="/wiki/X" title="X">X</a>
</td>
<td title="89 U+0059: LATIN CAPITAL LETTER Y" style="padding:1px;"><a href="/wiki/Y" title="Y">Y</a>
</td>
<td title="90 U+005A: LATIN CAPITAL LETTER Z" style="padding:1px;"><a href="/wiki/Z" title="Z">Z</a>
</td>
<td title="91 U+005B: LEFT SQUARE BRACKET" style="padding:1px;"><a href="/wiki/Left_square_bracket" class="mw-redirect" title="Left square bracket">&#91;</a>
</td>
<td title="92 U+005C: REVERSE SOLIDUS" style="padding:1px"><a href="/wiki/Backslash" title="Backslash">\</a>
</td>
<td title="93 U+005D: RIGHT SQUARE BRACKET" style="padding:1px;"><a href="/wiki/Right_square_bracket" class="mw-redirect" title="Right square bracket">&#93;</a>
</td>
<td title="94 U+005E: CIRCUMFLEX ACCENT" style="padding:1px"><a href="/wiki/%5E" class="mw-redirect" title="^">^</a>
</td>
<td title="95 U+005F: LOW LINE" style="padding:1px"><a href="/wiki/Underscore" title="Underscore">_</a>
</td></tr>
<tr>
<td style="height:2em;height:22pt;line-height:1">6x
</td>
<td title="96 U+0060: GRAVE ACCENT" style="padding:1px"><a href="/wiki/%60" class="mw-redirect" title="`">`</a>
</td>
<td title="97 U+0061: LATIN SMALL LETTER A" style="padding:1px"><a href="/wiki/A" title="A">a</a>
</td>
<td title="98 U+0062: LATIN SMALL LETTER B" style="padding:1px"><a href="/wiki/B" title="B">b</a>
</td>
<td title="99 U+0063: LATIN SMALL LETTER C" style="padding:1px"><a href="/wiki/C" title="C">c</a>
</td>
<td title="100 U+0064: LATIN SMALL LETTER D" style="padding:1px"><a href="/wiki/D" title="D">d</a>
</td>
<td title="101 U+0065: LATIN SMALL LETTER E" style="padding:1px"><a href="/wiki/E" title="E">e</a>
</td>
<td title="102 U+0066: LATIN SMALL LETTER F" style="padding:1px"><a href="/wiki/F" title="F">f</a>
</td>
<td title="103 U+0067: LATIN SMALL LETTER G" style="padding:1px"><a href="/wiki/G" title="G">g</a>
</td>
<td title="104 U+0068: LATIN SMALL LETTER H" style="padding:1px"><a href="/wiki/H" title="H">h</a>
</td>
<td title="105 U+0069: LATIN SMALL LETTER I" style="padding:1px"><a href="/wiki/I" title="I">i</a>
</td>
<td title="106 U+006A: LATIN SMALL LETTER J" style="padding:1px"><a href="/wiki/J" title="J">j</a>
</td>
<td title="107 U+006B: LATIN SMALL LETTER K" style="padding:1px"><a href="/wiki/K" title="K">k</a>
</td>
<td title="108 U+006C: LATIN SMALL LETTER L" style="padding:1px"><a href="/wiki/L" title="L">l</a>
</td>
<td title="109 U+006D: LATIN SMALL LETTER M" style="padding:1px"><a href="/wiki/M" title="M">m</a>
</td>
<td title="110 U+006E: LATIN SMALL LETTER N" style="padding:1px"><a href="/wiki/N" title="N">n</a>
</td>
<td title="111 U+006F: LATIN SMALL LETTER O" style="padding:1px"><a href="/wiki/O" title="O">o</a>
</td></tr>
<tr>
<td style="height:2em;height:22pt;line-height:1">7x
</td>
<td title="112 U+0070: LATIN SMALL LETTER P" style="padding:1px"><a href="/wiki/P" title="P">p</a>
</td>
<td title="113 U+0071: LATIN SMALL LETTER Q" style="padding:1px"><a href="/wiki/Q" title="Q">q</a>
</td>
<td title="114 U+0072: LATIN SMALL LETTER R" style="padding:1px"><a href="/wiki/R" title="R">r</a>
</td>
<td title="115 U+0073: LATIN SMALL LETTER S" style="padding:1px"><a href="/wiki/S" title="S">s</a>
</td>
<td title="116 U+0074: LATIN SMALL LETTER T" style="padding:1px"><a href="/wiki/T" title="T">t</a>
</td>
<td title="117 U+0075: LATIN SMALL LETTER U" style="padding:1px"><a href="/wiki/U" title="U">u</a>
</td>
<td title="118 U+0076: LATIN SMALL LETTER V" style="padding:1px"><a href="/wiki/V" title="V">v</a>
</td>
<td title="119 U+0077: LATIN SMALL LETTER W" style="padding:1px"><a href="/wiki/W" title="W">w</a>
</td>
<td title="120 U+0078: LATIN SMALL LETTER X" style="padding:1px"><a href="/wiki/X" title="X">x</a>
</td>
<td title="121 U+0079: LATIN SMALL LETTER Y" style="padding:1px"><a href="/wiki/Y" title="Y">y</a>
</td>
<td title="122 U+007A: LATIN SMALL LETTER Z" style="padding:1px"><a href="/wiki/Z" title="Z">z</a>
</td>
<td title="123 U+007B: LEFT CURLY BRACKET" style="padding:1px"><a href="/wiki/Left_curly_bracket" class="mw-redirect" title="Left curly bracket">{</a>
</td>
<td title="124 U+007C: VERTICAL LINE" style="padding:1px"><a href="/wiki/Vertical_bar" title="Vertical bar">&#124;</a>
</td>
<td title="125 U+007D: RIGHT CURLY BRACKET" style="padding:1px"><a href="/wiki/Right_curly_bracket" class="mw-redirect" title="Right curly bracket">}</a>
</td>
<td title="126 U+007E: TILDE" style="padding:1px"><a href="/wiki/~" class="mw-redirect" title="~">~</a>
</td>
<td title="127 U+007F: Control (alias DELETE) (alias DEL)" style="padding:1px;"><span style="display:inline-block; border:1px dashed blue;"> <a href="/wiki/Delete_character" title="Delete character">DEL</a> </span>
</td></tr>
</tbody></table>

::: credit
Formattering frå Wikipedia
:::

note:
Men nok om binærfiler.
Vi har nok utfordringer med tekstfiler.

Selv om vi om vi ofte tenker på tekstfiler som et primitivt
format distinkt fra binærfiler, er *alt* egentlig binærfiler,
med vilkårlier rekker av bytes med verdier mellom 0 og 255.

Når vi ser på dem som tekstfiler, har hvert tegn fått sin 
tallverdi, og hver byte blir forstått ved å slå opp nummeret
i tegnsettet.

Problemet er at der er mer enn ett tegnsett i verden.

Det eldste og mest kjente tegnsettet heter ASCII og ble
standardisert av *American National Standards Institute* 
eller ANSI allerede i 1963, med noen senere revisjoner.
Vi ser tegntabellen på foilen med 128 tegn.
Vi bruker altså ikke alle 256 tegn; den åttende bitten i hver
byte blir brukt til feilkontroll.

De første 32 tegnene er kontrolltegn, som inkluderer linje-
og sideskift, slutt-på-fil, avbryt eller *interrupt*,
slett eller *backspace* og ... pipetone ... altså et lydsignal.
Grunnen for alle kontrolltegnene var at på 1960-tallets maskiner måtte
alle tastene på tastaturet representeres som tegn.  Man hadde bare
ett tegnsett til all kommunikasjon mellom maskinen og terminalen, dvs. skjerm og tastatur.

Uansett ga dette under ett hundrede visuelle tegn, bare så vidt nok til 
26 bokstaver i stort og smått, ti sifre samt punktum, komma, parenteser
og lignende.

Det holdt lenge for amerikanerne, men ikke like lenge for europeerne.

---

<!-- slide template="[[tpl-smalltext]]" -->

<table border="1" style="border-collapse:collapse;text-align:center">
<caption style="font-size:140%">ISO/IEC 8859-1</caption>
<tbody><tr>
<td>
</td>
<td style="width:20pt">0</td>
<td style="width:20pt">1</td>
<td style="width:20pt">2</td>
<td style="width:20pt">3</td>
<td style="width:20pt">4</td>
<td style="width:20pt">5</td>
<td style="width:20pt">6</td>
<td style="width:20pt">7</td>
<td style="width:20pt">8</td>
<td style="width:20pt">9</td>
<td style="width:20pt">A</td>
<td style="width:20pt">B</td>
<td style="width:20pt">C</td>
<td style="width:20pt">D</td>
<td style="width:20pt">E</td>
<td style="width:20pt">F</td></tr>
<tr>
<td style="height:2em;height:22pt;line-height:1">Ax
</td>
<td title="160&#10;U+00A0: NO-BREAK SPACE" style="padding:1px;"><span style="display:inline-block; border:1px dashed blue;"> <a href="/wiki/NBSP" class="mw-redirect" title="NBSP">NBSP</a> </span>
</td>
<td title="161&#10;U+00A1: INVERTED EXCLAMATION MARK" style="padding:1px;"><a href="/wiki/%C2%A1" class="mw-redirect" title="¡">&#xa1;</a>
</td>
<td title="162&#10;U+00A2: CENT SIGN" style="padding:1px;"><a href="/wiki/%C2%A2" class="mw-redirect" title="¢">&#xa2;</a>
</td>
<td title="163&#10;U+00A3: POUND SIGN" style="padding:1px;"><a href="/wiki/%C2%A3" class="mw-redirect" title="£">&#xa3;</a>
</td>
<td title="164&#10;U+00A4: CURRENCY SIGN" style="padding:1px;"><a href="/wiki/%C2%A4" class="mw-redirect" title="¤">&#xa4;</a>
</td>
<td title="165&#10;U+00A5: YEN SIGN" style="padding:1px;"><a href="/wiki/%C2%A5" class="mw-redirect" title="¥">&#xa5;</a>
</td>
<td title="166&#10;U+00A6: BROKEN BAR" style="padding:1px;"><a href="/wiki/%C2%A6" class="mw-redirect" title="¦">&#xa6;</a>
</td>
<td title="167&#10;U+00A7: SECTION SIGN" style="padding:1px;"><a href="/wiki/%C2%A7" class="mw-redirect" title="§">&#xa7;</a>
</td>
<td title="168&#10;U+00A8: DIAERESIS" style="padding:1px;"><a href="/wiki/%C2%A8" class="mw-redirect" title="¨">&#xa8;</a>
</td>
<td title="169&#10;U+00A9: COPYRIGHT SIGN" style="padding:1px;"><a href="/wiki/%C2%A9" class="mw-redirect" title="©">&#xa9;</a>
</td>
<td title="170&#10;U+00AA: FEMININE ORDINAL INDICATOR" style="padding:1px;"><a href="/wiki/%C2%AA" class="mw-redirect" title="ª">&#xaa;</a>
</td>
<td title="171&#10;U+00AB: LEFT-POINTING DOUBLE ANGLE QUOTATION MARK" style="padding:1px;"><a href="/wiki/%C2%AB" class="mw-redirect" title="«">&#xab;</a>
</td>
<td title="172&#10;U+00AC: NOT SIGN" style="padding:1px;"><a href="/wiki/%C2%AC" class="mw-redirect" title="¬">&#xac;</a>
</td>
<td title="173&#10;U+00AD: SOFT HYPHEN" style="padding:1px;"><span style="display:inline-block; border:1px dashed blue;"> <a href="/wiki/Soft_hyphen" title="Soft hyphen">SHY</a> </span>
</td>
<td title="174&#10;U+00AE: REGISTERED SIGN" style="padding:1px;"><a href="/wiki/%C2%AE" class="mw-redirect" title="®">&#xae;</a>
</td>
<td title="175&#10;U+00AF: MACRON" style="padding:1px;"><a href="/wiki/%C2%AF" class="mw-redirect" title="¯">&#xaf;</a>
</td></tr>
<tr>
<td style="height:2em;height:22pt;line-height:1">Bx
</td>
<td title="176&#10;U+00B0: DEGREE SIGN" style="padding:1px;"><a href="/wiki/%C2%B0" class="mw-redirect" title="°">&#xb0;</a>
</td>
<td title="177&#10;U+00B1: PLUS-MINUS SIGN" style="padding:1px;"><a href="/wiki/%C2%B1" class="mw-redirect" title="±">&#xb1;</a>
</td>
<td title="178&#10;U+00B2: SUPERSCRIPT TWO" style="padding:1px;"><a href="/wiki/Superscript" class="mw-redirect" title="Superscript">&#xb2;</a>
</td>
<td title="179&#10;U+00B3: SUPERSCRIPT THREE" style="padding:1px;"><a href="/wiki/Superscript" class="mw-redirect" title="Superscript">&#xb3;</a>
</td>
<td title="180&#10;U+00B4: ACUTE ACCENT" style="padding:1px;"><a href="/wiki/%C2%B4" class="mw-redirect" title="´">&#xb4;</a>
</td>
<td title="181&#10;U+00B5: MICRO SIGN" style="padding:1px;"><a href="/wiki/%CE%9C" class="mw-redirect" title="Μ">&#xb5;</a>
</td>
<td title="182&#10;U+00B6: PILCROW SIGN" style="padding:1px;"><a href="/wiki/%C2%B6" class="mw-redirect" title="¶">&#xb6;</a>
</td>
<td title="183&#10;U+00B7: MIDDLE DOT" style="padding:1px;"><a href="/wiki/%C2%B7" class="mw-redirect" title="·">&#xb7;</a>
</td>
<td title="184&#10;U+00B8: CEDILLA" style="padding:1px;"><a href="/wiki/%C2%B8" class="mw-redirect" title="¸">&#xb8;</a>
</td>
<td title="185&#10;U+00B9: SUPERSCRIPT ONE" style="padding:1px;"><a href="/wiki/Superscript" class="mw-redirect" title="Superscript">&#xb9;</a>
</td>
<td title="186&#10;U+00BA: MASCULINE ORDINAL INDICATOR" style="padding:1px;"><a href="/wiki/%C2%BA" class="mw-redirect" title="º">&#xba;</a>
</td>
<td title="187&#10;U+00BB: RIGHT-POINTING DOUBLE ANGLE QUOTATION MARK" style="padding:1px;"><a href="/wiki/%C2%BB" class="mw-redirect" title="»">&#xbb;</a>
</td>
<td title="188&#10;U+00BC: VULGAR FRACTION ONE QUARTER" style="padding:1px;"><a href="/wiki/Fraction#Typographical_variations" title="Fraction">&#xbc;</a>
</td>
<td title="189&#10;U+00BD: VULGAR FRACTION ONE HALF" style="padding:1px;"><a href="/wiki/%C2%BD" class="mw-redirect" title="½">&#xbd;</a>
</td>
<td title="190&#10;U+00BE: VULGAR FRACTION THREE QUARTERS" style="padding:1px;"><a href="/wiki/Fraction#Typographical_variations" title="Fraction">&#xbe;</a>
</td>
<td title="191&#10;U+00BF: INVERTED QUESTION MARK" style="padding:1px;"><a href="/wiki/%C2%BF" class="mw-redirect" title="¿">&#xbf;</a>
</td></tr>
<tr>
<td style="height:2em;height:22pt;line-height:1">Cx
</td>
<td title="192&#10;U+00C0: LATIN CAPITAL LETTER A WITH GRAVE" style="padding:1px;"><a href="/wiki/%C3%80" title="À">&#xc0;</a>
</td>
<td title="193&#10;U+00C1: LATIN CAPITAL LETTER A WITH ACUTE" style="padding:1px;"><a href="/wiki/%C3%81" title="Á">&#xc1;</a>
</td>
<td title="194&#10;U+00C2: LATIN CAPITAL LETTER A WITH CIRCUMFLEX" style="padding:1px;"><a href="/wiki/%C3%82" title="Â">&#xc2;</a>
</td>
<td title="195&#10;U+00C3: LATIN CAPITAL LETTER A WITH TILDE" style="padding:1px;"><a href="/wiki/%C3%83" title="Ã">&#xc3;</a>
</td>
<td title="196&#10;U+00C4: LATIN CAPITAL LETTER A WITH DIAERESIS" style="padding:1px;"><a href="/wiki/%C3%84" title="Ä">&#xc4;</a>
</td>
<td title="197&#10;U+00C5: LATIN CAPITAL LETTER A WITH RING ABOVE" style="padding:1px;"><a href="/wiki/%C3%85" title="Å">&#xc5;</a>
</td>
<td title="198&#10;U+00C6: LATIN CAPITAL LETTER AE" style="padding:1px;"><a href="/wiki/%C3%86" title="Æ">&#xc6;</a>
</td>
<td title="199&#10;U+00C7: LATIN CAPITAL LETTER C WITH CEDILLA" style="padding:1px;"><a href="/wiki/%C3%87" title="Ç">&#xc7;</a>
</td>
<td title="200&#10;U+00C8: LATIN CAPITAL LETTER E WITH GRAVE" style="padding:1px;"><a href="/wiki/%C3%88" title="È">&#xc8;</a>
</td>
<td title="201&#10;U+00C9: LATIN CAPITAL LETTER E WITH ACUTE" style="padding:1px;"><a href="/wiki/%C3%89" title="É">&#xc9;</a>
</td>
<td title="202&#10;U+00CA: LATIN CAPITAL LETTER E WITH CIRCUMFLEX" style="padding:1px;"><a href="/wiki/%C3%8A" title="Ê">&#xca;</a>
</td>
<td title="203&#10;U+00CB: LATIN CAPITAL LETTER E WITH DIAERESIS" style="padding:1px;"><a href="/wiki/%C3%8B" title="Ë">&#xcb;</a>
</td>
<td title="204&#10;U+00CC: LATIN CAPITAL LETTER I WITH GRAVE" style="padding:1px;"><a href="/wiki/%C3%8C" title="Ì">&#xcc;</a>
</td>
<td title="205&#10;U+00CD: LATIN CAPITAL LETTER I WITH ACUTE" style="padding:1px;"><a href="/wiki/%C3%8D" title="Í">&#xcd;</a>
</td>
<td title="206&#10;U+00CE: LATIN CAPITAL LETTER I WITH CIRCUMFLEX" style="padding:1px;"><a href="/wiki/%C3%8E" title="Î">&#xce;</a>
</td>
<td title="207&#10;U+00CF: LATIN CAPITAL LETTER I WITH DIAERESIS" style="padding:1px;"><a href="/wiki/%C3%8F" title="Ï">&#xcf;</a>
</td></tr>
<tr>
<td style="height:2em;height:22pt;line-height:1">Dx
</td>
<td title="208&#10;U+00D0: LATIN CAPITAL LETTER ETH" style="padding:1px;"><a href="/wiki/%C3%90" class="mw-redirect" title="Ð">&#xd0;</a>
</td>
<td title="209&#10;U+00D1: LATIN CAPITAL LETTER N WITH TILDE" style="padding:1px;"><a href="/wiki/%C3%91" title="Ñ">&#xd1;</a>
</td>
<td title="210&#10;U+00D2: LATIN CAPITAL LETTER O WITH GRAVE" style="padding:1px;"><a href="/wiki/%C3%92" title="Ò">&#xd2;</a>
</td>
<td title="211&#10;U+00D3: LATIN CAPITAL LETTER O WITH ACUTE" style="padding:1px;"><a href="/wiki/%C3%93" title="Ó">&#xd3;</a>
</td>
<td title="212&#10;U+00D4: LATIN CAPITAL LETTER O WITH CIRCUMFLEX" style="padding:1px;"><a href="/wiki/%C3%94" class="mw-redirect" title="Ô">&#xd4;</a>
</td>
<td title="213&#10;U+00D5: LATIN CAPITAL LETTER O WITH TILDE" style="padding:1px;"><a href="/wiki/%C3%95" title="Õ">&#xd5;</a>
</td>
<td title="214&#10;U+00D6: LATIN CAPITAL LETTER O WITH DIAERESIS" style="padding:1px;"><a href="/wiki/%C3%96" title="Ö">&#xd6;</a>
</td>
<td title="215&#10;U+00D7: MULTIPLICATION SIGN" style="padding:1px;"><a href="/wiki/%C3%97" class="mw-redirect" title="×">&#xd7;</a>
</td>
<td title="216&#10;U+00D8: LATIN CAPITAL LETTER O WITH STROKE" style="padding:1px;"><a href="/wiki/%C3%98" title="Ø">&#xd8;</a>
</td>
<td title="217&#10;U+00D9: LATIN CAPITAL LETTER U WITH GRAVE" style="padding:1px;"><a href="/wiki/%C3%99" class="mw-redirect" title="Ù">&#xd9;</a>
</td>
<td title="218&#10;U+00DA: LATIN CAPITAL LETTER U WITH ACUTE" style="padding:1px;"><a href="/wiki/%C3%9A" title="Ú">&#xda;</a>
</td>
<td title="219&#10;U+00DB: LATIN CAPITAL LETTER U WITH CIRCUMFLEX" style="padding:1px;"><a href="/wiki/%C3%9B" title="Û">&#xdb;</a>
</td>
<td title="220&#10;U+00DC: LATIN CAPITAL LETTER U WITH DIAERESIS" style="padding:1px;"><a href="/wiki/%C3%9C" title="Ü">&#xdc;</a>
</td>
<td title="221&#10;U+00DD: LATIN CAPITAL LETTER Y WITH ACUTE" style="padding:1px;"><a href="/wiki/%C3%9D" title="Ý">&#xdd;</a>
</td>
<td title="222&#10;U+00DE: LATIN CAPITAL LETTER THORN" style="padding:1px;"><a href="/wiki/%C3%9E" class="mw-redirect" title="Þ">&#xde;</a>
</td>
<td title="223&#10;U+00DF: LATIN SMALL LETTER SHARP S" style="padding:1px;"><a href="/wiki/%C3%9F" title="ß">&#xdf;</a>
</td></tr>
<tr>
<td style="height:2em;height:22pt;line-height:1">Ex
</td>
<td title="224&#10;U+00E0: LATIN SMALL LETTER A WITH GRAVE" style="padding:1px;"><a href="/wiki/%C3%80" title="À">&#xe0;</a>
</td>
<td title="225&#10;U+00E1: LATIN SMALL LETTER A WITH ACUTE" style="padding:1px;"><a href="/wiki/%C3%81" title="Á">&#xe1;</a>
</td>
<td title="226&#10;U+00E2: LATIN SMALL LETTER A WITH CIRCUMFLEX" style="padding:1px;"><a href="/wiki/%C3%82" title="Â">&#xe2;</a>
</td>
<td title="227&#10;U+00E3: LATIN SMALL LETTER A WITH TILDE" style="padding:1px;"><a href="/wiki/%C3%83" title="Ã">&#xe3;</a>
</td>
<td title="228&#10;U+00E4: LATIN SMALL LETTER A WITH DIAERESIS" style="padding:1px;"><a href="/wiki/%C3%84" title="Ä">&#xe4;</a>
</td>
<td title="229&#10;U+00E5: LATIN SMALL LETTER A WITH RING ABOVE" style="padding:1px;"><a href="/wiki/%C3%85" title="Å">&#xe5;</a>
</td>
<td title="230&#10;U+00E6: LATIN SMALL LETTER AE" style="padding:1px;"><a href="/wiki/%C3%86" title="Æ">&#xe6;</a>
</td>
<td title="231&#10;U+00E7: LATIN SMALL LETTER C WITH CEDILLA" style="padding:1px;"><a href="/wiki/%C3%87" title="Ç">&#xe7;</a>
</td>
<td title="232&#10;U+00E8: LATIN SMALL LETTER E WITH GRAVE" style="padding:1px;"><a href="/wiki/%C3%88" title="È">&#xe8;</a>
</td>
<td title="233&#10;U+00E9: LATIN SMALL LETTER E WITH ACUTE" style="padding:1px;"><a href="/wiki/%C3%89" title="É">&#xe9;</a>
</td>
<td title="234&#10;U+00EA: LATIN SMALL LETTER E WITH CIRCUMFLEX" style="padding:1px;"><a href="/wiki/%C3%8A" title="Ê">&#xea;</a>
</td>
<td title="235&#10;U+00EB: LATIN SMALL LETTER E WITH DIAERESIS" style="padding:1px;"><a href="/wiki/%C3%8B" title="Ë">&#xeb;</a>
</td>
<td title="236&#10;U+00EC: LATIN SMALL LETTER I WITH GRAVE" style="padding:1px;"><a href="/wiki/%C3%8C" title="Ì">&#xec;</a>
</td>
<td title="237&#10;U+00ED: LATIN SMALL LETTER I WITH ACUTE" style="padding:1px;"><a href="/wiki/%C3%8D" title="Í">&#xed;</a>
</td>
<td title="238&#10;U+00EE: LATIN SMALL LETTER I WITH CIRCUMFLEX" style="padding:1px;"><a href="/wiki/%C3%8E" title="Î">&#xee;</a>
</td>
<td title="239&#10;U+00EF: LATIN SMALL LETTER I WITH DIAERESIS" style="padding:1px;"><a href="/wiki/%C3%8F" title="Ï">&#xef;</a>
</td></tr>
<tr>
<td style="height:2em;height:22pt;line-height:1">Fx
</td>
<td title="240&#10;U+00F0: LATIN SMALL LETTER ETH" style="padding:1px;"><a href="/wiki/%C3%90" class="mw-redirect" title="Ð">&#xf0;</a>
</td>
<td title="241&#10;U+00F1: LATIN SMALL LETTER N WITH TILDE" style="padding:1px;"><a href="/wiki/%C3%91" title="Ñ">&#xf1;</a>
</td>
<td title="242&#10;U+00F2: LATIN SMALL LETTER O WITH GRAVE" style="padding:1px;"><a href="/wiki/%C3%92" title="Ò">&#xf2;</a>
</td>
<td title="243&#10;U+00F3: LATIN SMALL LETTER O WITH ACUTE" style="padding:1px;"><a href="/wiki/%C3%93" title="Ó">&#xf3;</a>
</td>
<td title="244&#10;U+00F4: LATIN SMALL LETTER O WITH CIRCUMFLEX" style="padding:1px;"><a href="/wiki/%C3%94" class="mw-redirect" title="Ô">&#xf4;</a>
</td>
<td title="245&#10;U+00F5: LATIN SMALL LETTER O WITH TILDE" style="padding:1px;"><a href="/wiki/%C3%95" title="Õ">&#xf5;</a>
</td>
<td title="246&#10;U+00F6: LATIN SMALL LETTER O WITH DIAERESIS" style="padding:1px;"><a href="/wiki/%C3%96" title="Ö">&#xf6;</a>
</td>
<td title="247&#10;U+00F7: DIVISION SIGN" style="padding:1px;"><a href="/wiki/%C3%B7" class="mw-redirect" title="÷">&#xf7;</a>
</td>
<td title="248&#10;U+00F8: LATIN SMALL LETTER O WITH STROKE" style="padding:1px;"><a href="/wiki/%C3%98" title="Ø">&#xf8;</a>
</td>
<td title="249&#10;U+00F9: LATIN SMALL LETTER U WITH GRAVE" style="padding:1px;"><a href="/wiki/%C3%99" class="mw-redirect" title="Ù">&#xf9;</a>
</td>
<td title="250&#10;U+00FA: LATIN SMALL LETTER U WITH ACUTE" style="padding:1px;"><a href="/wiki/%C3%9A" title="Ú">&#xfa;</a>
</td>
<td title="251&#10;U+00FB: LATIN SMALL LETTER U WITH CIRCUMFLEX" style="padding:1px;"><a href="/wiki/%C3%9B" title="Û">&#xfb;</a>
</td>
<td title="252&#10;U+00FC: LATIN SMALL LETTER U WITH DIAERESIS" style="padding:1px;"><a href="/wiki/%C3%9C" title="Ü">&#xfc;</a>
</td>
<td title="253&#10;U+00FD: LATIN SMALL LETTER Y WITH ACUTE" style="padding:1px;"><a href="/wiki/%C3%9D" title="Ý">&#xfd;</a>
</td>
<td title="254&#10;U+00FE: LATIN SMALL LETTER THORN" style="padding:1px;"><a href="/wiki/%C3%9E" class="mw-redirect" title="Þ">&#xfe;</a>
</td>
<td title="255&#10;U+00FF: LATIN SMALL LETTER Y WITH DIAERESIS" style="padding:1px;"><a href="/wiki/%C5%B8" title="Ÿ">&#xff;</a>
</td></tr>
</tbody></table>

::: credit
Formattering frå Wikipedia
:::

note:
Efter hvert ble det vanlig å bruke 255 tegn, enten til ulike grafiske
tegn eller for å støtte sprog som norsk eller fransk.
På åttitallet hadde gjerne hver leverandør sitt tegnsett, men etter
hvert fikk vi internasjonale standarder.
Foilen viser Latin 1, som ble dominerende her i landet utover 1990-tallet,
og som fremdles brukes, f.eks., i CSV-filer fra *Statistisk Sentralbyrå*. 

De 128 første tegnene er identisk med ASCII og de neste 32 plassene
står ubrukt for å unngå forveksling med kontrolltegnene.
Likevel ser vi at vi har tegnene for å skrive norsk, svensk, samisk
og islandsk, men f.eks. fransk og finsk mangler fremdeles noen tegn.

For 25 år siden dukket også et nytt behov opp.
Da kom euroen som valuta, med sitt eget symbol.
Da kom Latin-15 som skulle dekke finsk og fransk,
samt eurosymbolet.

---

<!-- slide template="[[tpl-quote]]" -->

![[Popular_Emoji_Groups_Noto_Color_Emoji.svg]]

::: credit
By Google - Got SVGs from Noto Color Emoji github, arranged them in a square in PowerPoint, and saved the group of the squares as an SVG., OFL,
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=164632854)
:::

note:
Det sier seg selv at dette var fryktelig tungvint.
Maskinen kunne ikke kjenne igjen tegnsettet i en ren tekstfil,
så brukeren ville måtte holde rede på alle de tegnsett som trengs
til de sprog som skrives.
Tekstbehandlingsprogrammer kunne løse dette ved å bruke et binærformat med metadata, men f.eks. CSV-filer blir lett feil.

Det sier seg selv at vi aldri ville ha fått *emojis* med 256 tegn. 

Løsningen er *Unicode* som er et universelt tegnsett med snart 300.000
tegn.
Det første utkastet til standarden kom faktisk i 1990, men det tok
langt tid før *Unicode* kom i vanlig brukt, og i flere tiår har det
eksistert side om side med Latin-1 og andre regionale tegnsett.

Ulempen med *Unicode* er at hvert tegn trenger flere *bytes* som
gjør at filene blir større.
Dette gjøres på flere forskjellige måter.  Den vanligste er
UTF-8 som skal være bakoverkompatibel med ASCII.  Dvs. at
ASCII-tegnene kodes som én *byte*, mens andre tegn trenger flere.
Det går greit side ASCII bare bruker syv *bits* slik at den åttende
*bitten* signaliserer behovet for flere *bytes*.

---

<!-- slide template="[[tpl-twocolumn]]" -->

::: leftimage
![[latin1.png]]
:::

::: leftcredit
:::

::: rightimage
![[utf8.png]]
:::

::: rightcredit
:::

note:
Selv om nesten all programvare i dag bruker UTF-8, finnes
Latin-1, eller ISO 8859-1, fremdeles.
Og det gjelder særlig i datasett.
Derfor er det viktig å være oppmerksom på utfordringen.

Jeg vet ikke om du la merke til det da vi åpnet CSV-filer
i regnearket i sted, men der er et valg for tegnsett helt øverst.
Nederst i skjermbildet kan du se hvor det som er mer eller mindre
vanlige tegn i Latin-1 blir udefinert i UTF-8.

---

<!-- slide template="[[tpl-twocolumn]]" -->

::: leftimage
![[latin1.png]]
:::

::: leftcredit
:::

::: rightimage
![[latin15.png]]
:::

::: rightcredit
:::

note:
Latin-1 er derimot ikke riktig tegnkoding.
Hvis vi sammenligner Latin-1 og Latin-15, ser 
vi at brøkene for en halv og en kvart skulle være den franske
Œ-ligaturen.
Eurosymbolet er også nytt i Latin-15.

---

<!-- slide template="[[tpl-quote]]" -->

![[Consul_mechanical_typewriter_in_Třebíč,_Třebíč_District.jpg]]

::: credit
By Jiří Sedláček (Frettie) - Own work, CC BY 3.0,
via [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=10383564)
:::

note:
På tampen skal jeg nevne én utfordring til som dere kanskje kan støte på,
nemlig linjeskift.

ASCII tok mye av sin inspirasjon fra mekaniske skrivemaskiner, og der
består linjeskiftet av to operasjoner.  
Den ene er *line feed* som fører rullen og dermed arket et hakk opp,
slik at neste tegn treffer siden en linje lenger ned.
Den andre er *carriage return* består i at «vognen» dvs. den delen 
av maskinen som holder rullen og arket, føres tilbake til høyre
slik at neste tegn treffer helt til venstre på siden.

Dette gir opphav til to ASCII-tegn for *line feed* og for 
*carriage return*.
Windows bruker begge tegnene for å representere linjeskift,
mens Unix, og dermed linux og MaxOS, bruker bare *line feed*.
I gamle dager brukte MacOS endog bare *carriage return*, 
men det var var før de skrev om kjernen til Unix-standard for
25 år siden.

De fleste programmer i dag klarer å håndtere alle linjeskiftkombinasjonene
om hverandre, men hvis dere støter på ett som ikke gjør det, så skjønner
dere forhåpentligvis hva som skjer.

---

# Slutt

note:
Som dere skjønner er det mye i dataverden som ikke er helt gjennomtenkt.
Det meste har utviklet seg gradvis, med behov for bakoverkompatibilitet.
Dermed må vi fremdeles stri med løsninger fra 1960-tallet.

Jeg håper dette overordnete og historiske perspektivet gjør det litt
lettere å forstå hva som går galt, når dere utforsker data fra nye
kilder, og at det gjør det litt lettere å stå på og komme over
utfordringene.

Da kan ikke jeg gjøre mer enn å ønske lykke til.
