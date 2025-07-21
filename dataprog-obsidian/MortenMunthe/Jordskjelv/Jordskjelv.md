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

Arbeidet er lånt frå Morten Munthe ved UiB.
Bruksvilkår må avklarast.

:::

# Jordskjelv

Her skal me bruka ei  fil med over 200 000 jordskjelv fra 1973 til 2014.
Den store utfordringa som me skal løysa er å plotta jordskjelvdata på verdskartet. 
Dette er vanskeleg fordi jorda er rund og kartet er flatt, slik at me må rekna om geografisk posisjon frå jordkula til plankoordinatar på kartet.

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
djupna = data_J["Depth"]
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
values, counts = np.unique(djupna, return_counts = True)
plt.bar(values, counts, width = 1.0)
```

Dette var både treigt, og ikkje spesielt nyttig.  Djupe skjelv er openbert so sjeldne at me ikkje ser dei.
Me ser at det meste skjer mellom 0 og 150 meter, so me kan laga eit grovt histogram i dette intervallet.

```{code-cell} ipython3
plt.hist(djupna, bins=10, range=(0,150) )
```

::: {admonition} Oppgåve
Bruk dokumentasjonen til å laga pene og informative histogram over djupna.
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
plt.scatter(djupna, styrke, s = 0.1)
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

Henter området vi vil plotte jordskjelv over fra https://www.openstreetmap.org/export#map=5/51.500/-0.100

Skriv inn begrensningene for lengde og breddegrad og last ned


```{code-cell} ipython3
# Plotter posisjon overlagt et kart

import matplotlib.pyplot as plt

img = plt.imread("Equirectangular-projection.jpg")
fig, ax = plt.subplots(figsize=(10, 12), dpi=100)
ax.imshow(img, extent=[-180, 180, -90, 90])

plt.scatter(breddegrad, lengdegrad, s = 0.1, color = 'r')
plt.xlabel('Breddegrad')
plt.ylabel('Lengdegrad')
```

Kartet er et rektangelkart med ekvidistanse både langs lengde- og breddegradene. Kartet er hentet fra https://simple.wikipedia.org/wiki/Equirectangular_projection

```{code-cell} ipython3
# Plotter alle over en gitt styrke

import matplotlib.pyplot as plt

img = plt.imread("Equirectangular-projection.jpg")
fig, ax = plt.subplots(figsize=(10, 12), dpi=100)
ax.imshow(img, extent=[-180, 180, -90, 90])

styrke = float(input("Hva er den laveste styrken du vil plotte? "))

mag = data_J["Magnitude"]
leng = data_J["Latit"]
bred = data_J["Longit"]

n = len(data_J["Magnitude"])
lg = []
bg = []
for i in range(n):
    if mag[i+1] > styrke:
        lg.append(leng[i+1])
        bg.append(bred[i+1])   

plt.scatter(bg, lg, s = 5, color = 'r')
plt.xlabel('Breddegrad')
plt.ylabel('Lengdegrad')
```

```{code-cell} ipython3
# Plotter styrke som størrlse

import matplotlib.pyplot as plt

img = plt.imread("Equirectangular-projection.jpg")
fig, ax = plt.subplots(figsize=(10, 12), dpi=100)
ax.imshow(img, extent=[-180, 180, -90, 90])

year = float(input("Hvilket år vil du plotte (1973 - 2014)? "))

ar = data_J["Year"]
mag = data_J["Magnitude"]
leng = data_J["Latit"]
bred = data_J["Longit"]

n = len(data_J["Magnitude"])
size = []
lg = []
bg = []

styrke = 5.5

for i in range(n):
    if ar[i+1] == year and mag[i+1] > styrke:
        size.append((mag[i+1]-styrke) * (400/(9.1-styrke))) 
        lg.append(leng[i+1])
        bg.append(bred[i+1])

plt.scatter(bg, lg, s = size, facecolor = 'none', edgecolor = 'r') # Lager sirkler slik at det er letter å skille de ulike styrkene
plt.xlabel('Breddegrad')
plt.ylabel('Lengdegrad')
```

```{code-cell} ipython3
# Plotter styrke som størrlse og dybde med farge

import matplotlib.pyplot as plt

img = plt.imread("Equirectangular-projection.jpg")
fig, ax = plt.subplots(figsize=(10, 12), dpi=100)
ax.imshow(img, extent=[-180, 180, -90, 90])

year = float(input("Hvilket år vil du plotte (1973 - 2014)? "))

ar = data_J["Year"]
mag = data_J["Magnitude"]
leng = data_J["Latit"]
bred = data_J["Longit"]
depth = djupna

n = len(data_J["Magnitude"])
size = []
lg = []
bg = []
dyb = []

styrke = 5.5

for i in range(n):
    if ar[i+1] == year and mag[i+1] > styrke:
        size.append((mag[i+1]-styrke) * (400/(9.1-styrke))) 
        lg.append(leng[i+1])
        bg.append(bred[i+1])
        dyb.append(depth[i+1])

plt.scatter(bg, lg, s = size, c=dyb, cmap = 'YlOrRd') # Lager sirkler slik at det er letter å skille de ulike styrkene
plt.colorbar(label = 'Dybde i meter', fraction = 0.024)
plt.xlabel('Breddegrad')
plt.ylabel('Lengdegrad')
```

```{code-cell} ipython3
# Plotter animasjon av skjelv per år over gitt styrke

import matplotlib.pyplot as plt
from IPython import display

img = plt.imread("Equirectangular-projection.jpg")
fig, ax = plt.subplots(figsize=(10, 12), dpi=100)
ax.imshow(img, extent=[-180, 180, -90, 90])

styrke = float(input("Hva er den laveste styrken du vil plotte? "))

mag = data_J["Magnitude"]
leng = data_J["Latit"]
bred = data_J["Longit"]
n = len(data_J["Magnitude"])
lg = []
bg = []
startar = data_J["Year"][1]
ar = data_J["Year"][1]

for i in range(n):
    if mag[i+1] > styrke:
        startar = data_J["Year"][i+1]
        lg.append(leng[i+1])
        bg.append(bred[i+1])

    if ar != startar:                              
        #figure(figsize=(10,10))
        display.clear_output(wait=True)             # Her oppdatere vi plottet vårt
        img = plt.imread("Equirectangular-projection.jpg")
        fig, ax = plt.subplots(figsize=(10, 12), dpi=100)
        ax.imshow(img, extent=[-180, 180, -90, 90])
        plt.scatter(bg, lg, s = 5, color = 'r')
        plt.xlabel('Breddegrad')
        plt.ylabel('Lengdegrad')
        tid = "Årstall = " + str(ar)
        plt.title(tid)
        plt.pause(0.3)                                  # Pause mellom hver gang den oppdaterer plottet i sekunder
        ar = startar
        
```
