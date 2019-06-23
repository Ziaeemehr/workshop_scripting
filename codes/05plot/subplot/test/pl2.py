import numpy as np
import pylab as pl
import os
import matplotlib.gridspec as gridspec
import matplotlib.image as mpimg

fig = pl.figure(figsize=(8, 10))
outer = gridspec.GridSpec(3, 2, wspace=0.2, hspace=0.2)

for i in range(4):
    inner = gridspec.GridSpecFromSubplotSpec(2, 1,
                                             subplot_spec=outer[i], 
                                             wspace=0.1, 
                                             hspace=0)

    for j in range(2):
        ax = pl.Subplot(fig, inner[j])
        t = ax.text(0.5, 0.5, 'outer=%d, inner=%d' % (i, j))
        t.set_ha('center')
        ax.set_xticks([])
        ax.set_yticks([])
        fig.add_subplot(ax)

for i in range(4, 6):
    inner = gridspec.GridSpecFromSubplotSpec(1, 1,
                                             subplot_spec=outer[i])
    ax = pl.Subplot(fig, inner[0] )
    ax.set_xticks([])
    ax.set_yticks([])
    fig.add_subplot(ax)

pl.show()
