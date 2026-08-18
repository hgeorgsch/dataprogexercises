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
import sklearn.cluster
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

```{code-cell} ipython3
df = pd.read_csv("mitt_spotify_datasett.csv").dropna()
df
```

```{code-cell} ipython3
df.columns
features = df.columns[8:]
df_slft = df.groupby("spilleliste")[features].describe().drop("count", axis=1, level=1)
df_slft.columns = df_slft.columns.map("_".join)
df_slft
```

```{code-cell} ipython3
df_sl = df.groupby("spilleliste")[features].mean()
df_sl_std = df.groupby("spilleliste")[features].std()
df_sl_std.columns= df_sl_std.columns.map(lambda x: "std_"+x)
df_sl_std

df_grouped = pd.merge(df_sl, df_sl_std, left_index=True, right_index=True)
df_grouped = df_slft
```

```{code-cell} ipython3
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# 1. Skalering av dataene
# Maskinlæring misliker at 'tempo' (f.eks. 120) veier mer enn 'acousticness' (f.eks. 0.2)
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_grouped)

# 2. Beregne "Inertia" (treghet/varians innad i klyngene) for ulike antall klynger (k)
inertia_values = []
k_values = range(1, 11) # Vi tester fra 1 til 10 klynger

for k in k_values:
    # Setter random_state for at studentene skal få nøyaktig samme resultat hver gang
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(df_scaled)
    inertia_values.append(kmeans.inertia_)

# 3. Plotting av resultatene
plt.figure(figsize=(8, 5))
plt.plot(k_values, inertia_values, marker='o', linestyle='-', color='b')
plt.title('Elbow-metoden for spillelistene (16 rader, 22 features)')
plt.xlabel('Antall klynger (k)')
plt.ylabel('Inertia (Avstand innad i klyngene)')
plt.xticks(k_values)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
```

```{code-cell} ipython3
from sklearn.cluster import KMeans

k = 5
model = KMeans(n_clusters=k)
result = model.fit(df_grouped)
df_grouped["cluster"] = model.predict(df_grouped)
df_grouped
```

```{code-cell} ipython3
df_grouped["cluster"].to_frame()
```

```{code-cell} ipython3
df
```

```{code-cell} ipython3
df_sang_analyse = df.set_index("sang_id")[features].dropna()
df_sang_analyse
```

```{code-cell} ipython3
# 1. Skalering av dataene
# Maskinlæring misliker at 'tempo' (f.eks. 120) veier mer enn 'acousticness' (f.eks. 0.2)
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_sang_analyse)

# 2. Beregne "Inertia" (treghet/varians innad i klyngene) for ulike antall klynger (k)
inertia_values = []
k_values = range(1, 11) # Vi tester fra 1 til 10 klynger

for k in k_values:
    # Setter random_state for at studentene skal få nøyaktig samme resultat hver gang
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(df_scaled)
    inertia_values.append(kmeans.inertia_)

# 3. Plotting av resultatene
plt.figure(figsize=(8, 5))
plt.plot(k_values, inertia_values, marker='o', linestyle='-', color='b')
plt.title('Elbow-metoden for spillelistene (16 rader, 22 features)')
plt.xlabel('Antall klynger (k)')
plt.ylabel('Inertia (Avstand innad i klyngene)')
plt.xticks(k_values)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

from sklearn.metrics import silhouette_score

# Vi forutsetter at df_scaled er dataene dine skalert med StandardScaler()
# (Samme som i forrige steg)

silhouette_scores = []
k_values = range(2, 11) # Starter på 2, siden man må ha minst 2 klynger for å måle avstand mellom dem

for k in k_values:
    # Kjører K-Means for hver k
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    cluster_labels = kmeans.fit_predict(df_scaled)
    
    # Regner ut gjennomsnittlig Silhouette Score for alle punktene
    score = silhouette_score(df_scaled, cluster_labels)
    silhouette_scores.append(score)

# Plotting av Silhouette Scores
plt.figure(figsize=(8, 5))
plt.plot(k_values, silhouette_scores, marker='s', linestyle='-', color='g')
plt.title('Silhouette Score for sanger (460 rader)')
plt.xlabel('Antall klynger (k)')
plt.ylabel('Silhouette Score (-1 til 1)')
plt.xticks(k_values)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
```

```{code-cell} ipython3


ks = [2,4]

for k in ks:
    model = KMeans(n_clusters=k)
    result = model.fit(df_scaled)
    df[f"cluster_{k}"] = model.predict(df_scaled)
df
```

```{code-cell} ipython3
df_heat = df.groupby("cluster_5")[features].mean()
```

```{code-cell} ipython3
import seaborn as sns

scaler = StandardScaler()
scaled = scaler.fit_transform(df_heat)
#Tempo er for høy
dfs = pd.DataFrame(scaled)
dfs.columns = df_heat.columns

sns.heatmap(dfs)
```

# PCA


```{code-cell} ipython3
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA

# 1. Vi ber sklearn om å komprimere dataene ned til nøyaktig 2 dimensjoner
pca = PCA(n_components=2)

# 2. Utfør selve magien (fit_transform) på de skalerte musikkdataene
pca_features = pca.fit_transform(df_scaled)

# 3. Lagre de to nye "super-kolonnene" i den originale DataFramen vår
df['pca_x'] = pca_features[:, 0] # Dette blir X-aksen vår
df['pca_y'] = pca_features[:, 1] # Dette blir Y-aksen vår

# 4. Hvor mye av den opprinnelige informasjonen (variansen) beholdt vi?
varians = pca.explained_variance_ratio_
print(f"Dimensjon 1 forklarer {varians[0]*100:.1f}% av all variasjon i dataene")
print(f"Dimensjon 2 forklarer {varians[1]*100:.1f}% av all variasjon i dataene")
print(f"Totalt bevart informasjon: {sum(varians)*100:.1f}%")

# 5. Tegn opp det ferdige kartet! 
plt.figure(figsize=(10, 8))

# Vi fargelegger punktene basert på klyngene vi fant tidligere (f.eks. med k=5)
sns.scatterplot(data=df, x='pca_x', y='pca_y', hue='cluster_5', palette='tab10', s=60, alpha=0.8)

plt.title('Sanger komprimert til 2D (PCA) fargekodet etter K-Means klynger')
plt.xlabel(f'Hovedkomponent 1 ({varians[0]*100:.1f}%)')
plt.ylabel(f'Hovedkomponent 2 ({varians[1]*100:.1f}%)')
plt.legend(title='Klynge')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
```

```{code-cell} ipython3
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

# 1. Vi antar at dataene allerede er skalert (df_scaled)
# Bestemmer oss for å beholde f.eks. 3 hovedkomponenter (3D)
pca = PCA(n_components=3) 
pca_features = pca.fit_transform(df_scaled)

# La oss se hvor mye av den opprinnelige informasjonen vi har beholdt i disse 3 kolonnene
beholdt_info = sum(pca.explained_variance_ratio_) * 100
print(f"Vi komprimerte fra 11D til 3D, og beholdt {beholdt_info:.1f}% av informasjonen i dataene.")

# 2. Nå kjører vi K-Means på de KOMPRIMERTE dataene (pca_features), ikke originaldataene!
kmeans_pca = KMeans(n_clusters=5, random_state=42, n_init=10)

# 3. Lagrer det nye resultatet i DataFramen vår
df['cluster_etter_pca'] = kmeans_pca.fit_predict(pca_features)

```

```{code-cell} ipython3
import matplotlib.pyplot as plt
import seaborn as sns

# Vi forutsetter at du har lagret PCA-komponentene i dataframen din
# Hvis du ikke har gjort det ennå, legger vi de to første inn her:
df['pca_x'] = pca_features[:, 0] # Den viktigste komponenten
df['pca_y'] = pca_features[:, 1] # Den nest viktigste komponenten

# Setter opp et stort og tydelig lerret
plt.figure(figsize=(10, 8))

# Bruker seaborn til å lage et spredningsplott
# Legg merke til at vi fargelegger (hue) basert på den NYE klyngen: 'cluster_etter_pca'
sns.scatterplot(
    data=df, 
    x='pca_x', 
    y='pca_y', 
    hue='cluster_etter_pca', 
    palette='Set1', # 'Set1' gir sterke, tydelige farger som er fine på prosjektor
    s=70,           # Størrelse på prikkene
    alpha=0.8       # Gjør prikkene litt gjennomsiktige slik at vi ser overlapp
)

# Pynter grafen for klasserommet
plt.title('Sanger klynget ETTER komprimering med PCA', fontsize=16, pad=15)
plt.xlabel('Hovedkomponent 1 (Mest variasjon)', fontsize=12)
plt.ylabel('Hovedkomponent 2 (Nest mest variasjon)', fontsize=12)

# Fikser legend (tegnforklaringen)
plt.legend(title='Klynge (K-Means)', title_fontsize='12', fontsize='11', loc='best')
plt.grid(True, linestyle='--', alpha=0.5)

# Viser herligheten!
plt.show()
```

```{code-cell} ipython3
df2 = pd.read_csv("mitt_spotify_datasett.csv").dropna()
df2
```

```{code-cell} ipython3
df2.columns
features = df2.columns[8:]
df_slft = df2.groupby("spilleliste")[features].describe().drop("count", axis=1, level=1)
df_slft.columns = df_slft.columns.map("_".join)
df_slft
```

```{code-cell} ipython3

scaler = StandardScaler()
df_scaled = scaler.fit_transform(df_slft)


pca = PCA(n_components=12) 
pca_features = pca.fit_transform(df_scaled)


beholdt_info = sum(pca.explained_variance_ratio_) * 100
print(f"Vi komprimerte fra 77D til 3D, og beholdt {beholdt_info:.1f}% av informasjonen i dataene.")

kmeans_pca = KMeans(n_clusters=5, random_state=42, n_init=10)


df_slft['cluster_etter_pca'] = kmeans_pca.fit_predict(pca_features)
```

```{code-cell} ipython3
df_slft
```

```{code-cell} ipython3
# Vi forutsetter at du har lagret PCA-komponentene i dataframen din
# Hvis du ikke har gjort det ennå, legger vi de to første inn her:
df_slft['pca_x'] = pca_features[:, 0] # Den viktigste komponenten
df_slft['pca_y'] = pca_features[:, 1] # Den nest viktigste komponenten

# Setter opp et stort og tydelig lerret
plt.figure(figsize=(10, 8))

# Bruker seaborn til å lage et spredningsplott
# Legg merke til at vi fargelegger (hue) basert på den NYE klyngen: 'cluster_etter_pca'
sns.scatterplot(
    data=df_slft, 
    x='pca_x', 
    y='pca_y', 
    hue='cluster_etter_pca', 
    palette='Set1', # 'Set1' gir sterke, tydelige farger som er fine på prosjektor
    s=70,           # Størrelse på prikkene
    alpha=0.8       # Gjør prikkene litt gjennomsiktige slik at vi ser overlapp
)

# Pynter grafen for klasserommet
plt.title('Sanger klynget ETTER komprimering med PCA', fontsize=16, pad=15)
plt.xlabel('Hovedkomponent 1 (Mest variasjon)', fontsize=12)
plt.ylabel('Hovedkomponent 2 (Nest mest variasjon)', fontsize=12)

# Fikser legend (tegnforklaringen)
plt.legend(title='Klynge (K-Means)', title_fontsize='12', fontsize='11', loc='best')
plt.grid(True, linestyle='--', alpha=0.5)

# Viser herligheten!
plt.show()
```

```{code-cell} ipython3
df_en = df[["energy", "acousticness", "sang_id"]]
```

```{code-cell} ipython3
df.plot.scatter(x="energy", y="acousticness")
```

```{code-cell} ipython3
df.plot.scatter(x="danceability", y="acousticness")
```

```{code-cell} ipython3
df_slft
```

```{code-cell} ipython3
df.query("spilleliste == ' '")
```

```{code-cell} ipython3
testy = { "x" : list(df["energy"]), "y": list(df["acousticness"])}
with open("testdat.json", "w") as file:
    json.dump(testy,file)
```

# Que?

+++ {"editable": true, "slideshow": {"slide_type": ""}}

# Why pca test her
<iframe src="https://jonajh.folk.ntnu.no/jsx/pca.html" width="900" height="500"></iframe>

kanskje det funker etter eksport

```{code-cell} ipython3
from IPython.display import HTML

HTML("""
<iframe
    src="https://jonajh.folk.ntnu.no/jsx/pca.html"
    width="900"
    height="500"
    style="border:1px solid #ccc; border-radius:8px;"
></iframe>
""")
```


<iframe
    src="https://jonajh.folk.ntnu.no/jsx/pca.html"
    width="900"
    height="500"
    style="border:1px solid #ccc; border-radius:8px;"
></iframe>

```{code-cell} ipython3
pd.plotting.scatter_matrix(df[features], figsize=(10,10))
plt.show()
```

```{code-cell} ipython3
dfs_val = scaler.fit_transform(df[features])
dfs = pd.DataFrame(dfs_val)
dfs.columns = features
dfs["spilleliste"] = df["spilleliste"]
dfs["sang"] = df["sang"]
```

```{code-cell} ipython3
pd.plotting.scatter_matrix(dfs[features], figsize=(10,10))
plt.show()
```

```{code-cell} ipython3
dfs.plot.scatter(x="valence", y="energy")
```

```{code-cell} ipython3
print(dfs.columns)
def prikk_tittel(streng, makslen):
    if len(str(streng))>makslen:
        return streng[:(makslen-3)]+"..."
    return str(streng)[:makslen]

dfs["spilleliste_kort"] = dfs["spilleliste"].map(lambda x: prikk_tittel(x, 18))
sns.relplot(dfs, x="valence", y="energy", hue="spilleliste_kort", kind="scatter")
```

```{code-cell} ipython3

from sklearn.decomposition import PCA

# 1. Vi ber sklearn om å komprimere dataene ned til nøyaktig 2 dimensjoner
pca = PCA(n_components=2)

# 2. Utfør selve magien (fit_transform) på de skalerte musikkdataene
pca_features = pca.fit_transform(dfs[features])

# 3. Lagre de to nye "super-kolonnene" i den originale DataFramen vår
dfs['pca_x'] = pca_features[:, 0] # Dette blir X-aksen vår
dfs['pca_y'] = pca_features[:, 1] # Dette blir Y-aksen vår

# 4. Hvor mye av den opprinnelige informasjonen (variansen) beholdt vi?
varians = pca.explained_variance_ratio_
print(f"Dimensjon 1 forklarer {varians[0]*100:.1f}% av all variasjon i dataene")
print(f"Dimensjon 2 forklarer {varians[1]*100:.1f}% av all variasjon i dataene")
print(f"Totalt bevart informasjon: {sum(varians)*100:.1f}%")

# 5. Tegn opp det ferdige kartet! 
plt.figure(figsize=(10, 8))

# Vi fargelegger punktene basert på klyngene vi fant tidligere (f.eks. med k=5)
sns.scatterplot(data=dfs, x='pca_x', y='pca_y', hue='spilleliste_kort', palette='tab10', s=60, alpha=0.8)

plt.title('Sanger komprimert til 2D (PCA) fargekodet etter K-Means klynger')
plt.xlabel(f'Hovedkomponent 1 ({varians[0]*100:.1f}%)')
plt.ylabel(f'Hovedkomponent 2 ({varians[1]*100:.1f}%)')
plt.legend(title='Klynge')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
```

```{code-cell} ipython3
---
editable: true
slideshow:
  slide_type: ''
---
n_max = 11

pca = PCA(n_max)

pca_features = pca.fit_transform(dfs[features])
varians = pca.explained_variance_ratio_
tot = 0
for i in range(n_max):
    tot += varians[i]
    print(i, f"komponenter forklarerer {tot*100}% av variasjon") 


pca_behold = pca_features[:,:8]

# 3. Lagre de to nye "super-kolonnene" i den originale DataFramen vår
dfs['pca_x'] = pca_features[:, 0] # Dette blir X-aksen vår
dfs['pca_y'] = pca_features[:, 1] # Dette blir Y-aksen vår

kmeans_pca = KMeans(n_clusters=5, random_state=42, n_init=10)

dfs["cluster_5"] = kmeans_pca.fit_predict(pca_behold)
#df_slft['cluster_etter_pca'] = kmeans_pca.fit_predict(pca_features)


# Vi fargelegger punktene basert på klyngene vi fant tidligere (f.eks. med k=5)
sns.scatterplot(data=dfs, x='pca_x', y='pca_y', hue='cluster_5', palette='tab10', s=60, alpha=0.8)

plt.title('Sanger komprimert til 2D (PCA) fargekodet etter K-Means klynger')
plt.xlabel(f'Hovedkomponent 1 ({varians[0]*100:.1f}%)')
plt.ylabel(f'Hovedkomponent 2 ({varians[1]*100:.1f}%)')
plt.legend(title='Klynge')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()


ax = sns.scatterplot(data=dfs, x='pca_x', y='pca_y', hue='spilleliste_kort', s=60, alpha=0.8)
plt.title('Sanger komprimert til 2D (PCA) fargekodet etter K-Means klynger')
plt.xlabel(f'Hovedkomponent 1 ({varians[0]*100:.1f}%)')
plt.ylabel(f'Hovedkomponent 2 ({varians[1]*100:.1f}%)')
#plt.legend(title='Klynge')
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
          fancybox=True, shadow=True, ncol=5)

plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
```

```{code-cell} ipython3
# 2. Beregne "Inertia" (treghet/varians innad i klyngene) for ulike antall klynger (k)
inertia_values = []
k_values = range(1, 11) # Vi tester fra 1 til 10 klynger

for k in k_values:
    # Setter random_state for at studentene skal få nøyaktig samme resultat hver gang
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(pca_behold)
    inertia_values.append(kmeans.inertia_)

# 3. Plotting av resultatene
plt.figure(figsize=(8, 5))
plt.plot(k_values, inertia_values, marker='o', linestyle='-', color='b')
plt.title('Elbow-metoden for spillelistene (16 rader, 22 features)')
plt.xlabel('Antall klynger (k)')
plt.ylabel('Inertia (Avstand innad i klyngene)')
plt.xticks(k_values)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()


k_values  = range(2,9)
silhouette_scores = []
for k in k_values:
    # Kjører K-Means for hver k
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    cluster_labels = kmeans.fit_predict(pca_behold)
    
    # Regner ut gjennomsnittlig Silhouette Score for alle punktene
    score = silhouette_score(pca_behold, cluster_labels)
    silhouette_scores.append(score)

# Plotting av Silhouette Scores
plt.figure(figsize=(8, 5))
plt.plot(k_values, silhouette_scores, marker='s', linestyle='-', color='g')
plt.title('Silhouette Score for sanger (460 rader)')
plt.xlabel('Antall klynger (k)')
plt.ylabel('Silhouette Score (-1 til 1)')
plt.xticks(k_values)
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()
```

```{code-cell} ipython3




# 1. Vi ber sklearn om å komprimere dataene ned til nøyaktig 2 dimensjoner
pca = PCA(n_components=2)

# 2. Utfør selve magien (fit_transform) på de skalerte musikkdataene
pca_features = pca.fit_transform(dfs[features])

# 3. Lagre de to nye "super-kolonnene" i den originale DataFramen vår
dfs['pca_x'] = pca_features[:, 0] # Dette blir X-aksen vår
dfs['pca_y'] = pca_features[:, 1] # Dette blir Y-aksen vår

# 4. Hvor mye av den opprinnelige informasjonen (variansen) beholdt vi?
varians = pca.explained_variance_ratio_
print(f"Dimensjon 1 forklarer {varians[0]*100:.1f}% av all variasjon i dataene")
print(f"Dimensjon 2 forklarer {varians[1]*100:.1f}% av all variasjon i dataene")
print(f"Totalt bevart informasjon: {sum(varians)*100:.1f}%")

# 5. Tegn opp det ferdige kartet! 
plt.figure(figsize=(10, 8))

# Vi fargelegger punktene basert på klyngene vi fant tidligere (f.eks. med k=5)
sns.scatterplot(data=dfs, x='pca_x', y='pca_y', hue='spilleliste_kort', palette='tab10', s=60, alpha=0.8)

plt.title('Sanger komprimert til 2D (PCA) fargekodet etter K-Means klynger')
plt.xlabel(f'Hovedkomponent 1 ({varians[0]*100:.1f}%)')
plt.ylabel(f'Hovedkomponent 2 ({varians[1]*100:.1f}%)')
plt.legend(title='Klynge')
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()
```
