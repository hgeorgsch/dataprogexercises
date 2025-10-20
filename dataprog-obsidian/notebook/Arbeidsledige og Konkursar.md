---
jupytext:
  formats: md:myst,ipynb
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.17.2
kernelspec:
  name: dataprog
  language: python
  display_name: dataprog
---

# Samanheng mellom Arbeidsledige og Konkursar

Denne oppgåva føreset at du har gjort oppgåva om
[Arbeidsledige](Arbeidsledige.ipynb) inklusive 
[Tid og dato](Tid%20og%20dato.ipynb) som
forklarer korleis me formatterer dei to datasetta.
Her går me vidare med å slå saman datasetta for å sjekka
om der er samanheng mellom arbeidsledigheit og konkursar.

## Datasett

Koden under lastar dei to datasetta som me kom fram til i
øvinga om [Arbeidsledige](Arbeidsledige.ipynb).  
Koden er skrive meir kompakt, men bruker ingen nye teknikkar.
Du kan godt bruka din eigen kode i staden.
Merk at eg her kaller dei to *Data Frames* som me skal arbeida
med for `arbdf` og `kondf`.

### Arbeidsledige

```{code-cell} ipython3
import pandas as pd
df1 = pd.read_csv("1054.csv", sep=";", encoding="latin1",
                             header=0, index_col=None)

def formatertid(streng_inn):
    """
    Reformater ein periodestreng frå SSB-format til pandas-format.
    Månad og kvartal er støtta.  Me kan trengja andre frekvensar i framtida. 
    """
    return streng_inn.replace('M', '-').replace('K', 'Q')

df1["måned"] = df1["måned"].map(formatertid)
df1["måned"] = pd.PeriodIndex(df1["måned"], freq='M')
df1 = df1.set_index('måned')

arbdf = df1[ df1["statistikkvariabel"] == "Arbeidsledige (1000 personer)" ]
arbdf = arbdf[ arbdf["kjønn"] == "0 Begge kjønn" ]
arbdf = arbdf[ arbdf["alder"] == "15-74 15-74 år" ]
arbdf = arbdf[ arbdf["type justering"] == "T Trend" ]

idx = list( df1.columns )[-1]

arbdf = arbdf.copy()
arbdf = arbdf.rename( columns={ idx : "Arbeidsledige" } ) 

arbdf["Arbeidsledige"] = arbdf["Arbeidsledige"].astype( float )

display(arbdf)
arbdf["Arbeidsledige"].plot()
```

### Konkursar

```{code-cell} ipython3
df2 = pd.read_csv("62495.csv", encoding="ISO-8859-1", sep=";")
display( df2 )

df2["kvartal"] = df2["kvartal"].map(formatertid)
df2["kvartal"] = pd.PeriodIndex(df2["kvartal"], freq='Q')
df2 = df2.set_index('kvartal')

kondf = df2[ df2["statistikkvariabel"] == "Konkurser" ]
kondf = kondf[ kondf["organisasjonsform"] == "99 I alt" ]
kondf = kondf[ kondf["næring (SN2007)"] == "01-99 Total" ]
kondf = kondf[ kondf["region"] == "0 Hele landet" ]

idx = list( df2.columns )[-1]

kondf = kondf.copy()
kondf = kondf.rename( columns={ idx : "Konkurser" } ) 

display( kondf )
display( kondf["Konkurser"] )
```

## Slå saman data


For å studera samanhengar mellom arbeidsledigheit og konkursar 
skal me slå saman dei to *Data Frames* til éin.  
Der er fleire måtar å slå saman datasett på, og difor er ikkje
dette like enkelt som å leggja saman med `+` som fungerer for
mange andre datatypar.

Der er mange ting å tenkja på når me skal slå saman datasett:
* Matchande datatypar: to søyer er forkjellige dersom dei har forskjellige datatyper 
  sjølv om innhaldet er det same
* Kva radar høyrer saman i dei to datasetta?  Me må ha ei søyle (gjerne indeks) som
  er felles for dei to datasetta.
* Skal me behalda radar som berre finst i det eine datasettet?

Me har gjort ein del av jobben allereie.  Me har koda indeks som `Period`-objekt,
slik at desse er samanliknbare, men dei har ikkje same frekvens.
For lett å kunna samanlikna, kan det vera greit å visa berre eit lite utsnitt
av kvart datasett, t.d. ved å bruka `head()`-metoden.

```{code-cell} ipython3
display(kondf.head(2))
display(arbdf.head(2))
```

## Tidsindeks med ulik frekvens

Datasetta gjev oss altso tre observasjonar av arbeidsledigheita og éin av
konkursar for kvart kvartal.  Når me skal samanlikna vil me helst ha kvar
variabel éin gong per periode.  Der kan vera fleire måtar å handtera dette
på.  Ei enkel løysing er å ta gjennomsnittet over kvar periode.

Det fyrste me gjer er å laga ein ny søyed med `PeriodIndex` i `arbdf`, slik
at båe datasetta har ei søyle med same frekvens.

```{code-cell} ipython3
arbdf["kvartal"] = pd.PeriodIndex(arbdf.index, freq='Q')
display(arbdf.head(4))
```

Sjølvsagt får me då tre radar per kvartal.

No kan me bruka `kvartal`-søyla til å gruppera data, men når me gjer det,
me må tenkja på alle søylene.  Numeriske søyler er greie, for der kan me
slå saman data med gjennomsnitt (`mean`) eller sum.
Den nye `kvartal`-søyla er òg grei fordi det dén me bruker til å definera
gruppene.
Dei andre søylene er uproblematiske i teorien, fordi alle radane har same verdi,
men me må likevel fortelja python kva han skal gjera.

Det enklaste er å droppa dei problematiske søylene.  Sidan alle radane har
same verdi taper me inkje.

```{code-cell} ipython3
idxs = list( arbdf.columns )[0:4]
print(idxs)
arbdf = arbdf.drop( labels=idxs, axis=1 )
display( arbdf )
```

No er det råd å gruppera data per kvartal med `groupby()`-metoden.

```{code-cell} ipython3
arbgb = arbdf.groupby( "kvartal" )
display(arbgb)
```

::: {admonition} Refleksjon
Kva viser utskrifta her?  Kva er `arbgb` for noko?
:::

Det forvirra meg òg, at `groupby()` ikkje gjev ein ny *DataFrame*,
men ein eigen datatype.
Grunnen til det er at me ikkje har sagt korleis me skal aggregera radane
innanfor gruppa.
Dét gjer me i eit eige steg, og då vil me få den nye *DataFrame* som me
ynskjer oss.

```{code-cell} ipython3
argdf = arbgb.mean()
display(argdf)
```

::: {admonition} Merknad
I staden for `.mean()` kan me bruka `.sum()`, `.median()`, `.max()`, `.min()`, eller
kan henda andre.
:::


## Fletting av datasett


No kan me slå saman datasetta med `.merge()`.
Dette er forklart i meir detalj i øvinga
[Fyrste datasett med CSV](Fyrste%20datasett%20med%20CSV.ipynb).

```{code-cell} ipython3
df = pd.merge(kondf, argdf, how='outer', on="kvartal")
display( df )
```

::: {admonition} Repetisjonsspørsmål
Kva tyder argumentet `how='outer'`?
Kva med `on="kvartal"`?
:::

Me kan òg sjekka resultatet ved å plotta.

```{code-cell} ipython3
df.plot()
```

::: {hint}
Dette var enkelt, heilt utan argument til `plot()`.
Han plottar med indeksen på $x$-aksen, og sidan me har brukt tidspunkt eller periode
som indeks, vert det slik som me vil ha det.  Alle dei numeriske søylene vert 
plotta, medan dei ikkje-numeriske vert ignorert, som òg er bra for oss.
:::

Det går an å bruka funksjonar frå `pyplot` for å endra titlar og layout
på figuren.  Det fylgjande er berre eit døme.

```{code-cell} ipython3
import matplotlib.pyplot as plt
df.plot()
plt.xlabel("Tid")
```

## Korrelasjon

Ein annan måte å plotta på, er å plotta ein variabel på kvar akse,
i det me gjerne kaller spreidingsplott.

```{code-cell} ipython3
df.plot()
df.plot.scatter("Arbeidsledige", "Konkurser")
```

::: {admonition} Refleksjon
Kva kan du lesa frå spreidingsplottet.  Er der ein samanheng
mellom ledigheit og konkursar, trur du?
:::

Eit vanleg kvantitativt mål for samanhengen mellom to tidsrekkjer
er korrelasjonskoeffisienten, som mange kjenner frå statistikken.
Når me bed om korrelasjonen i pandas, reknar han ut for kvart par
av søyler, ogso for kvar søyle med seg sjølv, sjølv om denne alltid
er 1, som tilseier maksimal korrelasjon.  Difor må me òg ta bort
ikkje-numeriske søyler fyrst.

```{code-cell} ipython3
df1 = df[["Arbeidsledige","Konkurser"]]
df1.corr()
```

<a href="https://www.youtube.com/watch?v=WpZi02ulCvQ" 
  target="_blank"><img src="https://img.youtube.com/vi/WpZi02ulCvQ/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>


### Kovarians 

Korrelasjonskoeffisienten er ein normalisering av kovariansen, som
me òg kan rekna ut.

```{code-cell} ipython3
df1.cov()
```

<a href="https://www.youtube.com/watch?v=9Y0Alg8huJk" 
  target="_blank"><img src="https://img.youtube.com/vi/9Y0Alg8huJk/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>


## Oppsummering

Det er alltid litt plunder å få nye datasett på ein kjend form, men straks
me har samla fleire tidsrekkjer i éin *DataFrame* har me eit stort repertoir
av statistiske verktøy for å analysera dei.  Me skal ikkje i dette kurset gå
inn på nye statistiske metodar, men me vil gjerne ha utnytta dei metodane som
er kjende frå før.  Då gjeld det å søkja i dokumentasjonen eller spørja andre.
