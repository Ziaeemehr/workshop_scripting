from sympy import symbols, Eq, solve

x, y = symbols('x y')
eq1 = Eq(2*x-y-1)
eq2 = Eq(x+y-5)
sol = solve((eq1, eq2), (x, y))
print sol
