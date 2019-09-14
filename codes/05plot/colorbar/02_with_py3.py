# with python3
import numpy as np
import matplotlib.pyplot as plt
fig, axs = plt.subplots(nrows=1, ncols=2)


fig, ax = plt.subplots(nrows=1, ncols=2)
for i in range(2):
    im = ax[i].imshow(np.arange(100).reshape((10, 10)))
    cax = ax[i].inset_axes([1, 0.8, 0.03, 0.2])
    cb = fig.colorbar(im, cax=cax)

plt.savefig("f3")
# plt.show()
