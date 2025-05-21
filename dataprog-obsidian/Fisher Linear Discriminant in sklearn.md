---
tags:
  - sklearn
  - pandas
---

# Fisher Linear Discriminant

Klassifisering er eit standardproblem i statistikk og maskinlæring.



## Fisher sitt datasett

```{code-cell} python3
from sklearn import datasets

iris = datasets.load_iris()
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