---
jupytext:
  formats: md:myst,ipynb
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.18.1
kernelspec:
  name: dataprog
  language: python
  display_name: dataprog
---

# Listekomprehensjon

Her skal me ta utgangspunkt i dømet på [](Simulering av kontantstraum),
og sjå litt nærare på korleis me samlar opp data i ei liste.
Lat oss kjapt importera PyPlot og setja opp parametre for startsaldo,
rentesats og tidsperiode.

```{code-cell} ipython3
import matplotlib.pyplot as plt
start = 10000
rente = 0.04
tid = list(range(20))
```

Her reknar me kun med forrenting på startbeløpet og ingen periodisk 
sparing.
Saldoen etter $y$ år er då $s\cdot (1+r)^y$ der $s$ er startsaldoen
og $r$ er rentesatsen.
Dette kan me implementera som ein python-funksjon, slik.

```{code-cell} ipython3
def saldomedrente(start,years):
   return start*(1+rente)**years
```

Dersom me skal plotta saldoen som ein funksjon av tiden, må me
på ein eller annan måte laga oss ei liste med alle saldoane.
Dette kan me gjera med ein `for`-løkke slik:

```{code-cell} ipython3
y = [ ]
for i in tid:
   saldo = saldomedrente(start,i)
   y.append( saldo )
plt.plot(tid,y)
plt.show()
```

Med kan like gjerne gjera det med listekomprehensjon.
Da kan det sjå slik ut:

```{code-cell} ipython3
y = [ saldomedrente(start,i) for i in tid ]
plt.plot(tid,y)
plt.show()
```

Det som tek fire liner med `for`-løkka, kan me altso skrive som èi line
med listekomprehensjon.

## Andre døme

```{code-cell} ipython3
import numpy as np

start_aar = 2023
tid_aar = [f"01.01.{start_aar+t}" for t in tid if t%2 == 0]
print(tid_aar)
```

```{code-cell} ipython3
plt.bar(tid, y)
plt.xticks(ticks=np.arange(0,len(tid_aar)*2,2), labels=tid_aar, rotation=45) 
plt.show()
```

## Oppsummering

Ofte er slike listekomprehensjonar lette å lese, skriva og forstå.
Ein skal likevel ikkje overdriva.
Somme tider er ei *for*-løkke som byggjer opp lista med `append` enklare.
Det er viktig å fokusera på å skriva koden slik at han er lett å lesa.  Di vanskelegare koden er å lesa, di fleire feil vil ein gjera.
