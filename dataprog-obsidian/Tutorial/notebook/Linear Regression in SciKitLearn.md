---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.17.0
  formats: md:myst,ipynb
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

For å lasta datasettet importerer me `sklearn` og bruker biblioteket.

```{code-cell} python3
from sklearn.datasets import load_diabetes
diabetes = load_diabetes()
display(diabetes)
```

```
diabetes.target[:3]
diabetes.data.shape
```

```{code-cell} python3
from sklearn import linear_model
reg = linear_model.LinearRegression()
reg.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
reg.coef_
```

## References

+ [Medium post](https://medium.com/@heyamit10/how-to-perform-linear-regression-using-pandas-scikit-learn-9fcfa6085fb0)
