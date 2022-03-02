import numba
import numpy as np
import pylab as plt
from time import time
from numba import jit


def euler(x0, t, dt, derivative, par):
    x0 += dt * derivative(x0, t, par)
    return x0


def BogackiShampine(x0, t, dt, derivative, par):

    k1 = derivative(x0, t, par)
    k2 = derivative(x0 + 0.5 * dt * k1, t + 0.5 * dt, par)
    k3 = derivative(x0 + 0.75 * dt * k2, t + 0.75 * dt, par)
    x0 += dt / 9.0 * (2.0 * k1 + 3.0 * k2 + 4.0 * k3)

    return x0


# @jit(nopython=True)
def ho(x0, t, p):
    x, y = x0
    a, b = p
    xp = x - x * y - a * x * x
    yp = x * y - y - b * y * y
    return np.asarray([xp, yp])


def integrate(nstep, x0, par, integrator, derivative):

    sol = np.zeros((nstep, 2))
    sol[0, :] = x0
    for i in range(1, nstep):
        x0 = integrator(x0, i * dt, dt, derivative, par)
        sol[i, :] = x0

    return sol


param = np.array([0.001, 0.05])
dt = 0.01
tfinal = 3000
nstep = int(tfinal / dt)
x0 = np.array([0.1, 0.5])

ho = numba.jit(ho, nopython=True)

start = time()
# sol = integrate(nstep, x0, param, euler, ho)
sol = integrate(nstep, x0, param, BogackiShampine, ho)

print("Done in {:10.4f} seconds".format(time() - start))
print(sol.shape)

plt.plot(sol[:, 0])
plt.show()
