---
tags:
  - legacy/iif
  - pandas
---

# Pandas i praksis

* Vi kan hente data å analysere, feks fra [statistisk sentralbyrå](http://www.ssb.no)
* SSB bruker tegnkodinger «UTF-8» og «ISO-8859-1»

```{code-cell} ipython3
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
