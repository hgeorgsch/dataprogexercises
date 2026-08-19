---
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

# Lånesøknad

::: {admonition} Datasett
I denne oppgåva bruker me eit datasett frå Kaggle, som er eit arkiv
for datasett meint for testing av maskinlæring.
Datasettet heiter [Mall Customer Segmentation Data](https://www.kaggle.com/datasets/vjchoudhary7/customer-segmentation-tutorial-in-python).
Ein kopi av datasettet er tilgjengeleg som [Mall_Customers.csv](Mall_Customers.csv).
:::

::: {admonition} Oppgåve
Last ned datasettet og last det inn i pandas, slik som me har gjort før.
Vis datasettet.  Kva data inneheld det?
:::

```{code-cell} ipython3
import pandas as pd
df = pd.read_csv("Mall_Customers.csv")
display(df)
```

