---
jupytext:
  formats: md:myst,ipynb
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.17.0
kernelspec:
  name: dataprog
  language: python
  display_name: dataprog
---

# Lineær Regresjon i scikit-learn

*Scikit-learn* (`sklearn`) er eit populært bibliotek både for maskinlæring og
konvensjonell statistikk.  Mange populære datasett er inkludert
i biblioteket, til testing og utprøving, og her skal me bruka eitt 
av dei, nemleg eit for prediksjon av utvikling av diabetes.
Detaljane står i 
[dokumentasjonen på datasettet](https://scikit-learn.org/stable/datasets/toy_dataset.html#diabetes-dataset).

## Datasettet

For å lasta datasettet importerer me `sklearn` og bruker biblioteket.

```{code-cell} ipython3
from sklearn.datasets import load_diabetes
diabetes = load_diabetes()
display(diabetes)
```

::: {admonition} Oppgåve
Kva datatype er `diabetes`?
:::

Dette datasettet er førebudd spesielt for testing av regresjonsmodellar.
Difor skil det mellom *input* eller `data`, og den variabelen som ein
skal freista å predikera, *target*.

```{code-cell} ipython3
print(diabetes.data.shape)
print(diabetes.target.shape)
```

Det er alltid nyttig å sjå på dimensjonane på datasett.
Her har med 442 rader, same for `data` og `target`.
Der er ti inn-variablar i `data` og éin ut-variabel i `target`.
Om me ser på eit par liner i toppen av kvar matrise, ser me at alt
er tal.

```{code-cell} ipython3
print(diabetes.target[:3])
print(diabetes.data[:3,:])
```

::: {admonition} Oppgåve
Datastrukturen `diabetes` inneheld og ei beskriving, som `diabetes.DESCR`.
For å sjå beskrivinga, er det best å bruka `print` eller `display`?
Kva tyder dei ulike søylene?
:::

## Modellen

Normalt bruker ein fleire *input*-variablar i modellen, men for å
kunna visualisera han pent i 2D, skal me berre bruke éin.
T.d. kan me ta ut den tredje søyla.

```{code-cell} ipython3
import numpy as np
x = diabetes.data[:,2:3]
print(x.shape)
y = diabetes.target
print(y.shape)
```

::: {admonition} Oppgåve
Kva er skilnaden på `diabetes.data[:,2:3]` og `diabetes.data[:,2]`?  
Du kan sjekka ved å endra på koden?
:::

Merk at `x` må vera ei to-dimensjonal matrise når me går vidare,
sjølv om ho berre har éi søyle.

```{code-cell} ipython3
from sklearn import linear_model
reg = linear_model.LinearRegression()
reg.fit(x,y)
print(reg.coef_)
print(reg.intercept_)
```

## References

+ [Medium post](https://medium.com/@heyamit10/how-to-perform-linear-regression-using-pandas-scikit-learn-9fcfa6085fb0)
