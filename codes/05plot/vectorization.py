#1/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer

n = 100000
x = np.linspace(0, 1, n) # n points in [0, 1]
y = np.zeros(n)

def f(x):
    return x*x

# n zeros (float data type)
for i in xrange(n):
    y[i] = f(x[i])

#-----------------------------------------------#
from math import sin
start = timer()
for i in xrange(len(x)):
    y[i] = sin(x[i])
end = timer()
print end - start

start = timer()
for i in xrange(len(x)):
    y[i] =np.sin(x[i])
end = timer()
print end - start


start = timer()
y = np.sin(x)
end = timer()
print end - start

#-----------------------------------------------#
#import timeit
#n = 100000
#x = np.linspace(0, 2*np.pi, n+1)
#y = np.zeros(len(x))

#%timeit for i in xrange(len(x)): \
    #y[i] = np.sin(x[i])*np.exp(-x[i])

#%timeit y = np.sin(x)*np.exp(-x)
#masure the speedup
#-----------------------------------------------#


