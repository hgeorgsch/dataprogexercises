---
jupytext:
  formats: md:myst,ipynb
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.19.1
kernelspec:
  display_name: dataprog
  language: python
  name: dataprog
---

# Oppgåver til Demo sklearn

Me skal ta for oss eit enkelt datasett med lønsdata, som eg har henta frå
[Kaggle](https://www.kaggle.com/datasets/abhishek14398/salary-dataset-simple-linear-regression?resource=download).

+ **Datafil** [Salary_dataset.csv](Salary_dataset.csv)

Ifylgje dokumentasjonen på Kaggle, er der to søyler forutan indeks:
løn og erfaring i år.
Me kan altso freista å predikera lønen som ein funksjon av erfaringa i år.

## Datasettet i pandas

```{code-cell} ipython3
import pandas as pd
df = pd.read_csv( "Salary_dataset.csv" )
display( df )
```

```{code-cell} ipython3
df.plot.scatter( "YearsExperience", "Salary" )
```

## Datasettet i sklearn

```{code-cell} ipython3
import sklearn as sk
```

```{code-cell} ipython3
X = df[ [ "YearsExperience" ] ]
display( X )
```

```{code-cell} ipython3
Y = df[ "Salary" ]
display( Y )
```

```{code-cell} ipython3
trainX, testX, trainY, testY = sk.model_selection.train_test_split( X, Y )
```

## Trening av modellen

```{code-cell} ipython3
model = sk.linear_model.LinearRegression()
```

```{code-cell} ipython3
print( model )
```

```{code-cell} ipython3
model.fit( trainX, trainY )
```

## Prediksjon

```{code-cell} ipython3
predY = model.predict( testX )
```

```{code-cell} ipython3
predY
```

```{code-cell} ipython3
predY - testY
```

```{code-cell} ipython3
errors = predY - testY
print( errors )
```

```{code-cell} ipython3
errors = errors.abs()
print( errors )
```

```{code-cell} ipython3
errors.describe()
```

```{code-cell} ipython3
relerrors = errors / testY
print( relerrors )
```

```{code-cell} ipython3
relerrors.describe()
```

## Visualisering av feilanalysen

```{code-cell} ipython3
import matplotlib.pyplot as plt
plt.scatter( testX, testY, color="b" )
plt.scatter( testX, predY, color="r" )
```

```{code-cell} ipython3

```
