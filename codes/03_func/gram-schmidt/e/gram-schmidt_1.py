import numpy as np 
from copy import deepcopy
def normalize(v):
    return v / np.sqrt(v.dot(v))


A = np.asarray([[1,1],
                [2,-1]]).T
n = len(A)

# A[:, 0] = normalize(A[:, 0])
a = np.random.rand(5,6)
A = deepcopy(a)

for i in range(1, n):
    Ai = A[:, i]
    for j in range(0, i):
        Aj = A[:, j]
        t = Ai.dot(Aj)
        Ai = Ai - t * Aj
    A[:, i] = normalize(Ai)

print A


q, r = np.linalg.qr(a)
print "-------------"
print q
