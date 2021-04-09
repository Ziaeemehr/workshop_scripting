# https://docs.scipy.org/doc/scipy/reference/generated/scipy.sparse.linalg.spilu.html
# Compute an incomplete LU decomposition for a sparse, square matrix.
# The resulting object is an approximation to the inverse of A.


import numpy as np
from scipy.sparse import csc_matrix
from scipy.sparse.linalg import spilu


A = csc_matrix([[1., 0., 0.],
                [5., 0., 2.],
                [0., -1., 0.]],
               dtype=float)
lu = spilu(A)
b = np.array([1, 2, 3], dtype=float)
x = lu.solve(b)
print("x = ", x)
print("A.x = ", A.dot(x))
