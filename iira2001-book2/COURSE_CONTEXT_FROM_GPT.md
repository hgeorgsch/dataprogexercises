
# Prosjektkontekst: Programmering og data i økonomiske fag

## 1. Om emnet

Dette prosjektet inneholder pensumbok, undervisningsressurser, demonstrasjoner, øvinger og fremdriftsplan for emnet:

* **Emnenavn:** Programmering og data i økonomiske fag
* **Emnekode:** IIRA2001
* **Institusjon:** NTNU
* **Forfattere/fagansvarlige:** Jonas Julius Harang og Hans Georg Schaatun
* **Programmeringsspråk:** Python
* **Arbeidsmiljø:** Jupyter Notebook/JupyterLab
* **Bokformat:** Jupyter Book 2 med MyST Markdown

Emnet er primært rettet mot førsteårsstudenter innen økonomi, markedsføring og beslektede fagområder. Studentene har svært ulik erfaring med programmering. Mange har aldri programmert før, og noen har begrenset selvtillit i matematikk og tekniske fag.

Dette er ikke et tradisjonelt informatikkemne. Studentene skal ikke utdannes til programvareutviklere. Programmering brukes som et praktisk verktøy for:

* økonomiske beregninger
* modellering
* simulering
* behandling av data
* analyse av statistikk
* visualisering
* utforsking av økonomiske og samfunnsfaglige problemstillinger
* arbeid med virkelige datakilder som SSB og Eurostat

Hovedmålet er at studentene skal bli i stand til å bruke Python selvstendig til å løse relevante problemer i økonomiske fag.

---

# 2. Overordnet pedagogisk idé

Programmering skal introduseres gjennom konkrete problemer som gir mening for økonomi- og markedsføringsstudenter.

Studentene skal helst møte et problem før de møter den generelle programmeringsteknikken som løser problemet.

Eksempler:

* Variabler introduseres gjennom priser, kostnader, inntekter og renter.
* Funksjoner introduseres gjennom beregninger som må utføres flere ganger.
* Løkker introduseres gjennom utvikling over tid, kundelister eller gjentatte simuleringer.
* Betingelser introduseres gjennom segmentering, beslutningsregler og klassifisering.
* Ordbøker introduseres gjennom produkter, kunder eller markedsføringsdata.
* `while`-løkker og tilfeldige tall introduseres gjennom simulering.
* pandas introduseres når vanlige lister og løkker blir upraktiske for tabulære data.
* gruppering introduseres gjennom sammenligning av regioner, kundegrupper, næringer eller tidsperioder.
* pivotering og MultiIndex introduseres når data har flere dimensjoner.
* API-er introduseres gjennom autentiske data fra SSB, Eurostat og andre åpne datakilder.

Kurset skal bygge forståelse gradvis. Nye kapitler må ikke forutsette programmeringsteknikker som ennå ikke er forklart.

Kode skal i starten være eksplisitt og lett å følge. Kortest mulig kode er ikke nødvendigvis best kode for nybegynnere.

---

# 3. Studentenes forutsetninger

Anta normalt at studentene:

* ikke har programmert tidligere
* ikke kjenner terminalen
* ikke kjenner filsystem, arbeidsmappe eller relative filbaner godt
* ikke kjenner virtuelle miljøer eller pakkehåndtering
* har noe grunnleggende matematikk, men varierende matematisk trygghet
* kjenner økonomiske begreper bedre enn programmeringsbegreper
* lærer best når kode knyttes til et tydelig anvendt problem
* trenger mange små eksempler og anledning til å endre kode selv

Unngå derfor å gjøre installasjon, terminalbruk, Git eller miljøhåndtering til en stor del av undervisningen.

Studentene bør samtidig lære grunnleggende kontroll over egne filer:

* vite hvor notebooken ligger
* opprette en mappe for en oppgave
* lagre notebook og datafil i en fornuftig struktur
* bruke relative filbaner
* forstå forskjellen mellom en notebook, en Python-fil og en datafil
* kunne finne igjen og levere egne filer

En mulig lokal studentløsning er JupyterLab Desktop eller en tilsvarende enkel installasjon. Tidligere har Anaconda vært brukt, men det oppleves som tungvint. Undervisningsmateriellet bør ikke forutsette omfattende terminalarbeid.

---

# 4. Hva studentene skal kunne

Ved slutten av emnet bør studentene kunne:

## Grunnleggende programmering

* bruke variabler til å lagre tall, tekst og andre verdier
* utføre økonomiske beregninger med Python
* forstå enkle datatyper
* skrive og bruke funksjoner
* bruke parametere og returverdier
* arbeide med lister
* bruke `for`-løkker
* bruke `while`-løkker
* bruke boolske uttrykk
* bruke `if`, `elif` og `else`
* kombinere løkker og betingelser
* bruke ordbøker
* bruke enkle list comprehensions når vanlige løkker allerede er forstått
* generere tilfeldige tall
* gjennomføre enkle simuleringer
* lese data fra CSV-filer
* lage enkle diagrammer

## Dataanalyse med pandas

* opprette og forstå `Series` og `DataFrame`
* lese data fra CSV og andre relevante formater
* inspisere datasett
* velge rader og kolonner
* bruke `.loc`, `.iloc` og `.at`
* filtrere med boolske uttrykk
* bruke `.query()`
* opprette og endre kolonner
* gi nytt navn til kolonner
* håndtere manglende verdier
* håndtere duplikater
* endre datatyper med `.astype()`
* bruke mapping
* sortere data
* bruke `.value_counts()`
* gruppere data med `.groupby()`
* aggregere data
* hente de første eller viktigste observasjonene i hver gruppe
* slå sammen datasett
* omforme data mellom langt og bredt format
* bruke `.melt()`
* bruke `.pivot()` og `.pivot_table()`
* forstå og bruke MultiIndex
* sortere og slå opp i en MultiIndex
* bruke `.xs()` og `IndexSlice` når dette er hensiktsmessig
* arbeide med datoer og perioder
* bruke `PeriodIndex`
* tolke formater som kvartal, måned og år
* bruke rullerende beregninger
* bruke resampling
* aggregere kvartalsdata til årsdata
* visualisere data med pandas og relevante plottingbiblioteker

## Data fra eksterne kilder

* forstå prinsippet bak HTTP GET og POST på et grunnleggende nivå
* hente data fra åpne API-er
* lese API-dokumentasjon
* sende spørringer til SSBs API
* hente data fra Eurostats Statistics API
* forstå hovedstrukturen i JSON-stat
* gjøre API-data om til en pandas-DataFrame
* filtrere og analysere data fra offentlige statistikkilder
* bruke autentiske data til å formulere og undersøke en problemstilling

## Selvstendig analyse

* formulere en avgrenset økonomisk eller samfunnsfaglig problemstilling
* finne relevante data
* dokumentere datakilden
* rydde og strukturere data
* utforske data
* lage relevante figurer
* beskrive hva resultatene viser
* skille mellom resultat, tolkning og spekulasjon
* bruke egne analyser som grunnlag for konklusjoner
* være tydelig på begrensninger ved data og metode

---

# 5. Pensum: grunnleggende Python

## 5.1 Introduksjon til Jupyter og Python

Studentene må først lære:

* hva en notebook er
* forskjellen mellom tekstceller og kodeceller
* hvordan en celle kjøres
* at rekkefølgen cellene kjøres i har betydning
* hvordan en kernel kan restartes
* hvordan notebooken lagres
* hvor filer lagres
* hvordan feil vises
* hvordan man leser en enkel feilmelding

Det bør understrekes at en notebook skal kunne kjøres ovenfra og ned.

Eksemplene bør starte svært enkelt:

```python
pris = 50
antall = 4
kostnad = pris * antall

kostnad
```

## 5.2 Variabler, uttrykk og datatyper

Temaer:

* variabelnavn
* tilordning
* heltall
* desimaltall
* tekst
* boolske verdier
* regneoperatorer
* operatorrekkefølge
* enkel typekonvertering
* utskrift med `print`
* f-strenger

Økonomiske eksempler:

* pris ganger antall
* inntekt minus kostnad
* dekningsbidrag
* prosentvis endring
* merverdiavgift
* valutaberegninger
* enkel rente
* kjøpekraft
* kostnad per kunde
* gjennomsnittspris

## 5.3 Funksjoner

Temaer:

* hvorfor funksjoner brukes
* definisjon med `def`
* parametere
* returverdi
* forskjellen mellom å skrive ut og returnere
* lokale variabler
* flere parametere
* standardverdier der det er naturlig
* dokumentasjon med enkle docstrings

Aktuelle oppgaver:

* funksjon som beregner rabatt
* funksjon som beregner pris inklusive avgift
* sparekalkulator
* lånekalkulator
* annuitet eller enkel låneutvikling
* funksjon for prosentvis vekst
* funksjon som klassifiserer en kunde
* funksjon som beregner fortjeneste

Unngå avanserte funksjonskonsepter som dekoratører, generatorer og komplisert argumenthåndtering.

## 5.4 Lister

Temaer:

* opprette lister
* indeks
* negative indekser
* slicing
* endre elementer
* `append`
* `len`
* `sum`
* `min`
* `max`
* eventuelt enkel bruk av `sorted`

Økonomiske anvendelser:

* priser for flere produkter
* salg per måned
* avkastning over flere perioder
* kundeverdier
* inntekter og kostnader
* observasjoner fra en spørreundersøkelse

## 5.5 For-løkker

Temaer:

* iterasjon over en liste
* `range`
* akkumulator
* tellevariabel
* bygge opp en ny liste
* kombinere løkke og funksjon
* løkker over flere tidsperioder

Aktuelle modeller:

* utvikling av sparebeløp
* utvikling av gjeld
* økonomisk vekst over tid
* logistisk vekst
* prisutvikling
* salg over flere måneder
* beregning for en liste med kunder
* gjentatte produksjonsperioder

Studentene bør først skrive eksplisitte løkker før de møter comprehensions eller vektorisering.

## 5.6 Boolske uttrykk og kontrollflyt

Temaer:

* sammenligningsoperatorer
* `and`
* `or`
* `not`
* `if`
* `elif`
* `else`
* betingelser inne i løkker
* sammensatte beslutningsregler

Aktuelle anvendelser:

* kundesegmentering
* klassifisering som fattig, gjennomsnittlig eller rik
* kreditt- eller risikovurdering i en forenklet modell
* rabattregler
* bonusordninger
* lagerbestilling
* valg mellom sparealternativer
* kontroll av om et budsjett går i overskudd
* klassifisering av økonomisk utvikling

Modellene må presenteres som pedagogiske og forenklede modeller, ikke som realistiske automatiske beslutningssystemer.

## 5.7 Ordbøker

Temaer:

* nøkkel og verdi
* opprette ordbøker
* slå opp verdier
* legge til eller endre verdier
* iterere over nøkler og verdier
* ordbøker som enkel representasjon av en observasjon

Markedsføringseksempler:

```python
kunde = {
    "alder": 34,
    "inntekt": 520000,
    "segment": "familie",
    "har_kjøpt": True
}
```

Andre eksempler:

* produktinformasjon
* kampanjer
* butikker
* regioner
* priser
* kundedata
* salgskanaler

Ordbøker kan senere brukes som overgang til tabulære data og pandas.

## 5.8 Comprehensions

List comprehensions bør først introduseres etter at studentene behersker vanlige løkker.

Studentene bør forstå at:

```python
nye_priser = []

for pris in priser:
    nye_priser.append(pris * 1.05)
```

kan skrives som:

```python
nye_priser = [pris * 1.05 for pris in priser]
```

Comprehensions skal ikke brukes ukritisk. Lesbar kode er viktigere enn kompakt kode.

## 5.9 While-løkker og tilfeldige tall

Temaer:

* `while`
* stoppbetingelse
* tellere
* fare for uendelige løkker
* tilfeldige tall
* reproduksjon med seed
* gjentatte forsøk
* enkel Monte Carlo-simulering

Aktuelle oppgaver:

* simulere kundeatferd
* simulere hvor mange kunder som kjøper et produkt
* simulere tid til et sparemål nås
* simulere etterspørsel
* simulere økonomisk utvikling med tilfeldige sjokk
* repetere en prosess frem til en betingelse er oppfylt
* undersøke gjennomsnittlig resultat over mange simuleringer

## 5.10 CSV-filer og enkel plotting

Temaer:

* hva en CSV-fil er
* kolonner og rader
* skilletegn
* overskrifter
* filbaner
* relative filbaner
* enkel lesing
* konvertering fra tekst til tall
* enkel visualisering

Studentene bør tidlig få oppleve at Python kan brukes på data som finnes utenfor notebooken.

---

# 6. Økonomiske modeller og programmeringsoppgaver

Faget bruker flere konkrete modeller og simuleringsoppgaver.

## Sparekalkulator

Kan brukes til å lære:

* variabler
* funksjoner
* løkker
* rente
* vekst over tid
* plotting

Mulige varianter:

* startbeløp
* fast månedlig eller årlig sparing
* rente
* antall perioder
* sammenligning av sparealternativer
* tidspunktet et sparemål nås

## Lånekalkulator

Kan brukes til:

* funksjoner
* løkker
* tabeller
* rente og avdrag
* utvikling over tid
* scenarioanalyse

Modellen bør først være enkel og pedagogisk. Mer realistiske detaljer kan legges til senere.

## Logistisk vekst

Kan brukes som et alternativ til ren eksponentiell vekst.

Aktuelle tolkninger:

* markedsmetning
* produktadopsjon
* kundevekst
* spredning av en tjeneste
* begrenset økonomisk vekst

Studentene kan sammenligne logistisk og eksponentiell vekst.

## Banksegmentering

Et syntetisk datasett med omtrent 2000 bankkunder kan brukes til:

* inntektsfordeling
* segmentering
* klassifisering
* sortering
* gruppering
* visualisering
* beregning eller illustrasjon av Gini-koeffisient
* drøfting av hvordan grenser mellom kundegrupper påvirker resultatene

En enkel tidlig oppgave kan klassifisere kundene som for eksempel lavinntekt, gjennomsnittlig inntekt eller høyinntekt. Senere kan samme datasett analyseres med pandas.

## Incentivert sparing

En modell kan undersøke hvordan bonus, støtte eller andre insentiver påvirker sparing.

Dette kan brukes til:

* funksjoner
* betingelser
* løkker
* scenarioanalyse
* visualisering
* diskusjon av modellforutsetninger

## Phillipskurven

En forenklet simulering kan brukes til å undersøke sammenhengen mellom inflasjon og arbeidsledighet.

Oppgaven skal brukes til programmering og modellforståelse, ikke til å fremstille Phillipskurven som en universell eller stabil økonomisk lov.

Aktuelle programmeringselementer:

* funksjoner
* parametere
* tilfeldige sjokk
* tidsserier
* plotting
* sammenligning av scenarioer

## Rekeoligopol

Et spill eller en simulering med produsenter i et rekemarked kan brukes til:

* strategiske valg
* tilbud
* pris
* inntekt
* kostnad
* profitt
* løkker
* funksjoner
* samspill mellom aktører

Oppgaven kan la studentene endre produksjonsmengder og observere hvordan markedet påvirkes.

## Frikonkurranse med sjokk

En forenklet markedsmodell kan inneholde:

* tilbud
* etterspørsel
* markedslikevekt
* pris
* mengde
* tilfeldige eller forhåndsbestemte sjokk
* endringer i tilbud eller etterspørsel
* sammenligning av scenarioer

Modellen kan utvikles fra en enkel beregning til en simulering over tid.

## Monte Carlo-modell for kundeatferd

Eksempler på tilfeldige hendelser:

* kunden ser en kampanje
* kunden klikker
* kunden kjøper
* kunden kommer tilbake
* kunden avslutter et abonnement
* kunden anbefaler produktet

Studentene kan undersøke:

* forventet antall kjøp
* variasjon mellom simuleringer
* effekten av endrede sannsynligheter
* forskjellen mellom én simulering og mange simuleringer

---

# 7. Pensum: pandas og dataanalyse

Pandas-delen skal ikke bare være en katalog over metoder. Hvert tema bør introduseres gjennom et konkret behov.

## 7.1 Series og DataFrame

Temaer:

* hva tabulære data er
* rader og kolonner
* observasjoner og variabler
* opprette `Series`
* opprette `DataFrame`
* DataFrame fra ordbøker
* lese CSV
* indeks
* kolonnenavn
* `head`
* `tail`
* `shape`
* `columns`
* `index`
* `dtypes`
* `info`
* `describe`

Studentene bør lære å undersøke data før de begynner å analysere dem.

## 7.2 Oppslag og utvalg

Temaer:

* velge én kolonne
* velge flere kolonner
* `.loc`
* `.iloc`
* `.at`
* radetiketter mot radnummer
* slicing
* boolsk indeksering
* filtrering
* `.query()`

Studentene må forstå forskjellen mellom:

```python
df["inntekt"] > 500000
```

og:

```python
df[df["inntekt"] > 500000]
```

De må også forstå når `.loc` brukes til å velge både rader og kolonner.

## 7.3 Manipulering og nye variabler

Temaer:

* opprette en ny kolonne
* beregne kolonner fra eksisterende kolonner
* bruke funksjoner på data
* mapping
* kategorisering
* endre verdier
* prosentvis endring
* rangering
* enhetskonvertering

Eksempler:

* inntekt per person
* kostnad per enhet
* profitt
* markedsandel
* realverdi
* vekstrate
* aldersgruppe
* kundesegment

## 7.4 Datarensing

Temaer:

* meningsfulle kolonnenavn
* `.rename()`
* manglende verdier
* `.isna()`
* `.dropna()`
* `.fillna()`
* duplikater
* `.duplicated()`
* `.drop_duplicates()`
* feil datatype
* `.astype()`
* sortering
* `.sort_values()`
* `.sort_index()`
* reindeksering
* mapping av koder til lesbare navn

Rensing må alltid knyttes til en forklaring av hvorfor operasjonen er faglig rimelig. Studentene skal ikke lære å slette observasjoner automatisk bare fordi de inneholder manglende verdier.

## 7.5 Gruppering og aggregering

Temaer:

* `.groupby()`
* én grupperingsvariabel
* flere grupperingsvariabler
* gjennomsnitt
* median
* sum
* antall
* minimum
* maksimum
* flere aggregater
* navngitte aggregater
* `.value_counts()`
* hente første rad eller de største observasjonene i hver gruppe

Aktuelle problemstillinger:

* gjennomsnittsinntekt per region
* salg per produktkategori
* kjøp per kundegruppe
* arbeidsledighet per fylke
* energibruk per næring
* befolkningsutvikling per kommune
* markedsandel per virksomhet og år

Studentene må forstå forskjellen mellom å filtrere data, gruppere data og aggregere data.

## 7.6 Langt og bredt dataformat

Temaer:

* hva langt format er
* hva bredt format er
* når hvert format er nyttig
* `.melt()`
* `.pivot()`
* `.pivot_table()`

Bruk gjerne samme datasett i begge formater, slik at studentene ser at dataene kan representere det samme selv om tabellstrukturen er ulik.

Eksempler:

* år som kolonner
* regioner som kolonner
* ulike statistikkmål i separate kolonner
* resultat fra spørreundersøkelser
* data fra SSB eller Eurostat

## 7.7 Sammenslåing av datasett

Temaer:

* hvorfor data ligger i flere tabeller
* nøkkelvariabler
* `.merge()`
* `left`, `inner` og eventuelt andre join-typer
* én-til-én
* mange-til-én
* dupliserte nøkler
* kontroll av resultatet etter sammenslåing

Eksempler:

* koble kommuneinformasjon til statistikk
* koble kundeinformasjon til transaksjoner
* koble produkter til salg
* koble regionkoder til regionnavn
* koble prisindeks til nominelle verdier

## 7.8 MultiIndex

Temaer:

* hierarkisk indeks
* flere dimensjoner i rader
* flere nivåer i kolonner
* opprette MultiIndex gjennom gruppering eller pivotering
* `.sort_index()`
* oppslag i MultiIndex
* `.xs()`
* `IndexSlice`
* flytte indeksnivåer tilbake til kolonner med `.reset_index()`

MultiIndex skal introduseres gjennom et reelt behov, for eksempel data som varierer etter både region, år og statistikkvariabel.

Det må forklares at MultiIndex er nyttig, men at det av og til er enklere å bruke vanlige kolonner og langt format.

## 7.9 Perioder og datoer

Temaer:

* datoer som tekst
* konvertering til datetime
* forskjellen mellom tidspunkt og periode
* `Period`
* `PeriodIndex`
* år
* kvartal
* måned
* sortering av tidsdata
* tidsintervaller
* forskyvning
* prosentvis endring
* rullerende vindu
* resampling

Aktuelle formater kan være:

* `1980Q4`
* `1972K4`
* `1980M01`

Studentene skal lære å konvertere slike verdier til perioder når det er nødvendig.

Aktuelle operasjoner:

* treperioders rullerende gjennomsnitt
* kvartalsdata aggregert til år
* månedsdata aggregert til kvartal
* sammenligning med forrige periode
* utvikling over tid

## 7.10 Visualisering

Grunnleggende visualisering kan gjøres med:

* `Series.plot()`
* `DataFrame.plot()`
* matplotlib
* eventuelt seaborn når det gir en pedagogisk fordel

Aktuelle diagramtyper:

* linjediagram
* stolpediagram
* histogram
* spredningsdiagram
* flere grupper i samme figur

Senere kan det brukes funksjoner som:

* `seaborn.lineplot`
* `seaborn.lmplot`
* konfidensintervall eller error bars

Visualisering skal alltid knyttes til en faglig problemstilling. Studentene bør lære å:

* velge en rimelig diagramtype
* gi aksene navn
* bruke en beskrivende tittel
* kontrollere enheter
* unngå misvisende akser
* forklare hva figuren viser
* ikke overtolke små forskjeller eller visuell støy

---

# 8. SSB, Eurostat og åpne data

Arbeid med autentiske data er en sentral del av emnet.

## SSB

Studentene bør lære:

* å finne en relevant statistikkbanktabell
* å forstå tabellens dimensjoner
* å velge variabler og verdier
* å hente data gjennom API-et
* å forstå at en API-spørring må angi ønsket utvalg
* å behandle resultatet med pandas
* å dokumentere tabellnummer og datakilde

Data kan blant annet handle om:

* befolkning
* inntekt
* arbeidsledighet
* priser
* konsum
* utdanning
* næringer
* kommuner og fylker
* bolig
* energi
* demografi
* personlig økonomi

## Eurostat

Eurostats Statistics API kan brukes i stedet for å gjøre SDMX til en sentral del av introduksjonen.

Studentene kan lære:

* at dimensjoner filtreres med verdier
* at flere dimensjoner kombineres
* at én dimensjon kan ha flere valgte verdier
* at utelatte dimensjoner kan bety at flere eller alle verdier returneres
* filtrering på tidsperiode
* geografisk filtrering
* hvordan resultatet konverteres til tabulære data

## JSON-stat

Studentene trenger ikke kunne hele JSON-stat-spesifikasjonen, men bør kjenne hovedideen:

* datasettet har dimensjoner
* dimensjonene har kategorier
* `id` angir rekkefølgen på dimensjonene
* `size` angir størrelsen til hver dimensjon
* `dimension` beskriver dimensjonene
* `value` inneholder observasjonene
* verdiene må kobles til riktig kombinasjon av dimensjoner

En pedagogisk visualisering av hvordan en flerdimensjonal tabell blir til en flat liste med verdier er nyttig.

## Andre API-demonstrasjoner

Open-Meteo eller andre enkle åpne API-er kan brukes til å demonstrere:

* URL
* endepunkt
* parametere
* GET
* JSON
* statuskode
* `requests`
* konvertering til Python-objekter
* DataFrame

En enkel demonstrasjon av HTTP GET og POST kan inngå, men nettverksteknikk er ikke et hovedtema i faget.

---

# 9. Utforskingsoppgave og eksamensmappe

En sentral del av emnet er at studentene gjennomfører en selvvalgt utforskingsoppgave basert på data, typisk fra SSB eller Eurostat.

Dette er ikke bare en teknisk programmeringsoppgave. Studentene skal bruke programmering og dataanalyse til å undersøke en økonomisk eller samfunnsfaglig problemstilling.

## Oppgaven bør inneholde

1. En tydelig problemstilling.
2. Begrunnelse for hvorfor problemstillingen er interessant.
3. Presentasjon av datakilden.
4. Beskrivelse av relevante variabler.
5. Henting eller innlesing av data.
6. Rensing og strukturering.
7. Utforskende analyse.
8. Relevante tabeller og figurer.
9. Eventuelt hypotesetesting når dette er faglig og metodisk passende.
10. Tolkning av resultatene.
11. Diskusjon av begrensninger.
12. En konklusjon som faktisk bygger på analysen.

Studentene skal ikke bare kjøre kode. De må forklare:

* hvorfor dataene er relevante
* hva de har gjort
* hvorfor de har valgt analysen
* hva resultatene viser
* hva resultatene ikke kan fortelle
* hvilke antakelser analysen bygger på

## Typiske svakheter som undervisningen bør forebygge

* teksten beskriver et annet datasett enn koden faktisk bruker
* problemstillingen er for bred
* studenten viser figurer uten å forklare dem
* konklusjonen bygger ikke på resultatene
* grove antakelser presenteres som fakta
* tidsperioder, geografiske områder eller enheter blandes
* studenten bruker mange metoder uten å forstå hvorfor
* store deler av notebooken består av ubrukt kode
* datarensing gjennomføres uten begrunnelse
* korrelasjon omtales som årsak
* studenten refererer til «dataene» uten å forklare hvilke data

Oppgaven bør utvikles gradvis gjennom kurset. Studentene bør få arbeide med:

* valg av tema
* avgrensning av problemstilling
* datakilde
* første datainnhenting
* første figur
* foreløpig analyse
* tilbakemelding
* revisjon
* ferdig innlevering

---

# 10. Øvinger og vurdering

Emnet kan bruke en kombinasjon av:

* korte kontrolloppgaver
* CodeRunner-oppgaver
* Jupyter-notebooks
* større øvingsoppgaver
* demonstrasjoner
* refleksjonsoppgaver
* utforskingsoppgave
* eksamensmappe

## CodeRunner

CodeRunner-oppgaver bør:

* teste ett eller noen få læringsmål om gangen
* bruke økonomiske eller praktiske kontekster
* ha tydelig beskrivelse av input og forventet resultat
* være mulig å løse med teknikkene studentene har lært
* unngå skjulte krav om eksakt utskriftsformat med mindre formatet er læringsmålet
* gi informative tilbakemeldinger
* teste viktige kanttilfeller
* skille mellom syntaksfeil, logiske feil og feil resultat når det er mulig

Oppgavene kan organiseres i kategorier som:

* grunnleggende Python
* variabler og uttrykk
* funksjoner
* kontrollflyt
* lister og løkker
* ordbøker
* filer
* simulering
* pandas
* anvendte økonomiske oppgaver
* SSB og Eurostat
* utfordringsoppgaver

## Progresjon i oppgaver

Et tema kan gjerne ha følgende oppbygging:

1. Følg et ferdig eksempel.
2. Endre én verdi eller parameter.
3. Fyll inn en manglende kodelinje.
4. Skriv en liten del av løsningen.
5. Skriv hele løsningen.
6. Bruk teknikken i en ny økonomisk kontekst.
7. Forklar resultatet med egne ord.

---

# 11. Foreslått logisk progresjon i boka

Dette er en faglig progresjon, ikke nødvendigvis en fast ukeplan.

## Del I – Programmering

1. Introduksjon til Python og Jupyter
2. Variabler og beregninger
3. Funksjoner
4. Lister
5. For-løkker
6. Boolske uttrykk og kontrollflyt
7. Ordbøker
8. Comprehensions
9. While-løkker og tilfeldige tall
10. Simulering
11. CSV-filer
12. Grunnleggende visualisering

## Del II – Dataanalyse med pandas

1. Series og DataFrame
2. Lese og inspisere data
3. Velge rader og kolonner
4. Filtrering med boolske uttrykk og `.query()`
5. Opprette og endre variabler
6. Datarensing
7. Gruppering og aggregering
8. Sammenslåing av datasett
9. Langt og bredt format
10. Pivotering
11. MultiIndex
12. Datoer og perioder
13. Rullerende beregninger og resampling
14. Visualisering
15. SSB, Eurostat og API-er
16. Selvstendig dataanalyse

## Del III – Oppgaver

Oppgavene kan organiseres etter tema eller vanskelighetsgrad:

* grunnoppgaver
* anvendte oppgaver
* økonomiske modeller
* dataanalyseoppgaver
* API-oppgaver
* prosjektforberedende oppgaver
* utfordringsoppgaver

## Del IV – Demonstrasjoner

Notebook-demonstrasjoner kan samle større eksempler som:

* sparemodell
* lånemodell
* logistisk vekst
* bankkunder
* Phillipskurve
* rekeoligopol
* marked med sjokk
* Monte Carlo-simulering
* SSB-data
* Eurostat-data
* pandas-demonstrasjon
* tidsserieanalyse
* lang- og bredformat

---

# 12. Standard for kapitler

Et godt kapittel bør normalt inneholde:

## Innledning

Forklar hvilket problem eller behov kapitlet handler om.

## Læringsmål

Bruk noen få konkrete læringsmål, for eksempel:

> Etter dette kapitlet skal du kunne bruke en `for`-løkke til å beregne økonomisk utvikling over flere perioder.

## Første eksempel

Start med et lite, forståelig eksempel.

## Forklaring

Forklar koden linje for linje når konseptet er nytt.

## Økonomisk anvendelse

Vis hvordan konseptet brukes i en relevant situasjon.

## Vanlige feil

Vis typiske feil studentene faktisk kan gjøre.

## Kontrollspørsmål

Still korte spørsmål som krever at studenten forutsier eller forklarer kode.

## Små oppgaver

La studentene endre eller fullføre kode.

## Større oppgave

Avslutt gjerne med en mer selvstendig anvendelse.

## Oppsummering

Oppsummer de viktigste ideene uten å introdusere nye konsepter.

---

# 13. Kodestil i undervisningsmateriellet

Kode skal være:

* korrekt
* kjørbar
* lesbar
* konsistent
* tilpasset nybegynnere
* fri for unødvendig avanserte konstruksjoner

Bruk beskrivende variabelnavn:

```python
årlig_rente = 0.04
startbeløp = 10_000
antall_år = 10
```

eller engelske navn dersom resten av prosjektet bruker det konsekvent.

Ikke bland språk tilfeldig i samme eksempel.

Unngå navn som:

```python
x = 0.04
a = 10000
n = 10
```

når variablenes økonomiske betydning er viktig.

## Andre regler

* Bruk normalt én idé per kodecelle.
* Ikke skjul viktige steg i lange metodekjeder.
* Del kompliserte operasjoner i flere linjer.
* Bruk parenteser slik at uttrykk er lette å lese.
* Bruk seed i tilfeldige demonstrasjoner når resultatet skal være reproducerbart.
* Unngå globale tilstander når det ikke er nødvendig.
* Ikke introduser klasser og objektorientering uten et klart behov.
* Unngå lambdafunksjoner tidlig i kurset.
* Unngå kompliserte comprehensions.
* Ikke bruk NumPy eller pandas som en magisk snarvei før studentene har forstått problemet.
* Ikke optimaliser kode for ytelse når tydelighet er viktigere.
* Sørg for at notebooker kan kjøres fra første til siste celle.

---

# 14. Notebook-standard

Alle notebooker bør:

* ha en tydelig tittel
* ha en kort introduksjon
* oppgi læringsmål
* bruke ryddige overskrifter
* ha kodeceller i riktig rekkefølge
* unngå avhengighet av gamle kernelverdier
* bruke relative filbaner
* oppgi datakilde
* forklare figurer og resultater
* avslutte med en kort oppsummering eller oppgave

Notebooken bør testes med restart av kernel og kjøring av alle celler.

Unngå:

* skjulte variabler fra tidligere kjøringer
* absolutte filbaner fra utviklerens maskin
* kode som bare fungerer fra én bestemt arbeidsmappe uten forklaring
* svært store utskrifter
* tilfeldige resultater som endres ved hver bygging
* nettverkskall som gjør hele bokbyggingen ustabil

For API-demonstrasjoner kan det være nødvendig med en lagret lokal datafil eller en robust fallback når boka bygges.

---

# 15. Jupyter Book- og MyST-prosjektet

Prosjektet bruker Jupyter Book 2/MyST, med en struktur basert på blant annet:

* `myst.yml`
* en innholdsfortegnelse definert i prosjektkonfigurasjonen
* MyST Markdown-filer
* Jupyter-notebooks
* boktema
* NTNU-logo eller annen emneprofilering

Nåværende bokstruktur har blant annet hatt deler som:

* Part I – Programming

  * variables
  * functions
  * loops
* Part II – Pandas

  * dataframes
  * groupby
  * pandas-demo

Denne strukturen skal bygges videre ut og gjøres mer komplett.

## Regler ved arbeid med bokprosjektet

* Bruk syntaks for Jupyter Book 2 og gjeldende MyST-versjon.
* Ikke bland inn gamle Jupyter Book 1-løsninger med `_config.yml` og `_toc.yml` med mindre prosjektet faktisk bruker dem.
* Bevar korrekt YAML-innrykk.
* Kontroller at det ikke opprettes flere konkurrerende `toc`-nøkler.
* Kontroller at alle filer i innholdsfortegnelsen finnes.
* Ikke flytt eller gi nytt navn til filer uten å oppdatere alle referanser.
* Bevar eksisterende lenker og kryssreferanser.
* Følg eksisterende navnekonvensjoner.
* Bygg boka etter strukturelle endringer.
* Bruk streng bygging når prosjektet støtter det.

Aktuell kontrollkommando kan være:

```bash
uv run jupyter book build --html --strict
```

Codex skal først undersøke prosjektets faktiske konfigurasjon og eksisterende kommandoer før det endrer byggesystemet.

---

# 16. Canvas og publisering

Canvas brukes til organisering og publisering av kurset.

En hensiktsmessig struktur er:

* én generell modul for praktisk informasjon
* én modul for eksamen og vurdering
* én fremdriftsplan eller ukesoversikt
* moduler per uke eller tema
* konkrete filer, sider, oppgaver og lenker i ukesmodulene

Boka og Canvas skal ha ulike roller:

## Boka

Boka inneholder:

* sammenhengende pensum
* forklaringer
* eksempler
* demonstrasjoner
* referansestoff
* oppgaver som naturlig hører til teksten

## Canvas

Canvas inneholder:

* fremdriftsplan
* hva studentene skal gjøre den aktuelle uka
* praktisk informasjon
* frister
* lenker til relevante bokkapitler
* notebooker og datafiler
* innleveringer
* CodeRunner-oppgaver
* eksamensinformasjon

Det bør unngås å kopiere store mengder pensumtekst inn i Canvas. Canvas bør lede studentene til riktig innhold.

---

# 17. Føringer for Codex

Når du som Codex arbeider med dette prosjektet, skal du:

1. Undersøke eksisterende filer og stil før du gjør endringer.
2. Bevare den pedagogiske progresjonen.
3. Ikke bruke programmeringskonsepter før de er introdusert.
4. Skrive for økonomi- og markedsføringsstudenter, ikke informatikkstudenter.
5. Bruke økonomiske eller samfunnsfaglige eksempler når det er naturlig.
6. Prioritere lesbar kode fremfor kort kode.
7. Sørge for at kodeeksempler faktisk kan kjøres.
8. Teste notebooker fra en ren kernel.
9. Bruke relative filbaner.
10. Ikke introdusere nye avhengigheter uten en god grunn.
11. Følge eksisterende språk, terminologi og filstruktur.
12. Bruke tydelige overskrifter og korte avsnitt.
13. Forklare både hva kode gjør og hvorfor den brukes.
14. Unngå å presentere økonomiske modeller som mer realistiske enn de er.
15. Skille mellom pedagogiske modeller og empiriske analyser.
16. Dokumentere datakilder.
17. Unngå å gjøre terminal, Git eller miljøoppsett til en forutsetning for studentene.
18. Ikke gjøre store strukturelle endringer uten å kontrollere innholdsfortegnelse, lenker og bygging.
19. Ikke erstatte eksisterende faglig innhold med generisk AI-generert tekst uten å bevare fagets særpreg.
20. Spørre om eller markere faglige antakelser når prosjektfilene ikke gir tilstrekkelig informasjon.

---

# 18. Hva som kjennetegner godt innhold i dette emnet

Godt innhold:

* begynner med et forståelig problem
* introduserer få nye konsepter om gangen
* bruker realistiske, men håndterlige data
* viser mellomregninger og mellomresultater
* gir studenten mulighet til å eksperimentere
* knytter kode til økonomisk tolkning
* inneholder oppgaver med gradvis stigende vanskelighetsgrad
* hjelper studenten å oppdage og rette feil
* viser at flere løsninger kan være gyldige
* trener studentene i å forklare resultatene
* bygger mot selvstendig analyse

Dårlig innhold:

* er skrevet som dokumentasjon for erfarne utviklere
* introduserer mange biblioteker samtidig
* bruker kompakt og uoversiktlig kode
* mangler økonomisk kontekst
* viser lange programmer uten forklaring
* gjør studentene avhengige av å kopiere kode
* bruker data uten å oppgi kilde
* lager figurer uten tolkning
* introduserer pandas-operasjoner som magiske kommandoer
* fokuserer mer på syntaks enn problemløsing

---

# 19. Fagets identitet

Fagets særpreg er kombinasjonen av:

* grunnleggende Python
* økonomiske modeller
* simulering
* pandas
* autentiske offentlige data
* SSB og Eurostat
* visualisering
* studentdefinerte problemstillinger
* utforskende arbeid
* en større analyse i eksamensmappen

Studentene skal bevege seg fra små, styrte beregninger til selvstendig arbeid med virkelige data.

Den ønskede utviklingen kan oppsummeres slik:

> Først lærer studenten å beskrive en beregning med kode. Deretter lærer studenten å gjenta, organisere og generalisere beregningen. Til slutt lærer studenten å bruke programmering og dataanalyse til å undersøke en selvvalgt økonomisk eller samfunnsfaglig problemstilling.

Alt innhold som utvikles for prosjektet, bør støtte denne progresjonen.
