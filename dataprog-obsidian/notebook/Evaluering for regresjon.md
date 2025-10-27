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

Dette ser me tydleg i meiningsmålingar.
Ofte er der fleire byrå ute og gjer meiningsmålingar på same tid,
og dei bruker dei same statistiske metodane.
Likevel får dei forskjellige resultat, og
dei treff sjelden valresultatet presist.

Regresjonsmodellen som me fann i 
[forrige øving](Linear%20Regression%20in%20SciKitLearn)
gjev ei optimal skildring av datasettet som det er trent på.
Det som er interessant er derimot kor godt det skildrar resten
av populasjonen og kor godt det kan predikera nye og hittil ukjende
data.  Det finn me berre ut ved å testa.  På uavhengige data.

Her skal me gå gjennom eit enkelt og standardisert testlaup,
der me evaluerer modellen som me fann i den førre øvinga.

## Datasettet

Lat oss fyrst lasta datasettet på same måte som sist.  Me 
importerer òg dei same biblioteka som me brukte sist.

```{code-cell} ipython3
from sklearn.datasets import load_diabetes
from sklearn import linear_model
import matplotlib.pyplot as plt
import numpy as np

diabetes = load_diabetes()
x = diabetes.data[:,2:3]
y = diabetes.target
print(x)
print(y)
```

Me har ikkje fleire data enn det eine settet.  For å kunne evaluera
modellen må me difor halda tilbake ein del av datasettet til å testa
på.  Dette testsettet kan me ikkje bruka i treninga.
Ein vanleg tommelfingerregel er å bruka 20% av datasettet til testing
og 80% til trening.

::: {admonition} Merknad
Dette er ein tommelfingerregel.
Dersom du er kjend med estimering og hypotesetesting frå statistikk, 
so kan du kanskje rekna ut kor
mange datapunkt du treng i testsettet for å få eit statistisk
signifikant resultat. Det er naudsynt for å kunna vita kor mykje
me kan stola på modellen, men her skal me nøya oss med tommelfingerregelen.
:::

::: {admonition} Merknad
Der større testsett gjev ein meir påliteleg evaluering, vil større 
treningssett gje ein betre modell.  Det er eit dilemma.
:::

Me hadde 242 objekt i datasettet.  Eit testsett på 20% vert då
om lag 49 objekt, med 193 til treningssettet.

```{code-cell} ipython3
trainx = x[:193]
trainy = y[:193]
testx = x[193:]
testy = y[193:]
```

## Trening av diskriminanten

Me kan trena modellen som før.

```{code-cell} ipython3
reg = linear_model.LinearRegression()
reg.fit(trainx,trainy)
```

::: {admonition} Oppgåve
Visualiser treningssettet og prediksjonsmodellen (regresjonslinen).
Vert det svært forskjellig frå visualiseringa i forrige oppgåve,
då du trente på heile datasettet?
:::

Me kan òg sjekka nøyaktig kor mykje feil modellen gjer på treningssettet.

```{code-cell} ipython3
pred = reg.predict( trainx )
error = pred - trainy
print( error )
```

Legg merke til at me kan køyra prediksjonen på heile datasettet i eitt kall.

::: {admonition} Refleksjon
Kva skjer her?  Kva representerer `error`?  Kva verdi svarer til feil og kva til
rett prediksjon?
:::

Me kan plotta eit histogram over alle `error`-verdiane.

```{code-cell} ipython3
plt.hist(error, bins=15, range=[-200, 200])
plt.show()
```

::: {admonition} Refleksjon
Kva fortel histogrammet oss?
:::

Objektet `error` er ein `numpy` *array*, med alle dei metodane som 
`numpy` gjev oss.  Det er dermed enkelt å finna gjennomsnittleg feil.

```{code-cell} ipython3
print( "Gjennomsnittsfeil:", error.mean() )
print( "Minimum:", error.min() )
print( "Maksimum:", error.max() )
```

## Testing

Me kan gjera akkurat den same testen med testsettet,
som med treningssettet.

```{code-cell} ipython3
testpred = reg.predict( testx )
testerror = testpred - testy
print( testerror )
```

::: {admonition} Oppgåve
Lag eit histogram av `testerror`.

Kan du visa feila på test- og treningsettet i same figur?
:::

::: {admonition} Refleksjon
Samanlikna feila på test- og treningssettet?
Gjer denne modellen det like godt på det nye testsettet som det
gjorde på treningssettet?
:::

## Oppsummering

Læringsmålet i denne øvinga var å sjå korleis syntaksen
i python kan sjå ut når me skal testa ein regresjonsmodell 
i python.

Denne testinga er uhyre viktig.
Det skjer ofte at ein modell fungerer godt på treningssettet og
dårleg på testsettet.

Difor skal de ta med dykk desse teknikkane og prøva dei ut på større
og meir interessante datasett.

```{code-cell} ipython3

```

```{code-cell} ipython3

```

```{code-cell} ipython3

```
