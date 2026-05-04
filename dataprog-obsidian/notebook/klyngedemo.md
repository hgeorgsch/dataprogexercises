---
jupytext:
  formats: ipynb,md:myst,py:percent
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.19.1
kernelspec:
  display_name: dataprog
  language: python
  name: dataprog
---

# Demo: Klyngeanalyse

+++

Denne demonstrasjonen gjev ein rudimentær implementasjon av $k$-means.
Hensikta er å visa korleise modellen utviklar seg for kvar iterasjon.

Det er ikkje meininga, på dette stadiet, å gje ein fullverdig introduksjon her.
Poenget er grafane som eg bruker i eit føredrag.

## Definisjon av $k$-*means*

Den aller best kjende algoritmen for maskinlæring utan rettleiing
(*unsupervised learning*) heiter $k$-*means*.  Hensikta med $k$-*means*
er å ta eit datasett og dela det inn i $k$ klyngar (*clusters*) med
datapunkt som liknar på kvarandre.

Kvart datapunkt er ein vektor i eit $n$-dimensonalt rom, dvs. tuplar
av $n$ tal.  For at $k$-*means* skal fungera godt, må me normalisera
datasettet slik at alle variablane har om lag same omfang.  Dvs.
at kvar variabel (søyle) vert skalert. Dei to vanlegaste teknikkane
er å skalera slik at alle verdiane fell i intervallet $(0,1)$, eller
slik at gjennomsnittet vert 0 og utvalsstandardavviket 1.

I $k$-*means* vert kvar klynge representert ved ein vektor.
Målet når algoritmen er ferdig, er to eigenskapar
1.  Den representative vektoren er gjennomsnittet av alle vektorane i klynga.
2.  Kvar vektor i datasettet vert assosiert med den representative vektoren
    som ligger nærast (kortast euklidsk avstand).

For å nå dette målet vil algoritmen iterativt oppdatera løysinga og vekselsvis
oppnå mål 1 og mål 2.  For kvar iterasjon vert feilen i kvar eigenskap mindre.

Algoritmen startar med $k$ tilfeldig valde representative vektorar.  
I kvar iterasjon vil algoritmen
1.  Assosiera kvart datapunkt med den næraste representative vektoren og
    oppdatera klyngane.
2.  Rekna eit nytt sett med representative vektorar ved å ta gjennomsnittet
    av kvar klynge.

Algoritmen terminerer når ingen vektorar lenger byter klynge.
Det kan vera naudsynt å setja andre stoppvilkår dersom ei perfekt
løysing ikkje finst eller datasettet er svært stort.

## Konfigurasjon

I dette dømet skal me implementera $k$-means frå botnen av, so me
importerer berre `numpy` for matriserekning og `pyplot` for visualisering.

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt
```

Her vil me bruka konstant $k=3$ i $k$-*means*-*clustering*.
Me skal laga eit datasett med kring 100 (`size`) datapunkt per klynge.

```{code-cell} ipython3
k = 3
size = 100
```

## Tilfeldig generert datasett

For å få gode illustrasjonar vil me laga eit tilfeldig datasett med
tre overlappande klyngar.  Dette gjer me ved å trekkja tre normalfordelte
utval med litt ulike gjennomsnitt ($\mu$) og standardavvik ($\sigma$).
Av omsyn til visualiseringa har me berre to søyler i datasettet.

```{code-cell} ipython3
a = np.random.normal( size=[size, 2], loc=(2,0), scale=(0.6,1) )
b = np.random.normal( size=[size, 2], loc=(0,2), scale=(1.2,0.7) )
c = np.random.normal( size=[size, 2], loc=(-1,-1), scale=(1,1) )
```

Funksjonen `normal` gjev tilfeldige, normalfordelte verdiar.
Her er `loc` gjennomsnittet i kvar dimensjon og `scale` standardavviket.
For å visa kva me har generert, kan me visualisera med eit spreideplott.

```{code-cell} ipython3
plt.scatter( a[:,0], a[:,1], c="r", marker="x" )
plt.scatter( b[:,0], b[:,1], c="g", marker="+" )
plt.scatter( c[:,0], c[:,1], c="b", marker="d" )
```

Til sist skal me setja saman datasettet til éi matrise.

```{code-cell} ipython3
data0 = np.vstack( [ a,b,c] )
print( data0 )
```

Me definerer òg *ground truth* til seinare evaluering.
Dvs. ein vektor med eitt element (0, 1 eller 2) for kvar rad i `data0`.

```{code-cell} ipython3
gt0 = np.vstack( [ np.zeros( [30, 1] ), np.ones([30,1]), np.ones([30,1])*2 ] )
print( gt0 )
```

Algoritmen skal sjølvsagt ikkje ha informasjon om *ground truth*.
Difor skal me stokka radane tilfeldig.  
For å kunna stokka både `data0` og `gt0` lagar me fyrst ei liste med
indeksar som vert stokka, og so bruker me dei til å stokka datasettet.

```{code-cell} ipython3
idx = np.random.shuffle( list(range(300) ) )
print( idx )
```

```{code-cell} ipython3
gt = gt0[idx,:]
print( gt )
```

```{code-cell} ipython3
data = data0[idx,:]
print( data )
```



## Implementasjon av $k$-*means*

No må me definera ein tentativ modell, som består av $k$ vilkårleg valde punkt,
som representerer dei $k$ klyngane som me skal finna.

```{code-cell} ipython3
model = np.random.normal( size=(3,2))
print(model)
```

For å sjekka at alt er rett kan me plotta datasettet saman med modellpunkta, slik.

```{code-cell} ipython3
plt.scatter( data[:,0], data[:,1], c="b", marker="." )
plt.scatter( model[:,0], model[:,1], c="r", marker="x" )
```

Modellen er sjølvsagt ikkje god. Modellpunkta er klynga saman og er lite representative for spreidinga i datasettet,
men so var dei òg tilfeldig valde.

+++

## Predict

I $k$-means er der to steg som vert gjentekne.  Det fyrste er prediksjonen, 
der kvart datapunkt vert assosiert med det næraste modellpunktet.
Den fylgjande funksjonen gjer denne jobben. Returverdien er ein vektor med
eitt element for kvart datapunkt, der verdien er indeksen åt det næraste modellpunktet.

```{code-cell} ipython3
def predict( a, m ):
    A = a[np.newaxis,:,:]
    M = m[:,np.newaxis,:]
    diff = A - M
    dist = (diff**2).sum(axis=2)
    return dist.argmin(axis=0)
```

Me treng òg ein funksjon for å plotta datasettet med ulike farger for kvar klynge.

```{code-cell} ipython3
def kmplot( data, model, pred ):
    plt.scatter( data[:,0], data[:,1], c=p, marker="." )
    plt.scatter( model[:,0], model[:,1], c="k", marker="x" )
```

No kan me gjera prediksjonen og plotta resultatet, ved hjelp av funksjonane.

```{code-cell} ipython3
p = predict( data, model )
kmplot( data, model, p )
```

Modellpunkta er stadig dei same, men no kan me sjå kva datapunkt som høyrer til same klynge.
Det neste steget er å revidera modellen.  Fylgjande funksjon reknar ut nye modellpunkt som
gjennomsnittet frå kvar klynge.

```{code-cell} ipython3
def means( a, p ):
    l = []
    for i in range(k):
        t = a[ p==i, : ]
        l.append( t.mean(axis=0) )
    return np.vstack( l )
```

No kan me bruka denne funksjonen og plotta på nytt.

```{code-cell} ipython3
model = means( data, p )
kmplot( data, model, p )
```

Klyngene er dei same som sist, men me kan sjå korleis modellpunkta har flytta seg.

No kan me gjenta heile prosessen.

```{code-cell} ipython3
p = predict( data, model )
kmplot( data, model, p )
```

```{code-cell} ipython3
model = means( data, p )
kmplot( data, model, p )
```

```{code-cell} ipython3
p = predict( data, model )
kmplot( data, model, p )
```

```{code-cell} ipython3
model = means( data, p )
kmplot( data, model, p )
```

```{code-cell} ipython3
p = predict( data, model )
kmplot( data, model, p )
```

```{code-cell} ipython3
model = means( data, p )
kmplot( data, model, p )
```

```{code-cell} ipython3
for i in range(100):
   p = predict( data, model )
   model = means( data, p )
kmplot( data, model, p )
```

## Sketches on basic functionality

```{code-cell} ipython3
a = np.array( [[[1, 2,3 ],[ 1,0,2]]] ) *2
b = np.array( [[[ 2,2,2]],[[ 1, 1,1]] ] ) 
print(b)
```

```{code-cell} ipython3

```

```{code-cell} ipython3
c = a-b
print(c)
```

```{code-cell} ipython3
c.shape
```

```{code-cell} ipython3
d= c**2
print(d)
```

```{code-cell} ipython3
dist = d.sum( axis=2 )
print(dist)
```

```{code-cell} ipython3
dist.argmin(axis=0)
```

```{code-cell} ipython3

```
