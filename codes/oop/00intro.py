#!/usr/bin/python

class MyClass:
    '''A simple example class. '''
    i = 12345
    def f(self):
        return 'hello world!'

x = MyClass()

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0,-4.5)
print x.r
print x.i



#'https://docs.python.org/2/tutorial/classes.html'