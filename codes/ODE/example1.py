#!/usr/bin/python
'''
x'' + b * x' + C * sin(t)=0
'''
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import numpy as np

def pend(y, t, b, c=5.0):
    theta, omega = y
    dydt = [omega, -b*omega - c*np.sin(theta)]
    return dydt

b = 0.25
#c = 5.0
t = np.linspace(0, 40, 401)
y0 = [np.pi - 0.1, 0.0]
sol = odeint(pend, y0, t, args=(b,))
plt.plot(t, sol[:, 0], 'b', label='theta(t)')
plt.plot(t, sol[:, 1], 'g', label='omega(t)')
plt.legend(frameon=False, loc='best')
plt.xlabel('t')
plt.grid()
plt.show()
