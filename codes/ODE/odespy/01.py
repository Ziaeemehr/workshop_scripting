import numpy as np 
import odespy 
import pylab as pl


class Logistic:
    def __init__(self, a, R, A):
        self.a = a
        self.R = R
        self.A = A 
    def f(self, u, t):
        a, R = self.a, self.R 
        return a*u*(1-u/R)
    def u_exact(self,t):
        a, R, A = self.a, self.R, self.A 
        return R*A*np.exp(a*t)/(R + A*(np.exp(a*t)-1))
        
problem = Logistic(a=2, R=1e5, A=1)
solver = odespy.RK4(problem.f)
solver.set_initial_condition(problem.A)

T = 10
N = 30 
time_points = np.linspace(0,T,N+1)
u, t = solver.solve(time_points)

pl.plot(t, u, 'r-',
     t, problem.u_exact(t), 'bo')
# pl.savefig('tmppng'); savefig('tmp.pdf')
pl.show()