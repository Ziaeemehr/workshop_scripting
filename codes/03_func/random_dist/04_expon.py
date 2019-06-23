import numpy as np
import pylab as pl
from scipy import stats
from numpy.random import exponential
from sys import exit
np.random.seed(124)


import scipy.stats as stats
import matplotlib.pyplot as plt


N, lower, upper, scale = 1000, -1, 1, 1/0.76
X = stats.truncexpon(b=(upper-lower)/scale, loc=lower, scale=scale)
data = X.rvs(1000)
print type(data)

print len(data[data>0])/float(N)*100

fig, ax = plt.subplots()
ax.hist(data, bins=30, normed=True)
plt.savefig("truncated")

























exit(0)
fig, ax = pl.subplots(1, figsize=(6,6))


l = 0.5
N = 1224
# data = stats.expon.rvs(scale=1.0/l, size=N)
data = exponential(scale=l, size=N)
data = data/np.max(data)*7.0-1.0 
n1 = len(data[(data<1)])
print "num of data : ", n1
condition = (data>0) & (data<1)
n = len(data[condition])
print n, n/(n1+0.0)*100 
print "mean : ", np.mean(data)
print "SD   : ", np.std(data, ddof=1)
ax.hist(data, bins=100, density=True)
ax.set_title("Exponential: $\lambda e^{-\lambda x}, \lambda$ = %.2f" % l)
ax.set_ylabel("P(x)")
ax.set_xlabel("x")
ax.set_xlim(-1,1)
pl.savefig('exp1')
