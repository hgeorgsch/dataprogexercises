---
jupytext:
  formats: md:myst,ipynb
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

# Lineær Diskriminant

Klassifisering er eit standardproblem i statistikk og maskinlæring, som dukkar opp i ei lang rekkje praktiske problem.

I medisinsk biletbehandling kan ein t.d. sjå etter kreftsvulstar på MR-bilete av hjerna. Klassifisering handlar da om å skilja bileta i to klasser, ei med friskt vev og ei med kreftsvulstar.

Eit svært aktuelt problem i finansnæringa er kampen mot kvitvasking, der ein treng å klassifisera transaksjonar i lovlege og ulovlege.

::: {admonition} Definisjon
Eit klassifiseringsproblem ser på ein populasjon av objekt, der kvart objekt har nokre målbare drag (eng. *features*) som me kan observera og kvantifisera, og høyrer til ei klasse (ofte referert til som *label*). For kvart objekt er målet å avgjera kva klasse objektet høyrer til, ved berre å sjå på dei målbare draga. 
:::

I medisinsk biletbehandling kan me t.d. måla fargekvaliteten i kvar einast piksel. I finanstransaksjonar kan me måla tid og stad, avsendar og mottakar, og sjølvsagt beløpet.

Den store pionéren i klassifisering var den britiske statistikaren og biologen Ronald Fisher i mellomkrigstida. Me skal bruka det same datasettet og den same metoden som han brukte, for å illustrera hovudprinsippet for klassifisering. Moderne maskinlæringsalgoritmar gjer i prinsippet akkurat det same, bortsett frå at dei bruker langt fleire variablar; både fleire målbare drag i objekta og fleire fridomsgradar i modellen.

## Fisher sitt datasett

Fisher studerte klassifisering av tre ulike artar av blomen iris. Datasettet som han sette saman er stadig populært for testing av maskinlæringsmodellar. Datasettet omfattar femti eksemplar av kvar iris-art (Iris setosa, Iris virginica og Iris versicolor). Fire målbare drag er registrert for kvart eksemplar: lengd og breidd på beger- og kronblad.

![Iris Versicolor](Iris_versicolor_3.jpg)
Frå [wikimedia commons](https://commons.wikimedia.org/wiki/File:Iris_versicolor_3.jpg) CC-SA-3.0

Me skal bruka scikit-learn, og fordi iris-datasettet er so populært, er det allereie tilgjengeleg i biblioteket. Me kan lasta det slik:

```{code-cell} ipython3
from sklearn import datasets

iris = datasets.load_iris()

display( iris )
```

Datasettet er formattert for `sklearn`, som er forskjellig frå 
det som me er vande med frå `pandas`. 

::: {admonition} Refleksjon
Kva datatype er objektet `iris`?
:::

Mesteparten av datastrukturen er attributten `iris.data` som er ein $150\times4$ *array*.
Det stemmer med tre klasser à 50 eksemplar med fire målbare drag.
Der er òg ein attributt `feature_names`:

```{code-cell} ipython3
print(iris.data.shape)
print(iris.feature_names)
```

Der ser me altso kva søyle som er kva i datasettet.
Me òg vist `iris.data.shape` som er storleiken på `data`-matrisa.
Dernest legg me merke til det som scikit-learn kaller *target*.

```{code-cell} ipython3
print(iris.target.shape)
print(iris.target_names)
```

Her har me altso dei tre iris-artane.  Det som me elles kaller 
«klasse» eller *label* heiter altso *target* i scikit-learn.
Kvart artsnamn er koda som eit heiltal (0,1,2) i `iris.target` som
er ein ein-dimensjonal *array* med eitt element for kvar rekkje i
`iris.data`.

Då har me det som me treng, og me skal ikkje bry oss med resten av
datastrukturen.

### Scatter plot

For å få eit visuelt inntrykk av klassifiseringsproblemet, er det
nyttig med spreidingsplott (*scatter plot*).  Det er synd at me 
berre klarer å plotta to søyler i to dimensjonar, men me får ta
det me kan få.

```{code-cell} ipython3
import matplotlib.pyplot as plt

scatter = plt.scatter(iris.data[:, 0], iris.data[:, 1], c=iris.target)

ax = plt.gca()
ax.set(xlabel=iris.feature_names[0], ylabel=iris.feature_names[1])
ax.legend(
    scatter.legend_elements()[0], iris.target_names, loc="lower right", title="Classes"
)
```

Her plottar me dei to fyrste søylene. 
Legg merke til korleis me bruker klassene (*target*) til å velja
farge på punkta med `c`-argumentet.


::: {admonition} Oppgåve
Kva gjer `ax.set`?  Og kva gjer `ax.legend`?
(Kva skjer om du fjernar dei?
:::

Det fyrste argumentet til `ax.legend` er sikkert vondt å forstå.
Poenget med det er å henta ut fargane som er brukt i `scatter`-plottet,
der `scatter` er variabelen som vart tilordna plottet over.
Det andre argumentet er so lista med namn som skal knyttast til fargane.
Inntil vidare er det nok best ikkje å tenkja på korleis det fyrste 
argumentet er konstruert, og berre bruka det som eit fast mynster.

::: {admonition} Refleksjon
Kva irisart plar ha dei breidaste begerblada? 
Kva art plar ha dei lengste?
:::k

::: {admonition} Oppgåve
Plott ulike par av søyler frå datasettet.
Kva drag er nyttigast for å identifisera kvar irisart?
:::

## Diskriminant

Løysing åt Fisher er kjend som ein *Lineær Disriminant*.
For å kunna visualisera kva denne diskriminanten gjer, skal
me freista ei klassifisering basert berre på dei to måla som
me plotta over, dvs. lengd og breidd på begerblada.

::: {admonition} Merknad
I dag er der eit par forskjellige formlar for å rekna ut lineære diskriminantar.
Om du les [dokumentasjonen](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html), 
vil du sjå at scikit-learn støttar eit par forskjellige metodar. Me skal ikkje gå inn på skilnadene
eller på kva variant Fisher utvikla i si tid.
:::

Diskriminanten skil mellom to klasser, og me har tre.
Difor skal me fyrst skilja mellom *iris setosa* og *ikkje-setosa*
som den andre klassa.  Lat oss fyrst setja opp datasettet, slik:

```{code-cell} ipython3
X = iris.data[:,:2]
print( X.shape )
y = iris.target
print( y.shape )
```

Det er vanleg å bruka $x$ om innvariablane og $y$ om utvariablane.
Her har me altso to innvariablar og éin utvariabel.
Me har derimot tre klasser i $y$, og skulle berre ha to.
Det kan me fiksa slik.

```{code-cell} ipython3
print( y )
y[ y != 0 ] = 1
print( y )
```

Den midste lina er kanskje rar, men me har sett liknande notasjon
med pandas.  Den same notasjonen verkar her, sjølv om dette er numpy
*arrays*. Her set me altso alle $y$-verdiar som ikkje er 0 lik 1.

So er me klare for å laga ein lineær diskriminant.

```{code-cell} ipython3
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis 

lda = LinearDiscriminantAnalysis()  
lda.fit(X,y)
print(lda)
print(lda.coef_)
print(lda.intercept_)
```

Her er det mykje som skjer under panseret. Tilordninga `lda =` instansierer diskriminanten. Den andre lina `lda.fit` tilpassar diskriminanten til datasettet.

+++

::: {admonition} Oppgåve
Lag diskriminantar som skil ut hhv. *iris versicolor* og 
*iris virginica*.  Er alle like enkle å skilja på desse to
variablane?
:::

## Referansar

+ Dokumentasjonen for sklearn
	+  [datasets.load_iris](https://scikit-learn.org/1.4/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
	+ [LinearDiscriminantAnalysis](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html)
