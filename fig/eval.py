from sklearn.datasets import load_diabetes
from sklearn import linear_model
from sklearn import datasets
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis 
import matplotlib.pyplot as plt
import numpy as np

theta1 = np.pi/5

def rotf(theta):
    return np.array( [
        [ np.cos(theta), -np.sin(theta) ],
        [ np.sin(theta), np.cos(theta)  ],
      ] )

def mkset(n,sigma1,sigma2,mu1,mu2,theta):
   rot1 = rotf( theta )
   x1 = (np.random.rand(n,1)+mu1)*sigma1
   y1 = (np.random.rand(n,1)+mu2)*sigma2

   return np.dot( np.hstack( [x1,y1] ), rot1 )

n1 = 20
xy1 = mkset( n1, 4, 2, 0, 0.4, np.pi/5 )
z1 = np.zeros( [n1,1] )

n2 = 21
xy2 = mkset( n2, 3, 4, 0, -0.74, np.pi/7 )
z2 = np.ones( [n2,1] )

xy = np.vstack( [xy1,xy2] )
z = np.vstack( [z1,z2] )

def mklda(xy,z):
   lda = LinearDiscriminantAnalysis()  
   lda.fit(xy,z)

   x, y = lda.coef_.flatten()
   zz, = lda.intercept_
   beta = -zz/y
   alpha = -x/y
   return lambda xx : alpha*xx+beta

f = mklda(xy,z)

xv = [-2, +4]
yv = [ f(xx) for xx in xv ]


scatter = plt.scatter(xy1[:,0], xy1[:,1], color="blue" )
scatter = plt.scatter(xy2[:,0], xy2[:,1], color="red" )

ax = plt.gca()
ax.set(xlabel="$x$", ylabel="$y$")

ax.plot( xv, yv, "g--" )

plt.savefig( "eval01.svg" )
