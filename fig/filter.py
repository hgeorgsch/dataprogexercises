#! /usr/bin/env python3

from sklearn.datasets import load_diabetes
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model


diabetes = load_diabetes()

x = diabetes.data[:,6:7]
y = diabetes.target

df = pd.DataFrame( np.hstack( [x,y[:,np.newaxis]] ) )
df.to_csv( "regression.csv" )

ax = plt.subplot()
scatter = ax.scatter( x, y )
ax.set(xlabel="$x$", ylabel="$y$")

plt.savefig( "regdata.svg" )

reg = linear_model.LinearRegression()
reg.fit(x,y)

xv = np.array( [[ -0.09, 0, 0.1, 0.16 ]] ).T
print( xv.shape )
yv = reg.predict(xv)
ax.plot( xv, yv, "r:" )

plt.savefig( "regmodel.svg" )
