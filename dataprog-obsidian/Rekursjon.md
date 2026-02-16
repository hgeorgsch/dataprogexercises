---
title: Halveringsmetoden ved Rekursjon
tags:
   - stub
   - topic/recursion
---

# Halveringsmetoden ved Rekursjon

Me skal visa rekursjon.
Alt som me kan gjera med rekursjon, kan me òg gjera med løkker og vise versa.
Det er mykje smak og behag som avgjer kva me vel.

Hittil har me brukt ei while-løkke for å iterera over eit stadig mindre interval. I staden for løkka, kan ein bruka rekursjon; dvs. at funksjonen kallar seg sjølv.

```{code-cell} ipython3
def bisectR(f,l,u):
    fl = f(l)
    fu = f(u)
    if fl*fu >= 0: raise Exception ("Funksjonen byter ikkje forteikn på intervallet")
    m = (l+u)/2
    fm = f(m)
    if abs(l-u) < 0.01: return m
    elif fm == 0: return m
    elif fl*fm < 0: return bisectR(f,l,m)
    elif fm*fu < 0: return bisectR(f,m,u)
print ( bisectR(f,0,1))
```

Legg merke til feilsjekken, som sikrar at me ikkje køyrer halveringsmetoden på eit intervall der funksjonen har same forteikn i båe endane.
Det er ein god skikk å sikra seg mot alle tenkjelege feil på denne måten, men det er krevjande å tenkja på alt.  Dei fleste døma i dette kurset slurvar med denne typen feilsjekking.

::: {admonition} Oppgåve
Kva skjer om du droppar feilsjekken og køyrer t.d. ``bisectR(f,-1,0)``?
:::

```{code-cell} ipython3
def bisectRfeil(f,l,u):
    fl = f(l)
    fu = f(u)
    m = (l+u)/2
    fm = f(m)
    if abs(l-u) < 0.01: return m
    elif fm == 0: return m
    elif fl*fm < 0: return bisectR(f,l,m)
    elif fm*fu < 0: return bisectR(f,m,u)
print ( bisectRfeil(f,-1,0))
```

Her fekk me ``None``; dvs. funksjonen gav ikkje nokon returverdi. Korleis kan det ha seg?
Det må tyda at ingen av ``return``-satsane vart køyrde. 
Dersom du sjekkar utrekninga for hand, ser du at det gjev meining.
