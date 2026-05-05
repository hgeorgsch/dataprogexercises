---
jupytext:
  formats: md:myst,ipynb
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.19.1
kernelspec:
  name: python3
  display_name: Python 3 (ipykernel)
  language: python
---

# Klyngeanalyse

Klyngeanalyse er ein form for maskinlæring utan rettleiing.
Her skal me testa $k$-*means* som er den mest kjende klyngeteknikken
på eit litt banalt døme.  Kan me skilja kvinner frå menn basert på
BMI og høgde?

Datasettet me bruker er tilfeldig generert, so me slipp alle problem
med personvern.  Elles er datasettet egna som illustrasjon, sidan me
berre har to dimensjonar, og difor lett kan plotta.

## Oppsett

I tillegg til dei vanlege biblioteka som me kjenner, importerer
me `cluster`-biblioteket frå SciKitLearn.

```{code-cell} ipython3
import sklearn.cluster as cl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

Når me genererer tilfeldige data, tek me utgangspunkt i realistiske
gjennomsnitt blant folket.

```{code-cell} ipython3
menn_bmi = 26.9
kvinner_bmi = 25.2

menn_h = 180.4
kvinner_h = 167.2
```

Me kan òg rekna ut gjennomsnittsvektene.

```{code-cell} ipython3
mm = menn_bmi*(menn_h/100)**2
mk = kvinner_bmi*(kvinner_h/100)**2
```

Me skal generera `n` datapunkt, og definerer `n` som

```{code-cell} ipython3
n = 1000
```

## Tilfeldig datasett

Me genererer normalfordelte datasett vha. `np.random.normal`.

```{code-cell} ipython3
menn_bmi_liste = np.random.normal(loc=menn_bmi, scale=menn_bmi*0.2, size=n)
menn_hoyde_liste = np.random.normal(loc=menn_h, scale=8, size=n)

kvinner_bmi_liste = np.random.normal(loc=kvinner_bmi, scale=menn_bmi*0.2, size=n)
kvinner_hoyde_liste = np.random.normal(loc=kvinner_h, scale=6, size=n)
```

::: {tip}
Dei to parametrane `loc` og `scale` gjev hhv. gjennomsnitt og
standardavvik for normalfordelinga.
:::

Massa åt individane kan me rekna ut frå BMI og høgd som fylgjer.

```{code-cell} ipython3
menn_masse_liste = [ bmi*(h/100)**2 for bmi, h in 
                     zip(menn_bmi_liste, menn_hoyde_liste)]
kvinner_masse_liste = [ bmi*(h/100)**2 for bmi, h in 
                        zip(kvinner_bmi_liste, kvinner_hoyde_liste)]
```

::: {tip}
Funksjonen `zip` tek to lister og lagar ei ny liste med par av element
frå dei to listene.  
Her har me brukt mynsteret
```
for x,y in zip(xs,ys)
```
som er eit standardformular for å laupa gjennom par `(x,y)` der
`x` kjem frå `xs` og `y` kjem frå `ys`.

Her vert element nr. $i$ frå `xs` parra med $i$te element frå `ys`.
Me genererer altso ikkje alle moglege par. Kvart element vert parra
med berre eitt element frå den andre lista.
:::

## Visualisering

For å visulisera datasettet kan me bruka histogram.  For å få visinga kompakt, bruker eg `add_subplot` for å få alle plotta på ei rekkje.

```{code-cell} ipython3
plt.figure
fig = plt.figure(figsize=(12, 3))
fig.tight_layout(pad=0.0)

fig.add_subplot(1, 3, 1)
plt.hist(menn_hoyde_liste, bins=20, label="Menn")
plt.hist(kvinner_hoyde_liste, bins=20, alpha=0.5, label="Kvinner")
plt.title("Høyde")

fig.add_subplot(1, 3, 2)
plt.hist(menn_bmi_liste, bins=20, label="Menn")
plt.hist(kvinner_bmi_liste, bins=20, alpha=0.5, label="Kvinner")
plt.legend()
plt.title("BMI")

fig.add_subplot(1, 3, 3)
plt.hist(menn_masse_liste, bins=20, label="Menn")
plt.hist(kvinner_masse_liste, bins=20, alpha=0.5, label="Kvinner")
plt.legend()
plt.title("Vekt")
plt.show()
```

::: {tip}
Legg merke til at me må laga ein figur `fig`, fordi `add_subplot()` er ein metode i figuren og ikkje i modulen `plt`.
Elles er koden den same som ein ville brukt for å plotta histogramma einskildvis.
:::

```{code-cell} ipython3
data={"hoyde": np.concatenate((menn_hoyde_liste, kvinner_hoyde_liste)), 
      "vekt":  np.concatenate((menn_masse_liste, kvinner_masse_liste)),
      "Kjønn": ["Mann"]*n+["Kvinne"]*n}


df = pd.DataFrame(data)
df =df.reindex(np.random.permutation(df.index))
display(df)
```

```{code-cell} ipython3
df.plot.scatter(x="hoyde", y="vekt")
```

# K-Means clustering

* «Unsupervised learning»
* Vi prøver å dele data inn i klynger uten å nødvendigvis vite hva de representerer
* Noen ganger vet vi hvor mange klynger det burde være, andre ganger må vi prøve oss frem

```{code-cell} ipython3
from IPython.display import YouTubeVideo
#Lenke: https://www.naftaliharris.com/blog/visualizing-k-means-clustering/
YouTubeVideo('R2e3Ls9H_fc', width=800, height=300)
```

```{code-cell} ipython3
model = cl.KMeans(n_clusters=2)
result = model.fit(df[["vekt", "hoyde"]])
df["cluster"] = model.predict(df[["vekt", "hoyde"]])
df
```

## Seaborn

```{code-cell} ipython3
import seaborn as sns

sns.relplot(data=df, x="hoyde", y="vekt", hue="cluster")
sns.relplot(data=df, x="hoyde", y="vekt", hue="Kjønn")
```

# K-nearest neighbours

* «Supervised learning» - Vi har data hvor vi kjenner klassifiseringene
* For nye usette datapunkt undersøker vi de $k$ nærmeste naboene til datapunktet, og klassifiseringen deres
* Klassifiseringen til det nye datapunktet bestemmes av disse

```{code-cell} ipython3
YouTubeVideo('0p0o5cmgLdE', width=800, height=300)
```

```{code-cell} ipython3
from sklearn.neighbors import KNeighborsClassifier

X = df[["vekt", "hoyde"]]
y = df["Kjønn"]
model = KNeighborsClassifier(n_neighbors=2)
result = model.fit(X,y)
df["KNN"] = model.predict(X)
```

```{code-cell} ipython3
sns.relplot(data=df, x="hoyde", y="vekt", hue="Kjønn")
sns.relplot(data=df, x="hoyde", y="vekt", hue="KNN")
```

```{code-cell} ipython3
from sklearn.model_selection import train_test_split


model = KNeighborsClassifier(n_neighbors=50)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)
result = model.fit(X_train, y_train)

df_test = pd.DataFrame(X_test)
df_test = df_test.join(y_test)
df_test["KNN"] = model.predict(X_test)
test_probabilities = model.predict_proba(X_test)
df_test["KNN_prob"] = list(map(max, test_probabilities))
sns.relplot(data=df_test, x="hoyde", y="vekt", hue="Kjønn")
sns.relplot(data=df_test, x="hoyde", y="vekt", hue="KNN", size="KNN_prob")
df_test.dtypes
```

```{code-cell} ipython3

```
