# Litt overodnet info

## Fremdriftsplan

Kurset går fra uke 34 til og med uke 47, med to faste læringsøkter hver uke.

**Tirsdager**

- kl. 12.15–14.00: forelesning og demonstrasjon i auditorium Brosundet
- kl. 14.00–16.00: veiledning og øving i Storhavet

**Torsdager**

- kl. 08.15–12.00: samlet læringsøkt i Fyrtårnet

Tirsdagene har en tydelig overgang fra felles undervisning til veiledet arbeid.
Torsdagene gir større rom for workshops og utprøving av ulike
undervisningsformer. En vanlig torsdagsøkt vil likevel ofte bestå av forelesning
eller demonstrasjon etterfulgt av selvstendig arbeid, gruppearbeid og veiledning.

Kurset har to hoveddeler:

1. grunnleggende programmering gjennom økonomiske modeller og simulering
2. innhenting, behandling og analyse av data med pandas og API-er


Planen er tentativ. Rekkefølgen kan justeres etter progresjonen i gruppa og
koordineringen med metodefaget.

## Vurderingsmappe

Vurderingsmappen består av to individuelle arbeider skrevet som faglige essays i
Jupyter Notebook og et refleksjonsnotat:

- ett simuleringsessay
- ett dataanalyseessay
- ett refleksjonsnotat

Begge arbeidene leveres i desember. Endelig leveringsdato blir kunngjort senere.
Studentene arbeider med essayene over tid og leverer skisse og deltar i to obligatoriske
arbeidsverksteder:

- et simuleringsverksted etter den felles simuleringsdelen
- et dataanalyseverksted mot slutten av undervisningsperioden

Arbeidene skal kombinere kode, faglig problemstilling, begrunnede valg,
resultater, figurer, tolkning og refleksjon. Selvstendig bruk av Python i en
økonomisk eller markedsføringsfaglig kontekst er viktigere enn komplisert kode.

**Mer info om mappeinnlevering og vurdering senere**



## Ukeplan

| Uke | Tirsdag | Torsdag | Øving og mappeframdrift |
|---:|---|---|---|
| **34** | **Teknisk oppstart:** Jupyter-miljøet, notebookens oppbygning, tekst- og kodeceller, kjøring av celler, kernel, lagring og filer. | **Python som kalkulator:** regneoperatorer, enkle økonomiske beregninger, variabler og utskrift. | Opprette, lagre og kjøre en ryddig notebook ovenfra og ned. Lage en liten pris-, kostnads- eller inntektskalkulator. |
| **35** | **Logistisk vekst:** bruke variabler, uttrykk og datatyper til å beskrive populasjonsvekst, markedsmetning eller produktadopsjon. | **Funksjoner – første møte:** parametere, returverdier og gjenbruk av beregninger. | Endre parametere og sammenligne scenarioer. Tilpasse vekstmodellen til en økonomisk eller markedsføringsfaglig tolkning. |
| **36** | **Lister og indekser:** samle data for flere land, markeder eller scenarioer og hente ut verdier. | **For-løkker og plotting:** gjenta beregninger, følge utvikling over tid og lage enkle figurer med matplotlib. | Sammenligne flere vekstforløp. Påbegynne en enkel spare- eller lånekalkulator. |
| **37** | **Sparing og lån:** bruke funksjoner, lister, løkker og enkle betingelser i en ny kontekst. | **Bro til pandas:** ordbøker som observasjoner, liste med ordbøker, DataFrame, Series, rader og kolonner. | Overføre simulerte resultater til en DataFrame og lage en enkel tabell eller figur. |
| **38** | **Ekte data:** lese et lite SSB-datasett med `read_csv()`, finne kolonner og datatyper og velge relevante data. | **Deskriptiv analyse og visualisering:** `describe()`, `value_counts()`, gjennomsnitt, median og standardavvik; linje-, stolpe- og spredningsdiagram. | Lage en kort univariat analyse av arbeidsledighet eller et tilsvarende datasett. Etter denne uka skal studentene være klare til å bruke grunnleggende pandas i metodefaget. |
| **39** | **Betingelser og struktur:** `if`, `elif` og `else`, ordbøker og enkel klassifisering av kunder eller produkter. | **Tilfeldighet og simulering:** tilfeldige tall, seed, sannsynligheter og simulering av kundeatferd. | Undersøke hvordan endrede antakelser påvirker kjøp, kampanjer eller kundegrupper. Etisk stopp: Når blir segmentering urimelig eller misvisende? |
| **40** | **Gjentatte simuleringer:** `for` og `while`, stoppbetingelser og oppsummering av mange forsøk. | **Større simuleringscase:** kundeatferd som felles case; økonomiske og markedsføringsfaglige fordypningsoppgaver. Introduksjon til simuleringsessayet. | Velge eller tilpasse et case, formulere en foreløpig problemstilling og lage en første kjørbar modell. |
| **41** | **Utvalg og manipulering i pandas:** kolonner, rader, `.loc`, `.iloc`, boolsk filtrering og nye variabler. | **Obligatorisk simuleringsverksted:** problemstilling, modell, antakelser, første resultat og plan for videre arbeid. Medstudentrespons og veiledning. | Levere et kort prosessarbeid fra simuleringsessayet. Revidere modellen etter tilbakemelding. |
| **42** | **Innlesing og datakvalitet:** CSV-varianter, skilletegn, desimaltall, tegnkoding, manglende verdier, duplikater og datatyper. | **Gruppering og aggregering:** `value_counts()`, `groupby()` og relevante sammendrag for én eller flere grupper. Introduksjon til dataanalyseessayet. | Finne et mulig datasett og formulere en avgrenset problemstilling. Begrunne valg ved behandling av manglende eller uryddige data. |
| **43** | **Ryddige data:** langt og bredt format, `melt()`, `pivot()` og `pivot_table()`. | **Sammensatte tabeller:** flere grupperingsvariabler, sammenslåing av datasett og MultiIndex når datastrukturen gjør det nødvendig. | Arbeide med flytting, utflytting eller andre data fordelt på kommune, år og kategori. MultiIndex behandles som et behovsstyrt verktøy, ikke et mål i seg selv. |
| **44** | **Tidsdata:** konvertere tekst til datetime eller perioder, sortere og visualisere kronologisk og aggregere fra måned til kvartal. | **To tidsserier:** slå sammen konkurser og arbeidsledighet, undersøke korrelasjon og diskutere forskjellen mellom samvariasjon og årsak. | Lage en reproduserbar tidsanalyse i flere små steg. Etisk stopp: Hva kan analysen underbygge, og hva blir spekulasjon? |
| **45** | **Enkle API-er:** HTTP, GET, parametere, statuskoder, JSON og `requests`. | **Offentlig statistikk via API:** hente og dokumentere data fra SSB; Eurostat som sammenligning eller fordypning. | Hente et avgrenset datasett, lagre en lokal kopi og gjøre det om til en DataFrame. Avklare datakilde, vilkår og begrensninger. |
| **46** | **Maskinlæring 1:** data, forklaringsvariabler og målvariabel, splitting i trenings- og testdata, enkel regresjonsmodell, tilpasning, prediksjon og evaluering med scikit-learn. | **Maskinlæring 2:** SVM som kort demonstrasjon av modellgrensesnittet; k-means og kundesegmentering som ikke-veiledet læring og fordypning. | Endre et stillasbygget eksempel og tolke resultatet kritisk. Drøfte feil, overtilpasning, skalering og om matematiske klynger har en faglig mening. |
| **47** | **Data, verdi og ansvar:** etikk, personopplysninger, grunnprinsipper i GDPR og informasjonssikkerhet. Konfidensialitet, integritet og tilgjengelighet. | **Obligatorisk dataanalyseverksted:** problemstilling, datakilde, databehandling, første figurer og resultater, medstudentrespons og plan fram mot levering. | Kontrollere at analysen kan kjøres ovenfra og ned. Dokumentere datakilde, KI-bruk, begrensninger og relevante etiske, juridiske eller sikkerhetsmessige spørsmål. |


### Kvantitative og kvalitative metoder

Merk at pandas fra Del II i kurset sniker seg litt inn i del I også, spesielt i uke 38 og 39. 
Dette er slik at dere kan begynne å bruke `pandas` sammen med Njål i AM201306 til kvalitative metoder

```{image} ../images/luskenjaal.png
:align: center
```




<!---

## Felles undervisning og valgbare fordypninger

Forelesninger og demonstrasjoner bruker i hovedsak felles case som skal være
relevante for både økonomi- og markedsføringsstudenter. Sparing, lån,
markedsmetning og kundeatferd er sentrale fellesområder.

Øvingene gir større rom for spesialisering. Aktuelle fordypninger kan være:

- rekeoligopol, tilbud og etterspørsel eller makroøkonomiske sjokk
- kampanjer, konvertering, gjenkjøp, frafall eller kundereiser
- sparing, lån, sparemål eller andre scenarioanalyser
- kundesegmentering og k-means for studenter som vil utforske maskinlæring

Fordypningene er valgbare og er ikke låst til studieprogram.

-->

## Obligatorisk simuleringsverksted

Til verkstedet i uke 41 skal dere ha med:

- en foreløpig problemstilling
- et valgt eller egenutviklet simuleringscase
- en kort forklaring av modellen og de viktigste antakelsene
- en kjørbar førsteversjon
- minst ett foreløpig resultat eller én figur
- en plan for videre arbeid
- en kort redegjørelse for eventuell bruk av KI-verktøy

## Obligatorisk dataanalyseverksted

Til verkstedet i uke 47 skal dere ha med:

- en avgrenset problemstilling
- dokumentert datakilde og et datasett som kan leses inn
- en kort beskrivelse av nødvendig datarensing
- minst én relevant tabell eller figur
- et foreløpig resultat og en forsiktig tolkning
- en plan for ferdigstilling før levering i desember
- en kort vurdering av datakvalitet, begrensninger og relevante etiske eller
  juridiske spørsmål

I andre workshop blir det også relevant og gå gjennom hvordan mappen deres vurderes, og å se på noen gode eksempler, og kjipe feller å snuble i.

## Annen obligatorisk aktivitet

Der er også noen obligatoriske selvrettende øvinger, og vi ønsker å legge
inn et obligatorisk muntlig krav, men dette er ikke helt på plass ennå; **mer informasjon senere**


