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
plt.savefig( "klyngedemo-initial01.svg" )
```

::: {tip}
Me bruker `savefig()` for å lagra figuren til bruk i foilane.
Billetformatet er SVG som gjev vektorgrafikk særleg tilpassa bruk
saman med HTML.
:::

Til sist skal me setja saman datasettet til éi matrise.

```{code-cell} ipython3
data0 = np.vstack( [ a,b,c] )
print( data0 )
```

Me definerer òg *ground truth* til seinare evaluering.
Dvs. ein vektor med eitt element (0, 1 eller 2) for kvar rad i `data0`.

```{code-cell} ipython3
gt0 = np.vstack( [ np.zeros( [size, 1] ), np.ones([size,1]), np.ones([size,1])*2 ] )
print( gt0.T )
```

*Merk* at me skriv ut den transponerte for at utskrifta skal ta mindre plass.

Algoritmen skal sjølvsagt ikkje ha informasjon om *ground truth*.
Difor skal me stokka radane tilfeldig.  
For å kunna stokka både `data0` og `gt0` lagar me fyrst ei liste med
indeksar som vert stokka, og so bruker me dei til å stokka datasettet.

```{code-cell} ipython3
idx = np.arange(300)
np.random.shuffle( idx )
print( idx )
```

```{code-cell} ipython3
data = data0[idx,:]
gt = gt0[idx,:]
print( gt.T )
```

Indekseringa med `idx` over tek alle elementa, men i ny rekkjefylge.
Dermed kjem ikkje alle datapunkta frå same klasse etter kvarandre.

For å testa at datasettet stadig er rett, kan me plotta og samanlikna med spreideplottet over.

```{code-cell} ipython3
plt.scatter( data[:,0], data[:,1], c=gt, marker="." )
plt.savefig( "klyngedemo-initial02.svg" )
```

Dette ser rimeleg ut.
Me skal laga ein figur utan fargar òg.  Dette er berre til bruk
i foilane.

```{code-cell} ipython3
plt.scatter( data[:,0], data[:,1], c="b", marker="." )
plt.savefig( "klyngedemo-initial.svg" )
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
plt.savefig( "klyngedemo00.svg" )
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
def kmplot( data, model, pred, fn=None ):
    plt.scatter( data[:,0], data[:,1], c=p, marker="." )
    plt.scatter( model[:,0], model[:,1], c="k", marker="x" )
    if fn: plt.savefig( fn )
```

No kan me gjera prediksjonen og plotta resultatet, ved hjelp av funksjonane.

```{code-cell} ipython3
p = predict( data, model )
kmplot( data, model, p, "klyngedemo01a.svg" )
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
kmplot( data, model, p, "klyngedemo01b.svg" )
```

Klyngene er dei same som sist, men me kan sjå korleis modellpunkta har flytta seg.

No kan me gjenta heile prosessen.

```{code-cell} ipython3
p = predict( data, model )
kmplot( data, model, p, "klyngedemo02a.svg" )
```

```{code-cell} ipython3
model = means( data, p )
kmplot( data, model, p, "klyngedemo02b.svg" )
```

```{code-cell} ipython3
p = predict( data, model )
kmplot( data, model, p, "klyngedemo03a.svg" )
```

```{code-cell} ipython3
model = means( data, p )
kmplot( data, model, p, "klyngedemo03b.svg" )
```

```{code-cell} ipython3
p = predict( data, model )
kmplot( data, model, p, "klyngedemo04a.svg" )
```

```{code-cell} ipython3
model = means( data, p )
kmplot( data, model, p, "klyngedemo04b.svg" )
```

```{code-cell} ipython3
for i in range(1000):
   p = predict( data, model )
   model = means( data, p )
kmplot( data, model, p, "klyngedemo-final.svg" )
```

Det er ikkje sikkert at dei identifiserte klyngene stemmer med dei opprinnelege, men det kan vera gøy å samanlikna.
Då kan me bruka ulike farger for predikerte klasser og ulike symbol for *ground truth*.  Diverre kan me ikkje bruka ein `array` som `marker` på same måte som me gjer med `c`, so me må dela datasettet opp.

Me startar med å definera indeksane for kvar *ground truth*-klasse.

```{code-cell} ipython3
idx0 = gt == 0
idx1 = gt == 1
idx2 = gt == 2
print( idx0.T )
print( idx1.T )
print( idx2.T )
```

No kan me plotta kvar *ground truth*-klasse med ulik `marker`.

```{code-cell} ipython3
plt.scatter( data[idx0,0], data[idx0,1], c=p[idx0], marker="+" )
plt.scatter( data[idx1,0], data[idx1,1], c=p[idx1], marker="x" )
plt.scatter( data[idx2,0], data[idx2,1], c=p[idx2], marker="o" )
plt.scatter( model[:,0], model[:,1], c="k", marker="x" )
```

Det gjekk visst ikkje.  Me har brukt tre indeksar i ei todimensjonal matrise.  Det er vanskeleg å sjå kvar det kan vera.
Me har éin indeks på `p`, to på `modell` og to på `data`, men `idx` er ein `array` med to dimensjonar, og dermed indekserar me tre dimensjonar i `data`.
Løysinga er å flata ut `idx`.  Ho har berre éi søyle.

```{code-cell} ipython3
idx0 = idx0.flatten()
idx1 = idx1.flatten()
idx2 = idx2.flatten()
plt.scatter( data[idx0,0], data[idx0,1], c=p[idx0], marker="+" )
plt.scatter( data[idx1,0], data[idx1,1], c=p[idx1], marker="x" )
plt.scatter( data[idx2,0], data[idx2,1], c=p[idx2], marker="*" )
plt.scatter( model[:,0], model[:,1], c="k", marker="x" )
```

Dette vart òg rart.  Det ser ikkje ut som om same tal gjev same farge i kvart kall til `scatter`. 
Det ser ein òg om ein slår opp i [dokumentasjonen](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.scatter.html).
Fargen avheng av fleire faktorar.

Dette kan me fiksa ved å byta ut tala med farger i `p`.

```{code-cell} ipython3
pc = p.astype(str)
pc[ pc == "0" ] = "r"
pc[ pc == "1" ] = "g"
pc[ pc == "2" ] = "b"
plt.scatter( data[idx0,0], data[idx0,1], c=pc[idx0], marker="+" )
plt.scatter( data[idx1,0], data[idx1,1], c=pc[idx1], marker="x" )
plt.scatter( data[idx2,0], data[idx2,1], c=pc[idx2], marker="*" )
plt.scatter( model[:,0], model[:,1], c="k", marker="x" )
```

Det vart litt omstendeleg, men eg valde å visa nokre av dei feila som eg gjorde på vegen.

Me ser ganske godt samsvar mellom dei opprinnelege klyngene og prediksjonane, sjølv om det ikkje er perfekt.

+++

## Skisser til grunnleggjande syntaks

Det siste avsnittet er prøving og feiling med grunnleggjande syntaks.

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
