---
tags:
  - sklearn
  - pandas
---



```{code-cell} python3
from sklearn import linear_model
reg = linear_model.LinearRegression()
reg.fit([[0, 0], [1, 1], [2, 2]], [0, 1, 2])
reg.coef_
```

+ [Medium post](https://medium.com/@heyamit10/how-to-perform-linear-regression-using-pandas-scikit-learn-9fcfa6085fb0)

