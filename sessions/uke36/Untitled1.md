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
---

```{code-cell} ipython3
import math
def playlist(N,M,B):
    if N==M: return math.factorial(M)
    if M==B+1: return math.factorial(B)
    return playlist(N-1,M,B)+M*playlist(N-1,M-1,B)

def F(N,M,B):
    return math.factorial(M)/math.factorial(M-B)*(M-B)**(N-B)

print(playlist(20,10,8))
print(F(20,10,8))
```

```{code-cell} ipython3

```
