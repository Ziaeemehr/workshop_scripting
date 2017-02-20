import sympy
import sympy as sp
sp.init_printing()
from sympy import I,pi,oo
print sp.pi

x = sp.Symbol("x")
y = sp.Symbol("y",real=True)
print "y is real? ",y.is_real
print "z is real? ",sp.Symbol("z",imaginary=True).is_real

y = sp.Symbol("y",positive=True)
print sp.sqrt(x**2)

n1 = sp.Symbol("n")
n2 = sp.Symbol("n",integer=True)
n3 = sp.Symbol("n",odd=True)

print sp.cos(n1*pi)
print sp.cos(n2*pi)
print sp.cos(n3*pi)

a,b,c = sp.symbols("a,b,c",negative=True)
d,e,f = sp.symbols("d,e,f",positive=True)
#Numbers
i = sp.Integer(19)
print type(i)
print i.is_real,i.is_integer,i.is_odd
f=sp.Float(2.3)
print type(f)
print i.is_real,i.is_integer,i.is_odd
#Or
i, f = sp.sympify(19), sp.sympify(2.3)
print  type(i), type(f)

print i**3
print sp.factorial(100)
#The SymPy Float object can represent the real number 0.3
#without the limitations of floating-point numbers

print "%.25f" % 0.3 
print sp.Float(0.3, 25)
print sp.Float('0.3', 25)

print sympy.Rational(11, 13)
r1 = sympy.Rational(2, 3)
r2 = sympy.Rational(4, 5)
print r1 * r2
print r1/r2











