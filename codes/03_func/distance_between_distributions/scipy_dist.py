import numpy as np
import pylab as plt
from scipy.spatial.distance import pdist


def distribution(N, dim=1, loc=0, scale=1, normal=False):
    dist = []
    for i in range(N):
        dist.append(np.random.normal(loc=loc, scale=scale, size=dim))

    if normal:
        return np.asarray(dist) / N

    return np.asarray(dist)


N = 100
dim = 2
A = distribution(N, dim=2, loc=20, scale=1.0, normal=1)
B = distribution(N, dim=2, loc=20, scale=5.5, normal=1)
C = distribution(N, dim=2, loc=45, scale=1.0, normal=1)

print((A.T).shape)
print(pdist(A.T, 'hamming'))

for i in ["cosine", "euclidean", "sqeuclidean", "cityblock"]:
    print(pdist(A.T, i), pdist(B.T, i), pdist(C.T, i))


# if dim == 2:

#     plt.scatter([x for x, _ in A], [y for _, y in A], label='distribution A')
#     plt.scatter([x for x, _ in B], [y for _, y in B], label='distribution B')
#     plt.scatter([x for x, _ in C], [y for _, y in C], label='distribution C')
#     plt.legend()
#     plt.show()
