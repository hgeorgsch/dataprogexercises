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

# Arbeidsledigheit og konkursar

I denne øvinga skal me sjå på datasett frå 
[statistisk sentralbyrå](http://www.ssb.no).
Der er mykje å velja i, både forenkla datasett som er brukt til
konkrete rapportar og grafiske framstillingar, og meir komplekse
grunnlagsdata.
Seinare i kurset skal me sjå på [API-et](https://data.ssb.no/api/?lang=no)
som lèt oss velja ut data direkte frå databasen.
I denne øvingas skal me heller ta utgangspunkt i
[lista over ferdiglagde datasett](https://data.ssb.no/api/?lang=no).
Det òg verd å bla gjennom artiklane for å sjå kva slags analysar ein 
kan gjera.

Eg har freista å gjera denne øvinga mest mogleg realistisk.  
Andre øvingar tek gjerne utgangspunkt i programmeringsteknikkar som me vil
undervisa, og lagar eit forenkla datasett for å illustrera akkurat det som
skal undervisast.
Her tek me utgangspunkt i eit spørsmål som me vil ha svar på, finn eit
relevant datasett, og løyser dei problema som oppstår.
Dette gjer øvinga lang med mange krumspring, men det gjev oss eit realistisk
bilete av korleis ein arbeider med data frå røynda.

Når oppgåva ser stor og uoverstigeleg ut, skal me dela han opp, og zooma inn
på eitt delproblem åt gongen.  Ver merksame på dette, og ta delproblema alvorleg.
Kvart delproblem illustrerer teknikkar som er verd å læra.

Forskingsspørsmålet vårt er:

> Kva samanhengar er der mellom arbeidsledigheit og talet på bedriftskonkursar?

## Datasett frå SSB

::: {admonition} Oppgåve
Sjå på lista over [ferdiglagde datasett](https://data.ssb.no/api/?lang=no)
frå SSB.  Finn du datasett som kan brukast til å svara på forskingsspørsmålet? 
:::

For å ta ein ting åt gongen, startar me med data over arbeidsledige.

::: {admonition} Oppgåve
Last ned datasettet med ID 1054 i CSV-format.
Opna fila i ein teksteditor eller eit rekneark.
Korleis er ho formattert?
Kva data inneheld ho?

Plasser fila i same katalog som Jupyter-dokumentet som du arbeider med.
:::

Når me skal arbeida med slike datasett i python, bruker me eit biblotek
som heiter pandas.

```{code-cell} ipython3
import pandas as pd
df = pd.read_csv("1054.csv", sep=";", encoding="latin1",
                             header=0, index_col=None)
```

Legg merke til at me spesifiserer skiljeteiknet (`sep`) som semikolon i staden for
komma, og teikncodingen, som er Latin 1.

::: {admonition} Oppgåve
Kva skjer om du fjernar `sep`-argumentet?

Kva skjer om du fjernar `encoding`?
:::

::: {hint}
Dei viktigaste teiknkodinge for oss er `latin1`, eller meir
korrekt «ISO-8859-1», og `utf-8`, som er standard i pandas
dersom me ikkje seier noko anna.
UTF-8 er ein av fleire kodingar av eit teiknsett som heiter
Unicode, og dersom de vel feil teiknkoding, vil feilmeldingane
ofte referera til «Unicode» heller enn UTF-8.
:::

Dei to siste argumenta fortel pandas at den fyrste lina (nr. 0)
inneheld søyleoverskrifter og at der ikkje er noka søyle med
rekkjeindekser.

::: {admonition} Oppgåve
Kva skjer om du fjernar `header`- og `index_col`-argumenta?

Det er ikkje sikkert det gjer nokon forskjell.
:::

## Arbeidsledigheitsdatasettet

Datasettet 1054 inneheld mange forskjellige variablar, men dei
har ikkje fått eigne søyler.
I staden er der ein søyle `statistikkvariabel` som identifiserer
kva som er observert, og kvart tidspunkt har ein rad for kvar
variabel.

::: {admonition} Refleksjon
Sjå på søyla `statistikkvariabel`.  Kva variablar er observerte?
:::

I tillegg innheld datasettet fullstendige datasett for kvart kjønn
forutan båe kjønn samla, og for ulike og overlappande aldersgrupper.
For å kunna analysera datasettet, må me kunna isolera dei ulike 
tidsrekkjene.

::: {admonition} Tidsrekkje
Ei **tidsrekkje** er ei samling registreringar av éin bestemt
variabel på etterfylgjande tidspunkt, normalt med regelmessige
mellomrom.
:::

Dersom me kan ta ut alle radane med same verdi i alle søylene,
bortsett frå tidspunktet og den siste søyla med talverdien,
so har me ei tidsrekkje.

### Filtering

*Data frames* kan indekserast på mange ulike måtar,
inklusive bolsk indeksering, der me kan gje vilkår basert
på innhaldet i søylene.
Me kan t.d. velja ut éi tidsrekkje frå datasettet vårt slik:

```{code-cell} ipython3
df1 = df[ df["statistikkvariabel"] == "Arbeidsledige (1000 personer)" ]
df1 = df1[ df1["kjønn"] == "0 Begge kjønn" ]
df1 = df1[ df1["alder"] == "15-74 15-74 år" ]
df1 = df1[ df1["type justering"] == "T Trend" ]

display(df1)
```

Me samanliknar rett og slett innhaldet i søyla med ein fast streng,
og får med alle radane der vilkåret er sant.

Når me filtrerer, får me ikkje ein ny *data frame* men eit nytt *view*
på den gamle.  
Dette kan skapa problem når me skal manipulera utdraget og kanskje leggja
til utrekna søyler.
Difor kan det løna seg å kopiera *view*et, og dermed laga ein ny
*data frame*, slik:

```{code-cell} ipython3
df1 = df1.copy()
display( df1 )
```

### Plotting

For å sjekka at datasettet er ryddig og pent, er det alltid
verd å plotta.
Eg hadde store vanskar med å henta ut den aktuelle søyla, pga.
det frykteleg lange søylenamnet.
Det løner seg å byta namn, men då må me triksa litt.
Det er betre å henta ut namnet programmatisk enn å klippa og lima
frå visinga.
Me kan henta ut alle søyleindeksene med `columns`-attributten.

```{code-cell} ipython3
print( df1.columns )
print( type( df1.columns ) )
```

Dette gjev oss derimot ikkje namna som teiknstrengar, men eit
spesielt `Index`-objekt. Me kan konvertera til ei liste med strengar, slik:

```{code-cell} ipython3
idxlist = list( df1.columns )
print(idxlist)
```

Me kan henta ut det siste elementet frå lista, slik at me får
ein variabel `idx` med det vonde søylenamnet.

```{code-cell} ipython3
idx = idxlist[-1]
print(idx)
```

No har me det me treng for å byta namn på søyla med
`rename`-metoden.  Me lager eit nytt variabelnamn for
å minimera feil dersom me skulle gå tilbake og køyra 
gamle cellar om att.

```{code-cell} ipython3
df2 = df1.rename( columns={ idx : "Arbeidsledige" } ) 
display(df2)
```

::: {hint}
Legg merke til syntaksen. Argumentet til `rename`
er ein *dictionary* som avbildar gamle søylenamn til nye.
Søylename som ikkje er med i denne *dictionary* vert ikkje endra.
:::

No kan me enkelt henta ut den søyla som me er interesterte i,
ved å indeksera på søylenamn.

```{code-cell} ipython3
print( df2["Arbeidsledige"] )
```

Resultatet her er eit *Series*-objekt, som òg har ein
`plot()`-metode.

::: {admonition} Oppgåve
Test plotting av *Series*-objektet, slik
```
df1["Arbeidsledige"].plot()
```
Kva skjer?
:::

Oppgåva står der fordi dette faktisk var det som eg gjorde,
når eg skulla løysa problemet sjølv.  Det viser seg då at
søyla vår ikkje vert gjenkjend som tal.  Sannsynlegvis er
det fordi der var manglande data i det opprinnelege datasettet,
sjølv om utdraget ser ut som om det er rett.

Me ser at søyla ikkje er tal når me ser på utskrifta av objektet
over, der det står `dtype: object`.  Hadde det vore tal, so hadde
der stått namnet på ein numerisk type.

```{code-cell} ipython3
df2["Arbeidsledige"] = df2["Arbeidsledige"].astype( float )
```

No skal plottinga verka.

```{code-cell} ipython3
df2["Arbeidsledige"].plot()
```

::: {hint}
Her har me brukt den innebygde typen `float`.
Det er ofte betre å bruka typar frå numpy-biblioteket,
men det får me koma inn på ein annan dag.
:::

::: {admonition} Refleksjon
Ser plottet rimeleg ut?
:::

### Nye søyler

Legger til kolonne med arbeidsledighet i prosent

```{code-cell} ipython3
df1["prosent"] = df1["Arbeidsledige (1 000 personer)"]/1000
```

### Legacy notes

```{code-cell} ipython3
arbeidsledige_df.index.name = None

#med apply og lambdafunksjon
#arbeidsledige_df["prosent"] = arbeidsledige_df["Arbeidsledige (1 000 personer)"].apply(lambda x: f"{x/1000:.2%}") 
```

```{code-cell} ipython3
arbeidsledige_df["Arbeidsledige (1 000 personer)"].plot()
arbeidsledige_df.describe()
display(arbeidsledige_df) #Vi kan bruke display istedet for print for en "fin" tabell
arbeidsledige_df = arbeidsledige_df.drop("prosent", axis=1)
```

## Konkursar

```{code-cell} ipython3
# Vi henter et datasett med åpnede konkurser fra SSB
konkurser_df = pd.read_csv("konkurser.csv", encoding="ISO-8859-1", sep="\t", index_col = 0)
konkurser_df.index.name=None
konkurser_df
```

### Analyse:

* Vi vil slå sammen dataene våre om arbeidsledighet og åpnede konkurser
* Er det en sammenheng?

```{code-cell} ipython3
konkurser_df+arbeidsledige_df #Det funket dårlig....
```

# Slå sammen data

Vi må passe på en rekke ting når vi skal slå sammen data:
* Matchende datatyper: 2 kolonner blir ansett som forkjellige dersom de har forskjellige datatyper men matchende data
* Hva skal vi beholde (Alt som matcher, kun matchende data fra nr 1 eller 2 dataframe)
* Dersom man slår sammen på index, må disse samsvare


* Vi trenger nå å slå sammen data som går over forskjellige tidsspenn
* Indeksen vår består av *tekststrenger* -- dette byr på problemer
* [[Tid og dato]]

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
df.corr()
```

* De som trenger en oppfriskning på kovarians og korrelasjon kan se her:


### Kovarians (video)
<a href="https://www.youtube.com/watch?v=9Y0Alg8huJk" 
  target="_blank"><img src="https://img.youtube.com/vi/9Y0Alg8huJk/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>

### Korrelasjon (video)
<a href="https://www.youtube.com/watch?v=WpZi02ulCvQ" 
  target="_blank"><img src="https://img.youtube.com/vi/WpZi02ulCvQ/0.jpg" 
alt="IMAGE ALT TEXT HERE" width="240" height="180" border="10" /></a>
