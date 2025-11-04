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
   x1 = (np.random.randn(n,1)+mu1)*sigma1
   y1 = (np.random.randn(n,1)+mu2)*sigma2

   r = np.dot( np.hstack( [x1,y1] ), rot1 )
   return r

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

def plotLDA(f,rng=(-20,+20),ax=None):
   xv = list(rng)
   yv = [ f(xx) for xx in xv ]

   if ax is None:
      ax = plt.gca()
   ax.set(xlabel="$x$", ylabel="$y$")
   ax.plot( xv, yv, "g--" )

n1 = 20
xy1a = mkset( n1, 5, 3.5, 0, 4.4, np.pi/5 )
z1a = np.zeros( [n1,1] )

n2 = 21
xy1b = mkset( n2, 4, 6.2, 0, -2.74, np.pi/7 )
z1b = np.ones( [n2,1] )


f = mklda( [xy1a,xy1b], [z1a,z1b] )

plt.figure()
scatter = plt.scatter(xy1a[:,0], xy1a[:,1], color="blue" )
scatter = plt.scatter(xy1b[:,0], xy1b[:,1], color="red" )
plotLDA(f)
plt.savefig( "eval01.svg" )

n2a = 312
n2b = 391
xy2a0 = mkset( n2a, 5, 3.5, 0, 4.4, np.pi/5 )
xy2b0 = mkset( n2b, 4, 6.2, 0, -2.74, np.pi/7 )
xy2a = np.vstack( [ xy2a0, xy1a ] )
xy2b = np.vstack( [ xy2b0, xy1b ] )
z2a0 = np.zeros( [n2a,1] )
z2b0 = np.ones( [n2b,1] )
z2a = np.vstack( [z2a0,z1a] )
z2b = np.vstack( [z2b0,z1b] )

plt.figure()
scatter = plt.scatter(xy2a[:,0], xy2a[:,1], color="blue" )
scatter = plt.scatter(xy2b[:,0], xy2b[:,1], color="red" )
plotLDA(f)
plt.savefig( "eval02.svg" )

plt.figure()
scatter = plt.scatter(xy2a[:,0], xy2a[:,1], color="blue" )
scatter = plt.scatter(xy2b[:,0], xy2b[:,1], color="red" )
f2 = mklda( [xy2a,xy2b], [z2a,z2b] )
plotLDA(f2)
plt.savefig( "eval02bis.svg" )

n3a = 325
n3b = 281
xy3a0 = mkset( n3a, 9, 3.5, 0, 2.4, 0 )
xy3b0 = mkset( n3b, 5, 2, -1, -1.24, 0 )
xy3a = np.vstack( [ xy3a0, xy1a ] )
xy3b = np.vstack( [ xy3b0, xy1b ] )
z3a0 = np.zeros( [n3a,1] )
z3b0 = np.ones( [n3b,1] )
z3a = np.vstack( [z3a0,z1a] )
z3b = np.vstack( [z3b0,z1b] )

plt.figure()
scatter = plt.scatter(xy3a[:,0], xy3a[:,1], color="blue" )
scatter = plt.scatter(xy3b[:,0], xy3b[:,1], color="red" )
plotLDA(f)
plt.savefig( "eval03.svg" )
