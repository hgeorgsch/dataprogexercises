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

def mklda(xy,z):
    xy = np.vstack( xy )
    z = np.vstack( z )

    lda = LinearDiscriminantAnalysis()  
    lda.fit(xy,z.flatten())

    x, y = lda.coef_.flatten()
    zz, = lda.intercept_
    beta = -zz/y
    alpha = -x/y
    return lambda xx : alpha*xx+beta

def plotLDA(f,rng=(-2,+4),ax=None):
   xv = list(rng)
   yv = [ f(xx) for xx in xv ]

   if ax is None:
      ax = plt.gca()
   ax.set(xlabel="$x$", ylabel="$y$")
   ax.plot( xv, yv, "g--" )

n1 = 20
xy1 = mkset( n1, 4, 2, 0, 0.4, np.pi/5 )
z1 = np.zeros( [n1,1] )

n2 = 21
xy2 = mkset( n2, 3, 4, 0, -0.74, np.pi/7 )
z2 = np.ones( [n2,1] )


f = mklda( [xy1,xy2], [z1,z2] )

plt.figure()
scatter = plt.scatter(xy1[:,0], xy1[:,1], color="blue" )
scatter = plt.scatter(xy2[:,0], xy2[:,1], color="red" )
plotLDA(f,(-2,+4))
plt.savefig( "eval01.svg" )


n2a = 2000
xy2a = mkset( n2a, 4, 2, 0, 0.4, np.pi/5 )
z2a = np.zeros( [n2a,1] )

n2b = 2189
xy2b = mkset( n2b, 3, 4, 0, -0.74, np.pi/7 )
z2b = np.ones( [n2b,1] )

plt.figure()
scatter = plt.scatter(xy2a[:,0], xy2a[:,1], color="blue" )
scatter = plt.scatter(xy2b[:,0], xy2b[:,1], color="red" )
plotLDA(f,(-2,+4))
plt.savefig( "eval02.svg" )

plt.figure()
scatter = plt.scatter(xy2a[:,0], xy2a[:,1], color="blue" )
scatter = plt.scatter(xy2b[:,0], xy2b[:,1], color="red" )
f2 = mklda( [xy2a,xy2b], [z2a,z2b] )
plotLDA(f2,(-2,+4))
plt.savefig( "eval02bis.svg" )
