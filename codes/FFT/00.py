
'''
Fourier Transforms 
'''


from scipy.fftpack import fft, ifft
import numpy as np 
import pylab as pl

# One dimensional discrete Fourier transforms
x =  np.array([1.0, 2.0, 1.0, -1.0, 1.5])
y = fft(x)
# print y
yinv = ifft(y)
# print yinv 
# print np.sum(x)

# The example plots the FFT of the sum of two sines.
N = 600         # Number of sample points
T = 1.0/800.0   # sample spacing
x = np.linspace(0.0,N*T,N)
print N*T
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
yf = fft(y)
xf = np.linspace(0.0,1./(2.0*T),N//2)
pl.plot(xf,2.0/N*np.abs(yf[0:N//2]))
pl.grid()
pl.show()
