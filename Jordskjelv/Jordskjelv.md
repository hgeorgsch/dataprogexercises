---
jupytext:
  formats: md:myst,ipynb
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

::: {admonition} Opphavsrett

+ Original oppgåve ved Morten Munthe, Universitetet i Bergen, 2025.
+ Redigert og tilrettelagt av Hans Georg Schaathun, NTNU, 2025, med
  kodeforenkling og utdjuping.

Oppgåva kan brukast fritt under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

Kartet som er brukt offentleg eige (*public domain*) og henta
frå [Wikimedia Commons](https://commons.wikimedia.org/w/index.php?curid=1288245)
etter ein originalt frå [NASA (sensor Terra/MODIS)](http://visibleearth.nasa.gov/).

Datasettet er henta frå [USGS](https://earthquake.usgs.gov/earthquakes/search/).
:::

# Jordskjelv

Her skal me bruka ei fil med over 200 000 jordskjelv fra 1973 til 2014,
og sjå korleis me kan visualisera geografisk spreidning, styrke og djupne
på skjelva.

::: {admonition} Læringsutbyte
Denne løysinga skal visa korleis ein kan
+ plotta oppå bilete, som t.d. kart.
+ animera plot.
:::

## Datasettet

Me bruker dei vanlege biblioteka:

```{code-cell} ipython3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

Datafila heiter `NEIC_global_1973-2014.txt`.

::: {admonition} Oppgåve
Opna datafila og sjå kva slags format det er.
Kva skiljeteikn er brukt mellom søylene?
Korleis vert desimaltal skrive?
:::

Me kan importera datasettet slik:

```{code-cell} ipython3
data_J = pd.read_csv("NEIC_global_1973-2014.txt", sep='\t', decimal = ',')  
data_J.head(10)
```

::: {admonition} Oppgåve
+ Kva tyder argumentet `sep='\t'`?
+ Kva tyder argumentet `decimal=','`?
:::

Det kan vera nytt å sjå kva omfang dei ulika verdiane har.  T.d.

```{code-cell} ipython3
print(max(data_J["Depth"])) # maks er 700
print(min(data_J["Depth"])) # min er 0 (??)
print(max(data_J["Magnitude"])) # maks er 9.1
print(min(data_J["Magnitude"])) # Min er 4.5
```

Me kan gjera dette litt meir kompakt med pandas-funksjonane for minimum og maksimum.

```{code-cell} ipython3
print(data_J.max())
print(data_J.min())
```

::: {admonition} Oppgåve
Finn gjennomsnitt (*mean*) for dei ulike søylene.
Kan du finna (empiriske) standardavvik òg?
:::

Me skal i hovudsak sjå styrken og djupna, so me definerer dei med eigne variabelnamn.

```{code-cell} ipython3
djupne = data_J["Depth"]
styrke = data_J["Magnitude"]
```

## Histogram

Sjølve skjelvet er karakterisert ved djupna (under bakken) og magnityden (Richters skala).
Stolpediagram og histogram visualiserer fordelinga av éin variabel.

Den enklaste formen er eit stolpediagram, som me kan gjera slik:

```{code-cell} ipython3
values, counts = np.unique(styrke, return_counts = True)
plt.bar(values, counts, width = 0.09)
```

I den fyrste lina finn `np.unique` alle unike magnitydar (`values`) og talet på gongar (`counts`) der verdien opptrer.

::: {admonition} Oppgåve
Kva skjer om du endrar parameteren `width` i den andre lina?
:::

Stolpediagram er ikkje ein god løysing for kontinuerlege verdiar.  Det ser me om me skriv ut alle stolpane som ei liste.

```{code-cell} ipython3
print(list(zip(values,counts)))
```

::: {admonition} Kode
Du kjenner kanskje ikkje `zip`-funksjonen, men det er ein standardfunksjon som er verd å læra.
Han tek to lister, og set saman par med eitt element frå kvar liste.
:::

Kvar stolpe er eit par, med ei verdi og ei høgd.  Me kjenner igjen stolpane for 4,5, 4,6, 4,7, osv. både i lista og i diagrammet.

::: {admonition} Refleksjon
Kvar vert det av stolpane for 4,58 og 4,59 i diagrammet?
:::

Det ser ut som om datasettet stort sett bruker éin desimal for magnituden, og berre sjelden bruker to.
For å handtera kontinuerlege tal, er det betre å bruka eit histogram, der me grupperer verdiane i båser (*bins*).
Der er fleire måtar å spesifisera båsene (sjå [dokumentasjonen](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html)).
Her definerer me grenseverdiane mellom båsene.

```{code-cell} ipython3
plt.hist(styrke, bins=[ 0.1*x+0.05 for x in range(40,95) ])
```

Legg merke til at `hist`-funksjonen skriv ut både høgda på stolpane og grensene for båsene før plottet.
Det kan vera nyttig for å oppdaga feil.

::: {hint}
I akkurat dette tilfellet, kunne me ha fått det same resultatet ved å runda av alle verdiane til éin desimal, for så å plotta som eit stolpediagram slik som me gjorde fyrst.
:::

Me kan studera djupna på same måte.  Stolpediagrammet, som eit fyrste forsøk, ser slik ut.

```{code-cell} ipython3
values, counts = np.unique(djupne, return_counts = True)
plt.bar(values, counts, width = 1.0)
```

Dette var både treigt, og ikkje spesielt nyttig.  Djupe skjelv er openbert so sjeldne at me ikkje ser dei.
Me ser at det meste skjer mellom 0 og 150 meter, so me kan laga eit grovt histogram i dette intervallet.

```{code-cell} ipython3
plt.hist(djupne, bins=10, range=(0,150) )
```

::: {admonition} Oppgåve
Bruk dokumentasjonen til å laga pene og informative histogram av djupna.
Bør du bruka fleire eller færre båser?  Bruk gjerne fleire histogram for å
illustrera både grunne skjelv og heile spennet ned til 700m.
Legg tittel på diagrammet og på aksene.
:::

::: {admonition} Refleksjon
Kva fortel histogramma oss om fordelinga av jordskjelv?
Kva fortel dei ikkje?
:::

+++

## Samanheng mellom dybde og styrke

Histogrammet viser berre éin variabel åt gongen.
Det er nyttig å sjå samanhengen mellom djupa og magnityden.
Då bruker me eit spreideplott (*scatter plot*).

```{code-cell} ipython3
plt.figure(figsize=(8, 10), dpi=80)
plt.scatter(djupne, styrke, s = 0.1)
```

::: {admonition} Refleksjon
Kva kan dette plottet læra oss om jordskjelv?
:::

## Kartplott

No kjem me til den mest spanande delen av øvinga.
Me skal sjå på lengdegrad (*latitude*) og breiddegrad (*longitude*) for skjelva.
Lat oss starta med å definera posisjonsvariablane og plotta dei som eit spreideplott.

```{code-cell} ipython3
lengdegrad = data_J["Latit"]
breddegrad = data_J["Longit"]

plt.figure(figsize=(13, 6), dpi=80)
plt.scatter(breddegrad, lengdegrad, s = 0.1)
```

::: {admonition} Refleksjon
Kva kan me kjenna igjen i denne figuren?
:::


Me får eit betre inntrykk om me kan plotta skjelva oppå eit kart.
Då bør me bruka eit
[ekvirektangulært kart](https://simple.wikipedia.org/wiki/Equirectangular_projection),
Der ein lengde- og breiddegradane har same avstand overalt på kartet.
Me finn eit slikt kart på [Wikimedia Commons](https://simple.wikipedia.org/wiki/Equirectangular_projection#/media/File:Equirectangular-projection.jpg):
[Equirectangular-projection.jpg](Equirectangular-projection.jpg).

Lat oss fyrst sjå berre på kartet:

```{code-cell} ipython3
img = plt.imread("Equirectangular-projection.jpg")
fig, ax = plt.subplots(figsize=(10, 12), dpi=100)
ax.imshow(img, extent=[-180, 180, -90, 90])
```

Merk at me oppgjev omfanget på karted, frå 180° vest til 180° aust og
frå 90° sør til 90° nord.  Dette vert koordinatsystemet i figuren,
når me legg andre plott oppå.
No kan me kombinera koden frå spreideplottet og kartet, slik:

```{code-cell} ipython3
img = plt.imread("Equirectangular-projection.jpg")
fig, ax = plt.subplots(figsize=(10, 12), dpi=100)
ax.imshow(img, extent=[-180, 180, -90, 90])

plt.scatter(breddegrad, lengdegrad, s = 0.1, color = 'r')
plt.xlabel('Breddegrad')
plt.ylabel('Lengdegrad')
```

::: {admonition} Refleksjon
Kva seier dette plottet om førekomsten av jordskjelv?
Kjenner du igjen dei mynstra som du gjorde på spreideplottet utan kart?
:::

## Meir detaljerte kartplott

På kartet over ser me ingen forskjell mellom svake og sterke skjelv.  
T.d. ser me fleire skjelv i Europa, i område der me sjelden høyrer om skjelv.
Dei katastrofale skjelva som me høyrer om ligg andre plassar.

Lat oss sjå korleis me kan variera visualiseringa for å få fram meir informasjon.
Fyrst lagar me ein funksjon for å laga kartet, slik at me kan gjenbruka det med éi line, i staden for tre.

```{code-cell} ipython3
img0 = plt.imread("Equirectangular-projection.jpg")
def mapplot(img=img0):
   fig, ax = plt.subplots(figsize=(10, 12), dpi=100)
   ax.imshow(img, extent=[-180, 180, -90, 90])
   return fig, ax
```

::: {admonition} Refleksjon
Skjøner du koden som er brukt i funksjonen?
:::

Ei enkel løysing er berre å plotta dei sterkaste skjelva.
Då kan me definera ein minstestyrke og filtrera datasettet.

```{code-cell} ipython3
minstestyrke = 6

dat = data_J[ data_J["Magnitude"] >= minstestyrke ]

fig = mapplot()
plt.scatter(dat["Longit"], dat["Latit"], s = 5, color = 'r')
plt.xlabel('Breddegrad')
plt.ylabel('Lengdegrad')
```

::: {admonition} Refleksjon
Kva område i verda har dei sterkaste skjelva?
Du kan godt variera minstestyrken for å få fram andre detaljar.
:::

::: {admonition} Oppgåve
Det kan vera vanskeleg å få oversikt når ein ser på heile 
datasettet samstundes.  Ein enkel måte å sjå eit utsnitt er
å plotta berre eitt eller nokre få år.

Kopier koden over, og legg til eit filter som filtrerer ut
eitt år. 
:::

I eit meir rafinert plot kan me plotta store sirklar for sterke skjelv
og små sirklar for svake.
Parameteren `s` i `plt.scatter()` kan ta ei liste e.l. for å definera forskjellig
storleik på kvart punkt, og det kan me utnytta.
For å vera sikre på at storleiken høyrer til rett punkt, legg me han som ei
ny søyle i datasettet, slik.

```{code-cell} ipython3
fig = mapplot()

dat.loc[:,"size"] = (dat["Magnitude"]-minstestyrke) * (100/(9.1-minstestyrke))

plt.scatter(dat["Longit"], dat["Latit"], s = dat["size"], facecolor="none", color = 'r')
plt.xlabel('Breddegrad')
plt.ylabel('Lengdegrad')
```

::: {admonition} Oppgåve
Freist å variera koden for å læra kva dei ulike parametrane tyder.
+ Kva skjer om du endrar `facecolor` til `"y"` eller `"b"`?
+ Kva skjer om du endrar verdien på `minstestyrke`?
+ Kva skjer om du endrer konstanten 100 i utrekninga av storleik?
:::

På same måten som storleiken, kan ogso fargen variera for kvart punkt.
Dermed kan me t.d. representera styrke med storleik og djupne med farge,
slik.

```{code-cell} ipython3
fig = mapplot()

plt.scatter(dat["Longit"], dat["Latit"],
    s=dat["size"], c=dat["Depth"], cmap = 'YlOrRd') 
plt.colorbar(label = 'Dybde i meter', fraction = 0.024)
plt.xlabel('Breddegrad')
plt.ylabel('Lengdegrad')
```

::: {hint}
Parameteren `cmap` er ganske kryptisk.
Namnet står for *colour map*, og `YlOrRd` er berre namnet på eitt bestemt fargekart.
Sjå dokumentasjonen på
[fargar i pyplot](https://matplotlib.org/stable/users/explain/colors/colormaps.html).
:::

::: {admonition} Oppgåve
Ser det betre ut med eit anna fargekart?
Slå opp i dokumentasjonen og finn eit som du liker.
:::

::: {admonition} Refleksjon
Kva fortel dei siste plotta om fordelinga av skjelv i styrke og djupne?

Hugs at du kan filtrera datasettet akkurat som du vil, for å sjå det som 
interesserer deg.  Då kan det vera lurt å kopiera all koden inn i éin kodeblokk,
for å vera sikker på at resultatet ikkje avheng av tidlegare blokkar og du kan endra
alt på ein plass.  Du kan bruka dømet under om du vil.
:::

For å oppsummera alt me har brukt over, kan me samla alt i ein kodesnutt.
Her bruker me `query`-funksjonen for å filtrera datasettet.
Det er den enklaste løysinga når me filtrerer på fleire kriterium.

```{code-cell} ipython3
minstestyrke = 6
startar = 1983
sluttar = 1990

dat = data_J.query("Magnitude >= @minstestyrke & Year >= @startar & Year <= @sluttar")
dat.loc[:,"size"] = (dat["Magnitude"]-minstestyrke) * (100/(9.1-minstestyrke))

fig = mapplot()
plt.scatter(dat["Longit"], dat["Latit"],
    s=dat["size"], c=dat["Depth"], cmap = 'YlOrRd') 
plt.colorbar(label = 'Dybde i meter', fraction = 0.024)
plt.xlabel('Breddegrad')
plt.ylabel('Lengdegrad')
```

## Animasjon

For å gå eitt steg vidare, kan me freista å animera kartet, for å visa
jordskjelv år for år.  I praksis vil det seia at me lagar eitt kart for
kvart år, men speler dei saman som ein slags video.
Sjølve animasjonseffekten får me frå `display`-funksjonen som me 
importerer frå `IPython`.

For å ta eitt steg åt gongen, lagar me ein funksjon som plottar datasettet
for eitt år, og testar han.

```{code-cell} ipython3
from IPython import display
def yearplot(df,y=1973):
   df0 = df[ df["Year"] == y ]
   fig = mapplot()
   plt.scatter(df0["Longit"], df0["Latit"], s = 5, color = 'r')
   plt.xlabel('Breddegrad')
   plt.ylabel('Lengdegrad')
   plt.title("Årstall = " + str(y))
yearplot(data_J,1980)
```

::: {admonition} Refleksjon
Her skulle det meste vera kjend frå føregåande døme.
Skjøner du korleis funksjonen er bygd opp?
Kva gjer `plt.title()`?
:::

For å køyra animasjonen over riktig periode, må me finna fyrste og siste år, slik:
```{code-cell} ipython3
startar = data_J["Year"].min()
sluttar = data_J["Year"].max()
```

Då er alt klart for sjølve animasjonskoden.
Det er rett og slett ei løkke som itererer år for år over perioden,
og plottar for kvart år.

```{code-cell} ipython3
for y in range(startar,sluttar+1):
   display.clear_output(wait=True)             
   yearplot(data_J,y)
   plt.pause(0.25)
```

::: {admonition} Refleksjon
Er animasjonen nyttig for å forstå datasettet?
Gjev han eit betre inntrykk en tidlegare døme?
:::

::: {admonition} Oppgåve
Skriv om `yearplot()` slik at me får ein animasjon som viser
styrke og djupne med storleik og fargekoding.
:::
