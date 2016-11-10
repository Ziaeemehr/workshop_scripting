from numpy import *

def f(a,b):
    #print  a+b
    return a*a, b*b

x1 = 2
x2 = 5
r1,r2 = f(x1,x2)
print r1
print r2



x = array([1,2,3])
y = array([2,4,6])
z = f(x,y)
print z

