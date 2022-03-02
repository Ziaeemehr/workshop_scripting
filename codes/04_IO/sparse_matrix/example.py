from scipy.sparse import coo_matrix
from pprint import pprint
import numpy as np 

# Constructing a matrix using ijv format
row  = np.array([0, 3, 1, 0])
col  = np.array([0, 3, 1, 2])
data = np.array([4, 5, 7, 9])
mat = coo_matrix((data, (row, col)), shape=(4, 4)).toarray()

pprint(mat)

A_coo = coo_matrix(mat)
print(A_coo)
print(type(A_coo))
# A = A_coo.tolil()
# for i in A:
#     print(i, type(i))

