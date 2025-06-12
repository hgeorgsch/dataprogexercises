---
tags:
  - lecture/video
---
<!-- slide template="[[tpl-fitdiagram2]]" -->

![[ssb-statistisk-aarbog-1881.png]]
::: credit
Statistik årbok 1881, fra ssb.no
:::

note:
Før den digitale revolusjonen var datainnhenting en manuell og langsom prosess.

Skulle dataene være tilgjengelig for flest mulig, (forskere, journalister, byråkrater osv) ble de gjerne utgitt som trykte publikasjoner.

Bildet viser forsiden på ssbs statistiske årbok fra 1881 




---

<!--- slide template="[[tpl-diagram]]" -->
<!-- slide bg="white" -->
![[SSB-statistisk-aarbog-eksempel.png]]

note:
Årboken inneholdt trykte tabeller, og kunne hentes ut på feks et universitetsbibliotek

Dersom trengte ferskere data måtte man sende slike forespørsler per telefon eller post - og vente på svar gjennom posten. Mye av datainnhentingen blant akademikere skjedde gjennom nettverksbygging og brevkorrespondanse.

---
<!--- slide template="[[tpl-diagram]]" -->
<!-- slide bg="white" -->
![[Eurostat_Newlogo.png]]
![[Statistics_Norway_logo.svg.png]]

note: 
I dag skjer datalagring og distrubisjon digitalt, og man har tilgang på data av høy kvalitet fra feks ssb eller eurostat ved å bla seg gjennom nettsidene deres og laste de ned i et passende format.

Det vil ikke si at det nødvendigvis er lett å samle inn og distribuere data av høy kvalitet til store mengder med brukere - ssb hadde i 2023-2024 en utgiftsramme på 988 millioner kroner.

Terskelen er derimot veldig liten for å publisere data - vi trenger ikke lenger distribuere de rundt på biblioteker og universiteter i trykte medier, man kan feks bare legge de ut på github.com


---
# Et vell av data

note:
På det ganske internett finner vi da data som er tilgjengelig gratis, og som vi må betale for tilgang til. Vi finner data av høy kvalitet som har vært kostbart å sammenstille, og data som er mer «rå» og gjort tilgjenglig fordi det i tilsvarer noen særlig kostnad.

Det som i hvert fall er sikkert er at det en veldig mengde som er tilgjengelig for oss.

For å illustrere har jeg letet litt etter noen rare eksempler:

---
![[githubvanityplates.png]]


note:
På github fant jeg data over personlige bilskilt som er blitt flagget for gjennomgang av en saksbehandler. Den inneholder skilt, hvorfor den er blitt flagget, søkerens forklaring, saksbehandlers notat, og om skiltet er godkjent


---

![[plates-trump.png | 300]]

Søkers forklaring: «Funky trumpet in the funk music genre»


![[huf4rtd.png | 300]]


Søkers forklaring: «Have Unwaivering faith (4) Respect the Day

---

![[Pasted image 20250610131848.png ]]

note:
For de som vil dra på campingtur og ikke er redd for edderkopper, er det mulig å finne data om offentlige toalett

---

![[aussie-toilet.png]]
![[aussie-toilet-columns.png]]

note:
Her har vi gps-koordinater på rett under 25,000 offentlige toalett med et litt komisk detaljnivå

---

![[dolthub-bad-words.png]]

note:
På dolthub fant jeg en database med stygge ord, typisk bruk ville være en form for sensur.
Her har vi ufinheter på de fleste språk  inkludert Klingon, og vil du fornærme en franskmann, kan du kalle ham en balayette (toalettbørste)

---

#### sharkattackfile.net

![[haiangrep.png]]
+ Over 6000 registrerte haiangrep
+ Inkluder Odd Ingebretsen


---
<iframe src="https://www.nrk.no/stor-oslo/haisommer-i-oslofjorden-1.2984539" title="tittel her" width="600px" height="600px"></iframe>

---

### Karakteristikker

+ Kildepålitelighet
+ Validet og nøyaktighet
+ Kompletthet
+ Konsistens
+ Granularitet
+ Format og struktur
+ Tilgjengelighet
+ Aktualitet - tidsriktighet

note:
* Kildepålitelighet -- ssb, eurostat stoler vi på -- hva med en tilfeldig githubbruker?
* Validitet og nøyaktighet - Måler dataene det de påstår og er de presise?
* Kompletthet - Hvor stor del av fenomen eller populasjon er fanget opp?
* Konsistens - Er format og definasjoner de samme over tid / på tvers av kilder?
* Granularitet - Hvor detaljert er dataene? 
* Tilgjengelighet: gratis , åpen, registreringsvasert, paywall, rate-limit, filstørrelse
* Aktualitet / tidsriktighet: Hvor raskt oppdateres dataene etter at virkeligheten endrer seg

---

#### Noe data er ferskvare

note:
I områder som finans, sport, trafikk og vær er det å ha ny data helt kritisk.
I 2010 fullførte «Spread Network» en fiberlinje mellom Chicago og New Jersey, 1300km, til en kostnad på 300 millioner dollar. Dette for å være 14 millisekund foran på handler mellom Carteret New Jersey, hvor man kan finne datasenteret til nasdaq, og Chicago Mercentile Exchange.

Situasjonsrapportering og beredskap:
Smittetall, ekstremvær - Myndigheter og medier må handle raskt

---
### Programmatisk innhenting av data


note:
Når vi krøver høy aktualitet av dataene våres - blir det fort plagsomt, ineffektivt og dyrt å ha mennesker til å klikke seg seg gjennom nettsider for å manuelt laste ned nye csv-filer

Vi trenger automatiske prosesser til å gjøre dette - vi kan for eksempel skrive python-kode som gjør dette for oss

For å kunne gjøre dette må vi vite litt om hvordan datamaskiner kommuniserer over et nettverk

---

<!-- slide template="[[tpl-fitdiagram2]]" -->
![[communication-troubles.webp]]

::: credit
Illustrasjon generert av DALL-E
:::
---

<!-- slide template="[[tpl-fitdiagram2]]" -->
##### OSI-model

![[osi.svg]]

::: credit
:::

note:

