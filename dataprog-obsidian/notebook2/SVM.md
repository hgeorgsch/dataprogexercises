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

## Maskinlæringsproblemet

Fyrst lyt me setja opp sjølve problemet og definera kva variablar
me skal predikera.
Denne delen er uavhengig av om me vil bruka SVM eller andre algoritmar.

Den avhengige variabelen, som skal predikerast, er `Target`.
Som uavhengige variablar kan me henta ut alle søylene unnateke
`Target`.
Desse variablane kaller me gjerne *features*.
På norsk seier eg stundom *drag* eller *trekk*.

```{code-cell} ipython3
features = df.columns[~df.columns.str.contains("Target")]

X = df[features]
y = df["Target"]
```

Etter gamal vane kaller med den avhengige variabelen for `y` og
dei uavhengige for `X`.

SciKitLearn gjev oss ein funksjon for å dela heile datasettet i
trenings- og testsett, slik.

```{code-cell} ipython3
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
```

::: {admonition} Oppgåve
Sjekk at dei fire variablane (`X_train` osv.) er som dei skal vera.
Har dei rett tal på søyler og radar?
:::

## Support vector machine

Treninga av ein SVM-modell liknar svært på FLD.
Det er sjølvsagt fordi SciKitLearn er laga for at det skal
vera so likt som råd.

```{code-cell} ipython3
from sklearn import svm

clf = svm.SVC(probability=True,kernel='rbf')
result = clf.fit(X_train,y_train)
```

Dette gjev ein ferdig trent SVM-modell, `clf`.

::: {admonition} Merknad
SVM tek to argument som me ikkje har sett før.
Det fyrste, `probability`, skal me forklara under.
Det andre, `kernel`, viser til ein sentral komponent i SVM-modellen.
Ein kan velja ulike kjernar som gjev fleire eller færre fridomsgradar.
Dét blir for mykje å gå inn på, men RBF er eit vanleg val.
:::

Legg merke til at modellane i SciKitLearn vil ha $x$- og $y$-variablane
for seg.  Når me skal analysera, er det gjerne enklast å ha alt i éin
*DataFrame*, slik

```{code-cell} ipython3
df_test = X_test.join(y_test)
display( df_test )
```

Prediksjonen fungerer òg akkurat som me hugsar frå FLD.
Me kan leggja prediksjonan til som ein ny søyle i testsettet.

```{code-cell} ipython3
df_test["modell"] = clf.predict(X_test)
```

::: {admonition} Oppgåve
Sjå på innhaldet i `df_test`.
Er prediksjonane gode?

:::

Suksessraten kan me rekna ut slik.

```{code-cell} ipython3
korrekt = df_test[ "Target"]==df_test["modell" ]
sukksessrate = korrekt.sum()/korrekt.size
print(f"Modellen vår fungerer {sukksessrate:.2%} av gangene")
```

::: {admonition} Refleksjon
Suksessraten er ein god estimator for sannsynet for rett svar.
Dersom du hugsar nok statistikk, er det ein god idé å rekna
ut standardfeilen åt denne estimatoren.
:::

## Sannsynsestimat

Då me laga modellen, sa me `probability=True`.
Det tyder at modellen ikkje berre klassifiserer, men òg estimerer kor
rimeleg kvar mogleg klasse er.
For å få fatt i denne informasjonen, skal me bruka ein annan variant
til prediksjonen, slik:

```{code-cell} ipython3
probabilities = clf.predict_proba(X_test)
display(probabilities)
```

Dersom ei klasse har 90% sannsynsestimat kan me stola ganske godt på
at klassifikasjonen er rett.  Om sannsynsestimatet ligg rundt 50%, kan
det like gjerne vera feil.

