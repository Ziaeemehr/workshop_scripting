from quantities import Hz, s, ms
from elephant.spike_train_generation import homogeneous_poisson_process
import matplotlib.pyplot as plt
import numpy as np
spiketrain_list = [
    homogeneous_poisson_process(rate=10.0*Hz, t_start=0.0*s, t_stop=100.0*s)
    for i in range(100)]
for i, spiketrain in enumerate(spiketrain_list):
    t = spiketrain.rescale(ms)
    plt.plot(t, i * np.ones_like(t), 'k.', markersize=2)
plt.axis('tight')
plt.xlim(0, 10000)
plt.xlabel('Time (ms)', fontsize=16)
plt.ylabel('Spike Train Index', fontsize=16)
plt.gca().tick_params(axis='both', which='major', labelsize=14)
plt.show()