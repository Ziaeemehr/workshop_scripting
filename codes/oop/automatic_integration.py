#!/usr/bin/python
#http://hplgit.github.io/primer.html/doc/pub/class/._class-readable003.html

class Integral(object):
    def __init__(self, f, a, n=100):
        self.f, self.a, self.n, = f, a, n
    
    def __call__(self,x):
        return trapezoidal(self.f, self.a, x, self.n)
    
def trapezoidal(f,a,x,n):
    h = (x-a)/float(n)
    I = 0.5 * f(a)
    for i in range(1,n):
        I += f(a + i*n)
    I += 0.5*f(x)
    I *= h
    return I

def f(x):
    return exp(-x**2)*sin(10*x)

from math import sin,pi

G = Integral(sin,0,200)
value = G(2*pi)
print value
#or
print trapezoidal(sin, 0, 2*pi, 200)



#Verification via symbolic computing 
import sympy as sp
x = sp.Symbol('x')
f_expr = sp.cos(x) + 5*x
print f_expr
F_expr = sp.integrate(f_expr,x)
print F_expr
F = sp.lambdify([x],F_expr) # turn f_expr to F(x) func.
print F(0), F(1)