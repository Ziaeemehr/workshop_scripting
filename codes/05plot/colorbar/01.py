import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

fig = plt.figure()
ax = plt.subplot(111)
im = ax.imshow(np.arange(100).reshape((10, 10)))

c = plt.colorbar(im, cax=fig.add_axes([0.78, 0.5, 0.03, 0.38]))
pl.show()
