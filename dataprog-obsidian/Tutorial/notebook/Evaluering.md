---
jupytext:
  formats: ipynb,md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.17.0
kernelspec:
  display_name: dataprog
  language: python
  name: dataprog
---

# Evaluering av modellar

Modellar i statistikk og maskinlæring er tilfeldige konstruksjonar,
dvs. dei er like tilfeldige som datasettet som ligg til grunn.
Om me gjer nye observasjonar, vil dei se annleis ut, og me får ein
annan modell.

Dette ser me tydleg i meiningsmålingar.  Ofte er der fleire byrå
ut og gjer meiningsmålingar på same tid, og dei bruker dei same
statistiske metodane.  Likevel får dei forskjellige resultat, og
dei treff sjelden valresultatet presist.

Ein modell, som t.d. den lineære diskriminanten som me fann
i den førre øvinga ([[Fisher Linear Discriminant in sklearn]]), gjev ei optimal skildring av datasettet som det er trent på.
Det som er interessant er derimot kor godt det skildrar resten
av populasjonen og kor godt det kan predikera nye og hittil ukjende
data.  Det finn me berre ut ved å testa.

Her skal me gå gjennom eit enkelt og standardisert testlaup,
der me evaluerer modellen som me fann i den førre øvinga.

## Datasettet

Lat oss fyrst lasta datasettet på same måte som sist.  Me 
importerer òg dei same biblioteka som me brukte sist.

```{code-cell} ipython3
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis 
import numpy as np
iris = datasets.load_iris()
```

Me har ikkje fleire data enn det eine settet.  For å kunne evaluera
modellen må me difor halda tilbake ein del av datasettet til å testa
på.  Dette testsettet kan me ikkje bruka i treninga.
Ein vanleg tommelfingerregel er å bruka 20% av datasettet til testing
og 80% til trening.

::: {admonition} Merknad
Dette er ein tommelfingerregel.  Dersom du er kjend med estimering
og hypotesetesting frå statistikk, so kan du kanskje rekna ut kor
mange datapunkt du treng i testsettet for å få eit statistisk
signifikant resultat. Det er naudsynt for å kunna vita kor mykje
me kan stola på modellen, men her skal me nøya oss med tommelfingerregelen.

Der større testsett gjev ein meir påliteleg evaluering, vil større 
treningssett gje ein betre modell.  Det er eit dilemma.
:::

Når me deler datasettet vil me normalt syta for at klassene er
likt representerte i trenings- og testsettet.  Her har vi 50
blomar frå kva klasse, og vil då ta 40 frå kvar til testsettet.
Me tek også ut berre dei to fyrste søylene, akkurat som sist.

```{code-cell} ipython3
trening1 = iris.data[:40,:2]
trening2 = iris.data[50:90,:2]
trening3 = iris.data[100:140,:2]
test1 = iris.data[40:50,:2]
test2 = iris.data[90:100,:2]
test3 = iris.data[140:,:2]

trening = np.vstack( [ trening1, trening2, trening3 ] )
test = np.vstack( [ test1, test2, test3 ] )
```

Her bruker me seks variablar for å dela kvar klasse i 40+10 
rader, før me stablar saman tre delsett til test- og tremingssettet.
Me bruker numpy-funksjonen `vstack` som står for *vertical stack` 
til å setja saman matrisene.
Me kan sjekka:

```{code-cell} ipython3
print( "TRENING" )
print(trening)
print( "TEST" )
print(test)
```

Me må gjera det same med klassene *target*.
```{code-cell} ipython3
treningtarget = np.zeros( 120 )
treningtarget[40:] = 1
print( treningtarget )
```
Her gjer me det på ein litt annan måte, som er meir kompakt.
Det er mogleg fordi me veit kvar klassene er.
Den fyrste lina lagar ein vektor med 120 nullar, og den andre sett
alle elementa bortsett frå dei 40 fyrste, til ein.

For testsettet har me
```{code-cell} ipython3
testtarget = np.zeros( 30 )
testtarget[10:] = 1
print( testtarget )
```
Merk at me berre skil mellom iris setosa og ikkje-setosa.

## Trening av diskriminanten

Me kan trena diskriminanten som før.

```{code-cell} ipython3
lda = LinearDiscriminantAnalysis()  
lda.fit(trening,treningtarget)
print(lda.coef_)
print(lda.intercept_)
```

::: {admonition} Oppgåve
Visualiser treningssettet og diskriminanten.
:::

Me kan òg sjekka nøyaktig kor mykje feil modellen gjer på treningssettet.

```{code-cell} ipython3
pred = lda.predict( treningsett )
error = pred - treningtarget
print( error )
```

Legg merke til at me kan køyra prediksjonen på heile datasettet i eitt kall.

::: {admonition} Oppgåve
Kva skjer her?  Kva representerer `error`?  Kva verdi svarer til feil og kva til
rett prediksjon?
:::

For å telja feila, kan me t.d. gjera noko slikt:
```{code-cell} ipython3
error[ error != 0 ] = 1
print( sum(error)/len(error )
:::

::: {admonition} Oppgåve
Kva representerer dette talet `sum(error)/len(error)`?
:::


## Testing

Me kan gjera akkurat den same testen som med treningssettet.

```{code-cell} ipython3
testpred = lda.predict( testsett )
testerror = testpred - testtarget
print( testerror )
```

```{code-cell} ipython3
ax = plt.subplot()
scatter = ax.scatter(test[:, 0], test[:, 1], c=testtarget)
ax.set(xlabel=iris.feature_names[0], ylabel=iris.feature_names[1])
ax.legend(
    scatter.legend_elements()[0], ["setosa", "ikkje setosa"], loc="lower right"
)
```

## Oppsummering

