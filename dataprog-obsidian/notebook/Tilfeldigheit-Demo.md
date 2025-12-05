---
jupytext:
  formats: md:myst,ipynb
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

```{code-cell} ipython3

```
