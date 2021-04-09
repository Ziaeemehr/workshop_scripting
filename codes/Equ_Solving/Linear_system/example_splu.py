# used documentation of : help(dsolve)
import numpy as np
from scipy.sparse import csc_matrix, linalg as sla

A = csc_matrix([[1, 2, 0, 4],
                [1, 0, 0, 1],
                [1, 0, 2, 1],
                [2, 2, 1, 0.]])

lu = sla.splu(A)
b = np.array([1, 2, 3, 4])
x = lu.solve(b)
print("x = ", x)
print("A.x = ", A.dot(x))
