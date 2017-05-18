'''
Estimate power spectral density using a periodogram
'''

from scipy import signal
import numpy as np 
import pylab as pl 
'''
Generate a test signal, a 2 Vrms sine wave at 1234 Hz, corrupted by 0.001 V**2/Hz of white noise sampled at 10 kHz.
'''
fs = 10e3
N = 1e5
amp = 2*np.sqrt(2)
freq = 1234.0
noise_power = 0.001 * fs / 2
time = np.arange(N) / fs
x = amp*np.sin(2*np.pi*freq*time)
x += np.random.normal(scale=np.sqrt(noise_power), size=time.shape)
f, Pxx_den = signal.periodogram(x,fs)
print f 
print Pxx_den
pl.semilogy(f, Pxx_den)
pl.ylim([1e-7, 1e2])
pl.xlabel('frequency [Hz]')
pl.ylabel('PSD [V**2/Hz]')
pl.show()