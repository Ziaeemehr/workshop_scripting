import numpy as np
import pylab as plt
from pprint import pprint
import Matrix_Solver_Methods as lib
from scipy.sparse import csc_matrix, linalg as sla

actual_sol = np.array([1.0, 1.0])
b1 = np.array([3.0, 3.+1e-15])
A1 = np.array([[1, 2],
               [1.+1e-15, 2]])

maxIter = 500
tol = 1e-15
t1 = 10


print("\nA:")
pprint(A1)
print("\nb:")
pprint(b1)
print("\nApprox x:")
sol1_IR = lib.Iterative_Ref(A1, b1, tol, maxIter, t1)
print("\nActual Solution:")
pprint(actual_sol)

wellcond1 = np.linalg.cond(A1)
print("\nConditional number of matrix A is: {:e}".format(wellcond1))

# check
A1 = csc_matrix(A1)
lu = sla.splu(A1)
x = lu.solve(b1)
print("x = ", x)
print("A.x = ", A1.dot(x))
