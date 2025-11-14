---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.18.1
kernelspec:
  display_name: dataprog
  language: python
  name: dataprog
---

# Akademisk suksess

[Dataset](https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success)

```{code-cell} ipython3
import pandas as pd
```

```{code-cell} ipython3
df = pd.read_csv("stud_dropout.csv")
df["Target"].unique()
```

## Support vector machine

«supervised learning»

```{code-cell} ipython3
from IPython.display import YouTubeVideo

YouTubeVideo('_YPScrckx28', width=800, height=300)
```

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
