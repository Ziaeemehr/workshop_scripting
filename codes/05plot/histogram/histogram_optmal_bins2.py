import numpy as np 
import pylab as pl 
from elephant.spike_train_generation import homogeneous_poisson_process
from quantities import Hz, s, ms
from sys import exit
def optimum_bin_size(k, delta):
    K = np.mean(k)
    v = np.std(k)
    c = (2*K-v) / (delta * delta)
    return c


Data = np.load('01.npz')
t_isi = Data['t_isi']
print len(t_isi)
# exit(0)
fig, axs = pl.subplots(nrows=1, figsize=(10,5))
# axs[0].hist(a, bins='auto')
# axs[0].set_title("Histogram with 'auto' bins")


nbin = np.arange(100,100000,100)
nb = len(nbin)
cn = np.zeros(nb)
delta = np.zeros(nb)

# for i in range(nb):
#     hist, bins = np.histogram(spiketrains, bins=nbin[i])
#     delta[i] = abs(bins[1]-bins[0])
#     cn[i] = optimum_bin_size(hist, delta[i])

hist, bins = np.histogram(t_isi, bins='auto')  # bins=20
width = (bins[1] - bins[0])
center = (bins[:-1] + bins[1:]) / 2
axs.bar(center, hist, align='center', width=width)

# axs.plot(delta, cn)


axs.set_ylim(0,50)


pl.savefig('optm.png')



pl.show()
