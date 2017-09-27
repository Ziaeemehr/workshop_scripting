"""
A. Ziaeemehr 25.09.2017

interpolate a polynomial with the Lagrange method
order 1 uses linear interpolation through 2 points 
order 2 uses quadratic interpolation through 3 points
"""


import numpy as np 
import pylab as pl 
from math import sin, pi
from sys import exit
from time import time

def interp(X, Y, x, order):

    global n0
    
    if x>max(X) or x< min(X):
        print "data out of interval [X_min, X_max]" 
        print x , "[",min(X), max(X), "]"
        exit(0)

    N = len(X)

    ''' find left end of interval for interpolation '''
    while(X[n0+1] < x):
        n0+=1;
    while(X[n0] > x):
        n0-=1;
        
    #if x >= X[N-2]:
        #n0 = N-2
    #else:
        #while x>X[n0+1]:
            #n0 = n0 + 1
    
    '''linear interpolation'''
    if order == 1:
        xp = []
        yp = []

        for i in range(order+1):
            xp.append(X[n0+i]); yp.append(Y[n0+i])
        dydx = (yp[1]-yp[0])/float(xp[1]-xp[0])

        return yp[0]+dydx*(x-xp[0])
    
    ''' quadratic interpolation '''
    if order == 2:
        xp = []
        yp = []

        if n0 < (N-2):
            for i in range(3):
                xp.append(X[n0+i]); yp.append(Y[n0+i])
        else:
            for i in range(3):
                xp.append(X[n0-1+i]); yp.append(Y[n0-1+i])

        L = []
        for k in range(3):
            term_N = 1; term_D = 1
            for j in range(3):
                if j!=k :
                    term_N *= (x - xp[j])
                    term_D *= (xp[k]- xp[j])
            L.append(term_N / term_D)

        return sum(L[i]*yp[i] for i in range(3))


start = time()

X = np.arange(0,2*pi,0.1)
Y = [sin(i) for i in X]
x  = np.arange(0,np.max(X)+0.05,0.05)

print "max X:", max(X), "max x:", max(x)

y  = []
n0 = 0
for i in range(len(x)):
    y.append( interp(X, Y, x[i], 2))
y_exact = np.sin(x)
y = np.array(y)
print np.max(abs(y_exact-y))
print len(y_exact), len(y)
print time()-start , "seconds"

pl.plot(X,Y,"ko",label="XY")
pl.plot(x,y,marker=">",markersize=5,label="xy")
pl.plot(x,y_exact,label=r"$\sin(x)$")
pl.legend()
pl.show()
