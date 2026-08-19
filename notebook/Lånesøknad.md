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

# Lånesøknad

::: {admonition} Datasett
I denne oppgåva bruker me eit datasett frå Kaggle, som er eit arkiv
for datasett meint for testing av maskinlæring.
Datasettet heiter [Loan Approval Dataset](https://www.kaggle.com/datasets/anishdevedward/loan-approval-dataset?select=loan_approval.csv).
Ein kopi av datasettet er tilgjengeleg som [loan_approval.csv](loan_approval.csv).

Dette datasettet er gjort tilgjengeleg frå Kaggle under MIT-lisens.
:::

::: {admonition} Oppgåve
Last ned datasettet og last det inn i pandas, slik som me har gjort før.
Vis datasettet.  Kva data inneheld det?
:::

```{code-cell} ipython3
import pandas as pd
df = pd.read_csv("loan_approval.csv")
display(df)
```
