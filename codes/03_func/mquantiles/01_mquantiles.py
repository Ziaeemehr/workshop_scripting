import numpy as np
import pylab as plt
from numpy.random import rand 
from scipy.stats.mstats import mquantiles

prob = [0.025, 0.975]
a = np.random.rand(100, 20)
t = np.linspace(0, 1, len(a))
qs = mquantiles(a, axis=1, prob=prob)
print(t.shape)
print(qs.shape)
# exit(0)
plt.fill_between(t, *qs.T, alpha=0.7, color="#7A68A6")
plt.show()
