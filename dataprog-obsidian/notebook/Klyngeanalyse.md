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

### Tilfeldig datasett

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

### Visualisering

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

+++

### Dataanalyse

Neste steg er å sette det tilfeldige datasettet inn i ein pandas *DataFrame*.
Dette kan ein gjera på forskjellige måtar.  
Her bruker me ein `dict` med eitt element for kvar søyle.
Det kjekke er at nyklane frå `dict` vert søyleoverskrifter.

```{code-cell} ipython3
data={"Høyde": np.concatenate((menn_hoyde_liste, kvinner_hoyde_liste)), 
      "Vekt":  np.concatenate((menn_masse_liste, kvinner_masse_liste)),
      "Kjønn": ["Mann"]*n+["Kvinne"]*n}


df = pd.DataFrame(data)
df =df.reindex(np.random.permutation(df.index))
display(df)
```

::: {tip}
Datasetta er numpy *arrays* og difor må me bruka `concatenate()` frå numpy for å setja dei saman.
Til kjøn bruker me lister, so dei kan me skøyta med `+`.
Legg merke til trikset med `["Mann"]*n`.  Me kan multiplisera ei liste med eit tal for å repetera elementa.
:::

For å visualisera samanhengen mellom høgd og BMI kan me bruka eit spreideplott, slik:

```{code-cell} ipython3
df.plot.scatter(x="Høyde", y="Vekt")
```

## K-Means clustering

::: {tip}
[](../norun/klyngedemo) gjev ei detaljert innføring i $k$-*means*.
:::

Me *Unsupervised learning* freistar me å dela data inn i klynger utan å vita kva klyngene representerer.
Somme tider veit me kormange klynger der bør vera, som når me føreset to kjønn.
Andre gongar må ein prøva seg fram.  I $k$-*means* må me gå ut frå eit bestemt tal `k` på klynger.

Denne videoen gjev ei kort *briefing* på kva me skal oppnå.

```{code-cell} ipython3
from IPython.display import YouTubeVideo
#Lenke: https://www.naftaliharris.com/blog/visualizing-k-means-clustering/
YouTubeVideo('R2e3Ls9H_fc', width=800, height=300)
```

SciKitLearn implementerer omtrent det same APIet for maskinlæring utan rettleiing, som me kjenner med rettleiing.
Det ser slik ut.

```{code-cell} ipython3
model = cl.KMeans(n_clusters=2)
result = model.fit(df[["Vekt", "Høyde"]])
df["cluster"] = model.predict(df[["Vekt", "Høyde"]])
display(df)
```

Me kjenner igjen instantiering av modellen, tilpassing med `fit()` og prediksjon med `predict()`.  
Dette er det same som me har gjort med rettleidd læring tidlegare.
For å halda fram analysen legg me prediksjonen inn som ei ny søyle i `df`.

I dei radane som me ser verkar prediksjonen ganske vilkårleg, men for å få eit fullstendig inntrykk må me visualisera (eller rekna).

+++

### Seaborn

Til visualiseringa skal me bruka SeaBorn, mest for å prøva
noko nytt.  SeaBorn gjev ein del nye moglegheiter, men dette
kunne me ha gjort med `pyplot` òg.

```{code-cell} ipython3
import seaborn as sns

sns.relplot(data=df, x="Høyde", y="Vekt", hue="cluster")
sns.relplot(data=df, x="Høyde", y="Vekt", hue="Kjønn")
```

::: {admonition} Refleksjon
Kva synest du om klyngeinndelinga?  Er ho nyttig?
:::

::: {admonition} Oppgåve
Køyr klyngeanalysa fleire gongar på det same datasettet.
Gjev ho same resultat kvar gong?
:::


## $k$-*nearest neighbours*

Der er ein algoritme som byggjer på same prinsipp som $k$-means,
men som er laga for rettleidd læring.

Når me ser nye usette datapunkt undersøker me dei $k$ næraste grannane
til datapunktet, og bruker klassifiseringa deira til å 
klassifisera det nye datapunktet.
Videoen gjev ei kjapp *briefing*.

```{code-cell} ipython3
YouTubeVideo('0p0o5cmgLdE', width=800, height=300)
```

SciKitLearn implementerer `KNeighborsClassifier` med det same APIet
som andre maskinlæringsmodellar.
Sidan dette er rettleidd læring, må målvariabelen `y`, dvs. kjønn, 
vera med.

```{code-cell} ipython3
from sklearn.neighbors import KNeighborsClassifier

X = df[["vekt", "hoyde"]]
y = df["Kjønn"]
model = KNeighborsClassifier(n_neighbors=2)
result = model.fit(X,y)
df["KNN"] = model.predict(X)
```

Me kan visualisera som i stad:

```{code-cell} ipython3
sns.relplot(data=df, x="hoyde", y="vekt", hue="Kjønn")
sns.relplot(data=df, x="hoyde", y="vekt", hue="KNN")
```

::: {admonition} Refleksjon
Er der skilnad mellom klyngene i $k$-*means* og $k$-*nearest
neighbour*, eller er det omtrent det same?
:::

### Evaluering

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
