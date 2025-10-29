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

rot1 = rot( np.pi/5)
n1 = 20
x1 = np.random.rand(n1,1)*4
y1 = np.random.rand(n1,1)*2
z1 = np.zeros(n1,1)

xy1 = np.hstack( [x1,y1] )*rot1

rot2 = rot( np.pi/7)
n2 = 21
x2 = np.random.rand(n2,1)*3
y2 = np.random.rand(n2,1)*4
z2 = np.ones(n2,1)

xy2 = np.hstack( [x2,y2] )*rot2

xy = np.vstack( [xy1,xy2] )
z = np.vstack( [z1,z2] )

scatter = plt.scatter(xy[:, 0], xy[:, 1], c=z)

ax = plt.gca()
ax.set(xlabel="$x$", ylabel="$y$")

plt.savefig( "eval01.svg" )
