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
tags:
  - exercise
  - data/map
---

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

```{code-cell} ipython3
print(max(data_J["Latit"])) # y-akse (kommer først)
print(min(data_J["Latit"]))
print(max(data_J["Longit"])) # x-akse (siste)
print(min(data_J["Longit"]))
print(max(data_J["Depth"])) # maks er 700
print(min(data_J["Depth"])) # min er 0 (??)
print(max(data_J["Magnitude"])) # maks er 9.1
print(min(data_J["Magnitude"])) # Min er 4.5
```

## Numeriske plott

```{code-cell} ipython3
# Plotter antall skjelv av de ulike typene


values, counts = np.unique((data_J["Magnitude"]).values, return_counts = True)
plt.bar(values, counts, width = 1.0)
```

```{code-cell} ipython3
# Plotter antall skjelv ved ulike dybder

values, counts = np.unique((data_J["Depth"]).values, return_counts = True)
plt.bar(values, counts, width = 1.0)
```

```{code-cell} ipython3
# Plotter dybde mot styrke

dybde = data_J["Depth"]
dybde = dybde*(-1)
styrke = data_J["Magnitude"]
print(dybde[0:10])

plt.figure(figsize=(8, 10), dpi=80)
plt.scatter(dybde, styrke, s = 0.1)
```

## Kartplott

Henter området vi vil plotte jordskjelv over fra https://www.openstreetmap.org/export#map=5/51.500/-0.100

Skriv inn begrensningene for lengde og breddegrad og last ned

```{code-cell} ipython3
# Plotter posisjon

lengdegrad = data_J["Latit"]
breddegrad = data_J["Longit"]

plt.figure(figsize=(13, 6), dpi=80)
plt.scatter(breddegrad, lengdegrad, s = 0.1)
```

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
depth = data_J["Depth"]

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
