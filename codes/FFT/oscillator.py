#!/usr/bin/env python

#sample point is crucial to determine the frequency
# the higher frequencies, the more sample point is needed
# min dt is 0.005 for 50 Hz

import numpy as np 
import pylab as pl 
from scipy.integrate import odeint
from scipy.fftpack import fft

def osc(ic, t, omega):
    x = ic
    dydt = [0,0]
    dydt[0] = omega[0]+ np.sin(x[1]-x[0])
    dydt[1] = omega[1]+ np.sin(x[0]-x[1])
    return dydt

def find_frequencies(x,y):
    N = len(x)
    dt0 = x[2]-x[1]
    xf = np.linspace(0.0, 1.0/(2.0*dt0), N/2)
    yf = fft(y)
    yfplot = 2.0/N * np.abs(yf[0:N//2])
    return xf, yfplot
    
N = 8001 # sampling points
t = np.linspace(0, 40, N)
y0 = [1.0,0.5]
nu =np.array([50.1,57.3])
omega = 2.0*np.pi*nu 
sol = odeint(osc, y0, t, args=(omega,))

for i in range(2):
    a,b = find_frequencies(t,np.cos(sol[:,i]))
    pl.plot(a,b)

pl.show()





