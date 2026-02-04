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

# Oppgåver til Demo Kontrollflyt

Desse oppgåvene er utgangspunktet for ein demonstrasjonsvideo med to 
formål.  Eg skal demonstrera syntaksen for grunnleggjande kontrollflyt i 
python, og eg skal vise litt korleis eg tenkjer når eg tek fatt på å skriva
kode.

## Vilkår

```{code-cell} ipython3
tal1 = 19
tal2 = 4
```

```{code-cell} ipython3
print( "Dei to tala er", tal1, " og ", tal2 )
```

::: {admonition} Oppgåve
Skriv eit program som tek dei to tala (`tal1` og `tal2`)
og skriv ut produktet dersom dette er
mindre enn 500, og elles skriv ut summen.

Kjelde: [pynative](https://pynative.com/python-basic-exercise-for-beginners/)
:::

```{code-cell} ipython3
tal2 = 92
produkt = tal1 * tal2
if produkt < 500:
    print( produkt )
else:
    print( tal1 + tal2 )
```

Denne *if*-satsen ser ut til å løse oppgaven både for store og små tall.

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
produktellersum( 19, 92 )
```

Testen gjev same resultat som over, so funksjonen gjer det same som løysinga på fyrste oppgåve.

```{code-cell} ipython3
produktellersum( 19, 13 )
```

```{code-cell} ipython3
def produktellersum2( tal1, tal2 ):
    produkt = tal1 * tal2
    if produkt < 500:
        return produkt
    else:
        return tal1 + tal2 

produktellersum2( 19, 13 )
```

```{code-cell} ipython3
v1 = produktellersum( 19, 13)
```

```{code-cell} ipython3
v2 = produktellersum2( 19, 13)
```

```{code-cell} ipython3
print( v1 )
```

```{code-cell} ipython3
print( v2 )
```

Legg merke til skilnaden `return` og `print`.

+++

## Løkker

```{code-cell} ipython3
liste1 = list( range( 10 ) )
liste2 = [ 1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53 ]
```

```{code-cell} ipython3
print( liste2 )
```

```{code-cell} ipython3
print( liste1 )
```

::: {admonition} Oppgåve
Skriv ei løkke som skriv ut summen av alle tala i `liste2`.
:::

```{code-cell} ipython3
sum( liste2 )
```

```{code-cell} ipython3
s = 0
for x in liste2:
    s = s + x
print( s )
```

Denne *for*-løkka gjev rett svar på `liste2`.

+++

::: {admonition} Oppgåve
Skriv ei løkke skriv ut alle dei alle dei kummulative summane frå `liste1`,
dvs. fyrst (summen av) det fyrste talet, so summen av dei to fyrste, so dei
tre fyrste, osv.
:::

```{code-cell} ipython3
s = 0
for x in liste1:
    s = s + x
    print( s )
```

::: {admonition} Oppgåve
Skriv ei løkke som lagar ei liste med dei kummulative summane.
:::

```{code-cell} ipython3
s = 0
liste = [] 
for x in liste1:
    s = s + x
    liste.append( s )
    print( liste )
```

Testen gjev dei same tala som forrige løysing.

+++

::: {admonition} Oppgåve
Skriv ei løkke som reknar ut Fibonacci-fylgja som startar med $1,1,\ldots$.
:::

::: {admonition} Definisjon
Ei Fibonacci-fylgje er ei talfylgje der kvart tal er summen av dei to føregåande
:::

```{code-cell} ipython3
liste = [ 1, 1 ]
for x in range(10):
    liste.append( liste[-1] + liste[-2] )  
    print( liste )
```

```{code-cell} ipython3
liste = [ 1, 1 ] 
while len( liste ) < 50:
    liste.append( liste[-1] + liste[-2] )  
print( liste )
```

Me kan gå gjennom lista frå ende til ende og sjekka at kvart tal er summen av dei to føregåande.

+++

## Listemanipulasjon

::: {admonition} Oppgåve
Skriv ei løkke som reknar ut Fibonacci-fylgja som startar med $1,1,\ldots$,
vha. berre éin variabel.
:::

```{code-cell} ipython3
a = 1
b = 1
for x in range(10):
    c = a + b
    print( c )
    a = b
    b = c
```

Her er me nøydde til å vera nøye med rekkjefylgja på tilordningane av `a` og `b` inne i løkka.

```{code-cell} ipython3

```
