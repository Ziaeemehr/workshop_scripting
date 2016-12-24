#!/usr/bin/python
#http://hplgit.github.io/primer.html/doc/pub/class/._class-readable003.html
class Derivative(object):
    def __init__(self, f, h=1E-5):
        self.f = f
        self.h = float(h)
        
    def __call__(self,x):
        f,h = self.f, self.h
        return (f(x+h)-f(x))/h

from math import sin,cos,pi
df = Derivative(sin)
x = pi
print 'df(x): ',df(x) ,'exact : ', cos(x)

def g(t):
    return t**3
dg = Derivative(g)
t = 1
print 'dg(t): ',dg(t) ,' exact : ', 3

#Verification

def test_Derivative():
    # The formula is exact for linear functions, regardless of h
    f = lambda x: a*x + b
    a = 3.5; b = 8
    dfdx = Derivative(f, h=0.5)
    diff = abs(dfdx(4.5) - a)
    assert diff < 1E-14, 'bug in class Derivative, diff=%s' % diff

test_Derivative()