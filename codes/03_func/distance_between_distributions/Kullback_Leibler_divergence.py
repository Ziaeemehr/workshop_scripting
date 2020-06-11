"""
Three ways of computing the Hellinger distance between two discrete
probability distributions using NumPy and SciPy.
"""

import numpy as np
import pylab as plt
from sklearn.metrics import mutual_info_score


def distribution(N, dim=1, loc=0, scale=1, normal=False):
    dist = []
    for i in range(N):
        dist.append(np.random.normal(loc=loc, scale=scale, size=dim))
    
    if normal:
        return np.asarray(dist) / N 

    return np.asarray(dist)



N = 100
A = distribution(N, dim=1, loc=20, scale=1.0, normal=1)
B = distribution(N, dim=1, loc=20, scale=5.5, normal=1)
C = distribution(N, dim=1, loc=45, scale=1.0, normal=1)
D = np.sin(np.random.rand(N))

# print(A.shape)

print(" MI between A, B is ", mutual_info_score(A.reshape(-1), B.reshape(-1)))
print(" MI between B, C is ", mutual_info_score(B.reshape(-1), C.reshape(-1)))
print(" MI between A, C is ", mutual_info_score(A.reshape(-1), C.reshape(-1)))
print(" MI between A, D is ", mutual_info_score(A.reshape(-1), D.reshape(-1)))
# print("*" * 70)


plt.scatter(range(len(A)), A, label='A')
plt.scatter(range(len(B)), B, label='B')
plt.scatter(range(len(C)), C, label='C')
plt.scatter(range(len(D)), D, label='D')


plt.legend(loc="upper right")
plt.show()

