---
tags:
  - lecture/video
css:
  - custom.css
---
# Datastrukturar

note:

---

## Primitive datatypar

- `int` : $\ldots, -1, 0, +1, +2, \ldots$
- `float` :  t.d. $-50.1$, $0$, $0.1$, $2.4$,  $10.0$
- `bool` : `True` eller `False`
- `str` : t.d. `"Hello World!"`

note:
De primitive datatypene håper jeg du kjenner.
De representerer enkeltverdier, som tall, sann/usann, eller
tegnstrenger.

Det kan diskuteres om tegnstrenger egentlig er en primitiv
datatype.  I mange sprog er de definitivt ikke det, men python
behandler dem stort sett som primitive.

---
## Samansette datatypar

- `tuple` : t.d. `(1,0.5)`
- `list` (liste) : t.d.  `[ 2, 3, 11, 3, 11, 11 ]`
- `set` (mengd) :  `{ 1, 2, 3, 5, 7, 11, 13 }`
- `dict` for *dictionary* (oppslag)  `{` nykel : verdi, $\ldots$ `}`

note:

---

```python
a = (1,2)
b = [1,2]
```

```
In [3]: print( a[0], b[0] )
1 1

In [4]: b[0] = 2

In [5]: a[0] = 2
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[5], line 1
----> 1 a[0] = 2

TypeError: 'tuple' object does not support item assignment

```
<!-- element class="fragment" -->

---

```python
liste = [ "Ola", "Kari", "Mons" ]
```

---

```pythoh
kunde = { 
    "fornamn" : "Ola",
    "etternamn" : "Normann",
    "postnummer" : 6016,
    "gate" : "Borgundvegen",
    "nummer" : 666,
  }
```

```
In [3]: print( kunde["fornamn"] )
Ola

In [4]: print( kunde["gate"], kunde["nummer"]  )
Borgundvegen 666
```
---

# Listekomprehension

Snarvei til å lage lister, set og dictionaries

---

* Liste:
```python
[ uttrykk for element in samling if betingelse]
```
* Set:
```python
{ uttrykk for element in samling if betingelse}
```
* Dictionary:
```python
{ utrykk_key: uttrykk_value for element in samling if betingelse ]
```

---

Standard måte å lage liste på:

```{code-cell} ipython3
import matplotlib.pyplot as plt
#Plot saldo på sparekonto

def forrentning(P,r,t):
    return P*(1+r)**t

n_tid = 10
tid = list(range(n_tid))
saldo = []
start = 1000
rente = 0.05
for t in tid:
    ny_saldo = forrentning(start, rente, t)
    saldo.append(ny_saldo)

plt.plot(tid, saldo)
plt.show()
```

+++ {"editable": true, "slideshow": {"slide_type": "subslide"}}

Med listekomprehensjon

```{code-cell} ipython3
import matplotlib.pyplot as plt
import numpy as np


def forrentning(P,r,t):
    return P*(1+r)**t

n_tid = 10
start = 1000
rente = 0.05

tid = [ t for t in range(n_tid)]
saldo = [forrentning(start, rente, t) for t in tid]

start_aar = 2023
tid_aar = [f"01.01.{start_aar+t}" for t in tid if t%2 == 0]
print(tid_aar)
plt.bar(tid, saldo)
plt.xticks(ticks=np.arange(0,10,2), labels=tid_aar, rotation=45) 
plt.show()

```

---

* Ofte er slike listekomprehensjoner lette og lese, skrive og forstå
* Man må passe på ikke ta av -- de kan bli kompliserte og vanskelige å forstå

---

Man lager `set` på akkura samme måte

```{code-cell} ipython3
import json
with open("kundedata1.json", 'r') as file:
    kundedata = json.load(file)


alle_etternavn = {kunde["etternavn"] for kunde in kundedata}
etternavn_H = {kunde["etternavn"] for kunde in kundedata if kunde["etternavn"][0] == 'H'}
print(etternavn)

```

+ Kan bli vanskelig å lese eller for komplisert
+ Dictionary av alle kunder med etternavn som begynner på 'H'

```{code-cell} ipython3
H_klubben = { navn: [kunde["fornavn"] for kunde in kundedata if kunde["etternavn"] == navn] 
             for navn in etternavn_H }

def finnKunde(etternavn):
    treffliste = []
    for kunde in kundedata:
        if etternavn == kunde["etternavn"]:
            treffliste.append(kunde)
    if treffliste == []:
        print(f"Ingen kunder med etternavn '{etternavn}' funndet")
        return None
    else:
        print(f"Vi fant {len(treffliste)} kunder med etternavn '{etternavn}'")
        return treffliste

H_klubben = { navn: finnKunde(navn) for navn in etternavn_H}

with open("kundedata_test.json", 'w') as file:
    json.dump(H_klubben, file)
```

---

## Oppg:

* Bruk komprehensjon til å lage en dictionary som inneholder allekunder med startsaldo større enn 120,000
* Dictionary skal bestå av nøkler som tilsvarer etternavnet til kundene, og verdiene skal være en liste med kundene på samme format som originalt

+ lag liste med rike kunder
+ lag set med etternavnene
+ lag dictionary med kunder { kundensetternavn: [liste med kunder]}

```{code-cell} ipython3
grense = 120e3
rike_kunder = [ kunde for kunde in kundedata if kunde["startsaldo"] > grense]
etternavn_rik = {kunde["etternavn"] for kunde in rike_kunder}
data_rike_kunder = {navn: [kunde for kunde in rike_kunder if kunde["etternavn"] == navn] for navn in etternavn_rik}
```

```{code-cell} ipython3
data_rike_kunder
```


---

## Dynamiske datatypar

+ iterator
+ klasser

---

## numpy


---

# Slutt
