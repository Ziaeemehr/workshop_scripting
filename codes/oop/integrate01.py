#!/usr/bin/python

class Trapezoidal:
    """The Trapezoidal rule for integrals on [-1,1]."""
    def __init__(self):
        self.setup()
    def setup(self):
        self.points = (-1, 1)
        self.weights = (1, 1)
    def eval(self, f):
        sum = 0.0
        for i in range(len(self.points)):
            sum += self.weights[i]*f(self.points[i])
        return sum
# usage:
rule = Trapezoidal()
integral = rule.eval(lambda x: x**3)
print integral
