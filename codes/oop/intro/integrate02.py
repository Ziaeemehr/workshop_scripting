#!/usr/bin/python
import math

class Integrate:
    def __init__(self):
        self.setup()

    def setup(self):
        # to be overridden in subclasses:
        self.weights = None
        self.points = None 

    def eval(self, f):
        sum = 0.0
        for i in range(len(self.points)):
            sum += self.weights[i]*f(self.points[i])
        return sum

class Trapezoidal(Integrate):
    def setup(self):
        self.points = (-1, 1)
        self.weights = (1, 1)

class Simpson(Integrate):
    def setup(self):
        self.points = (-1,0,1)
        self.weights= (1/3.,4/3.,1/3.)

class GaussLegendre2(Integrate):
    def setup(self):
        p = 1/math.sqrt(3)
        self.points = (-p, p)
        self.weights = (1, 1)


# usage:
s = Simpson()
v = s.eval(lambda x: math.sin(x)*x)

print v