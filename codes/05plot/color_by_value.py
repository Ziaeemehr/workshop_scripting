import numpy as np
import matplotlib.pylab as pl

x = np.linspace(0, 2*np.pi, 64)
y = np.cos(x)

pl.figure()
pl.plot(x, y)

n = 20
colors = pl.cm.brg(np.linspace(0, 1, n))

for i in range(n):
    pl.plot(x, i*y, color=colors[i])

pl.show()
