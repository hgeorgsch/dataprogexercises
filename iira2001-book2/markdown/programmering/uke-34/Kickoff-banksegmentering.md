# Hvor langt kommer du med KI før du kan programmere?

I denne kickoffoppgaven skal du forsøke å gjennomføre en ganske krevende
dataanalyse **før** du har lært verktøyene som vanligvis brukes til å løse den.
Du får bruke en valgfri KI-assistent som samarbeidspartner.

:::{important} Dette skal være vanskelig
Du forventes ikke å forstå all koden eller komme helt i mål. Oppgaven er ikke
en test av hva du kan fra før. Den er et eksperiment: Hvor langt kommer du med
KI nå, og hva trenger du selv å kunne for å vurdere det KI-en lager?
:::

## Hvorfor gjør vi dette?

En KI-assistent kan raskt produsere kode, figurer og en analyse som ser
overbevisende ut. Det er ikke det samme som at analysen er riktig eller nyttig.

Senere i semesteret skal du vende tilbake til forsøket og undersøke om du da:

- forstår mer av koden
- lettere oppdager feil og svake antakelser
- stiller bedre spørsmål til KI-en
- har bedre kontroll over analysen og konklusjonene

Ta derfor vare på både det som virker, det som feiler, og det du ikke forstår.

## Scenarioet

Du arbeider med analyse for en bank eller kortutsteder. Banken har data om
hvordan omtrent 9 000 kunder har brukt kredittkortet sitt de siste seks
månedene. Banken ønsker å forstå kundene bedre og finne mønstre eller
kundegrupper som kan være nyttige når den tar beslutninger.

Oppdraget ditt er å bruke KI til å:

1. utforske datasettet
2. formulere et interessant forretningsspørsmål
3. gjennomføre en analyse i en Jupyter Notebook
4. presentere og forsøke å tolke noen funn
5. vurdere hvor mye du faktisk forstår, og hvor sikker du er på resultatet

Målet er ikke å lage den «beste» analysen. Et delvis eller mislykket forsøk kan
være minst like lærerikt som en analyse som tilsynelatende fungerer perfekt.

## Datasettet

Dere skal bruke **Credit Card Dataset for Clustering**. Filen heter
`cc_general.csv` og inneholder blant annet opplysninger om saldo, kjøp,
kontantuttak, kredittgrense, betalinger og kundeforholdets varighet.

[Last ned `cc_general.csv`](../../../data/uke-34/cc_general.csv). Datasettet
kommer opprinnelig fra
[Credit Card Dataset for Clustering på Kaggle](https://www.kaggle.com/datasets/arjunbhasin2013/ccdata),
men du trenger ikke en Kaggle-konto for å laste ned kopien som brukes i kurset.

Legg CSV-filen i samme mappe som notebooken din.

:::{dropdown} Hva slags opplysninger finnes i datasettet?
I datasettet finner du blant annet:

- kundens saldo og hvor ofte saldoen oppdateres
- samlede kjøp, engangskjøp og avbetalingskjøp
- kontantuttak (*cash advance*)
- frekvenser og antall transaksjoner
- kredittgrense
- betalinger og minimumsbetalinger
- andelen ganger hele beløpet er betalt
- hvor lenge kunden har hatt kundeforholdet

Variabelnavnene og forklaringene på Kaggle-siden kan hjelpe deg med å tolke
kolonnene. Be gjerne KI-en forklare dem, men kontroller forklaringen mot
beskrivelsen av datasettet.
:::

## Velg en innfallsvinkel

Velg én av inngangene under, kombiner dem, eller formuler en annen relevant
problemstilling. Tenk først og fremst på et **forretningsproblem**, ikke på
hvilken teknisk metode som skal brukes.

:::::{tab-set}
::::{tab-item} Markedsføring
### Kundesegmentering

Undersøk om dataene kan fortelle noe om ulike typer kunder og hvordan banken
kan møte dem. Du kan for eksempel spørre:

- Finnes det meningsfulle kundegrupper basert på hvordan kortet brukes?
- Hva kjennetegner gruppene?
- Hvilke kundegrupper kan være spesielt interessante for banken?
- Hvordan kan banken tilpasse kommunikasjon, produkter eller tilbud?
- Finnes det tydelige mønstre knyttet til aktivitet, kontantuttak,
  avbetalingskjøp eller betalingsgrad?
::::

::::{tab-item} Økonomi
### Økonomisk atferd og mulige risikosignaler

Undersøk økonomiske mønstre som kan være relevante for banken. Du kan for
eksempel se etter:

- høy saldo sammenlignet med kredittgrensen
- mye bruk av kontantuttak
- lave betalinger sammenlignet med saldoen
- stor avhengighet av minimumsbetalinger
- lav andel full betaling
- kombinasjoner som kan tyde på presset likviditet eller sårbar økonomisk
  atferd

:::{warning} Ikke kall dette en modell for mislighold
Datasettet forteller ikke hvem som faktisk misligholder eller påfører banken
tap. Du kan omtale mønstrene som **mulige risikosignaler**, men du kan ikke
konkludere med at bestemte kunder kommer til å misligholde.
:::
::::

::::{tab-item} Egen idé
### En annen relevant problemstilling

Du kan formulere et annet spørsmål som passer til dataene og bankens behov.
Vær tydelig på:

- hva du vil finne ut
- hvorfor svaret kan være nyttig
- hva datasettet faktisk kan og ikke kan fortelle deg
::::
:::::

## Bruk KI som samarbeidspartner

Vi anbefaler [GPT NTNU](https://gpt.ntnu.no), der du kan velge mellom flere
åpne språkmodeller. Logg inn med Feide mens du er koblet til eduroam, eller
koble deg til NTNUs nettverk gjennom VPN først. Du kan også bruke ChatGPT,
Claude, Gemini, Copilot eller en annen tilsvarende KI-assistent.

Du får ingen ferdig startprompt eller teknisk oppskrift. En del av eksperimentet
er å finne ut hvordan du selv må forklare oppdraget og føre samtalen videre.

Arbeid omtrent slik:

1. Fortell KI-en om scenarioet, datasettet og hva du vurderer å undersøke.
2. Be om hjelp til å forstå dataene og utvikle en problemstilling.
3. Be KI-en foreslå kode du kan kjøre i notebooken.
4. Kjør koden. Kopier også feilmeldinger tilbake til KI-en når noe ikke virker.
5. Be om forklaringer på kode, metoder og resultater du ikke forstår.
6. Forsøk å kontrollere påstander og resultater. Still oppfølgingsspørsmål.
7. Stopp opp underveis og noter hva du fortsatt er usikker på.

:::{tip} Du styrer samtalen
Du trenger ikke godta KI-ens første problemstilling, metode eller forklaring.
Be den forenkle, begrunne valgene, forklare én linje av gangen eller foreslå en
annen løsning. Hvis løsningen blir uoversiktlig, kan du be om en enklere start.
:::

:::{warning} KI-en kan ta feil
Kode som kjører kan fortsatt behandle dataene feil. En figur kan se profesjonell
ut uten å svare på problemstillingen, og en overbevisende forklaring kan bygge
på antakelser som ikke finnes i datasettet. Ikke legg personopplysninger,
fortrolige data eller passord inn i en KI-tjeneste.
:::

## Før en enkel arbeidslogg

Dokumenter forsøket mens du arbeider. Ikke rydd bort alle blindveier og feil;
de viser hva KI-en hjalp med og hvor du selv mistet oversikten.

Ta vare på:

- noen representative spørsmål eller prompter du ga KI-en
- KI-generert kode du forsøkte å bruke
- tabeller, figurer og andre resultater
- minst én feilmelding eller blindvei, dersom du møtte noen
- minst ett eksempel på kode eller en metode du **ikke forstår**
- korte notater om hva du tror resultatene betyr

Du kan lime inn korte utdrag fra KI-samtalen i tekstceller i notebooken. For
lange samtaler kan du heller ta skjermbilder eller oppsummere hva dere prøvde.

## Kort rapport

Bruk helst notebooken som en kort rapport. Kombiner tekstceller, kodeceller og
resultater, og gi den et forståelig filnavn. Rapporten skal inneholde:

1. **Problemstilling:** Hva forsøkte du å finne ut, og hvorfor er det nyttig?
2. **KI-dialog:** Noen representative prompter og hvordan du fulgte dem opp.
3. **Fremgangsmåte:** En kort beskrivelse av hva du og KI-en gjorde.
4. **Resultater:** Relevante tabeller, figurer eller andre funn.
5. **Tolkning:** Hva tror du funnene betyr?
6. **Usikkerhet:** Hva forstår du ikke, og hva kan være feil eller misvisende?

Dette er dokumentasjon av et eksperiment, ikke en polert akademisk rapport. Du
blir ikke vurdert etter hvor avansert analyse KI-en klarer å produsere.

:::{admonition} Før du avslutter
:class: note

Skriv korte svar på disse spørsmålene i rapporten:

1. Hva prøvde du å finne ut?
2. Hva ba du KI-en om å hjelpe med?
3. Hva fikk du faktisk til?
4. Hva var vanskelig?
5. Hvilke deler av koden eller analysen forstår du ikke?
6. Hvor sikker er du på at resultatene er riktige og meningsfulle?
7. Hva skulle du ønske at du kunne selv for å bruke KI bedre?
:::

## Levering

Lever rapporten eller notebooken i den angitte innleveringen på
[Moodle](https://iirmoodle.it.ntnu.no). 
Leveringen er ikke obligatorisk - men vi lar det telle som 1 godkjent øving dersom du velger å levere inn arbeidet.
Fristen er satt til fredag 28. august.

## Perfekt mat til refleksjonsnotatet

Du skal møte denne analysen igjen mot slutten av kurset. Da skal du blant annet
kunne spørre:

- Forstår jeg nå kode som jeg ikke forstod i starten?
- Ville jeg formulert promptene annerledes i dag?
- Ser jeg nå feil, svakheter eller unødvendig kompliserte løsninger?
- Klarer jeg bedre å kontrollere hva KI-en gjør?
- Har programmeringskunnskap gjort KI mer nyttig?
- Hva kan jeg delegere til KI, og hva må jeg selv forstå?

Oppbevar derfor både notebooken, rapporten og relevante deler av KI-samtalen.
Som en del av mappeinnleveringen, skal du også levere et refleksjonsnotat over læringsprossessen,
**Et lite eksperiment som dette er perfekt mat å tygge på i et refleksjonsnotat**
