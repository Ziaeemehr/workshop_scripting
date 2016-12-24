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
        
    def eval(self, f):
        sum = 0.0
        for i in range(len(self.points)):
            sum += self.weights[i]*f(self.points[i])
        return sum

s = Trapezoidal()
v = s.eval(lambda x: 2.0 + math.sin(2.0 * math.sqrt(x)))

print v











class TransFunc:
    def __init__(self, f, h):
        self.f = f;  self.h = h

    def coor_mapping(self, xi):
        """Map local xi in (-1,1) in interval j to global x."""
        return (self.j-0.5)*self.h + 0.5*self.h*xi

    def __call__(self, xi):
        x = self.coor_mapping(xi)
        return self.f(x)
        

def integrate(integrator, a, b, f, n):
    # integrator is an instance of a subclass of Integrator
    sum = 0.0
    h = (b-a)/float(n)
    g = TransFunc(f, h)
    for j in range(1, n+1):
        g.j = j
        sum += integrator.eval(g)
    return 0.5*h*sum        