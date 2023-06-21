# https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.hilbert.html
# https: // www.gaussianwaves.com/2017/04/extracting-instantaneous-amplitude-phase-frequency-hilbert-transform/
import numpy as np 
import pylab as plt 
from scipy.signal import hilbert, chirp

duration = 1.0 
fs = 400.0
samples = int(fs*duration)
t = np.arange(samples)/fs

signal = chirp(t, 20.0, t[-1], 100.0)
signal *= (1.0 + 0.5 * np.sin(2.0*np.pi*3.0*t))

# The amplitude envelope is given by magnitude of the analytic signal.
analytic_signal = hilbert(signal)
amplitude_envelope = np.abs(analytic_signal)

instantaneous_phase = np.unwrap(np.angle(analytic_signal))
instantaneous_frequency = (np.diff(instantaneous_phase) /
                           (2.0*np.pi) * fs)

fig = plt.figure(figsize=(10,8))
ax0 = fig.add_subplot(311)
ax0.plot(t, signal, label='signal')
ax0.plot(t, amplitude_envelope, label='envelope')
ax0.set_xlabel("time in seconds")
ax0.legend()
ax1 = fig.add_subplot(312)
ax1.plot(t[1:], instantaneous_frequency, label='frequency')
ax1.set_ylim(0.0, 120.0)
ax1.legend()

ax2 = fig.add_subplot(313)
ax2.plot(t, instantaneous_phase, label='instantaneous phase')
ax2.set_xlabel("time in seconds")
ax2.legend()
plt.tight_layout()

plt.show()
