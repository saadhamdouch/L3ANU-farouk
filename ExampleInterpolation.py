from math import *
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    y = 1/(1+25*x**2)
    return y


def diffdiv(x,y):
    n = len(x)
    D = np.zeros((n,n))
    D[:,0] = y
    for j in range (1,n):
        for i in range (n-j):
            D[i,j] = (D[i+1,j-1]-D[i,j-1])/(x[i+j]-x[i])
    return D


def fastexp(x,D,t):
    n = len(x)
    y = D[0,n-1]*np.ones(len(t))
    for k in range (n-2,-1,-1):
        y = (t-x[k])*y + D[0,k]
    return y


x = np.linspace(-1,1,400)
y = f(x)
plt.plot(x,y, label = "f")

for n in range (1,10):
    X = np.linspace(-1,1,n+1)
    val  = f(X)
    D = diffdiv(X,val)
    yp = fastexp(X,D,x)
    plt.plot(x,yp,'--',label = "n = "+str(n))
plt.legend(loc="best")
plt.title("Polynomes d'interpolation de degre n")
plt.show()
