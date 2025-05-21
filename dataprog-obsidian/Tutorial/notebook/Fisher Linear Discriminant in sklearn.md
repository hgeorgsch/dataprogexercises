---
tags:
  - sklearn
  - pandas
---

# Fisher Linear Discriminant

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

```{code-cell} python3
from sklearn import datasets

iris = datasets.load_iris()

display( iris )
```

### Scatter plot

```{code-cell} python3
import matplotlib.pyplot as plt

_, ax = plt.subplots()
scatter = ax.scatter(iris.data[:, 0], iris.data[:, 1], c=iris.target)
ax.set(xlabel=iris.feature_names[0], ylabel=iris.feature_names[1])
_ = ax.legend(
    scatter.legend_elements()[0], iris.target_names, loc="lower right", title="Classes"
)
```

## Diskriminant

```{code-cell} python3
# Import necessary libraries  
import numpy as np  
import pandas as pd  
import matplotlib.pyplot as plt  
from sklearn.model_selection import train_test_split  
from sklearn.preprocessing import StandardScaler  
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA  
from sklearn.metrics import accuracy_score  
from sklearn.linear_model import LogisticRegression

lda = LinearDiscriminantAnalysis()  
lda_t = lda.fit_transform(X,y)
```

## Referansar

+ Dokumentasjonen for sklearn
	+  [datasets.load_iris](https://scikit-learn.org/1.4/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris "sklearn.datasets.load_iris")
	+ [LinearDiscriminantAnalysis](https://scikit-learn.org/stable/modules/generated/sklearn.discriminant_analysis.LinearDiscriminantAnalysis.html)