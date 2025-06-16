---
tags:
  - lecture/video
---
<!-- slide template="[[tpl-fitdiagram2]]" -->


![[ssb-statistisk-aarbog-1881.png]]
::: credit
Statistsik årbok 1881, fra ssb.no
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
Årboken inneholdt trykte tabeller, og kunne hentes ut på feks et universitetsbibliotek. Her ser vi en av tabellene over "tilstedeværende folkemengder" fordelt etter opprinnelsesland og trosbekjennelse, og merkelig nok også sindsvage døvstumme og blinde. Merk at idioter ikke er medregnet de sindssvage)

Dersom en trengte ferskere data måtte man sende en forespørsler per telefon eller post til aktuell insttutisjon - og vente på svar gjennom posten. Mye av datainnhentingen blant akademikere skjedde gjennom nettverksbygging og brevkorrespondanse.

---
<!--- slide template="[[tpl-diagram]]" -->
<!-- slide bg="white" -->
![[Eurostat_Newlogo.png]]
![[Statistics_Norway_logo.svg.png]]

note: 
I dag skjer datalagring og distrubisjon digitalt, og man har tilgang på data av høy kvalitet fra feks ssb eller eurostat ved å bla seg gjennom nettsidene deres og laste de ned i et passende format.

Det vil ikke si at det nødvendigvis er lett å samle inn og distribuere data av høy kvalitet til store mengder med brukere - ssb hadde i 2023-2024 en utgiftsramme på 988 millioner kroner. Datakvalitet og distribusjonslogistikken her er fortsatt kostbar

Terskelen er derimot veldig liten for å publisere data - vi trenger ikke lenger distribuere de rundt på biblioteker og universiteter i trykte medier, dersom man vil kan man bare dumpe dataen man ønsker å gjøre tilgjengelig ut på feks github uten å nøle særlig


---
# Et vell av data

note:
Det gjør at på det ganske internett finner vi data som er tilgjengelig gratis, og som vi må betale for tilgang til. Vi finner data av høy kvalitet som har vært kostbart å sammenstille, og data som er mer «rå» og gjort tilgjenglig fordi det i tilsvarer noen særlig kostnad.

Og det som i hvert fall er sikkert er at det en veldig mengde som er tilgjengelig for oss.

For å illustrere har jeg letet litt etter noen rare eksempler:

---
![[githubvanityplates.png]]


note:
På github fant jeg data over personlige bilskilt som er blitt flagget for gjennomgang av en saksbehandler på biltilsynet i California (DMV). Den inneholder skiltsøknad, hvorfor den er blitt flagget, søkerens forklaring på bilskiltet, saksbehandlers notat, og om skiltet er godkjent


---

![[plates-trump.png | 300]]

Søkers forklaring: «Funky trumpet in the funk music genre»


![[huf4rtd.png | 300]]


Søkers forklaring: «Have Unwaivering faith (4) Respect the Day

note:
Her finner vi blant annet FUKTRMP - som visstnok skulle være "funky trumpet in the funk music genre". Eller HUF4RTD som en skjønner må bety Have unwaivering faith (4) Respect the day.
Artig å forestille seg en byråkrat på biltilsynet sitte å vurdere luringer som prøver å få gjennom vulgære bilskilt

---

![[Pasted image 20250610131848.png ]]

note:
For de som vil dra på campingtur og ikke er redd for edderkopper, er det mulig å finne data om offentlige toalett i Australia

---

![[aussie-toilet.png]]
![[aussie-toilet-columns.png]]

note:
Det ser omtrent slik ut.
Her har vi gps-koordinater på rett under 25,000 offentlige toalett med et litt komisk detaljnivå

---

![[dolthub-bad-words.png]]

note:
På dolthub fant jeg en database med stygge ord, typisk bruk ville være en form for sensur.
Her har vi ufinheter på de fleste språk  inkludert Klingon, jeg tror det var 3 datapunkter der, og vil du fornærme en franskmann, kan du kalle ham en balayette (toalettbørste)

---

#### sharkattackfile.net

![[haiangrep.png]]
+ Over 6000 registrerte haiangrep
+ Inkludert Odd Ingebretsen


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
I tillegg finner vi selvfølgelig masse annet særdeles seriøs data om boligprisindekser, vær, trafikk osv.

Det er tydelige forskjeller mellom dataene, og vi kan peke på noen viktige karakteristikker:
* Kildepålitelighet -- ssb, eurostat stoler vi på -- hva med en tilfeldig github-bruker som  legger ut data om bilskilt?
* Validitet og nøyaktighet - Måler dataene det de påstår og er de presise?
* Kompletthet - Hvor stor del av fenomen eller populasjon er fanget opp?
* Konsistens - Er format og definasjoner de samme over tid / på tvers av kilder?
* Granularitet - Hvor detaljert er dataene, toalettdataene hadde feks veldig høy granularitet? 
* Format og struktur - Hvilket format er dataene på? Stygge-ord-databasen var feks i SQL, som krever annen behandling enn et excelfil
* Tilgjengelighet: gratis , åpen, registreringsvasert, paywall, rate-limit, filstørrelse
* Aktualitet / tidsriktighet: Hvor raskt oppdateres dataene etter at virkeligheten endrer seg

---

#### Noe data er ferskvare

note:
I områder som finans, sport, trafikk og vær er det å ha ny data helt kritisk.

Som et eksempel kan vi vise til «Spread Network», som i2010 fullførte  en fiberlinje mellom Chicago og New Jersey, 1300km, til en kostnad på 300 millioner dollar. Dette for å være 14 millisekund foran på handler mellom Carteret New Jersey, hvor man kan finne datasenteret til nasdaq, og Chicago Mercentile Exchange. I High-frequency trading snakker vi altså om millisekunder

Et annet eksempel er situasjonsrapportering og beredskap:
Tenk smittetall under covid, eller ekstremvær - Myndigheter og medier må handle raskt på tidsriktig data

---
### Programmatisk innhenting av data


note:
Når vi krøver høy aktualitet av dataene våres - blir det fort plagsomt, ineffektivt og dyrt å ha mennesker til å klikke seg seg gjennom nettsider for å manuelt laste ned nye csv-filer

Vi trenger automatiske prosesser til å gjøre dette - vi kan for eksempel skrive python-kode som gjør dette for oss. 

Det er flere grunner til at programmatisk innhenting er ønskelig. Feks om du skal hente inn og slå sammen data for mange variabler, område eller tidspunkter. Kanskje vil du "laste ned" og sammenligne strømpriser fra mange ulike regioner eller tidspunkt, eller laste ned data for 50 ulike kommuner.

For å kunne bruke feks python til å hente inn data for oss, må dataprogrammet vårt kommunisere og sende en forespørsel til en eller annen ressurs (også en datamaskin) et eller annet sted ute på internett, og da trenger vi å kunne litt om hvordan datanettverk fungerer

---

<!-- slide template="[[tpl-fitdiagram2]]" -->
![[communication-troubles.webp]]

::: credit
Illustrasjon generert av DALL-E
:::

note: 
Det er veldig mange tekniske problemer som trenger løsninger når to datamaskiner som kanskje er på forskjellige kontinent skal kommunisere og kanskje gjøre komplekse samhandlinger

* Meldingen må skrives på et format som mottaker forstår og som de er enige om
* Det må opprettes kontakt mellom datamaskinene slik at begge parter vet at nå skal vi kommunisere
* Meldingen må typisk deles opp i mange mindre pakker, og vi må ha system på disse og at alle kommer fram
* Alle pakkene må så på en eller annen måte finne frem til riktig sted over internett
* Og i begge ender må disse pakkene finne fram på et lokalt nettverk og gjøres om mellom fysisk strøm på en nettverkskabel og faktiske 0'ere og 1'ere

---


<!-- slide template="[[tpl-fitdiagram2]]" -->
##### OSI-modellen

![[osi.svg]]

::: credit
:::

note:
Vi bruker ofte og dele inn alle disse tekniske løsningene eller problemene inn i 7 lag i det som kalles OSI-modellen

Modellen representerer oppbyggingen av nettverkskommunikasjon, og hvert lag utfører en spesifikk oppgave

Det fysiske laget nederst består av fysiske kabler, radiosignaler og elektriske pulser. Her bestemmes det hvordan feks en nettverkskabel må lages for å kunne transportere elektriske signal. 

I datalink-laget skal data overføres over det lokale nettverket på jobben eller skolen, for eksempel mellom laptopen din og til den trådløse routeren

I nettverkslaget skal dataene finne veien gjennom internet, og vi må bestemme hvilken rute vi skal ta

Transportlaget finnes det rutiner for at transporten over internett skjer riktig ved å dele opp meldinger i mindre biter og sikre at alle bitene blir mottatt

I sesjonslaget holder man styr på forbindelsen og passer på at komponentene som skal kommunisere faktisk er «koblet sammen»

Presentasjonslaget sin rolle er i hovedsak å gjøre data leselig - det er blant annet her kryptering og dekryptering skjer

Det øverste laget kalles applikasjonslaget, og her vil det vi faktisk ser på skjermen gjøres om til et format som er tilpasset nettverket - Når du feks skriver en e-post i outlook eller gmail og tykker send, er det applikasjonlaget som må håndtere eposten din, pakke den sammen og pusse på den slik at den kan sendes over et nettverk

De ulike lagene har tydelig definerte roller i dataoverføring - men hvordan disse rollene faktisk utføres - altså hvordan lagene kommuniserer - styres av ulike protokoller

---

<!-- slide template="[[tpl-fitdiagram2]]" -->
### Protokoller i etikette

![[etikette.png]]

::: credit
:::

note:
Protokoller er alt som har å gjøre med høytidelige former, formaliteter, seremonielle forbindelser og etikette. Særlig da på kongehuset.

Vi snakker da om regler for sosial omgang, oppførsel, takt og tone, skikk og bruk.

Skal du, Knutsen og Ludvigsen på middag hos Kong Harald den 5. må du følge den kongelige protokoll:
* Kongen tiltales deres Majestet kongen, eller hans majestet kongen.
* Du skal bukke så dypt og lenge nok til å inspisere skopussen eller neie ved å føre høyre fot bak venstre, bøye knærne nok til at det begynner å svi i lårmuskelen og bøye hodet godt frem.
* Du tiltaler ikke de kongelige under middagspraten, det er de som tiltaler deg
* Når du skal forlate kongen, skal dette gjøres uten å snu ryggen til osv.


---
<!-- slide template="[[tpl-fitdiagram2]]" -->
<!-- slide bg="white" -->
#### Nettverksprotokoller

![[osi_prot.svg]]

::: credit
:::

note:
Datamaskiner må også meget nøye kjøreregler for sosial-omgang når de skal kommunisere. En protokoll i datanettverk er rett og slett et sett med regler og prosedyrer som bestemmer hvordan to enheter skal kommunisere så de forstår hverandre. Datakommunikasjon fungerer bare når begge følger samme protokoll, og internett består av mange protokoller som samarbeider - ofte én på hvert lag i OSI-modellen.

På figuren har jeg listet opp noen protokoller lagvis. De fleste P-ene i forkortelsene står for protokoll, og noen av de har dere kanskje hørt om, slik som IP-addresser (Internet protocol address). Det er en protokoll i nettverkslaget - og den beskriver hvordan vi kan identifisere ulike enheter på et nettverk. Hver enhet på nettverket får en unik IP-addresse som 192.168.0.2 og vi kan putte denne på en datapakke som addressen på et brev og sende den over nettverket. Hvilken vei den skal ta for å komme dit, og hvordan vi forsikrer oss om at den kommer fram, er det andre protokoller som står for

Det er to protokoller uthevet. Det vil si, JSON er egentlig et dataformat mer enn en protokoll, men vi kommer til å bruke den mye, og den passer greit inn i presentasjonslaget.

Den andre er **HTTP** - Hypertext Transfer Protocol - som er en applikasjonslagsprotokoll som brukes til å overføre data mellom en klient og en server - spesielt da for web.

Protokollen definerer hvordan en klient (f.eks. nettleseren din) kan forespørre ressurser (slik som HTML-sider, bilder eller JSON-data) fra en server, og hvordan serveren svarer.

Når vi vil skrive et dataprogram som skal hente inn data fra feks SSB, så er det denne protokollen vi må følge.

(Hva denne http-protokollen består av, og hvordan vi kan sende slike forespørsler programmatisk skal vi se på i neste video)

---

<!-- slide template="[[tpl-fitdiagram2]]" -->
### Avslutningsvis

![[Slides/slidefig/ssb-statistisk-aarbog-1881.png]]

::: credit
:::
note:

I bunn og grunn er datainnhenting ganske likt som i 1881. Biblioteket man kunne låne ut den statistiske årboken fra, er erstattet av nettsider med servere som lagrer dataen i litt andre formater - Og brevvekslingen med akademiske kolleger er erstattet med http-forespørsler til webtjenere som sender svar på forespørslen din umiddelbart

Den store forskjellen er mengden med data, og hvor lett og raskt den er tilgjengelig for oss