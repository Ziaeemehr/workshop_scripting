#!/usr/bin/python

def yfunc(t,v0=6):
   g = 9.81
   y = v0*t - 0.5 *g*t*t
   dydt = v0 - g*t
   return y, dydt

#sample calls:
print  yfunc(0.1)
print  yfunc(0.1, v0=6)
print  yfunc(t=0.1, v0=6)
print  yfunc(v0=6, t=0.1)
a , b = yfunc(v0=6, t=0.1)
print a
print b
