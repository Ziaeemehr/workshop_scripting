from scipy.fftpack import fft
from scipy import signal
import numpy as np
import pylab as pl

t = np.linspace(0,10,101)
y1 = np.sin(t)
y2 = np.cos(t)
# y2n = np.diff(y1)
y2n = np.gradient(y1)
y2n = y2n/np.max(y2n)
print y2n-y2
pl.plot(t,y1,label='y1')
pl.plot(t,y2,label='y2')
pl.plot(t,y2n,label='y2n')
pl.legend()
pl.show()
