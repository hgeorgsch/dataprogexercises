---
jupytext:
  formats: md:myst,ipynb
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.17.0
kernelspec:
  display_name: dataprog
  language: python
  name: dataprog
---

# Iris-datasettet

**Hensikta** med dette dokumentet er å laga plott til foilar.

Fisher studerte klassifisering av tre ulike artar av blomen iris. Datasettet som han sette saman er stadig populært for testing av maskinlæringsmodellar. Datasettet omfattar femti eksemplar av kvar iris-art (Iris setosa, Iris virginica og Iris versicolor). Fire målbare drag er registrert for kvart eksemplar: lengd og breidd på beger- og kronblad.

Me bruker scikit-learn, og fordi iris-datasettet er so populært, er det allereie tilgjengeleg i biblioteket. Me kan lasta det slik:

```{code-cell} ipython3
from sklearn import datasets
iris = datasets.load_iris()
```

## Scatter plot

For å få eit visuelt inntrykk av klassifiseringsproblemet, er det
nyttig med spreidingsplott (*scatter plot*).  Det er synd at me 
berre klarer å plotta to søyler i to dimensjonar, men me får ta
det me kan få.

```{code-cell} ipython3
import matplotlib.pyplot as plt

scatter = plt.scatter(iris.data[:, 0], iris.data[:, 1], c=iris.target)

ax = plt.gca()
ax.set(xlabel=iris.feature_names[0], ylabel=iris.feature_names[1])
ax.legend(
    scatter.legend_elements()[0], iris.target_names, loc="lower right", title="Classes"
)
```

Me skil dei tre klassene i tre ulike datasett.

```{code-cell} ipython3
X1 = iris.data[iris.target == 0,:]
X2 = iris.data[iris.target == 1,:]
X3 = iris.data[iris.target == 2,:]
```

No kan me finna gjennomsnitt og standardavvik for kvar klasse.

```{code-cell} ipython3
m1 = X1[:,1].mean()
s1 = X1[:,1].std()
print(m1,s1)
m2 = X2[:,1].mean()
s2 = X2[:,1].std()
print(m2,s2)
```

```{code-cell} ipython3
import numpy as np
from scipy.stats import norm

xr = np.arange(1.3,5,0.001)
plt.plot( xr, norm.pdf(xr,m1,s1) )
plt.plot( xr, norm.pdf(xr,m2,s2) )
```

## Oppsummering
