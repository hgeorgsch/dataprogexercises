---
title: Listekomprehension
tags: exercise
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
# Listekomprehension

Her skal me ta utgangspunkt i dømet på [[Simulering av kontantstraum]], og sjå litt nærare på korleis me samlar opp data i ei liste.

```{code-cell} ipython3
import matplotlib.pyplot as plt
start = 10000
rente = 0.04
tid = list(range(20))
```

```{code-cell} ipython3
def saldomedrente(start,years):
   return start*(1+rente)**years
```
```
    
```{code-cell} ipython3
y = [ ]
for i in tid:
   saldo = saldomedrente(start,i)
   y.append( saldo )
plt.plot(tid,y)
plt.show()
```


Med listekomprehensjon

```{code-cell} ipython3
y = [ saldomedrente(start,i) for i in tid ]
plt.plot(tid,y)
plt.show()
```

## Andre døme

```{code-cell} ipython3
import matplotlib.pyplot as plt
import numpy as np


tid = [ t for t in range(n_tid)]
saldo = [forrentning(start, rente, t) for t in tid]

start_aar = 2023
tid_aar = [f"01.01.{start_aar+t}" for t in tid if t%2 == 0]
print(tid_aar)
plt.bar(tid, saldo)
plt.xticks(ticks=np.arange(0,10,2), labels=tid_aar, rotation=45) 
plt.show()

```

## Oppsummering

Ofte er slike listekomprehensjonar lette å lese, skriva og forstå.
Ein skal likevel ikkje overdriva.
Somme tider er ei *for*-løkke som byggjer opp lista med `append` enklare.
Det er viktig å fokusera på å skriva koden slik at han er lett å lesa.  Di vanskelegare koden er å lesa, di fleire feil vil ein gjera.