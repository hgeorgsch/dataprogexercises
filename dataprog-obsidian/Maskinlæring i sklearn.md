

# Noen eksempler fra sklearn
* Klynger
* Support vector machines

```{code-cell} ipython3
import sklearn.cluster
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


menn_bmi = 26.9
kvinner_bmi = 25.2

menn_h = 180.4
kvinner_h = 167.2

mm = menn_bmi*(menn_h/100)**2
mk = kvinner_bmi*(kvinner_h/100)**2

n = 1000
```

```{code-cell} ipython3
menn_bmi_liste = np.random.normal(loc=menn_bmi, scale=menn_bmi*0.2, size=n)
menn_hoyde_liste = np.random.normal(loc=menn_h, scale=8, size=1000)

kvinner_bmi_liste = np.random.normal(loc=kvinner_bmi, scale=menn_bmi*0.2, size=n)
kvinner_hoyde_liste = np.random.normal(loc=kvinner_h, scale=6, size=n)

menn_masse_liste = [ bmi*(h/100)**2 for bmi, h in zip(menn_bmi_liste, menn_hoyde_liste)]
kvinner_masse_liste = [ bmi*(h/100)**2 for bmi, h in zip(kvinner_bmi_liste, kvinner_hoyde_liste)]

plt.hist(menn_hoyde_liste, bins=20, label="Menn")
plt.hist(kvinner_hoyde_liste, bins=20, alpha=0.5, label="Kvinner")
plt.title("Høyde")
plt.show()


plt.hist(menn_bmi_liste, bins=20, label="Menn")
plt.hist(kvinner_bmi_liste, bins=20, alpha=0.5, label="Kvinner")
plt.legend()
plt.title("BMI")
plt.show()

plt.hist(menn_masse_liste, bins=20, label="Menn")
plt.hist(kvinner_masse_liste, bins=20, alpha=0.5, label="Kvinner")
plt.legend()
plt.title("Vekt")
plt.show()


```

```{code-cell} ipython3
data={"hoyde": np.concatenate((menn_hoyde_liste, kvinner_hoyde_liste)), 
      "vekt":  np.concatenate((menn_masse_liste, kvinner_masse_liste)),
      "Kjønn": ["Mann"]*n+["Kvinne"]*n}


df = pd.DataFrame(data)
df.plot.scatter(x="hoyde", y="vekt")
df =df.reindex(np.random.permutation(df.index))
df
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
from sklearn.cluster import KMeans

model = KMeans(n_clusters=2)
result = model.fit(df[["vekt", "hoyde"]])
df["cluster"] = model.predict(df[["vekt", "hoyde"]])
df
```

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

# Akademisk sukksess

[Dataset](https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success)

```{code-cell} ipython3
df = pd.read_csv("stud_dropout.csv")
df["Target"].unique()
```

# Support vector machine

«supervised learning»

```{code-cell} ipython3
YouTubeVideo('_YPScrckx28', width=800, height=300)
```

```{code-cell} ipython3
from sklearn import svm

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