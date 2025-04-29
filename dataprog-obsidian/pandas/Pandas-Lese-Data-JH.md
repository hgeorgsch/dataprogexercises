---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.17.0
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

# Hente og lese inn data til pandas

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

## CSV 

* En vanlig måte å lagre data på er i csv-format
* csv = comma separated values
* I en csv-fil har vi data lagret som tekst i en type tabellformat
* Hver linje i filen er et datapunkt, og inneholder et eller flere felt med data (kolonner)
* Datafeltene er separert med en *separator*, ofte et komma
* Første linje i filen gir gjerne metadata (navn på kolonnene)

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

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

#### SSB
* SSB bruker 'UTF-8' for .XML og JSON formater (mer om JSON senere)
* SSB bruker 'ISO-8859-1' for .csv formatene sine

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

## CSV + Pandas

* Vi bruker pandas til å lese og lagre csv-filer
* `pd.read_csv("filnavn")`
* `read_csv` har **haugevis** med keyword arguments for å lese rare og potensielt føkka csv-filer
* Vi burde i de fleste tilfeller klare oss med:
    - `encoding = "input-enc"` feks `"utf-8"`
    - `sep = "separator"` feks `","` eller "`\t`" (tab)
    -  `header = rad` feks `header=0`dersom første rad gir kolonnenavnene
    -  `index_col = «kolonnenummer»` Angir hvilken av kolonnene som skal brukes som indeks (nummer eller etikette) 

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: subslide
---
import pandas as pd

BB_df= pd.read_csv("blackboard.csv", encoding="utf-16", sep="\t")
BB_df = BB_df.set_index("Unnamed: 0")
BB_df.index.name = None


#Alternativt
BB_df= pd.read_csv("blackboard.csv", encoding="utf-16", sep="\t", index_col=0)
BB_df
```

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

* Filen vi har lastet inn er klasselisten fra blackboard
* på iirmoodle.it.ntnu.no er det mulig å melde folk opp i fag ved å laste *opp* en csv-fil
* `moodle_example.csv` viser hvordan denne filen skal se ut

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
moodleEx_df = pd.read_csv("moodle_example.csv")
moodleEx_df
```

+++ {"slideshow": {"slide_type": "slide"}}

### Opppgave 1

* Lag et dataframe fra "blackboard.csv" som er formatert slik moodle vil ha det

```{code-cell} ipython3
---
slideshow:
  slide_type: subslide
---
data = {"username": BB_df["Brukernavn"], "firstname": BB_df["Fornavn"], "lastname": BB_df["Etternavn"]}
datatest = pd.DataFrame(data)

#Med for-løkke
#ny_data = []
#for bruker in datatest["username"]:
#    ny_data.append(f"{bruker}@stud.ntnu.no")
#datatest["email"] = ny_data

#Med listekomprehensjon
#datatest["email"] = [f"{bruker}@stud.ntnu.no" for bruker in data["username"]]

#Med apply/map:
#datatest["email"] = datatest["username"].apply(lambda bruker: f"{bruker}@stud.ntnu.no")

#Med pandas sin serialisering av dataseries
datatest["email"] = datatest["username"]+"@stud.ntnu.no"
datatest
```

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

* Vi lagrer et dataframe til csv med `df.to_csv("filnavn.csv", **kwargs)`
* når vi ser `**kwargs` på denne måten, betyr det at her kommer «keyword arguments»
* Vi kan se i [dokumentasjonen](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html) får å finne hvilke «kwargs» funksjonen tar

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
datatest.to_csv("moodle_formatert.csv", index=False)
```

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

* Det er mye å holde styr på i Pandas, og vi går ikke igjennom alle aspekter
* Ha en [cheat sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf) for hånden
* Slå opp i diverse [tutorials](https://pandas.pydata.org/pandas-docs/stable/getting_started/tutorials.html)
* Spesielt [denne](https://www.skytowner.com/explore/pandas_recipes_reference) kan være kjekk (Pandas oppskrifter :) )

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

# Pandas i praksis

* Vi kan hente data å analysere, feks fra [statistisk sentralbyrå](http://www.ssb.no)
* SSB bruker tegnkodinger «UTF-8» og «ISO-8859-1»

```{code-cell} ipython3
---
slideshow:
  slide_type: subslide
---
#Vi går til ssb.no og henter et datasett om arbeidsledige
arbeidsledige_df = pd.read_csv("arbeidsledige.csv", sep=";", header=1, index_col=0)

arbeidsledige_df.index.name = None

#Legger til kolonne med arbeidsledighet i prosent

#med apply og lambdafunksjon
#arbeidsledige_df["prosent"] = arbeidsledige_df["Arbeidsledige (1 000 personer)"].apply(lambda x: f"{x/1000:.2%}") 

#Med serialisering/vektorisering
arbeidsledige_df["prosent"] = arbeidsledige_df["Arbeidsledige (1 000 personer)"]/1000

arbeidsledige_df["Arbeidsledige (1 000 personer)"].plot()
arbeidsledige_df.describe()
display(arbeidsledige_df) #Vi kan bruke display istedet for print for en "fin" tabell
arbeidsledige_df = arbeidsledige_df.drop("prosent", axis=1)
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: subslide
---
# Vi henter et datasett med åpnede konkurser fra SSB
konkurser_df = pd.read_csv("konkurser.csv", encoding="ISO-8859-1", sep="\t", index_col = 0)
konkurser_df.index.name=None
konkurser_df
```

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

### Analyse:
* Vi vil slå sammen dataene våre om arbeidsledighet og åpnede konkurser
* Er det en sammenheng?

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: fragment
---
konkurser_df+arbeidsledige_df #Det funket dårlig....
```

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

# Slå sammen data
Vi må passe på en rekke ting når vi skal slå sammen data:
* Matchende datatyper: 2 kolonner blir ansett som forkjellige dersom de har forskjellige datatyper men matchende data
* Hva skal vi beholde (Alt som matcher, kun matchende data fra nr 1 eller 2 dataframe)
* Dersom man slår sammen på index, må disse samsvare

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

* Vi trenger nå å slå sammen data som går over forskjellige tidsspenn
* Indeksen vår består av *tekststrenger* -- dette byr på problemer

<img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgCOoEr1biiaMsoejCtfdvgJAq_T6TfbjVkrc-zyfJ8ReSf8BvldJXPjyNy1gjfGVmB2hk2i39ybpaLHKDK4kTn4n2Zh-dXlaayliZoiygxhTQ3W7mC2LoxzTOARAhltRmSn84pdQdmqrbu/s1600/AD951881-737E-4F2C-AE8E-D80E280CFFD5.png">

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

## Datetime, pandas.Period
* Veldig mye av data tilgjengelig viser statistiske variabler over tid.
* For ingeniører er tid veldig enkelt: Det er en fysisk størrelse og en av grunnenhetene i SI-system: *sekund*
* I business er det verre. Vi måler tid i dager, sekunder, minutter, uker, måneder, kvartaler eller år
* År er delt inn i måneder med ujevnt fordelte dager, vi har skuddår og tidssoner, sommertid/vintertid osv...
* Vi kan få masse hjelp dersom tidsseriene vår bruker datatyper for tid fra `datetime` eller `pandas.Period`

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: subslide
---
#Jeg måtte gjøre følgende for å få norsk output
#import locale
#locale.setlocale(locale.LC_ALL, "nb_NO.utf8")
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: subslide
---
import datetime
from zoneinfo import ZoneInfo
#Henter tid/dato fra datetime.datetime
dato_og_tid = datetime.datetime.now()

#Henter dato fra datetime.date
dato = datetime.date.today()

print("I dag er datoen", dato)
print("Mer nøyaktig er vi nå", dato_og_tid)
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: subslide
---
#Vi kan lage et spesifikt tidspunkt eller dato:

min_dato = datetime.date(1990,4, 23) #År, måned, dag
print("Jeg valgte dato: ", min_dato)

tid = datetime.datetime(2024,12,13,12, tzinfo=ZoneInfo("Europe/Oslo")) #År, måned, dag, time, minutt, sekund, tzinfo=TIDSSONE
print("Mappeinnlevering stenger", tid)

#Vi kan også lage en ENDRING I TID:
#datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
utsettelse = datetime.timedelta(days=1, hours=4)
ny_tid = tid+utsettelse
print("Ny tid for mappeinnlevering:", ny_tid)

#Vi kan sammenligne tider/datoer
print(ny_tid > tid)
```

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

* Fordelen med en slik datatype er at biblioteket selv kan holde kontroll på tidssoner og denslags
* Biblioteket lar oss plusse/trekke fra tider eller datoer med hverandre
* Vi kan sammenligne tid/datoer som betyr at vi lett kan sortere de

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

# Formattere dato ut
* vi bruker `min_tid.strftime("FORMATTERINGSSTRENG")` for å formatere en dato eller tid
* Formateringsstrenger er litt som en f-streng, men vi limer inn feks året for `"%Y"` i stedet for `f"{year}"`
  | Formatkode | Beskrivelse                            | Eksempel (med dato: 2024-10-21 15:30:45) |
|------------|----------------------------------------|------------------------------------------|
| `%a`       | Forkortet ukedag                       | Man                                      |
| `%A`       | Fullt navn på ukedag                   | Mandag                                   |
| `%w`       | Ukedag som tall (Søndag=0, Mandag=1)   | 1                                        |
| `%d`       | Dag i måneden (nullutfylt)             | 21                                       |
| `%b`       | Forkortet månednavn                    | Okt                                      |
| `%B`       | Fullt månednavn                        | Oktober                                  |
| `%m`       | Måned som tall (nullutfylt)            | 10                                       |
| `%y`       | År (to siffer)                         | 24                                       |
| `%Y`       | År (fire siffer)                       | 2024                                     |
| `%H`       | Time (nullutfylt, 24-timers klokke)    | 15                                       |
| `%I`       | Time (nullutfylt, 12-timers klokke)    | 03                                       |
| `%p`       | AM/PM                                 | PM                                       |
| `%M`       | Minutter (nullutfylt)                  | 30                                       |
| `%S`       | Sekunder (nullutfylt)                  | 45                                       |
| `%f`       | Mikrosekunder (nullutfylt)             | 000000                                   |
| `%z`       | Tidsforskjell fra UTC                  | +0000                                    |
| `%Z`       | Tidsnavn (timezone)                    | UTC                                      |
| `%j`       | Dagnummer i året (001-366)             | 295                                      |
| `%U`       | Ukenummer (Søndag som første dag)      | 43                                       |
| `%W`       | Ukenummer (Mandag som første dag)      | 43                                       |
| `%c`       | Lokal dato og tid                      | Man 21 Oct 15:30:45 2024                 |
| `%x`       | Lokal dato (kort format)               | 21.10.2024                               |
| `%X`       | Lokal tid (kort format)                | 15:30:45                                 |
| `%%`       | Et prosenttegn                        | %                                        |

```{code-cell} ipython3
print("Mappen skal leveres: ", ny_tid.strftime("Senest klokken %H:%M %A den %d."))
print(ny_tid.strftime("%c"))
```

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

## Lese inn et datoformat
* Enda mer nyttig er det å kunne lese inn tid/dato skrevet i rare formater
* Da bruker vi samme tabell som for `strftime`, men bruker `datetime.datetime.strptime(dato, "FORMATERINGSSTRENG")`

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: fragment
---
dato_inn = "21/04/1987"
dato_lest = datetime.datetime.strptime(dato_inn, "%d/%m/%Y")
print("Dato som datetime objekt:", dato_lest)
```

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

## Pandas.period
* Pandas har en egen klasse/type for å jobbe med perioder og tidsintervall
* Vi jobber da med spenn av tid, pandas kaller det `frekvenser`
  | Frekvenskode | Beskrivelse              | Eksempel                               |
|--------------|--------------------------|----------------------------------------|
| `A` or `Y`   | Årlig (Year-End)          | 2024                                  |
| `Q`          | Kvartalsvis               | 2024Q1                                |
| `M`          | Månedlig                  | 2024-10                               |
| `W`          | Ukentlig (Søndag)         | 2024-42 (42. uke, sluttdato Søndag)  |
| `W-MON`      | Ukentlig (Mandag)         | 2024-42 (42. uke, sluttdato Mandag)  |
| `D`          | Daglig                    | 2024-10-21                            |
| `B`          | Virkedag (uten helger)    | 2024-10-21                            |
| `H`          | Time                     | 2024-10-21 15:00                      |
| `T` or `min` | Minutt                    | 2024-10-21 15:30                      |
| `S`          | Sekund                    | 2024-10-21 15:30:45                   |
| `L`          | Millisekund               | 2024-10-21 15:30:45.123               |
| `U`          | Mikrosekund               | 2024-10-21 15:30:45.123456            |
| `N`          | Nanosekund                | 2024-10-21 15:30:45.123456789         |

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: subslide
---
#pd.Period('verdi', freq='frekvenskode')
periode = pd.Period('2024-10-21 15:00', freq='Q') #Verdien er en gyldig tekststreng i en periode med frekvens freq=..
langt_frem = periode+26
langt_frem
```

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

### pd.PeriodIndex
* Vi vil som regel ha mange perioder som indeks i et dataset
* Da kan vi bruke:
  *  `pd.PeriodIndex([«liste med perioder»], freq='frekvenskode')`
  *  `pd.period_range('2024-01', '2025-05', freq='M')` ie (start, slutt, frekvens) 
  *  `pd.period_range('2024-01', periods=12, freq='Q')` ie (start, antall perioder, frekvens)

*Vi har også en `pd.date_range(start, perioder, frekvens)` om vi vil ha `datetime` i stedet*

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: fragment
---
tidserie = pd.period_range('1980Q1', periods=15, freq="Q")
tidserie2 = pd.period_range('1980', '2000', freq='M')
tidserie2
```

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

### Konvertere mellom `datetime` og `Period`
* Ofte trenger man å konvertere mellom `datetime` og `Period`
* Kanskje har man brukt `strptime(...)` til å lese inn riktig dato først
* Vi bruker da `df['date'].dt.to_period('frekvenskode')`
* Skal vi gå andre veien bruker vi `df["periode"].to_timestamp()`

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

* Det er mye mer vi kunne sett på her
* Tid/dato kan bli uhyre komplisert i det virkelige liv

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

# Tilbake til analysen vår:
* Vi kan nå prøve å konvertere tidsseriene våres til et ordentlig format, og slå de sammen

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: fragment
---
display(konkurser_df.head(2))
display(arbeidsledige_df.head(2))
```

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

* Arbeidsledige har nesten riktig format på indeks
* "1972K1" skulle vært "1972Q1" for at `pd.Periods` skal skunne "lese det riktig"

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: fragment
---
arbeidsledige_df = pd.read_csv("arbeidsledige.csv", sep=";", header=1, index_col=0)
arbeidsledige_df.index.name = None

def formater_kvartal(streng_inn):
    streng_ut = streng_inn.replace('K', 'Q')
    return streng_ut

arbeidsledige_df["kvartal"] = arbeidsledige_df.index.map(formater_kvartal)
arbeidsledige_df["kvartal"] = pd.PeriodIndex(arbeidsledige_df["kvartal"], freq='Q')
arbeidsledige_df =arbeidsledige_df.set_index('kvartal')
arbeidsledige_df
```

+++ {"editable": true, "slideshow": {"slide_type": "slide"}}

* Dataframe av konkurser gjør vi litt mer arbeid med
* '1923M01' er ikke gyldig/lesbart for `pd.Period` - det skulle vært '1923-01'
* Vi kan gjøre som sist og bytte ut 'M' med '-', men hva om det var enda mer komplisert?
* Da kan vi bruke `datetime.datetime.strptime(streng, formatstreng)`

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: fragment
---
konkurser_df = pd.read_csv("konkurser.csv", encoding="ISO-8859-1", sep="\t", index_col = 0)
konkurser_df.index.name=None

konkurser_df["date"] = konkurser_df.index.map(lambda x: datetime.datetime.strptime(x, "%YM%m")) #med lambdafunksjon
konkurser_df["date"] = konkurser_df["date"].dt.to_period('Q')
konkurser_df
```

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

* Nå trenger vi bare å summe sammen alle konkurser per kvartal
* Vi kan bruke `.groupby(...)` til dette
* `groupby()` slår sammen deler av data i grupper
* feks alle "menn" i en gruppe og alle kvinner i en annen gruppe om vi har en kolonne "kjønn" i dataene våre
* Det returnes et spesialobjekt som vi kan gjøre noe med, typisk, `.sum(), .mean(), .median(), .max(), .min()`
* Deretter får vi et nytt dataframe ut

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: fragment
---
konkurser_df = konkurser_df.groupby(by="date").sum()
konkurser_df.index.name="kvartal"
```

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

* Nå kan vi slå sammen datasettene med `.merge(...)`

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---

df = pd.merge(konkurser_df, arbeidsledige_df, how='outer', on="kvartal")
df = df.dropna(axis=0)
df = df.rename(columns={"Arbeidsledige (1 000 personer)": "Arbeidsledige", "Opna konkursar": "Konkurser"})
#df = df.set_index("kvartal")
df
```

+++ {"editable": true, "slideshow": {"slide_type": ""}}

* Når vi har fått dataen slik vi vil ha den er det vanskelige over
* Vil vi feks plotte:

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
import matplotlib.pyplot as plt
df.plot()
plt.xlabel("Tid")
df.plot.scatter("Arbeidsledige", "Konkurser")
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---

```

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

* Å finne kovarians og korrelasjon er også lett

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: fragment
---
df.cov()
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: fragment
---
df.corr()
```

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

* De som trenger en oppfriskning på kovarians og korrelasjon kan se her:


### Kovarians (video)
<a href="https://www.youtube.com/watch?v=9Y0Alg8huJk" 
  target="_blank"><img src="https://img.youtube.com/vi/9Y0Alg8huJk/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>

### Korrelasjon (video)
<a href="https://www.youtube.com/watch?v=WpZi02ulCvQ" 
  target="_blank"><img src="https://img.youtube.com/vi/WpZi02ulCvQ/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>
