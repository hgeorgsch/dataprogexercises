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

```{code-cell} ipython3
import numpy as np
import matplotlib.pyplot as plt
```

Her vil me bruka konstant $k=3$ i $k$-*means*-*clustering*.

```{code-cell} ipython3
k = 3
size = 100
```

## Tilfeldig generert datasett

```{code-cell} ipython3
a = np.random.normal( size=[size, 2], loc=(2,0), scale=(0.6,1) )
b = np.random.normal( size=[size, 2], loc=(0,2), scale=(1.2,0.7) )
c = np.random.normal( size=[size, 2], loc=(-1,-1), scale=(1,1) )

plt.scatter( a[:,0], a[:,1], c="r", marker="x" )
plt.scatter( b[:,0], b[:,1], c="g", marker="+" )
plt.scatter( c[:,0], c[:,1], c="b", marker="d" )
```

```{code-cell} ipython3
data = np.vstack( [ a,b,c] )
gt = np.vstack( [ np.zeros( [30, 1] ), np.ones([30,1]), np.ones([30,1])*2 ] )
```

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
