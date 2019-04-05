import numpy as np 
import pylab as pl 
from elephant.spike_train_generation import homogeneous_poisson_process
from quantities import Hz, s, ms
def optimum_bin_size(k, delta):
    K = np.mean(k)
    v = np.std(k)
    c = (2*K-v) / (delta * delta)
    return c


# rng = np.random.RandomState(10)  # deterministic random data
# a = np.hstack((rng.normal(size=10000),
#                rng.normal(loc=5, scale=2, size=10000)))
spiketrain_list = [homogeneous_poisson_process(rate=10.0*Hz, t_start=0.0*s,
t_stop=10.0*s ) for i in range(100)]
spiketrains = []
for i, spiketrain in enumerate(spiketrain_list):
    t = spiketrain.rescale(ms)
    spiketrains.extend(t)

fig, axs = pl.subplots(nrows=1, figsize=(10,5))
# axs[0].hist(a, bins='auto')
# axs[0].set_title("Histogram with 'auto' bins")


nbin = np.arange(100,100000,100)
nb = len(nbin)
cn = np.zeros(nb)
delta = np.zeros(nb)

for i in range(nb):
    hist, bins = np.histogram(spiketrains, bins=nbin[i])
    delta[i] = abs(bins[1]-bins[0])
    cn[i] = optimum_bin_size(hist, delta[i])

# hist, bins = np.histogram(a, bins='auto')  # bins=20
# width = (bins[1] - bins[0])
# center = (bins[:-1] + bins[1:]) / 2
# axs[0].bar(center, hist, align='center', width=width)

axs.plot(delta, cn)





pl.savefig('optm.png')



pl.show()
