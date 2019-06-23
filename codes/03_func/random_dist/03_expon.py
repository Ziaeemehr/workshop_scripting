import numpy as np
import pylab as pl
from scipy import stats

np.random.seed(124)

fig, ax = pl.subplots(2, figsize=(10,8))

l = 0.5
x = np.arange(0, 15, 0.1)
y = l*np.exp(-l*x)
ax[0].plot(x, y)
ax[0].set_title("Exponential: $\lambda$ = %.2f" % l)
ax[0].set_xlabel("x")
ax[0].set_ylabel("probability density")

data = stats.expon.rvs(scale=2, size=1000)
print "mean : ", np.mean(data)
print "SD   : ", np.std(data, ddof=1)
ax[1].hist(data, bins=20, normed=True)
# ax[1].set_title("Exponential random variables")
pl.savefig('exp')
