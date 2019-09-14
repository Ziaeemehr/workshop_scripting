# http://blog.originlab.com/graphing/visualizing-the-negative-log


import numpy as np
import pylab as pl

# x = [-10000, -1000, -100, -10, 0, 10, 100, 1000, 10000]
x = [-10000, -1000, -100, -10, -0.5, 0, 0.5, 10, 100, 1000, 10000]


# log modulus transform
x_log_modulus_transform = np.sign(x)*(np.log10(np.abs(x)+1))

f, ax = pl.subplots(2, sharex=True)
ax[0].plot(x, 'o')

ax[0].margins(x=0.12, y=0.2)

ax[1].plot(x_log_modulus_transform, '--o')

ax[1].margins(x=0.12, y=0.2)
ax[0].set_ylabel('x')
ax[1].set_ylabel('sign(x)*(log(|x|+1))')
pl.show()
