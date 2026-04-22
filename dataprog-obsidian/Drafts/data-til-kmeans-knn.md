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
import matplotlib.pyplot as plt
import seaborn as sns
```

```{code-cell} ipython3

menn_bmi = 26.9
kvinner_bmi = 25.2

menn_h = 180.4
kvinner_h = 167.2

mm = menn_bmi*(menn_h/100)**2
mk = kvinner_bmi*(kvinner_h/100)**2

n = 10000
```

```{code-cell} ipython3
menn_bmi_liste = np.random.normal(loc=menn_bmi, scale=menn_bmi*0.2, size=n)
menn_hoyde_liste = np.random.normal(loc=menn_h, scale=8, size=n)

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
n = 1000

stats = {
    "mann": {
        "høyde": 180.4,
        "bmi": 26.9,
        "fot": 26.5,
        "hår": 5.0
    },
    "kvinne": {
        "høyde": 167.2, 
        "bmi": 25.2,
        "fot": 23.0,
        "hår": 30.0
    }
}
         

def generer_hoyde(kjønn):
    mu = stats[kjønn]["høyde"]
    return np.random.normal(loc=mu, scale=mu*0.2)

def generer_bmi(kjønn):
    mu = stats[kjønn]["bmi"]
    return np.random.normal(loc=mu,scale=mu*0.2)
    

def generer_person():
    kjønn = np.random.choice(("mann", "kvinne"))
    bmi = generer_bmi(kjønn)
    h = max(100,generer_hoyde(kjønn))
    masse = max(20,bmi*(h/100)**2)
    person = pd.Series({"kjønn": kjønn, "bmi": bmi, "høyde": h, "vekt": masse})
    return person


personer = [generer_person() for _ in range(n)]
df = pd.DataFrame(personer)


df

```

```{code-cell} ipython3
sns.relplot(data=df, x="høyde", y="vekt", hue="kjønn", kind="scatter")
sns.pairplot(data=df, hue="kjønn")
```

```{code-cell} ipython3
df_sko = df.copy()

def fotl(h,k):
    mu = stats[k]["fot"]
    h_mu = stats[k]["høyde"]
    a = mu/h_mu
    l = a*h+a*h*np.random.normal(loc=0, scale=0.03)
    return l
    

def generer_skostørrelse(pers):
    h = pers["høyde"]
    k = pers["kjønn"]
    fot_lengde = fotl(h,k)
    if k=="menn":
        sko_str = np.ceil(3*(fot_lengde+1.5)/2)
    else:
        sko_str = np.floor(3*(fot_lengde+1.5)/2)
    return pd.Series({"fot": fot_lengde, "sko": sko_str})


df_ny = df_sko.apply(generer_skostørrelse, axis=1)
df_sko = pd.concat([df_sko, df_ny], axis=1)

    
```

```{code-cell} ipython3
dfk = df_sko.copy()

def generer_hår(k):
    mu_m = stats["mann"]["hår"]
    mu_k = stats["kvinne"]["hår"]

    if k=="mann" and np.random.uniform() < 0.8:
        return max(0,np.random.normal(loc=mu_m, scale = 3))
    else:
        return max(0,np.random.normal(loc=mu_k, scale = 12))

dfk["hår"] = dfk["kjønn"].map(generer_hår)
dfk
    
```

```{code-cell} ipython3
sns.pairplot(data=dfk, hue="kjønn")
```

```{code-cell} ipython3
numeriske = dfk.columns[1:]
korrelasjon = dfk[numeriske].corr()

sns.heatmap(korrelasjon, annot=True, fmt=".1f", cmap="coolwarm", vmin=-1, vmax=1)
```

```{code-cell} ipython3
dfk
```

```{code-cell} ipython3
sns.relplot(data=dfk,x="fot", y="høyde", hue="kjønn", kind="scatter")
```

```{code-cell} ipython3
sns.pairplot(data=dfk)
```

```{code-cell} ipython3

```

```{code-cell} ipython3
# Importerer verktøyet for standardisering fra scikit-learn
from sklearn.preprocessing import StandardScaler

# Lager en "skalerings-maskin"
scaler = StandardScaler().set_output(transform="pandas")

# Kjører dataene våre gjennom maskinen. 
# (Fit regner ut gjennomsnittet, transform utfører selve endringen)
df_scaled = scaler.fit_transform(dfk[numeriske])

# Tar en titt på de skalerte dataene. Legg merke til at tallene nå er små (både positive og negative)!
df_scaled.head()
```

```{code-cell} ipython3
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Vi tester antall klynger (k) fra 2 til og med 10
k_list = range(1, 10)

inertia_list = []
sil_score = []

for k in k_list:
    # random_state=11 sørger for at K-Means gir nøyaktig samme svar hver gang
    model = KMeans(n_clusters=k, n_init=50).set_output(transform="pandas")
    
    # Vi trener modellen på de skalerte variablene våre
    result = model.fit_predict(df_scaled)
    
    # Lagrer poengsummene
    inertia_list.append(model.inertia_)
    if k==1:
        continue
    sil_score.append(silhouette_score(df_scaled, result))

# --- Plotter Inertia (Elbow-metoden) ---
plt.figure(figsize=(8, 4))
plt.plot(k_list, inertia_list, 'o-', color="blue")
plt.xticks(k_list)
plt.title("Elbow-metoden (Inertia)")
plt.xlabel("Antall klynger (K)")
plt.ylabel("Inertia (lavere er bedre)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()

# --- Plotter Silhouette-score ---
plt.figure(figsize=(8, 4))
plt.plot(k_list[1:], sil_score, 'o-', color="orange")
plt.xticks(k_list[1:])
plt.title("Silhouette-score")
plt.xlabel("Antall klynger (K)")
plt.ylabel("Score (høyere er bedre)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()
```

```{code-cell} ipython3

cluster_n = 2

kmeans = KMeans(n_clusters=cluster_n, n_init=50)

clusters = kmeans.fit_predict(df_scaled)

df_clusters = dfk.co

df_clusters["cluster"] = clusters
```

```{code-cell} ipython3
klynge_storrelser = df_clusters["cluster"].value_counts().sort_index()


display(klynge_storrelser.to_frame(name="Antall"))
```

```{code-cell} ipython3
from sklearn.decomposition import PCA

# Klemmer dataene ned til 2 dimensjoner for plotting
pca = PCA(n_components=2).set_output(transform="pandas")

# Kjører PCA på de SKALERTE dataene
pca_resultater = pca.fit_transform(df_scaled)

# Legger til koordinatene i hovedtabellen
df_clusters["PCA1"] = pca_resultater["pca0"]
df_clusters["PCA2"] = pca_resultater["pca1"]

# Plotter klyngene med navnene
plt.figure(figsize=(10, 8))
sns.scatterplot(
    data=df_clusters, 
    x="PCA1", 
    y="PCA2", 
    hue="cluster", 
    palette="viridis", 
    alpha=0.5          
)

plt.title("Kundesegmentene visualisert i 2D (PCA)")
plt.xlabel("Hovedkomponent 1 (Største variasjon i dataene)")
plt.ylabel("Hovedkomponent 2 (Nest største variasjon)")
plt.grid(True, linestyle="--", alpha=0.5)
plt.show()

# Hvor mye av den totale variasjonen (100 %) fanger de to PCA-aksene våre opp?
print(f"Varians forklart av 2D-plottet: {pca.explained_variance_ratio_.sum() * 100:.1f} %")
```

```{code-cell} ipython3
sns.pairplot(data=df_clusters, hue="cluster")
```

```{code-cell} ipython3
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
```

```{code-cell} ipython3
from sklearn.model_selection import train_test_split

X = df_scaled[numeriske]
y = dfk["kjønn"]

model = KNeighborsClassifier(n_neighbors=50)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)
result = model.fit(X_train, y_train)

df_test = pd.DataFrame(X_test)
df_test = df_test.join(y_test)
df_test["KNN"] = model.predict(X_test)
test_probabilities = model.predict_proba(X_test)
df_test["KNN_prob"] = list(map(max, test_probabilities))
sns.relplot(data=df_test, x="høyde", y="vekt", hue="kjønn")
sns.relplot(data=df_test, x="høyde", y="vekt", hue="KNN", size="KNN_prob")
df_test.dtypes
```

```{code-cell} ipython3
df
```

```{code-cell} ipython3
sns.pairplot(data=df_test, hue="KNN")
```
