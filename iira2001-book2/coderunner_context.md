# Kontekst for utvikling av CodeRunner-oppgaver i IIRA2001

Denne filen gir Codex nødvendig faglig, pedagogisk og teknisk kontekst for å
lage selvrettende treningsoppgaver til emnet «Programmering og data i økonomiske
fag» (IIRA2001).

Oppgavene utvikles med det lokale rammeverket i `CodeRunnerHero/` og skal brukes
i Moodle CodeRunner. Rammeverket ligger i bokprosjektet for å gjøre samarbeidet
med Codex enklere, men er ikke en del av den studentrettede Jupyter Book-boka.
Ikke legg `CodeRunnerHero/` eller denne filen inn i `myst.yml` uten at det blir
bedt om eksplisitt.

## Autoritative kilder

Les relevante kilder før en oppgave utformes eller endres:

1. `markdown/fremdrift.md` er autoritativ for ukeplan, rekkefølge og tidspunkt.
2. `CodeRunnerHero/questions/iira2001/OPPGAVEPLAN.md` beskriver den planlagte
   oppgavebanken og prioriteringen mellom quizzer.
3. Denne filen er autoritativ for oppgavepedagogikk og standard arbeidsflyt.
4. `COURSE_CONTEXT_FROM_GPT.md` beskriver studentgruppen, fagets identitet,
   eksempler og mulig pensum. Den er en kontekst- og idébank, ikke en bindende
   liste over alt studentene skal mestre.
5. `CodeRunnerHero/README.md` og `CodeRunnerHero/CLAUDE.md` beskriver det
   faktiske lokale rammeverket.
6. `CodeRunnerHero/CR_DOCS.md` er oppslagsverk for Moodle CodeRunner.
7. Eksisterende oppgaver i `CodeRunnerHero/questions/` er fasit for gjeldende
   filstruktur og implementasjonsmønstre.

Ved konflikt skal ukeplanen og eksplisitte beskjeder fra faglærer ha forrang.
Ikke anta at eldre eksempeloppgaver viser ønsket pensum eller vanskenivå.

## Studentgruppe og overordnet mål

Studentene går økonomi og administrasjon eller markedsføring og ledelse. Mange
har aldri programmert før. Forkunnskapene i matematikk og statistikk varierer
betydelig, og markedsføringsstudentene har normalt mindre matematikk og
statistikk enn økonomistudentene.

Dette er ikke et informatikkemne. Studentene skal lære å bruke Python selvstendig
i en økonomisk, administrativ eller markedsføringsfaglig kontekst. Det viktigste
er at de kan:

- beskrive en beregning eller enkel modell med kode
- organisere og gjenta beregninger
- hente, rydde, undersøke og visualisere data
- formulere og utforske en faglig problemstilling
- tolke resultater og beskrive begrensninger
- lese, kontrollere og tilpasse kode, også når KI-verktøy brukes

Emnet har mappevurdering med et simuleringsessay, et dataanalyseessay og et
refleksjonsnotat. CodeRunner-oppgavene er primært formative treningsoppgaver. De
skal bygge delferdigheter og gi rask tilbakemelding, ikke erstatte essayenes
åpne problemløsning, analyse og formidling.

## Pedagogiske hovedprinsipper

### Begynn med et behov

Introduser programmeringsteknikken gjennom et forståelig problem. Studenten bør
helst møte behovet før den generelle syntaksen.

Eksempler:

- variabler gjennom pris, inntekt, kostnad, rente eller vekst
- funksjoner når samme beregning må gjentas
- lister når flere land, kunder, produkter eller perioder skal behandles
- løkker gjennom utvikling over tid eller gjentatte simuleringer
- betingelser gjennom beslutningsregler og segmentering
- ordbøker gjennom én kunde, ett produkt eller én observasjon
- pandas når lister og ordbøker blir upraktiske for tabulære data
- gruppering gjennom regioner, kundegrupper, kategorier eller tidsperioder
- API-er gjennom autentiske data fra SSB, Eurostat eller en enkel åpen tjeneste

### Test få læringsmål om gangen

En vanlig oppgave bør teste ett hovedmål og høyst ett eller to støttemål.
Oppgaven skal være liten nok til at tilbakemeldingen peker på en bestemt
misforståelse. Ikke gjem en enkel løkkeoppgave inne i et langt, matematisk case.

### Bruk gradvis selvstendighet

En oppgaveserie kan følge denne progresjonen:

1. kjør eller forstå et ferdig eksempel
2. endre én verdi eller ett uttrykk
3. fylle inn en manglende kodelinje
4. fullføre en funksjon med gitt signatur
5. skrive en liten løsning fra bunnen av
6. bruke teknikken i en ny faglig kontekst
7. forklare eller tolke resultatet utenfor CodeRunner

CodeRunner egner seg best til trinn 2–6. Faglig forklaring og åpen tolkning
trenes i notebook, læringsøkt og mappearbeid.

### Felles kjerne, valgbare kontekster

Forelesningene har en felles kjerne. Oppgaver kan tilby parallelle kontekster:

- felles: priser, sparing, lån, markedsmetning og kundeatferd
- økonomisk fordypning: tilbud og etterspørsel, oligopol og makroøkonomiske sjokk
- markedsføringsfordypning: kampanjer, konvertering, gjenkjøp, frafall og
  kundereiser

Sporene skal være valgbare og ikke låses til studieprogram. Parallelle oppgaver
bør teste samme programmeringsmål og ha omtrent samme arbeidsmengde.

### Lesbarhet foran kortest mulig kode

- Bruk eksplisitt og lettlest kode for nybegynnere.
- Bruk beskrivende variabel- og funksjonsnavn.
- Hold språkbruken konsistent i hvert eksempel.
- Ikke krev comprehensions, `lambda`, objektorientering eller andre kompakte
  konstruksjoner før de er introdusert og faktisk er læringsmålet.
- Ikke premier en avansert løsning bare fordi den er kort.
- Ikke krev `input()` uten at interaktiv inndata er selve læringsmålet.
  Parameterceller og funksjonsargumenter passer bedre i reproduserbare notebooks.

## Standard for en ny oppgave

Avklar følgende før implementasjon:

| Felt | Krav |
|---|---|
| Uke/tema | Når kan oppgaven gis ifølge ukeplanen? |
| Hovedmål | Én konkret ferdighet studenten skal trene |
| Forkunnskaper | Bare konsepter som er introdusert tidligere |
| Kontekst | Hvorfor problemet er relevant eller forståelig |
| Kontrakt | Eksakt funksjonsnavn, parametere, returtype og eventuell startkode |
| Synlige eksempler | Små eksempler studenten kan forstå og prøve |
| Grensetilfeller | Tomme data, null, negative tall, manglende verdier eller annet relevant |
| Teknikkrav | Bare krav som følger direkte av læringsmålet |
| Poeng | Vekt funksjonell oppførsel høyere enn kosmetiske detaljer |
| Tilbakemelding | Norsk, konkret og handlingsrettet uten å røpe fasiten |

Hvis faglig kontrakt eller forventet metode er uklar, stopp og avklar før
retteren bygges. En presis oppgavekontrakt er nødvendig for rettferdig automatisk
testing.

## Valg av oppgavetype

### Enkel oppgave er standard

Bruk en vanlig enkelttrinnsoppgave når studenten skal skrive eller fullføre én
funksjon eller én avgrenset kodebit. Ta utgangspunkt i:

`CodeRunnerHero/questions/for-loop-test/`

Denne typen passer til de fleste treningsoppgaver i variabler, funksjoner,
lister, løkker, betingelser og avgrensede pandas-operasjoner.

### Flertrinnsoppgave brukes bevisst

Bruk `graderstate`, kontrollpunkter og trinnvis grensesnitt når senere steg
faktisk bygger på godkjent kode fra tidligere steg. Ta utgangspunkt i:

- `CodeRunnerHero/questions/mapping-with-graderstate/` for en kort
  flertrinnsoppgave
- `CodeRunnerHero/questions/random-search/` for en lengre algoritme med flere
  funksjoner

Ikke gjør alle små oppgaver til flertrinnsoppgaver. Kompleksiteten i retter,
graderstate, HTML og JavaScript må gi en tydelig pedagogisk gevinst.

### LLM-retting er et særtilfelle

`CodeRunnerHero/questions/transducere-gpt/` viser fri tekst vurdert med en LLM.
Ikke bruk LLM-retting for deterministiske Python- eller pandasoppgaver som kan
testes lokalt. LLM-retting krever eksplisitt bestilling, avklart kostnad,
personvern, API-tilgang og robust håndtering av ustabile svar.

## CodeRunnerHero: struktur og arbeidsflyt

Rammeverket er en lokal forfatterløsning for egendefinerte Moodle
CodeRunner-templategradere. Delt kode ligger i `CodeRunnerHero/framework/`, og
hver oppgave ligger i en bladmappe under `CodeRunnerHero/questions/`. Oppgaver
kan organiseres på vilkårlig dybde, for eksempel
`CodeRunnerHero/questions/iira2001/variabler/01-pris-og-antall/`.

### Filer som normalt forfattes

- `question.md`: læringsmål, faglig begrunnelse, oppgavetekst,
  vurderingsplan og testplan for oppgaveforfatteren
- `question_text.html.twig`: studentrettet tekst ved full XML-eksport
- `answer_preload.py`: eventuell startkode i editoren
- `corr_answer.py`: oppgaveforfatterens referanseløsning
- `stud_answer.py`: lokal prøvebesvarelse
- `test_prog1.py`, eventuelt flere: selve testlogikken
- `template.py`: template-graderen som kjører tester og bygger CodeRunner-svar
- `template_variables.twig`: stabile eller studentavhengige parametere
- `question_config.py`: bare når Python må bake inn serialiserbare parametere
- `moodle_question.toml`: manifest og CodeRunner-innstillinger for XML-eksport
- `sample_answers/`: riktige og bevisst mangelfulle svar som prøver retteren
- `Makefile`: det korte inkluderingsskriptet som peker til felles rammeverk

For en ny publiserbar oppgave bør `question_text.html.twig`,
`moodle_question.toml` og relevante eksempelbesvarelser normalt være med.

### Filer som ikke skal håndredigeres

Ikke rediger genererte filer som:

- `template_variables_moodle.twig`
- `question_params.json.twig`
- `test_prog_params.json.twig`
- `output.py`
- `template_to_moodle.py`
- `question_to_moodle.xml`
- `graderstate.json`
- `graderres.json`
- `code.py`

Endre kildefilene og bygg på nytt. Ikke endre `CodeRunnerHero/framework/` når
oppgaven bare er å lage kursoppgaver. Rammeverksendringer må være eksplisitt
bestilt og testes mot eksisterende oppgaver.

### Lokal arbeidsflyt

Kommandoene kjøres fra den aktuelle oppgavemappen:

```bash
cd CodeRunnerHero/questions/<emne>/<tema>/<oppgavenavn>
make test1
make grade
make all
make xml
```

- `make test1` kjører testprogrammet gjennom samme escaping- og gradersti som
  Moodle.
- `make grade` kjører hele graderen og oppdaterer lokal graderstate.
- `make all` lager den selvstendige template-graderen
  `template_to_moodle.py`.
- `make xml` lager `question_to_moodle.xml` når
  `moodle_question.toml` finnes.
- `make web` starter en Moodle-lignende lokal forhåndsvisning for interaktive
  oppgaver.

Ikke rapporter en oppgave som ferdig før relevante korrekte og mangelfulle
eksempelbesvarelser er prøvd. Full XML-eksport skal valideres i Moodle før
studentbruk, særlig dersom spørsmålsteksten inneholder JavaScript.

## Implementasjonskrav for tester

### Grunnformat

Testprogrammet oppretter ett `codegrader.Test`-objekt per vurderingsmoment og
skriver hvert objekt på én egen linje:

```python
test = cg.Test(testName="Beskrivende navn")
test.addResult("mark", 2)
test.addResult("description", "Norsk og målrettet tilbakemelding.")
test.pass_test(passed)
print(test.dump())
```

Linjeorientert `Test.dump()`-output er en nødvendig del av rammeverket. Ikke
skriv innrykket JSON over flere linjer. Vanlig utskrift fra studentkoden skal
fanges opp slik at den ikke forstyrrer testresultatene.

`template.py` skal normalt:

1. legge inn `TEST_PROG1` med korrekt Twig-escaping
2. kjøre det med `CodeGrader.runTest(timeout=...)`
3. bygge resultattabell med norske kolonner
4. kalle `results.mark()`
5. gi forståelig melding ved timeout eller testfeil
6. skrive `results.getCodeRunnerOutput(...)`

### Test oppførsel før implementasjonsstil

Test som hovedregel hva koden gjør:

- korrekt returverdi og datatype
- korrekt form, kolonner eller indeks
- at inndata ikke endres uten at det er avtalt
- tomme og små inndata
- null, negative tall og relevante grenser
- manglende eller uventede kategorier når kontrakten åpner for dem

Bruk AST-analyse bare når bruk eller fravær av en bestemt konstruksjon er
læringsmålet, for eksempel en eksplisitt `for`-løkke. Ikke avvis alternative
korrekte løsninger for å tvinge fram lærerens referanseløsning.

AST-kontroller er bedre enn enkle tekstsøk fordi kommentarer, strenger og
variabelnavn ellers kan gi falske treff.

Hold AST-kontrollene små og lokale: finn den aktuelle funksjonen og kontroller
bare konstruksjonen som er læringsmålet. Testprogrammet skal kunne leses og
endres av en faglærer uten omfattende kjennskap til AST. Studentkoden kjøres
allerede isolert i en tidsbegrenset underprosess på Jobe-serveren, så retteren
trenger ikke et stort defensivt lag rundt alle mulige feil.

### Feil skal bli til tilbakemelding

Gi målrettet tilbakemelding for feil som oppgaven uttrykkelig trener på, for
eksempel:

- syntaksfeil
- manglende funksjon eller feil signatur
- utskrift i stedet for returverdi
- mutasjon av inndata
- timeout eller uendelig løkke
- uventet datatype eller tabellstruktur

Det er akseptabelt at andre syntaks- og kjørefeil går gjennom den vanlige
CodeRunner/Jobe-feilhåndteringen. Ikke bygg store `try`/`except`-strukturer bare
for å hindre at et testprogram avsluttes. Når en feil fanges, vis normalt
feiltypen, for eksempel `TypeError`, men ikke studentkontrollert HTML eller
skjulte testverdier.

### Tall

- Sammenlign flyttall med toleranse, for eksempel `math.isclose`,
  `numpy.isclose` eller `numpy.allclose`.
- Velg testverdier som avslører vanlige logiske feil.
- Ikke krev identisk avrunding med mindre avrunding er læringsmålet og er
  spesifisert i oppgaven.

### Tilfeldighet og simulering

- Testene skal være reproduserbare og ikke flakke tilfeldig mellom bestått og
  ikke bestått.
- Sett seed når det er hensiktsmessig.
- Test egenskaper eller injiser en kontrollert tilfeldig funksjon fremfor å
  kreve én bestemt tilfeldig sekvens.
- Bruk kort timeout på `while`-løkker og gi en forståelig melding ved timeout.
- Ikke test statistiske egenskaper med så små utvalg at riktige løsninger kan
  feile tilfeldig.

### pandas

Pandas-oppgaver skal bruke små datasett som kan forstås og feilsøkes. Kontroller
etter behov:

- at resultatet er en `Series` eller `DataFrame`
- kolonnenavn, indeks og form
- relevante datatyper
- verdier, inkludert manglende verdier
- radrekkefølge bare når oppgaven krever den
- at original DataFrame ikke endres dersom funksjonen skal returnere en ny

Bruk `pandas.testing.assert_series_equal` eller
`pandas.testing.assert_frame_equal` når sandkassen har riktig pandas-versjon.
Sett eksplisitt hvilke forskjeller som er relevante; ikke gjør testen mer
følsom for navn, dtype eller rekkefølge enn oppgavekontrakten.

Datafiler som trengs av testen skal følge oppgaven eller bygges direkte i
testprogrammet. Ikke bruk absolutte filbaner.

### Figurer

Test primært beregningene og dataene bak figuren. Dersom plotting er
læringsmålet, kan retteren kontrollere diagramtype, akseetiketter og dataserier
gjennom matplotlib-objekter. Ikke sammenlign skjermbilder eller pikselverdier.

### API-er og eksterne data

Automatiske tester skal ikke avhenge av levende nettverk, API-nøkler eller at en
ekstern tjeneste svarer. Bruk små, lokale JSON-/CSV-eksempler eller mock en
kontrollert respons. Studentene kan gjøre ekte nettverkskall i notebookøvinger,
mens CodeRunner tester parsing, parameterbygging eller behandling av et kjent
svar.

### scikit-learn

Maskinlæring er hovedsakelig demonstrasjon og fordypning. Eventuelle
CodeRunner-oppgaver skal være stillasbygde og teste den grunnleggende
arbeidsflyten:

`data → splitting → modell → fit → predict → evaluering`

Bruk et lite, fast datasett og fast `random_state`. Test forståelige egenskaper
og evalueringsmål, ikke eksakt intern modelltilstand som kan variere mellom
bibliotekversjoner. K-means skal omtales som ikke-veiledet læring, og
kundeklynger skal ikke presenteres som automatisk meningsfulle segmenter.

## Synlige og skjulte tester

- Vis minst ett lite eksempel i oppgaveteksten.
- Skjulte tester skal kontrollere generalisering og relevante grensetilfeller,
  ikke overraskende, udokumenterte krav.
- Bruk deterministiske skjulte tester når det er mulig.
- Beskriv kategorien som feilet uten å avsløre de skjulte verdiene.
- Ikke bruk skjulte stilkrav.

En student som følger den offentlige kontrakten, skal ha nok informasjon til å
løse alle testene.

## Poeng og tilbakemelding

Funksjonell korrekthet skal normalt veie mest. Fordel poeng på meningsfulle
momenter, for eksempel:

- funksjon og grensesnitt
- vanlige inndata
- relevante grensetilfeller
- robusthet eller bevaring av inndata
- påkrevd teknikk når den er læringsmålet

Ikke gi poeng for et teknikktreff som bare finnes i ubrukt kode. Ikke gjør
små kosmetiske detaljer avgjørende for hele oppgaven.

Tilbakemeldingen skal:

- være på norsk
- si hva slags problem studenten må rette
- bruke begreper studentene har møtt
- skille mellom syntaksfeil, kjørefeil og feil resultat
- ikke vise hele løsningskoden
- ikke røpe skjulte testdata
- ikke være nedlatende eller overlesset

Standard resultattabell kan bruke:

| Moodle-kolonne | Intern nøkkel |
|---|---|
| `iscorrect` | `passed` |
| `Test` | `name` |
| `Beskrivelse` | `description` |

## Sikkerhet og hemmeligheter

- Studentkoden skal kjøres i rammeverkets tidsbegrensede underprosess.
- Bruk `{{ STUDENT_ANSWER | e('py') }}` når studentkode settes inn i en
  Python-streng i testprogrammet.
- I testprogrammer brukes den naturlige, ene `e('py')`-escapingen.
  `prepformoodle.py` legger automatisk til ekstra escaping ved eksport.
- Bruk aldri `| raw` for studentens svar.
- Ikke bygg studentkode eller rå feilmeldinger direkte inn i HTML eller
  JavaScript.
- Ikke legg API-nøkler, passord, personopplysninger eller andre hemmeligheter i
  repoet, template-parametere, graderstate eller vanlig Moodle XML.
- `sandboxparams.json` er lokal og gitignorert. Dokumenter forventet form i
  `sandboxparams.example.json` uten reelle hemmeligheter.
- `make xml` utelater sandbox-parametere. `make xml-private` kan inkludere
  hemmeligheter og skal bare brukes etter eksplisitt beslutning; resultatet må
  behandles som en hemmelig fil.
- Graderstate er klientpåvirkelig. Python-retteren, ikke JavaScript, skal avgjøre
  poeng og faseoverganger.

## Uketilknytning

Oppgaver skal ikke kreve konsepter før de er introdusert. Tabellen angir når et
tema er tilgjengelig etter den tentative ukeplanen. Kontroller alltid den
oppdaterte `markdown/fremdrift.md` før oppgaver produseres.

| Uke | Tema som introduseres | Egnede CodeRunner-oppgaver |
|---:|---|---|
| 34 | Jupyter, uttrykk, operatorer, variabler og utskrift | Beregne pris, kostnad, inntekt, prosent eller enkel rente; endre uttrykk og variabler |
| 35 | Datatyper, logistisk vekst og enkle funksjoner | Fullføre en funksjon med parametere og returverdi; beregne ett vekststeg eller markedsmetning |
| 36 | Lister, indekser, `for` og enkel plotting | Slå opp verdier, akkumulere over en liste, bygge resultatliste og beregne utvikling over tid |
| 37 | Sparing/lån, betingelser, ordbøker og bro til pandas | Generalisere spareberegning; representere en kunde; lage Series/DataFrame fra en enkel struktur |
| 38 | `read_csv`, inspeksjon, deskriptiv statistikk og grunnleggende diagrammer | Lese en liten medfølgende fil; velge kolonne; beregne sammendrag; forberede data til figur |
| 39 | `if/elif/else`, kundeklassifisering, tilfeldighet og simulering | Rabatt- eller segmentregel; ett tilfeldig kjøp; gjenta enkel kundeatferd med fast seed |
| 40 | `for`, `while`, stoppbetingelser og gjentatte simuleringer | Simulere til et mål; oppsummere mange forsøk; kontrollere stopp og returverdi |
| 41 | pandas-utvalg, `.loc`, `.iloc`, filtrering og nye kolonner | Filtrere kunder/regioner, velge rader og kolonner, beregne ny faglig variabel |
| 42 | CSV-varianter, datakvalitet, manglende data, duplikater, `groupby` | Lese norsk CSV-format; rense med begrunnede regler; aggregere per gruppe |
| 43 | Langt/bredt format, `melt`, `pivot`, sammenslåing og MultiIndex ved behov | Omforme et lite datasett; koble tabeller på nøkkel; hente et forståelig utsnitt |
| 44 | datetime/perioder, resampling, sammenslåtte tidsserier og korrelasjon | Parse tid, aggregere måned til kvartal, koble to serier og beregne et enkelt mål |
| 45 | HTTP, JSON, `requests`, SSB og Eurostat | Bygge parametere; tolke lokal JSON; gjøre et kjent API-svar om til DataFrame uten levende nettverk |
| 46 | scikit-learn, splitting, regresjon, evaluering, SVM og k-means | Stillasbygd workflow med fast datasett; valgfri utfordring for interesserte studenter |
| 47 | GDPR, informasjonsverdi, sikkerhet og dataanalyseverksted | Korte kontrollspørsmål passer bedre enn programmeringsoppgaver; ikke la CodeRunner erstatte refleksjon |

Workshopene ligger på torsdager i uke 41 og 47. Ikke legg ordinære
CodeRunner-frister slik at de konkurrerer med workshopforberedelsen.

## Definisjon av ferdig oppgave

En CodeRunnerHero-oppgave er ikke ferdig før:

- læringsmål, uke og forkunnskaper er dokumentert
- studentteksten har presis kontrakt og forståelige eksempler
- referanseløsningen består alle tester
- minst én realistisk feilbesvarelse feiler med nyttig norsk tilbakemelding
- relevante grensetilfeller er testet
- testen er deterministisk og har rimelig timeout
- `make test1` og eventuelle andre `make testN` fullfører
- `make grade` gir riktig poeng og resultattabell
- `make all` fullfører
- `make xml` fullfører når oppgaven skal importeres som XML
- genererte filer ikke er håndredigert eller lagt til som kildemateriale
- interaktive flertrinnsoppgaver er prøvd med `make web` og senere i faktisk
  Moodle-miljø

Ved overlevering skal Codex oppgi:

- hvilken uke og hvilket læringsmål oppgaven støtter
- hvilken oppgavemappe som er opprettet eller endret
- hvilke korrekte og mangelfulle svar som er prøvd
- hvilke bygge- og testkommandoer som er kjørt
- eventuelle forutsetninger om Moodle-sandbox, pakker eller datafiler
