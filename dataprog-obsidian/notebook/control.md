---
jupytext:
  formats: md:myst,ipynb
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.18.1
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

# Løysingar frå Demo Kontrollflyt

Desse oppgåvene er utgangspunktet for ein demonstrasjonsvideo med to 
formål.  Eg skal demonstrera syntaksen for grunnleggjande kontrollflyt i 
python, og eg skal vise litt korleis eg tenkjer når eg tek fatt på å skriva
kode.

> Hei, jeg kan skrive *markdown*.

## Vilkår

```{code-cell} ipython3
tal1 = 17
tal2 = 4
print( "Det første tallet er", tal1 )
```

::: {admonition} Oppgåve
Skriv eit program som tek dei to tala (`tal1` og `tal2`)
og skriv ut produktet dersom dette er
mindre enn 500, og elles skriv ut summen.

Kjelde: [pynative](https://pynative.com/python-basic-exercise-for-beginners/)
:::

```{code-cell} ipython3
tal2 = 20
produkt = tal1 * tal2
if produkt < 500:
    print( produkt )
else:
    print( tal1 + tal2 )
```

Dette ser ut til å virke for små og store tall.

+++

## Funksjonar

::: {admonition} Oppgåve
Skriv om programmet over som ein funksjon som tek dei to tala som argument.
:::

```{code-cell} ipython3
def produktellersum( tal1, tal2 ):
    produkt = tal1 * tal2
    if produkt < 500:
        print( produkt )
    else:
        print( tal1 + tal2 )
```

```{code-cell} ipython3
produktellersum( 4, 17 )
produktellersum( 40, 17 )
produktellersum( 20, 17 )
produktellersum( 400, 17 )
```

## Løkker

```{code-cell} ipython3
liste1 = list( range( 10 ) )
liste2 = [ 1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53 ]
print( liste2 )
```

```{code-cell} ipython3
print( liste1 )
```

::: {admonition} Oppgåve
Skriv ei løkke som skriv ut summen av alle tala i `liste2`.
:::

```{code-cell} ipython3
s = 0
for x in liste2:
    s += x
    print( x, s )
print( "Summen er", s )
```

::: {admonition} Oppgåve
Skriv ei løkke skriv ut alle dei alle dei kummulative summane frå `liste1`,
dvs. fyrst (summen av) det fyrste talet, so summen av dei to fyrste, so dei
tre fyrste, osv.
:::

```{code-cell} ipython3
s = 0
for x in liste1:
    s += x
    print( s )
```

::: {admonition} Oppgåve
Skriv ei løkke som lagar ei liste med dei kummulative summane.
:::

```{code-cell} ipython3
liste = []
for x in liste1:
    liste.append( x )
print( liste )
```

::: {admonition} Oppgåve
Skriv ei løkke som reknar ut Fibonacci-fylgja som startar med $1,1,\ldots$.
:::

```{code-cell} ipython3
a = 1
print( a )
b = 1
print( b )
for _ in range(20):
    c = a + b
    print( c )
    a = b
    b = c
    
    
```

::: {admonition} Definisjon
Ei Fibonacci-fylgje er ei talfylgje der kvart tal er summen av dei to føregåande
:::

```{code-cell} ipython3
### TODO
```

## Listemanipulasjon

::: {admonition} Oppgåve
Skriv ei løkke som reknar ut Fibonacci-fylgja som startar med $1,1,\ldots$,
vha. berre éin variabel.
:::

```{code-cell} ipython3
liste = [ 1, 1 ]
while len( liste ) < 20:
    liste.append( liste[-1] + liste[-2] )

print( liste )
```

```{code-cell} ipython3

```
