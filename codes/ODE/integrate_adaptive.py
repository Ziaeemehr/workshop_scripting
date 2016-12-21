import numpy as np
from scipy.integrate import ode
import matplotlib.pyplot as plt
import warnings


def logistic(t, y, r):
    return r * y * (1.0 - y)

r = .01
t0 = 0
y0 = 1e-5
t1 = 5000.0

#backend = 'vode'
backend = 'dopri5'
#backend = 'dop853'

solver = ode(logistic).set_integrator(backend, nsteps=1)
solver.set_initial_value(y0, t0).set_f_params(r)
# suppress Fortran-printed warning
solver._integrator.iwork[2] = -1

sol = []
warnings.filterwarnings("ignore", category=UserWarning)
while solver.t < t1:
    solver.integrate(t1, step=True)
    sol.append([solver.t, solver.y])
warnings.resetwarnings()
sol = np.array(sol)

plt.plot(sol[:,0], sol[:,1], 'b.-')
plt.show()