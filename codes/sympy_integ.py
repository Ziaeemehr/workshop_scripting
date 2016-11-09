#!/usr/bin/python
from sys import exit
from sympy import *
x = Symbol('x')
print integrate(x**2,x)

print integrate(x**2,(x,0,5))
print integrate(x/(x**2+2*x+1), x)
