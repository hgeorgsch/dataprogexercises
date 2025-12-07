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

---

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
