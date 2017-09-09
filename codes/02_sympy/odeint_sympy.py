


from scipy.integrate import odeint
from sys import exit
from sympy import *

t = Symbol('t')
x = Function('x')(t)
y = Function('y')(t)
z = Function('z')(t)

exit(0)
# x = sympy.Symbol('x')
# y = sympy.Symbol('y')
# t = sympy.Symbol('t')

# dx/dt = 0.0387*x - 0.0005*x*y
# dy/dt = 0.0036*x*y - 0.1898*y

# def dX_dt(X, t):
#     vals = dict(x=X[0], y=X[1], t=t)
#     return [eq.evalf(subs=vals) for eq in systemOfEquations]


# odeint(dX_dt, [1,2], np.linspace(0, 1, 5))