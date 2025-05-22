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

::: {admonition}
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

```{code-cell} ipython3
lda = LinearDiscriminantAnalysis()  
lda.fit(trening,trenningtarget)
print(lda.coef_)
print(lda.intercept_)
```


```{code-cell} ipython3
scatter = plt.scatter(iris.data[:, 0], iris.data[:, 1], c=iris.target)

ax = plt.gca()
ax.set(xlabel=iris.feature_names[0], ylabel=iris.feature_names[1])
ax.legend(
    scatter.legend_elements()[0], iris.target_names, loc="lower right", title="Classes"
)
```



## Visualisering av diskriminanten

Diskriminanten definerer ei line som freistar å skilja dei to klassene frå kvarande.
Før me går inn på bruk av modellen, skal me visualisera han, slik at me veit kva me arbeider med.
Koden under vil vera kryptisk for dei som ikkje har lese ein del matematikk og spesielt lineær algebra,
og det er ikkje viktig å forstå alt. 

Lat oss kalla dei vektene for $x$ og $y$ og konstantleddet for $z$.

```{code-cell} ipython3
x, y = lda.coef_.flatten()
z, = lda.intercept_
print( x, y, z )
```

Du hugsar kanskje at ei rak line kan skrivast som ei likning eller funksjon $y=\alpha x + \beta$ eller $f(x)=\alpha x+\beta$.
For diskriminanten er denne lina gitt slik at
$\alpha = - x/y$
og
$\beta = -z/y$, eller i kode som:

```{code-cell} ipython3
beta = -z/y
alpha = -x/y
def f(xx): return alpha*xx+beta
```

Denne lina kan me bruka til å plotta diskriminanten.  Me må gjenta koden for å plotta spreidingsplottet, og kan då skriva,

```{code-cell} ipython3
ax = plt.subplot()
scatter = ax.scatter(iris.data[:, 0], iris.data[:, 1], c=iris.target)
ax.set(xlabel=iris.feature_names[0], ylabel=iris.feature_names[1])
ax.legend(
    scatter.legend_elements()[0], ["setosa", "ikkje setosa"], loc="lower right"
)

xv = [4, 8]
yv = [ f(xx) for xx in xv ]
ax.plot( xv, yv, "--" )

ax.quiver( 5.6, f(5.6), x, y, scale=10, width=2**(-8) )
```

Som me ser klarer diskriminanten stort sett å skilja iris setosa frå
dei to andre artane.  Der er berre nokre få atypiske eksemplar som
vert feilklassifiserte.

Den svarte pilen er plotta med `quiver`-funksjonen. Han viser normalvektoren på diskriminantlina, dvs. ei vektor som står vinkelrett på skiljelina.
Denne vektoren har koordinatar `(x,y)`, dvs. `lda.coef_`.

::: {admonition} Merknad
Om du har eit punkt $(x',y')$ og normalvektoren er $(x,y)$, vil dot-produktet $(x,y)\cdot(x',y')=xx'+yy'$ vera negativ på den eine sida av determinantlina og positiv på den andre. På lina er produktet null. Dess lenger frå lina punktet $(x',y')$ er, dess større er absoluttverdien. Det er altso dette produktet modellen bruker for å predikera klassa for eit nytt objekt $(x',y')$.
:::


::: {admonition} Oppgåve
Lag diskriminantar som skil ut hhv. *iris versicolor* og 
*iris virginica*.  Er alle like enkle å skilja på desse to
variablane?
:::

## Prediksjon vha modellen

Lat oss billa oss inn at me har målt tre blomar, og målt begerblada.
Me skriv kvar blome som ei liste med [*lengd*, *breidd*].

```{code-cell} ipython3
x1 = np.array([[ 4.4, 3.5 ]])
x2 = np.array([[ 4.8, 2.5 ]])
x3 = np.array([[ 7.5, 2.6 ]])
```

No kan me sjekka kva modellen meiner om desse blomane.

```{code-cell} ipython3
for x in [ x1, x2, x3 ]:
   print( f"{x} -> {lda.predict(x)}" )
```

::: {admonition}
Kva gjer koden min over?
Kva tyder tala over?
:::

Me skal sjå at modellen predikerer setosa (0) for den fyrste, og ikkje for dei to andre.

Lat oss sjå korleis det ser ut i spreidingsplottet òg.
Me legg til dei tre nye blomane med kross i plottet for å skilja dei
frå treningssettet, slik:

```{code-cell} ipython3
ax = plt.subplot()
scatter = ax.scatter(iris.data[:, 0], iris.data[:, 1], c=iris.target)
ax.set(xlabel=iris.feature_names[0], ylabel=iris.feature_names[1])
ax.legend(
    scatter.legend_elements()[0], ["setosa", "ikkje setosa"], loc="lower right"
)

xn = [ x[0,0] for x in [ x1, x2, x3 ] ]
yn = [ x[0,1] for x in [ x1, x2, x3 ] ]
ax.plot( xn, yn, "x" )
```

## Oppsummering

Det me har vist her er ikkje berre ein metode som var hipp og kul på
1930-talet og for lengst forelda.
Me har vist hovudprinsippet for mange moderne maskinlæringsmetodar òg.
Den store skilnaden er at den lineære modellen berre har to vekter,
eller generelt éi vekt per *input*-variabel.
Djupe nevrale nettverk kan ha mange milliardar vekter.  Dei er heller
ikkje lineære.
Når djupe nevrale nettverk vert brukte til klassifisering, definerer
dei ei ikkje-lineær hyperflate som skiljer to klasser.

Der er to viktige ting som me ikkje har vist her:
+ Lineær diskriminant med meir enn to *inputs*.
+ Evaluering av modellen.
Dette skal me koma tilbake til.

+ Meir dokumentasjonen på klearn
    +  [datasets.load_iris](https://scikit-learn.org/1.4/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
    + [LinearDiscriminantAnalysis](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html)
