import numpy as np 
import pylab as pl 

rng = np.random.RandomState(10)  # deterministic random data
a = np.hstack((rng.normal(size=10000),
               rng.normal(loc=5, scale=2, size=10000)))

fig, axs = pl.subplots(2, figsize=(10,8))
axs[0].hist(a, bins='auto', normed=True)
axs[0].set_title("Histogram with 'auto' bins")

hist, bins = np.histogram(a, bins='auto', normed=True) # bins=20
width = (bins[1] - bins[0])
center = (bins[:-1] + bins[1:]) / 2
axs[1].bar(center, hist, align='center', width=width)
# print hist
pl.show()
