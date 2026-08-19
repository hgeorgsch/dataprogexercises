---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.18.1
kernelspec:
  display_name: Python 3 (ipykernel)
  language: python
  name: python3
---

```{code-cell} ipython3
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import json
```

```{code-cell} ipython3
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
```

```{code-cell} ipython3
df = pd.read_csv("mitt_spotify_datasett.csv")
df
```

```{code-cell} ipython3
df.isna().sum()
```

```{code-cell} ipython3
#df = df[~df["spilleliste"].isna()] # Beholder navnløs spilleliste
df = df[~df["valence"].isna()]
df.isna().sum()
```

```{code-cell} ipython3
feature_columns = df.columns[-11:]
df_features = df[feature_columns]
df_features
```

```{code-cell} ipython3
sns.heatmap(data=df_features.corr(), cmap="coolwarm", vmax=1, vmin=-1, fmt=".1f", annot=True)
```

```{code-cell} ipython3
#Valg av k

k_list = range(1,12)
inertia_list = []
sil_scores = []
for k in k_list:
    model = KMeans(n_clusters=k,n_init=50)
    clusters = model.fit_predict(df_features)
    inertia_list.append(model.inertia_)
    if k > 1:
        sil_scores.append(silhouette_score(df_features, clusters))

```

```{code-cell} ipython3

plt.plot(k_list, inertia_list, "o-")
plt.show()
plt.plot(k_list[1:], sil_scores, "o-", color="orange")
plt.show()    
```

```{code-cell} ipython3
scaler = StandardScaler().set_output(transform="pandas")
df_scaled=scaler.fit_transform(df_features)
```

```{code-cell} ipython3
#Valg av k

k_list = range(1,12)
inertia_list = []
sil_scores = []
for k in k_list:
    model = KMeans(n_clusters=k,n_init=50)
    clusters = model.fit_predict(df_scaled)
    inertia_list.append(model.inertia_)
    if k > 1:
        sil_scores.append(silhouette_score(df_scaled, clusters))

```

```{code-cell} ipython3

plt.plot(k_list, inertia_list, "o-")
plt.show()
plt.plot(k_list[1:], sil_scores, "o-", color="orange")
plt.ylim(0,1)
plt.show()    
```

```{code-cell} ipython3
k = 3

model = KMeans(n_clusters=k, n_init=50)
clusters = model.fit_predict(df_scaled)
df_clusters = df.copy()
df_clusters["clusters"] = clusters
df_scaled["clusters"] = clusters
df_clusters
```

```{code-cell} ipython3
table = df_clusters.groupby(by="spilleliste")["clusters"].value_counts().to_frame().unstack(fill_value=0)["count"]
index_liste = list(table.index)
index_liste[7] = "Procul Harum - A whiter..."
table.index = index_liste
table
```

```{code-cell} ipython3

```

```{code-cell} ipython3
df_clusters["clusters"].value_counts()
```

```{code-cell} ipython3
table.plot.bar(stacked=True)
```

```{code-cell} ipython3

table_rel = table.div(table.sum(axis=1), axis=0)
sns.heatmap(table_rel, cmap="Blues", annot=True, fmt=".2f")
```

```{code-cell} ipython3
pca = PCA(n_components=2)
xpca = pca.fit_transform(df_scaled[feature_columns])
centroids = pca.transform(model.cluster_centers_)
df_clusters["pca_x"] = xpca[:,0]
df_clusters["pca_y"] = xpca[:,1]

ax = sns.relplot(data=df_clusters, x="pca_x", y="pca_y", hue="clusters", kind="scatter")
plt.plot(centroids[:,0], centroids[:,1], 'X', markersize=15)
plt.show()
```

```{code-cell} ipython3
cluster_tab = df_scaled.groupby(by="clusters")[feature_columns].mean()
sns.heatmap(data=cluster_tab, cmap="coolwarm", vmax=1, vmin=-1, fmt=".2f", annot=True)
```

```{code-cell} ipython3

```

# KNN

Kanskje?

```{code-cell} ipython3
spillelister_enum = enumerate(df["spilleliste"].unique())
for i, spilleliste in spillelister_enum:
    print(i,spilleliste)
```

```{code-cell} ipython3
kategorier = {"prog": [5,14,15,],
              "pop": [1,2,6,0,8,10],
              "rock": [12,13],
              "jazz": [9]}
```

```{code-cell} ipython3
kategorier
```
