#! /usr/bin/env python3

from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis 

iris = datasets.load_iris()


scatter = plt.scatter(iris.data[:, 0], iris.data[:, 1], c=iris.target)

ax = plt.gca()
ax.set(xlabel=iris.feature_names[0], ylabel=iris.feature_names[1])
ax.legend(
    scatter.legend_elements()[0], iris.target_names, loc="lower right", title="Classes"
)

plt.savefig( "fisher.svg" )

X = iris.data[:,:2]
y = iris.target
y[ y != 0 ] = 1

lda = LinearDiscriminantAnalysis()  
lda.fit(X,y)


x, y = lda.coef_.flatten()
z, = lda.intercept_
beta = -z/y
alpha = -x/y
def f(xx): return alpha*xx+beta

xv = [4, 8]
yv = [ f(xx) for xx in xv ]
ax.plot( xv, yv, "--" )

plt.savefig( "fishersep.svg" )

