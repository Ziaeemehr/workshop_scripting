import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import numpy as np

fig, ax = plt.subplots()
im = ax.imshow(np.arange(100).reshape((10, 10)))

cax = inset_axes(ax, "100%", "100%", bbox_to_anchor=[0.78, 0.5, 0.03, 0.38],
                 bbox_transform=ax.transAxes, borderpad=0)
cb = fig.colorbar(im, cax=cax)
plt.savefig('f2')
