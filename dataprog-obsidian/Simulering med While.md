---
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
tags:
  - lecture
  - simulering
  - stub
---

# Simulere med `While`

* Vi har blitt ganske godt kjent med `for`-løkken
* Den bruker vi når vi skal gjøre noe «for» alle elementene i en samling
* Vi vet altså på forhånd hvor mange ganger løkken skal iterere

* Dersom vi undersøker feks kundeadferd og bruker tilfeldige tall til å simulere avgjørelser vet man typisk ikke hvor mange ganger en løkke trenger å kjøre
* Da kan vi bruke `while` løkken



```python
while «boolsk uttrykk»:
    #Koded
    #Kode
    #Kode
```

* Løkken kjører så lenge det "boolske uttrykket" evalueres til `True`
* Dersom vi trenger å avbryte en løkke midt i en iterasjon kan vi bruke `break`
* Dersom vi trenger å starte løkken på nytt midt i en iterasjon kan vi bruke `continue`

```{code-cell} ipython3
---
slideshow:
  slide_type: fragment
---
sjekkevariabel = True
while sjekkevariabel:
    tilfeldig_tall = random.random()
    if tilfeldig_tall < 0.2:
        print("Vi avbryter")
        break
    else:
        print("Vi fortsetter")
        continue
    print("Her kommer vi aldri")
    
```

