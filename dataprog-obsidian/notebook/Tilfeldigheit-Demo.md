---
jupytext:
  formats: ipynb,md:myst
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

# Demonstrasjonar med slumptal

```{code-cell} ipython3
import random
import matplotlib.pyplot as plt
import scipy.stats
```

```{code-cell} ipython3
def terning():
    return random.randint(1,6)

print( [ terning() for _ in range(10) ] )
```

```{code-cell} ipython3
print( [ random.random() for _ in range(10) ] )
```

```{code-cell} ipython3
print( [ random.gauss() for _ in range(10) ] )
```

```{code-cell} ipython3
plt.bar( list(range(1,7)), [ 1/6 for _ in range(6) ] )
plt.ylim( [ 0, 1 ] )
plt.xlabel( "Verdi" )
plt.ylabel( "Sannsyn" )
plt.title( "Diskret, uniform fordeling" )
plt.savefig( "diskretuniform.svg" )
```

```{code-cell} ipython3
plt.plot( [ 0, 1 ], [ 1, 1 ] )
plt.ylim( [ 0, 1.1 ] )
plt.xlim( [ 0, 1 ] )
plt.xlabel( "Verdi" )
plt.ylabel( "Sannsyn" )
plt.title( "Kontinuerlig, uniform fordeling" )
plt.savefig( "kontuniform.svg" )
```

```{code-cell} ipython3
n = 100
mx = 4
xs = [ 2*mx*i/n-mx for i in range(n+1) ]
ys = [ scipy.stats.norm.pdf( x ) for x in xs ]
plt.plot( xs, ys )
plt.ylim( [ 0, 1.1 ] )
plt.xlim( [ -4, 4 ] )
plt.xlabel( "Verdi" )
plt.ylabel( "Sannsyn" )
plt.title( "Normalfordeling" )
plt.savefig( "gauss.svg" )
```

# Leketydøme

Den enkle lineære kongruensgeneratoren frå føredraget kan me
implementera slik

```{code-cell} ipython3
def f(x,a=7,m=97): 
    return x*a % m
```

For å testa perioden, kan me definera funksjonar som køyrer
generatoren rekursivt.

```{code-cell} ipython3
def g(s,**kw):
    s.append( f( s[-1], **kw ) )
    return s

def r(s,m=97,**kw):
    if len(s) > 2*m: return s
    else: return r(g(s,**kw))

print( r( [1] ) )
```

Legg merke til korleis heile fylgjen gjentek seg sjølv.

Under feilsøk brukte eg ein litt meir brutal metode for å testa
alle moglege koeffisiantar $a$.

```{code-cell} ipython3
def test(a,m=97):
    s = set(r([1],a=a,m=m))
    return (a,len(s))

r = [ test(a) for a in range(2,97) ]
```

Her bruker me mengetypen `set` for å verta kvitt gjentekne element.
I returverdien skal `len(s)` vera talet på unike element.

Til figurane brukte eg denne funksjonen for å 

```{code-cell} ipython3
def fx(s,a=7,m=97):
    s1 = f(s)
    v = s1/m
    return ( s, s1, v )

def rx(s,**kw):
    rs = []
    for _ in range(9):
        r = fx(s,**kw)
        s = r[1]
        rs.append(r)
    return rs

print( rx(13) )
```

For å formattera dette til bruk i $\LaTeX$, brukte eg denne koden

```{code-cell} ipython3
rs = rx(13)

def fmt1( v ):
   s = ""
   for t in v:
       s += "{" + f"{t}" + "}"

def fmt2( v ):
   return " ".join( fmt1( v ) )

print( fmt2(rs) )
```


