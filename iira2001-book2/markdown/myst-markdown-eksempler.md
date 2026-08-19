---
bibliography:
  - myst-referanser.bib
kernelspec:
  name: python3
  display_name: Python 3
numbering:
  headings: true
  figure: true
  table: true
  code: true
  equations: true
abbreviations:
  API: Application Programming Interface
  CSV: Comma-Separated Values
  GDPR: General Data Protection Regulation
  HTML: HyperText Markup Language
  JSON: JavaScript Object Notation
---

# MyST Markdown: et demonstrasjonskapittel

Dette kapitlet er både et **oppslagsverk** og en **lekeplass**. Det viser
hvordan vanlig Markdown og MyST-utvidelser faktisk ser ut i denne Jupyter
Book-boken. Eksemplene er med vilje mer omfattende enn det man vanligvis vil
bruke i ett kapittel.

:::{important} Bruk kapittelet som et utstillingsvindu
Kopier et mønster du liker, bytt ut innholdet og bygg boken på nytt. Det er
lettere enn å huske alle direktivnavnene og alternativene.
:::

{button}`Offisiell MyST-guide <https://mystmd.org/guide>`
{button}`Gå til figurdemoen <#myst-bilder-og-figurer>`
{button}`Last ned BibTeX-filen <myst-referanser.bib>`

:::{dropdown} Hva er forskjellen på Markdown, MyST og Jupyter Book?
**Markdown** gir grunnsyntaksen for tekst, lister, lenker og kode.
**MyST Markdown** legger til direktiver, roller, kryssreferanser, matematikk,
siteringer og rike sideelementer. **Jupyter Book 2** bygger MyST-filer og
notebooks til en samlet bok eller nettside.
:::

## Grunnleggende typografi

Vanlig tekst kan inneholde *kursiv*, **fet tekst**, ***fet kursiv***,
{del}`gjennomstreking`, {u}`understreking`, {sc}`kapitéler` og
`kode skrevet i teksten`. En eksplisitt linjeskift kan lages med to mellomrom
på slutten av linjen.  
Da starter denne setningen på ny linje uten et nytt avsnitt.

Du kan lenke til [NTNU](https://www.ntnu.no), vise en URL direkte som
<https://mystmd.org>, eller lenke til [fremdriftsplanen](./fremdrift.md).
En tom intern lenketekst, `[](./fremdrift.md)`, lar MyST hente sidetittelen:
[](./fremdrift.md).

MyST har også små roller i løpende tekst:

- tastatur: {kbd}`Ctrl+Shift+P`
- senket tekst: H{sub}`2`O
- hevet tekst: 10{sup}`3`
- eksplisitt forkortelse: {abbr}`SSB (Statistisk sentralbyrå)`
- automatisk forkortelse fra frontmatter: API, CSV, JSON, HTML og GDPR

::::{dropdown} Vis koden for rollene
```markdown
{kbd}`Ctrl+Shift+P`
H{sub}`2`O
10{sup}`3`
{abbr}`SSB (Statistisk sentralbyrå)`
{del}`gjennomstreket`
{u}`understreket`
{sc}`kapitéler`
```
::::

### Lister

En punktliste kan ha flere nivåer:

- Dataanalyse
  - lese data
  - vaske data
  - visualisere data
- Simulering
  - modell
  - tilfeldighet
  - gjentakelse

En nummerert prosedyre:

1. Formuler en problemstilling.
2. Skaff data.
3. Undersøk datakvaliteten.
4. Analyser og formidle.

En oppgaveliste:

- [x] Opprett bokprosjekt
- [x] Legg inn et MyST-kapittel
- [ ] Bytt ut demonstrasjonsteksten med kursinnhold

### Definisjonslister

Variabel
: Et navn som peker på en verdi.

Funksjon
: En navngitt og gjenbrukbar del av et program.

Parameter
: Et navn i funksjonsdefinisjonen.

Argument
: Verdien som sendes inn når funksjonen kalles.

### Sitater, epigrafer og fremhevede sitater

> Data er ikke automatisk innsikt.
>
> Innsikten oppstår når data tolkes i en faglig sammenheng.

:::{epigraph}
Alle modeller er forenklinger. Det viktige er om forenklingen hjelper oss å
tenke klarere.
:::

:::{pull-quote}
Kode er også formidling: navn, struktur og forklaring er en del av analysen.
:::

En horisontal skillelinje:

---

## Admonitions: merknader og varselbokser

MyST har ti navngitte standardtyper. Farge og ikon bestemmes av typen.

::::{grid} 1 1 2 2
:::{note} Note
Et nøytralt tillegg eller en presisering.
:::

:::{important} Important
Noe leseren må få med seg.
:::

:::{hint} Hint
Et lite dytt i riktig retning.
:::

:::{seealso} See also
Peker mot beslektet fagstoff.
:::

:::{tip} Tip
Et praktisk råd som gjør arbeidet enklere.
:::

:::{attention} Attention
Dette krever litt ekstra oppmerksomhet.
:::

:::{caution} Caution
Her er det lett å gjøre en feil.
:::

:::{warning} Warning
Et tydelig varsel før man går videre.
:::

:::{danger} Danger
En alvorlig fallgruve.
:::

:::{error} Error
Viser en konkret feil eller en ugyldig løsning.
:::
::::

En boks kan få egen tittel, skjule ikonet og bruke en enklere stil:

:::{admonition} En selvvalgt tittel
:class: tip simple
:icon: false

Dette er den generelle `admonition`-varianten med klassene `tip` og
`simple`.
:::

::::{dropdown} Vis grunnsyntaksen
```markdown
:::{tip} En valgfri tittel
Dette er innholdet i boksen.
:::

:::{admonition} En helt egen tittel
:class: warning simple
:icon: false

Her kommer innholdet.
:::
```
::::

## Dropdowns og skjulte løsningsforslag

:::{dropdown} En vanlig dropdown
Innholdet er skjult fram til leseren klikker. Her kan man ha tekst, lister,
matematikk som $2 + 2 = 4$, og kode:

```python
def dobbelt(x):
    return 2 * x
```
:::

:::{dropdown} Denne starter åpen
:open: true

Alternativet `:open: true` gjør innholdet synlig ved innlasting.
:::

:::{note} En admonition som også er en dropdown
:class: dropdown

Klassen `dropdown` kan legges på en vanlig admonition. Dette passer godt for
hint og korte fasiter.
:::

:::{tip} Åpen nå, men kan lukkes
:class: dropdown
:open: true

Kombiner `:class: dropdown` og `:open: true`.
:::

## Kort, grids og «decks»

En kortstokk eller et «card deck» lages som et responsivt `grid` med
`card`-elementer. Tallene etter `grid` er antall kolonner ved ulike
skjermbredder.

::::{grid} 1 1 2 3
:::{card} Variabler
:header: Grunnmur 🧱
:footer: Uke 34

Lagre tall, tekst og andre verdier under forståelige navn.
:::

:::{card} Funksjoner
:header: Gjenbruk ♻️
:footer: Uke 35

Samle en beregning og gjør forutsetningene til parametere.
:::

:::{card} Pandas
:header: Data 📊
:footer: Fra uke 40

Les, vask, transformer og oppsummer tabulære data.
:::
::::

Et helt kort kan være klikkbart:

:::{card} Åpne den offisielle MyST-guiden
:link: https://mystmd.org/guide
:header: Ekstern ressurs
:footer: mystmd.org

Klikk hvor som helst på kortet.
:::

Et asymmetrisk grid kan styre bredden på hvert element:

::::{grid} 1 1 12 12
:::{grid-item}
:columns: 4

**Smalt felt**

Passer til nøkkeltall, definisjoner eller navigasjon.
:::

:::{grid-item}
:columns: 8

**Bredt felt**

Passer til forklaring, kode, tabeller eller figurer som trenger mer plass.
:::
::::

:::::{dropdown} Vis koden for en kortstokk
```markdown
::::{grid} 1 1 2 3
:::{card} Kort 1
:header: Overskrift
:footer: Bunntekst

Innhold.
:::

:::{card} Kort 2
Mer innhold.
:::
::::
```
:::::

## Faner og synkroniserte tabs

::::{tab-set}
:::{tab-item} Python
:sync: programmeringssprak
:selected: true

```python
verdier = [10, 20, 30]
sum(verdier)
```
:::

:::{tab-item} Regneark
:sync: regneark

Skriv verdiene i tre celler og bruk `=SUMMER(A1:A3)`.
:::

:::{tab-item} Forklaring
Faner er nyttige når samme idé skal vises på flere måter uten at siden blir
veldig lang.
:::
::::

Valget kan synkroniseres med en annen fanegruppe ved å gjenbruke samme
`:sync:`-verdi:

::::{tab-set}
:::{tab-item} Python
:sync: programmeringssprak

I Python bruker vi ofte funksjoner og datastrukturer.
:::

:::{tab-item} Regneark
:sync: regneark

I regneark bruker vi ofte cellereferanser og formler.
:::
::::

(myst-bilder-og-figurer)=
## Bilder, figurer og underfigurer

### Vanlig Markdown-bilde

![NTNU-logo med vanlig Markdown-syntaks](../images/NTNU-logo.png "NTNU")

### Bildedirektivet

:::{image} ../images/NTNU-logo.png
:alt: NTNU-logo
:width: 280px
:align: center
:title: Et bilde med eksplisitt bredde og alternativ tekst
:::

### Nummerert figur med bildetekst

:::{figure} ../images/NTNU-logo.png
:label: myst-demo-figur
:alt: NTNU-logo brukt i en MyST-figur
:width: 320px
:align: center

En nummerert figur med **formatert bildetekst**, alternativ tekst og en label.
:::

Vi kan nå henvise automatisk til [](#myst-demo-figur), skrive
[figur {number}](#myst-demo-figur), eller bruke kortformen @myst-demo-figur.

### Flere bilder i én figur

:::{figure}
:label: myst-demo-underfigurer
:align: center

![Lys logovariant](../images/NTNU-logo.png)

![Mørk logovariant](../images/NTNU-logo-dark.png)

Lys og mørk variant samlet i én figur. Delene kan få bokstavnummerering i
utdataformater som støtter underfigurer.
:::

::::{dropdown} Vis koden for en kryssrefererbar figur
```markdown
:::{figure} ../images/NTNU-logo.png
:label: min-figur
:alt: Beskrivende alternativ tekst
:width: 320px
:align: center

Bildeteksten står her.
:::

Se [](#min-figur).
```
::::

## Tabeller

### Enkel pipe-tabell

| Variabel | Verdi | Enhet |
| :--- | ---: | :---: |
| Pris | 125.00 | kr |
| Antall | 40 | stk. |
| Inntekt | 5000.00 | kr |

Kolonene kan venstrejusteres, høyrejusteres eller sentreres i skillelinjen.

### Tabell med bildetekst, label og referanse

:::{table} Eksempel på beskrivende statistikk
:label: myst-demo-tabell
:align: center

| Mål | Observasjoner | Gjennomsnitt | Median |
| --- | ---: | ---: | ---: |
| Inntekt | 120 | 542 000 | 510 000 |
| Sparing | 120 | 38 500 | 31 200 |
:::

Tabellen kan omtales som [](#myst-demo-tabell) eller
[tabell {number}](#myst-demo-tabell).

### List-table

:::{list-table} Resultat fra tre scenarioer
:header-rows: 1
:label: myst-demo-list-table

* - Scenario
  - Vekstrate
  - Sluttverdi
* - Lav
  - 0.02
  - 1104
* - Basis
  - 0.05
  - 1276
* - Høy
  - 0.08
  - 1469
:::

### CSV-table

:::{csv-table} Et lite datasett skrevet direkte som CSV
:header: "Produkt", "Pris", "Antall"
:label: myst-demo-csv-table

"Kaffe", 39.90, 12
"Te", 34.50, 8
"Kakao", 42.00, 5
:::

## Kode for visning

En vanlig kodeblokk gir syntaksfarging, men blir ikke kjørt:

```python
def beregn_inntekt(pris, antall):
    return pris * antall
```

Et `code`-direktiv kan få filnavn, linjenummer, markering, bildetekst og label:

```{code} python
:filename: analyse.py
:linenos:
:emphasize-lines: 2,5-6
:caption: En liten funksjon med et eksempel på bruk
:label: myst-demo-kode

def prosentvis_endring(gammel, ny):
    endring = ny - gammel
    andel = endring / gammel
    prosent = andel * 100
    return prosent

print(prosentvis_endring(100, 115))
```

Vi kan henvise til [](#myst-demo-kode).

### Inkluder kode fra en fil

Dette utdraget leses direkte fra bokas `myst.yml`, så eksemplet oppdateres når
konfigurasjonen endres:

```{literalinclude} ../myst.yml
:filename: myst.yml
:language: yaml
:start-at: project:
:end-before: site:
:linenos:
```

## Kjørbare kodeceller i Markdown

En MyST-fil kan også fungere som en tekstbasert notebook. Denne cellen blir
kjørt når boken bygges med `--execute`:

```{code-cell} python
:label: myst-demo-kodecelle
:linenos:

priser = [49.90, 125.00, 79.50]
gjennomsnittspris = sum(priser) / len(priser)
round(gjennomsnittspris, 2)
```

Uten `--execute` vises cellen, men det genereres ikke et nytt resultat. En
side med kodeceller trenger `kernelspec` i frontmatter, slik dette kapittelet
har.

::::{dropdown} Bygg og kjør kodecellene
```bash
uv run jupyter book build --html --execute
```

Inline-resultater kan settes inn med `{eval}`-rollen når siden er kjørt, for
eksempel `{eval}`gjennomsnittspris``.
::::

## Matematikk og ligninger

Inline matematikk kan skrives med dollartegn, $r = 0.05$, eller med rollen
{math}`K_1 = K_0(1+r)`.

En frittstående ligning:

:::{math}
:label: myst-demo-rentesrente

K_n = K_0(1+r)^n
:::

Se [](#myst-demo-rentesrente), eller skriv
[ligning {number}](#myst-demo-rentesrente).

Flere linjer og justering:

$$
\begin{aligned}
I &= p \cdot q \\
K &= c \cdot q + F \\
\pi &= I - K
\end{aligned}
$$

En matrise:

$$
X =
\begin{bmatrix}
1 & x_1 \\
1 & x_2 \\
1 & x_3
\end{bmatrix}
$$

:::{tip}
Bruk `\$` når du faktisk mener et dollartegn, for eksempel \$125, og ikke
vil starte et matematikkuttrykk.
:::

## Kryssreferanser og labels

(myst-demo-maal)=
### Et navngitt mål

En label plasseres på linjen før overskriften. Deretter kan vi lenke til
[](#myst-demo-maal), skrive [avsnittet «{name}»](#myst-demo-maal), eller bruke
kortformen @myst-demo-maal.

Labels kan også settes direkte på direktiver med `:label:`. Det er brukt på
figuren, tabellene, ligningen og kodeblokken over. Samme referansesyntaks virker
på tvers av innholdstyper.

::::{dropdown} Vis referansesyntaks
```markdown
(mitt-avsnitt)=
## En overskrift

Se [](#mitt-avsnitt).
Se [avsnittet «{name}»](#mitt-avsnitt).
Se @mitt-avsnitt.
```
::::

## Fotnoter

En kort kommentar kan flyttes ut av hovedteksten med en fotnote.[^fotnote-demo]
Fotnoter kan også inneholde flere avsnitt, lister og annen Markdown.[^rik-fotnote]

[^fotnote-demo]: Fotnoten får automatisk nummer og vises nederst på siden eller
    som en forhåndsvisning i nettløsningen.

[^rik-fotnote]: Dette er første avsnitt i en rik fotnote.

    - Den kan ha en liste.
    - Den kan ha *formatert tekst*.

    Den kan også ha flere avsnitt når fortsettelsen rykkes inn.

## Kilder, siteringer og litteraturliste

En narrativ henvisning skrives slik: @mckinney2010 introduserte sentrale
datastrukturer for statistisk arbeid i Python. En parenteshenvisning ser slik
ut [@downey2024]. Flere kilder kan samles i samme parentes
[@mckinney2010; @mystmd2026].

Det kan også legges til prefiks og sidetall
[se for eksempel @downey2024, kap. 2]. BibTeX-filene angis i sidens
frontmatter, og litteraturlisten genereres automatisk nederst på siden.

::::{dropdown} Vis siteringssyntaks
```yaml
---
bibliography:
  - myst-referanser.bib
---
```

```markdown
@mckinney2010
[@downey2024]
[@mckinney2010; @mystmd2026]
[se @downey2024, kap. 2]
```
::::

BibTeX-filen kan tilbys direkte som en nedlasting:
{download}`myst-referanser.bib`.

## Ordliste, termer og indeks

:::{glossary}
DataFrame
: En todimensjonal pandas-datastruktur med navngitte rader og kolonner.

API
: Et grensesnitt som gjør at programmer kan kommunisere på en avtalt måte.

Reproduserbar analyse
: En analyse der datagrunnlag, kode og valg er dokumentert slik at resultatet
  kan gjenskapes.
:::

Når en term er definert, kan den brukes med hover-forklaring og lenke:
{term}`DataFrame`, {term}`API` og
{term}`reproduserbarhet <Reproduserbar analyse>`.

:::{index} pandas; DataFrame
:::

:::{index}
pair: data; reproduserbarhet
single: API
:::

`index`-direktivet lager skjulte registeroppføringer. En egen indeksside kan
vise alle oppføringene:

```markdown
:::{show-index}
:::
```

::::{dropdown} Vis ordlistesyntaks
```markdown
:::{glossary}
DataFrame
: En todimensjonal pandas-datastruktur.
:::

Les mer om {term}`DataFrame`.

:::{index} pandas; DataFrame
:::
```
::::

## Inline-attributter og CSS-klasser

Alternativer kan skrives kompakt i direktivets eller rollens åpningslinje.
Dette er nyttig ved prototyping, men funksjonen regnes fortsatt som beta:

{span .text-red-600}`Denne teksten får en CSS-klasse for rød tekst.`

:::{tip .dropdown open=true} Kompakt direktivsyntaks
Denne boksen kombinerer klassene og alternativene direkte i åpningslinjen:
`:::{tip .dropdown open=true}`.
:::

```markdown
{span #min-id .text-red-600}`Rød tekst med ID og klasse.`

:::{tip .dropdown open=true} Tittel
Skjult innhold som starter åpent.
:::
```

## Øvinger og løsninger

:::{exercise}
:label: myst-demo-oving

Skriv en funksjon `beregn_inntekt(pris, antall)` som returnerer produktet av
de to parameterne. Prøv funksjonen med minst to ulike argumentpar.
:::

:::{solution} myst-demo-oving
:label: myst-demo-losning
:class: dropdown

```python
def beregn_inntekt(pris, antall):
    return pris * antall

print(beregn_inntekt(125, 40))
print(beregn_inntekt(79.90, 12))
```
:::

Se [](#myst-demo-oving). Løsningen kobles til øvingen ved at
`solution`-direktivet får øvingens label som argument. Klassen `dropdown`
gjør at fasiten ikke vises med en gang.

## Definisjoner, teoremer, bevis og algoritmer

:::{proof} Definisjon: Dekningsbidrag
:label: myst-demo-definisjon

Dekningsbidrag er salgsinntekt minus variable kostnader:
$DB = p\cdot q - c\cdot q$.
:::

:::{proof} Påstand: Lineær skalering
:label: myst-demo-proposisjon

Hvis pris og enhetskostnad er konstante, skalerer totalt dekningsbidrag lineært
med antall solgte enheter.
:::

:::{proof}
:label: myst-demo-bevis

Vi faktoriserer antall enheter:

$$
DB = p q - c q = (p-c)q.
$$

Når $p-c$ er konstant, er uttrykket lineært i $q$.
:::

:::{proof} Algoritme: Gjennomsnitt
:label: myst-demo-algoritme

**Inndata:** en ikke-tom liste med tall.

1. Summer tallene.
2. Tell antall tall.
3. Del summen på antallet.
4. Returner resultatet.
:::

:::{caution} Navngitte proof-varianter er versjonsavhengige
MyST-spesifikasjonen beskriver blant annet `proof:definition`,
`proof:theorem`, `proof:proposition` og `proof:algorithm`. Jupyter Book
2.1.6 markerer foreløpig disse som ukjente, mens det generelle `proof`-
direktivet over fungerer. Syntaksen som er ment å brukes når variantene er
tilgjengelige, er:

```markdown
:::{proof:theorem} Teoremets tittel
:label: mitt-teorem

Innholdet i teoremet.
:::
```
:::

## Mermaid-diagrammer

Mermaid egner seg til flytdiagrammer uten egne bildefiler:

```{mermaid}
:label: myst-demo-mermaid

flowchart LR
    A[Problemstilling] --> B[Data]
    B --> C{God datakvalitet?}
    C -- Nei --> D[Vask data]
    D --> C
    C -- Ja --> E[Analyse]
    E --> F[Formidling]
```

Et sekvensdiagram:

```{mermaid}
sequenceDiagram
    participant Student
    participant Notebook
    participant API
    Student->>Notebook: Kjør kode
    Notebook->>API: HTTP-forespørsel
    API-->>Notebook: JSON-data
    Notebook-->>Student: Tabell og figur
```

## Sideinnhold, tema og egne blokker

:::{aside} En merknad i margen
Dette er indirekte relevant stoff. I brede visninger kan temaet plassere det i
margen; i smale visninger flyttes det inn i tekstflyten.
:::

:::{topic} Et selvstendig sidetema
Et `topic` er en liten, selvstendig seksjon som er skilt fra hovedfortellingen.
Den kan inneholde lister, kode og andre elementer.
:::

:::{div}
:class: col-page-right

Denne `div`-blokken har CSS-klassen `col-page-right`, som boktemaet kan bruke
til å la innholdet strekke seg inn i høyremargen.
:::

## Gjenbruk: include, literalinclude og embed

### Inkluder en separat MyST-fil

```{include} myst-inkludert-snutt.md
```

Kildekoden kan i stedet vises bokstavelig:

```{literalinclude} myst-inkludert-snutt.md
:filename: myst-inkludert-snutt.md
:language: markdown
:linenos:
```

### Gjenbruk et allerede merket element

:::{note} En gjenbrukbar forklaring
:label: myst-demo-gjenbrukbar

Et element med label kan refereres til eller bygges inn et annet sted.
:::

Her bygges innholdet inn på nytt:

:::{embed} #myst-demo-gjenbrukbar
:::

Forskjellen er at `include` leser en kildefil, mens `embed` gjenbruker et
element som MyST allerede har tolket og gitt en label.

## Innebygd video og nettside

:::{iframe} https://www.youtube.com/embed/F3st8X0L1Ys
:width: 100%
:title: Introduksjon til MyST Markdown
:align: center

En innebygd video med `iframe`-direktivet. I statiske eksportformater blir
bildeteksten stående selv om selve rammen ikke kan vises.
:::

::::{dropdown} Vis iframe-syntaksen
```markdown
:::{iframe} https://www.youtube.com/embed/F3st8X0L1Ys
:width: 100%
:title: Beskrivende tittel for tilgjengelighet
:placeholder: et-lokalt-bilde.png

En bildetekst eller forklaring.
:::
```
::::

Lokale MP4-filer kan også settes inn med vanlig bildesyntaks,
`![](video.mp4)`, eller legges i et `figure`-direktiv for å få bildetekst og
referanse.

## HTML når Markdown ikke strekker til

MyST kan slippe gjennom enkel HTML i HTML-utgaven av boken:

<details>
<summary>Et HTML-element med details/summary</summary>
<p>Dette er nyttig for små eksperimenter, men MyST-direktiver gir vanligvis
bedre eksport til PDF, Word og andre formater.</p>
</details>

Du kan også bruke <mark>markert tekst</mark>, <kbd>Ctrl</kbd> +
<kbd>Enter</kbd> og eksplisitte linjeskift med <code>&lt;br&gt;</code>.

:::{warning}
Rå HTML er mindre portabelt enn MyST. Bruk først MyST-direktiver når innholdet
også skal kunne eksporteres til andre formater enn HTML.
:::

## Kommentarer, blokker og sideskift

En linje som starter med prosenttegn er en MyST-kommentar og vises ikke:

% Denne kommentaren finnes i kildefilen, men ikke i den ferdige siden.

```markdown
Synlig tekst.
% En kommentar som ikke blir vist.
Mer synlig tekst.
```

`+++` deler en tekstbasert notebook i blokker eller celler. Metadata kan
festes til blokken:

```markdown
+++ {"cell": "introduksjon"}
Første innholdsblokk.

+++ {"cell": "analyse", "tags": ["viktig"]}
Andre innholdsblokk.
```

Et sideskift for PDF- eller Word-eksport kan markeres slik:

```markdown
+++ {"page-break": true}
```

## Frontmatter og sideinnstillinger

YAML-frontmatter står helt øverst i filen og kan styre metadata og gjengivelse:

```yaml
---
title: Eksempelkapittel
description: En kort beskrivelse for metadata og søk
authors:
  - name: Ola Nordmann
bibliography:
  - referanser.bib
kernelspec:
  name: python3
  display_name: Python 3
numbering:
  headings: true
  figure: true
abbreviations:
  SSB: Statistisk sentralbyrå
---
```

Globale valg hører hjemme under `project:` eller `site:` i `myst.yml`.
Side-frontmatter brukes når valget bare gjelder ett kapittel.

## En liten formatoppskrift

::::{grid} 1 1 2 2
:::{card} Forklaring
Bruk vanlig Markdown, korte avsnitt og en figur eller tabell med label.
:::

:::{card} Oppgave
Bruk `exercise` og en skjult `solution`.
:::

:::{card} Alternativer
Bruk tabs når innholdet er parallelt, og dropdown når det er valgfritt.
:::

:::{card} Navigasjon
Bruk labels og tomme MyST-lenker slik at nummer og tittel oppdateres automatisk.
:::
::::

:::{tip} En god tommelfingerregel
Velg element etter mening, ikke bare utseende: `warning` for et faktisk
varsel, `exercise` for en oppgave, `figure` for noe som skal ha bildetekst,
og `dropdown` for valgfri fordypning.
:::

## Nyttige ressurser

- [MyST Markdown-guiden](https://mystmd.org/guide)
- [Oversikt over direktiver](https://mystmd.org/guide/directives)
- [Jupyter Book-dokumentasjonen](https://jupyterbook.org)
- [Mermaid-dokumentasjonen](https://mermaid.js.org)
- {download}`BibTeX-filen brukt på denne siden <myst-referanser.bib>`

Litteraturlisten nedenfor er laget automatisk fra henvisningene i kapittelet.
