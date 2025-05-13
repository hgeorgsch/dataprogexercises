---
title: Klasser og Objekt
jupytext:
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

* Når vi skulle simulere fiskeskuter lagde vi en dictionay som holdt dataen til de individuelle fiskeskutene

```{code-cell} ipython3
skute = {"navn": "Tilfeldig", 
         "last": 0,
         "fiskefunksjon": lambda: 75}
```

* Her representerer dataen vår en skute, et objekt -- og skuten har inneholder både data *og metoder*

+++

* Når dataen vår er slik (objekter med vanlig data og metoder) er det vanlig å representere dataen i en *klasse* heller enn en dictionary
* Klasser definerer objekter slik som skuten vår, og vi har egentlig brukt de masse

```{code-cell} ipython3
heltall = 4
print(type(heltall))
```

```{code-cell} ipython3
tekststreng = "Heisann!"
print(type(tekststreng))
```

* Variablene `heltall` og `tekststreng` er objekter, eller instanser av henholdsvis klassene `int` og `str`
* Når vi skal ha tak i et objekts data og metoder (funksjoner) bruker vi punktum `objekt.data`, `objekt.funksjon()`

```{code-cell} ipython3
min_liste = [1,2,3,4]
print(type(min_liste))
min_liste.pop()
```

* Her er `min_liste` et objekt av typen `list` eller en instans av klassen `list`
* Listeobjekter har innebygde metoder/funksjoner som gjør ting med dataen til objektet (feks, pop(), append() osv)

+++

* Vi kan lage egne klasser:

```{code-cell} ipython3
class Skute:

    antall_skuter = 0 #Klassevariabel for alle skuter

    #funksjonen __init__(...) er spesiell: Den kalles hver gang vi skal lage en instans av klassen
    def __init__(self, navn, fiskefunksjon): #Første argument i klassefunksjoner er alltid objektet selv
        self.navn = navn #Skuteobjekt får variabel navn
        self.last = 0 #Skuteobjekt får variabel last
        self.id = Skute.antall_skuter #Setter id til objekt (en skute) til hele klassens variabel (alle skuter)
        Skute.antall_skuter += 1 #Oppdaterer klassevariabel (tilhører alle skuter)

        def fisk():
            self.last = fiskefunksjon()

        self.fisk = fisk    

    def fjern_last(self):
        self.last=0
        
        
```

```{code-cell} ipython3


print(Skute.antall_skuter)
greedy_ships = []
    
for i in range(10):
    ny_skute = Skute("Grådig", lambda: 75) #Lager en ny instans av klassen
    greedy_ships.append(ny_skute)

skute_ids = [skute.id for skute in greedy_ships]
skute = greedy_ships[0]
print("skutelast:", skute.last)
skute.fisk()
skute.test()
print("skutelast etter fiske:", skute.last)
print(skute_ids)
```

* Når man baserer programmet sitt på bruk av klasser og objekter kaller vi dette *objektorientert programmering*
* Dette er ikke pensum, eller noe vi skal gjøre
* Men vi bruker objekter og klasser hele tiden når vi henter inn funksjonalitet fra ulike biblioteker
* Det er derfor greit å *vite om*

```{code-cell} ipython3
class test:
    variabel = 10

objekt = test()
```

```{code-cell} ipython3
objekt.variabel
```

```{code-cell} ipython3
skute.test()
print("antall", Skute.antall_skuter)
```

```{code-cell} ipython3

```
