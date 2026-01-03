---
title: Predator-Prey
jupytext:
  formats: md:myst,ipynb
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.17.0
kernelspec:
  display_name: dataprog
  language: python
  name: dataprog
---

# Rovdyr og byttedyr

::: {admonition} Kjelder
Løysinga er delvis inspirert av
[mhawryluk på githun](https://github.com/mhawryluk/abm-predator-prey).
:::

Rovdyr og byttedyr er eit klassisk simuleringsproblem i biologi og økologi.
Det er interessant fordi det er so dynamisk.
Dersom der er mykje byttedyr, har rovdyra mykje mat, og dei vert fleire.
Når der er myke rovdyr, har byttedyra dårlege kår, og dei vert færre.
Når der so vert færre byttedyr, vil rovdyra svelta, og dei vert færre.

Ein kan simulera denne dynamikken på fleire måtar, men her skal me bruka
han til å illustrera agent-basert modellering og objekt-orienter programmering.
Me skal sjå på alle dyra som agentar.

For å gjera det enkelt, har me berre to artar, rev og kanin.

For å gjera det enkelt, let me verda vera eit rutenett i to dimensjonar,
der alle dyra lever.  Kvar rute har plass til eitt dyr.

Dyr har nokre felles eigenskapar.
+ Dei har ein plassering $(x,y)$ i verda.
+ Dei kan flytta seg til ei naborute.
+ Dei kan sjå kva som er i rutane kring seg, slik at dei veit kvar det er lurast å gå.
+ Dei kan formera seg saman med eit individ av same art og motsett kjønn 

I tillegg kan ein rev eta ein kanin, dersom dei kjem i same rute.

I tillegg til artane treng me ei klasse for verda, som held greie både på
landskapet (rutenettet) og tida.
Me skal simulera i diskret tid.
Dvs. at me har faste tidssteg, t.d. éin dag, og kvar agent får ei sjanse til å 
handla for kvart tidssteg.


```{code-cell} ipython3
import random
```

```{code-cell} ipython3
class Agent:
   maxenergy = 4
   def __init__(self,world):
      self.world = world
      self.energy = random.randint(self.maxenergy)
   def act(self,moves):
      pass
```

```{code-cell} ipython3
class Fox(Agent):
      pass
class Rabbit(Agent):
      pass
```

```{code-cell} ipython3
class World:
   def __init__(self,size=(600,400)):
      self.xlen, self.ylen = size
      self.worldgrid = {}
   def act(self,moves):
      agents = list(self.worldgrid.items())
      random.shuffle( agents )
      for pos, agent in agents:
          agent.act()

   def getpoints(self):
      return [[]]
```
