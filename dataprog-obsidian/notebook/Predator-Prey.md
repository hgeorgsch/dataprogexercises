---
jupytext:
  formats: md:myst,ipynb
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.18.1
kernelspec:
  display_name: dataprog
  language: python
  name: dataprog
---

# Rovdyr og byttedyr

::: {admonition} Kjelder
Løysinga er delvis inspirert av
[mhawryluk på github](https://github.com/mhawryluk/abm-predator-prey).
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

## Grunnstruktur

Lat oss fyrst setja opp ein grunnmodell med dei klassene som me treng.
Me kjem til å bruka slumptal og plotting, so lat oss importera biblioteka
med ein gong.

```{code-cell} ipython3
import random
import matplotlib.pyplot as plt
```

Me treng ei klasse for verda.
I fyrste omgong, freistar me å få dette so enkelt som råd.

Klassa treng eit rutenett for verda.  Me definerer dette som ein `dict`
med oppslag for $(x,y)$-verdiar.
Me har ein metode for å setja inn ein agent, no på tilfeldig plass, og
ein for å fjerna agentar.

For simuleringa er `act` den sentrale metoden.  Denne køyrer eitt tidssteg
og lèt alle agentane handla.
Til sist har me ein metode for å returnera alle agentane slik at me kan plotta.

```{code-cell} ipython3
class World:
   def __init__(self,size=(600,400)):
      """
      Instantier verda med eit rutenett.
      """
      self.xlen, self.ylen = size
      self.worldgrid = {}
   def addAgent(self,agent):
      """
      Set ein agent inn på tilfeldig plass i rutenettet.
      """
      ag = 1
      while ag is not None:
          x = random.randint( 0, self.xlen )
          y = random.randint( 0, self.ylen )
          ag = self.worldgrid.get( (x,y) )
      self.worldgrid[(x,y)] = agent
      return (x,y)
   def removeAgent(self,agent):
      """
      Fjern agenten frå ein gjeven plass i rutenettet.
      """
      del self.worldgrid[agent.getPosition]
   def act(self,moves):
      """
      Køyr eitt tidssteg i simulator, dvs. bed alle agentane om å handla.
      """
      agents = list(self.worldgrid.items())
      random.shuffle( agents )
      for pos, agent in agents:
          agent.act()
   def getPoints(self):
       """
       Returner posisjonane til alle agentane.
       Returverdien er ein `dict` med oppslag for kvar type agent.
       Kvart oppslag er ei liste med $(x,y)$-verdiar.
       """
       r = {}
       for pos, agent in self.worldgrid.items():
           t = agent.getType()
           r.setdefault( t, [] )
           r[t].append( pos )
       return r
```

Det fyrste utkastet til agenten er ufullstendig, men me lagar det for
å kunna testa `World`-klassa.
Alt me treng er konstruktøren, som òg set agenten inn i verda, samt
metodar for å henta ut typen og posisjonen til agenten.

```{code-cell} ipython3
class Agent:
   agenttype = None
   def __init__(self,world):
      self.world = world
      self.position = self.world.addAgent( self )
   def getPosition(self):
      return self.position
   def act(self,moves):
      pass
   def getType(self):
      return self.agenttype
```

Me kan laga ulike typar agentar, men førebels har dei berre kvart
sitt namn, «Fox» eller «Rabbit».

```{code-cell} ipython3
class Fox(Agent):
    agenttype = "Fox"
class Rabbit(Agent):
    agenttype = "Rabbit"
```

## Testing

No er alt klart for testing.
Steg 1 er å oppretta verda og agentane.

```{code-cell} ipython3
world = World()
_ = [ Rabbit(world) for _ in range(50) ]
_ = [ Fox(world) for _ in range (25) ]
```

Hugs at agenten legg seg sjølv inn i verda når han vert instantiert.
Difor treng me ikkje lagra agentane i nokon variabel.  Alt ligg i `world`.
For å sjekka at ting verkar, kan me plotta verda med alle agentane som fargeflekkar.

```{code-cell} ipython3
pts = world.getPoints()
for key, lst in pts.items():
   x = [ x for (x,y) in lst ]
   y = [ y for (x,y) in lst ]
   plt.scatter( x, y, label=key )
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

```

Dette skulle sjå greitt ut.  


## Oppførsel

No er det på tide å laga agentane slik at dei kan gå, eta og verta etne.

```{code-cell} ipython3
class Agent:
   maxenergy = 4
   agenttype = None
   def __init__(self,world):
      self.world = world
      self.energy = random.randint(0,self.maxenergy)
      self.position = self.world.addAgent( self )
   def getPosition(self): return self.position
   def act(self,moves):
      if self.energy <= 0: self.die()
   def die(self):
      self.world.removeAgent( self )
   def getType(self): return self.agenttype
```
