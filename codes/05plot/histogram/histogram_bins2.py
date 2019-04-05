import numpy as np 
import pylab as pl 

rng = np.random.RandomState(10)  # deterministic random data
# a = np.hstack((rng.normal(size=10000),
#                rng.normal(loc=5, scale=2, size=10000)))

a = np.load('01.npz')['t_isi']

fig, axs = pl.subplots(nrows=2, ncols=4, figsize=(20,8))
axs[0,0].hist(a, bins='auto')
axs[0,0].set_title("Histogram with 'auto' bins")

axs[0,1].hist(a, bins='fd')
axs[0,1].set_title("Histogram with 'fd' bins")

axs[0,2].hist(a, bins='doane')
axs[0,2].set_title("Histogram with 'doane' bins")

axs[0,3].hist(a, bins='scott')
axs[0,3].set_title("Histogram with 'scott' bins")

axs[1,0].hist(a, bins='rice')
axs[1,0].set_title("Histogram with 'rice' bins")

axs[1, 1].hist(a, bins='sturges')
axs[1, 1].set_title("Histogram with 'sturges' bins")

axs[1, 2].hist(a, bins='sqrt')
axs[1, 2].set_title("Histogram with 'sqrt' bins")
axs[1, 3].set_axis_off()

for i in range(2):
    for j in range(4):
        axs[i,j].set_ylim(0, 50)

pl.savefig('bins2.png')



# pl.show()
