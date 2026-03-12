---
jupytext:
  formats: ipynb,md:myst
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

# Support Vector Machine 

*Support Vector Machines* (SVM) var kanskje den mest populære 
maskinlæringsalgoritmen før djuplæring vart realistisk etter 2010.
Der er delte meiningar om SVM eigentleg er maskinlæring.  
På mange måtar lignar SVM meir på klassiske teknikkar som Fishers
lineære diskriminant, med ein presis matematisk formel for løysinga.
Det er ikkje ein iterativ algoritme som tilpasser vektene i ein svart
boks.

Det spiller derimot ingen rolle.  SVM gjev oss ikkje-lineære
diskriminantar og regresjonsmodellar med svært mange fridomsgradar
og likevel god køyretid.  Dersom du har nokon titals eller hundretals
innvariablar, kan det godt vera at SVM gjev raskare og betre resultat
enn nevrale nettverk,

Lat oss sjå på eit døme.
Datasettet er statistikk over studentar som fell ut frå høgare utdanning.
+ [Kjelde](https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success)
+ [CSV-fil](./stud_dropout.csv)

```{code-cell} ipython3
from IPython.display import YouTubeVideo
YouTubeVideo('_YPScrckx28', width=800, height=300)
```

## Datasettet

Me lastar datasettet som me er vande med.
Hugs å lasta ned datafila over.

```{code-cell} ipython3
import pandas as pd
df = pd.read_csv("stud_dropout.csv")
```

::: {admonition} Øving
Sjå på datasettet.  Kva data har me?
:::

Ein snarveg for å sjå klassene, eller *labels*, som er i bruk, er å bruka
`unique()`-metoden, slik:

```{code-cell} ipython3
df["Target"].unique()
```

Me har altso tre kategoriar av studentar.

## Support vector machine


```{code-cell} ipython3
from sklearn import svm
from sklearn.model_selection import train_test_split


features = df.columns[~df.columns.str.contains("Target")]

X = df[features]
y = df["Target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

#clf: for classifier
clf = svm.SVC(probability=True,kernel='rbf')
result = clf.fit(X_train,y_train)

probabilities = clf.predict_proba(X_test)

df_test = X_test
df_test = df_test.join(y_test)
df_test["modell"] = clf.predict(X_test)

res = df_test[["Target", "modell"]]
```

```{code-cell} ipython3
korrekt = res["Target"]==res["modell"]
sukksessrate = korrekt.sum()/korrekt.size
print(f"Modellen vår fungerer {sukksessrate:.2%} av gangene")
```

```{code-cell} ipython3

```

```{code-cell} ipython3

```
