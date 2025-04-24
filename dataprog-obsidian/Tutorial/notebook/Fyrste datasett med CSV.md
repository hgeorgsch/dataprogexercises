---
title: Fyrste datasett med CSV
author: Hans Georg Schaathun
tags:
  - csv
  - plot
  - session
  - exercise/tutorial
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.17.0
kernelspec:
  display_name: pythonenv
  language: python
  name: pythonenv
---

# Arbeida med store datasett

Eitt hovudmål i dette kurset er å kunna handtera store datasett frå røynda vha. programmering, i praksis i python. Me skal starta med datasettet, og so tek me programmeringsteknikkane etter kvart. Mange har gjort liknande ting i Excel eller andre rekneark, og då vil det ta ein del tid før føremonane ved programmering kjem til syne. Enkle oppgåver er som regel enklare å gjera, og i alle fall raskare å læra, i rekneark. Det er berre samansette oppgåver og store datasett som vert enklare ved programmering. Eitt problem med Excel spesifikt er maksgrensa på ein million radar. Me skal etter kvar sjå på datasett som er større enn det.

Merk at dette dokumentet er tenkt presentert munnleg i eit seminar. Forklaringane kan difor vera litt knappe til sjølvstudium.

## Fyrste datasett

Mange aktørar publiserer datasett. Me skal starta med valutakursar
[Noregs Bank](https://www.norges-bank.no/tema/Statistikk/Valutakurser/?tab=api).
Eg har lasta ned kursane for USD/EUR/GBP/DKK/SEK dei siste fem åra i fila `EXR20250401.csv`.

Dette er ei CSV-fil som står for «comma separated values». 
Namnet er ikkje alltid dekkjande; fila frå Noregs Bank bruker semikolon, og ikkje komma, som skiljeteikn.
Andre kjelder kan bruka tabulator eller røyr (`|`).
Dette må ein vera merksam på når ein skal lesa fila.

Fila er rein tekst, slik at me kan opna ho i ei teksteditor (vim, notepad, e.l.).
Dersom du vil opna ho i Excel, kan det løna seg å opna Excel med eitt tomt ark, og so bruka import-funksjonen frå menyane. Då skal du få opp ein dialogboks der du kan fortelja maskina at semikolon er skiljeteikn, og komma er det ikkje.

:::{admonition} Oppgåve
Opna fila i eit program du kjenner og sjå korleis ho ser ut.
Du kan godt opna både i ein teksthandsamar og i eit rekneark.
Kan du finna att kursen på pund sterling for fem år sidan?  Kva med svenske kroner 1. januar i år?
:::

Fila inneheld gjerne meir data enn me er interesserte i. Det skal me ikkje tenkja på.  
Me legg vekt på å forstå det som er nyttig for oss.

:::{hint}
Når du skal arbeida med eit nytt datasett, løner det seg å sjå på fila for å forsikra deg om at du har fått det du ville.
:::
No kan me gå vidare til å opna fila i python.  Me bruker biblioteket pandas.

```{code-cell} ipython3
---
slideshow:
  slide_type: subslide
---
import pandas as pd

df = pd.read_csv("EXR20250401.csv", sep=";")

df
```

**Merk**
1. Me måtte spesifisera semikolon som skiljeteikn (`sep=";"`).
2. Berre `df` (evt. `display(df)`, og ikkje `print(df)` gjev den penaste utskrifta.
3. Me ser dei fyrste og dei siste linene i fila.
4. Me har fått ei ekstra indekssøyle til venstre, som ikkje finst i fila. Dette er berre for å nummerera radane.

Neste steg er å visualisera valutakursane.  Litt naïvt kan me freista `.plot()`:

```{code-cell} ipython3
---
slideshow:
  slide_type: ''
---
df.plot()
```

OK.  Me kan i alle fall sjå at `plot()` finst som funksjon og faktisk teiknar eit plott, sjølv om dette plottet ikkje er nyttig. Me har jo ikkje sagt kva søyler me vil ha plotta.

## Ein liten digresjon om funksjonsnotasjon

Lat oss dvela litt ved notasjonen. Me har sett fleire variantar av funksjonar.
1. `print( df )` 
2. `pd.read_csv("EXR20250401.csv", sep=";")`
3. `df.plot()`
Kvifor heiter det ikkje `df.print()` eller `plot(df)`?

Grunnen er kvar funksjonen er definert.  I det fyrste dømet er `print` ein *global* funksjon.  
Han er alltid tilgjengeleg.  Argumentet `df` fortel kva data `print` skal prenta.

I det andre dømet hentar me funksjonen `read_csv` frå eit bibliotek, pandas, som me døypte `pd` då me importerte det. Då er `pd` kjelda der me finn `read_csv` og `"EXR20250401.csv", sep=";"` er filnamn og konfigurasjon som funksjonen opererer på.

I det tredje dømet er funksjonen `plot()` definert i *objektet* `df`, som fekk verdien sin frå `pd.read_csv(...)` tidlegare.  Her treng me ikkje noko argument, fordi funksjonen allereie kjem frå, og veit om, `df`, og freistar å plotta dette objektet.


## Plottet

**Refleksjonsspørsmål** Kva søyler er interessante å plotta?

Me kan freista med `TIME_PERIOD` og `OBS_VALUE` som ser ut som dato og kurs.

```{code-cell} ipython3
%%script python --no-raise-error
df.plot( x="TIME_PERIOD", y="OBS_VALUE" )
```

Dette var òg for naivt. *«No numeric data to plot»* er kanskje litt overraskande, men lat oss sjå nærare på dei to søylene.  Me kan be pandas om datatypane for alle søylene, slik:

```{code-cell} ipython3
df.dtypes
```

Dette var rart.  Der er to numeriske søyler, `DECIMALS` og `UNIT_MULT`. Dei er heiltal i intervallet $-2^{63}\ldots2^{63}-1$ (`int64`), men dei varierer lite og er neppe interessante.  På den andre sida, kan me no sjå at dette var dei to søylene som fyrst vart plotta.

Dei to søylene som interesserer oss har typen `object`, noko som kan vera nær sagt kva som helst, men ikkje noko som pandas veit å plotta. Me må altso læra å omsetja desse søylene til noko numerisk. 

## Datatypar

Datattypar kan skapa mykje forvirring når me arbeider med data, og det kan vera komplisert fordi der er uendeleg mange datatypar, og kvar type vert representert ulikt internt i maskinen og overfor brukaren. Internt i maskina er alt representert som ein serie med *bits*, der kvar *bit* er 0 eller 1, av eller på, sann eller usann; kjært barn har mange namn.  Har ein åtte *bits* (ein *byte*), kan ein tolka dei saman som eit heiltal mellom 0 og 255, eller som eit tein (bokstav eller anna) frå ein eller annan tabell. Har ein fleire *bytes* kan ein tolka det som ein teiknstreng (t.d. `"Hello World"`).

I python har me sett at teiknstrengar vert skrivne i gåseaugo, medan tal vert skrivne utan.  Difor er `100` ikkje det same som `"100"` eller `"eitt hundrede"`.  For oss kan det vera det same, men for maskina er det berre `100` som er eit tal.

I CSV-fila er alt teiknstrengar.  Det er gjort slik for at me skal kunna opna og manipulera filen enklast mogleg med ulike verkty og program. Det som framstår som `object` over er teiknstrengar som pandas ikkje klarte å forstå som noko anna. Dei andre to typane er

+ `bool`, som er kort for *Boolean* eller bolsk på norsk.  Denne typen har verdiane sann eller usann (`True` eller `False`)
+ `int64` er kort for *integer* eller heiltal, med 64 bits, som er nok for å representera positive og negative tal opp til $2^{63}$ eller cirka $8\cdot10^{18}$. Dersom me prøver å lagra tal som er større enn dette, får me ein overflytfeil. Nokre system kan varsla om slike feil, men ofte kan slike feil vera vanskeleg å finna.

Me skal straks sjå to typar til

+ `float64` er desimaltal med 64 *bits*.  *Float* er kort for *floating point number*, eller flyttal på norsk. Dette vil seia at desimalkommaet «flyt», slik at ein bruker mange desimalplassar for små tal, og få for store. Flyttal er i dag einerådande som representasjon av desimaltal. *Fixed point numbers* finst i ein del eldre programmeringsspråk, men då skal me tilbake til 1970- og 60-talet.
+ `datetime64` representerer eit tidspunkt, her ogso med 64 bits.

Det er typisk å bruka 64-*bits* tal fordi prosessorane (CPU) i dag stort sett er 64-*bits* og dermed handsamar 64-*bits*-verdiar som ei eining.  Bruker ein fleire *bits* må prosessoren handsame det i fleire omgongar, og bruker ein færre «sløser» ein med prosessorkapasiteten.


## Problemet frå Noregs Bank

**Kursen** Denne søyla ser ut som desimaltal, og det kan verka rart at pandas ikkje skjøner det. Ser me litt nøyare etter ser me at datafila bruker desimal*komma* medan pandas ventar seg det engelske desimal*punktumet*. Det er altso dette me må fiksa. Me treng då to steg, fyrst må me byta ut desimalkomma i heile søyla, og deretter må me be pandas tolka ho på nytt som tal, t.d. slik:

```{code-cell} ipython3
df['engelsk'] = df['OBS_VALUE'].str.replace(',', '.')
df['kurs'] = pd.to_numeric(df['engelsk'])
df.dtypes
```

Merk notasjonen.  Klammene, i `df['OBS_VALUE']` let oss adressera éi søyle i datasettet. Dette kan me gjera både på venstre og høgre side av tilordninga (`=`).  På venstre side tilordnar me ei ny søyle («engelsk» og «kurs»). På høgre side bruker me ei eksisterande søyle i utrekninga til den nye. Slik me har gjort det her, vert den gamle søyla (`OBS_VALUE`) ikkje endra.

Den fyrste lina bruker strengfunksjonen `replace` på kvar einaste verdi i søyla. Den andre lina bruker konverteringsrutinen `to_numeric` for å lesa eit tal frå teiknstrengen. I utlistinga ser me at datasettet har fått t nye søyler, der `"kurs"` er flyttal.  Lat oss sjå på heile datasettet.

```{code-cell} ipython3
display(df)
```

Dette ser jo bra ut, men so må me gjera noko med datosøyla.  Dette er meir komplisert fordi der er so frykteleg mange måtar å skriva tidspunkt på.  Me skal bruka [`to_datetime`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html)-funksjonen, som fungerer litt som `to_numeric`, bortsett frå at me må fortelja han korleis datoen er formatter, slik:

```{code-cell} ipython3
df['dato'] = pd.to_datetime(df['TIME_PERIOD'], format='%Y-%m-%d')
df.dtypes
```

```{code-cell} ipython3
display(df)
```

Her har eg laga nye søyler. Det er vanleg å overskriva eksisterande søyler når ein formatterer dei, t.d. slik
```
df['OBS_VALUE'] = pd.to_numeric( df['OBS_VALUE'].str.replace(',', '.') )
df['TIME_PERIOD'] = pd.to_datetime(df['TIME_PERIOD'], format='%Y-%m-%d')
```
Grunnen til at eg ikkje har gjort det her, er dels for å kunne samanlikna den nye og den gamle søyla, og dels fordi eg då ikkje risikerer å bruka feil søyle om eg skulle gå tilbake i *notebook*-fila og køyra ei gamal celle omatt.


## Tilbake til plotting

```{code-cell} ipython3
df.plot( "dato", "kurs")
```

Dette så rart ut, men lat oss ta det positive fyrst.
1. $x$-aksen ser ut som dato dei siste fem åra
2. $y$-aksen har talverdiar som kan vera valutakursar, mellom 10 og 150.
3. Me har kurvar som går litt opp og ned som valutakursar gjer.

Det er ein god start, men kva er dei rake krosslinene?

Problemet finn me i fila, som har fem ulike valutaar. Dei fem valuataane har ikkje kvar si søyle.
I staden er der ei søyle for valutakode.

:::{admonition} Refleksjonsspørsmål
Kva del av plottet svarer til kva valuta?
:::

For å få eit godt plott, må me filtrera datasettet for å skilja dei fem valutaane frå kvarandre.

```{code-cell} ipython3
gbp = df[ df["BASE_CUR"] == "GBP" ]
display( gbp )
gbp.plot( "dato", "kurs" )
```

Det såg betre ut. Me kan freista å gjera datasettet litt ryddigare ved å filtrera ut søyler og byta namn på dei.

```{code-cell} ipython3
gbp = gbp.reset_index()
gbp["GBP"] = gbp["kurs"]
gbp = gbp.filter( items= [ "dato", "GBP" ] )
gbp
```

Merk at `reset_index()` gjer to ting. For det fyrste renummerer han radane, slik at dei startar på null. For det andre vert datasettet kopiert. Opprinneleg viste `gbp` berre til eit stykke (*slice*) av `df`, og då ville me ikkje hatt lov til å laga nye søyler slik som me gjer i den andre lina.

Denne omnamninga er ein god start til å plotta fleire kursar i eitt diagram.
Fyrst lagar me eit datasett for danske kroner.

```{code-cell} ipython3
dkk = df[ df["BASE_CUR"] == "DKK" ]
dkk = dkk.reset_index()
dkk["DKK"] = dkk["kurs"]
dkk = dkk.filter( items= [ "dato", "DKK" ] )
dkk
```

So kan me fletta dei to datasetta saman.  Me vil fletta på datosøyla. 
Sannsynlegvis speler ikkje det noka rolle her, sidan me reknar med at båe valutaane er notert på alle dei same datoane.
Generelt er det greitt å tenkja på, sidan somme verdiar ofte manglar i faktiske datasett.
For å vera på den sikre sida, bruker me `on`-parameteren. Då får me ei line for kvar dato som finst i eitt av datasetta.

```{code-cell} ipython3
mrg = pd.merge_asof( dkk, gbp, on="dato" )
display(mrg)
mrg.plot()
```

OK.  Datasettet ser fint ut, men plottet var ikkje det som me venta.

**Refleksjonsspørsmål** Kva er det eigentleg som er plotta?

Når me vel $x$- og $y$-akse i `plot`-funksjonen, kan me gje ei liste med søyler, slik:

```{code-cell} ipython3
mrg.plot( x="dato", y = [ "GBP", "DKK" ])
```

:::{admonition} Oppgåve  
Bruk det som me har lært til no for å plotta alle dei fem valutaane i eitt diagram.
:::


## Skriva ut ein fil

Heilt til slutt skal me sjå korleis me kan skriva det reformatterte datasettet tilbake til fil.

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
# Skriva ut CSV-fila
mrg.to_csv("EXR-formattert.csv", index=False)
```

Me ser ikkje noko utdata frå denne funksjonen, so for å sjå kva som skjedde, må me finna att fila i filsystemet.

:::{admonition} Oppgåve
Finn fila i filsystemet og opna ho i Excel eller eit anna program. Inneheld ho det ho skal?
:::

## Avrunding

Der er mykje å halda styr på i pandas. Her har me berre sett eitt døme og nokre få teknikkar. Når du skal bruka python og pandas i praksis vil du stadig vekk ha bruk for å slå opp konkrete teknikkar.  T.d.

* [Cheat sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
* [Tutorials](https://pandas.pydata.org/pandas-docs/stable/getting_started/tutorials.html)
* [Kokebok](https://www.skytowner.com/explore/pandas_recipes_reference) 

Det er ikkje sikkert at det er mykje hjelp i desse kjeldene enno, før du har lært litt meir. I neste demo skal me forklara nokre fleire grunnleggjande konsept. Målet er å læra nok til å søkja etter resten, lesa dokumentasjon og å stilla gode spørsmål når du treng det.
