# from sympy import sin, cos, Matrix 
# from sympy.abc import rho, phi 
# X = Matrix([rho*cos(phi), rho*sin(phi), rho**2])
# Y = Matrix([rho, phi])
# X.jacobian(Y)

from sympy.abc import x, y
from sympy import Matrix, sin
from sympy.printing.cxxcode import cxxcode

X = Matrix([x**2*y, 5*x+sin(y)])
Y = Matrix([x,y])
print X.jacobian(Y)
# print(cxxcode(X.jacobian(Y)))
