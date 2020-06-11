"""
Three ways of computing the Hellinger distance between two discrete
probability distributions using NumPy and SciPy.
"""

import numpy as np
import pylab as plt
from scipy.linalg import norm
from scipy.spatial.distance import euclidean


def hellinger1(p, q):
    return norm(np.sqrt(p) - np.sqrt(q)) / np.sqrt(2)


def hellinger2(p, q):
    return euclidean(np.sqrt(p), np.sqrt(q)) / np.sqrt(2)


def hellinger3(p, q):
    return np.sqrt(np.sum((np.sqrt(p) - np.sqrt(q)) ** 2)) / np.sqrt(2)


def distributions(N, m_a=10, m_b=10, m_c=25):
    dist_a = []
    dist_b = []
    dist_c = []
    for i in range(N):
        dist_a.append(np.random.randn(2) + m_a)
        dist_c.append(np.random.randn(2) + m_c)
        dist_b.append(np.random.randn(2) * 5.5 + m_b)

    return dist_a, dist_b, dist_c


def distribution(N, dim=1, loc=0, scale=1, normal=False):
    dist = []
    for i in range(N):
        dist.append(np.random.normal(loc=loc, scale=scale, size=dim))

    if normal:
        return np.asarray(dist) / N

    return np.asarray(dist)


N = 100
dim = 2
normal = False
A = distribution(N, dim=dim, loc=20, scale=1.0, normal=normal)
B = distribution(N, dim=dim, loc=20, scale=5.5, normal=normal)
C = distribution(N, dim=dim, loc=45, scale=1.0, normal=normal)
# D = np.sin(np.random.rand(N))


print("hellinger distance between A, B is ", hellinger1(np.abs(A), np.abs(B)))
print("hellinger distance between A, C is ", hellinger1(np.abs(A), np.abs(C)))
print("hellinger distance between B, C is ", hellinger1(np.abs(B), np.abs(C)))


if dim == 1:
    print("*" * 70)
    print("hellinger distance between A, B is ",
          hellinger2(np.abs(A), np.abs(B)))
    print("hellinger distance between A, C is ",
          hellinger2(np.abs(A), np.abs(C)))
    print("hellinger distance between B, C is ",
          hellinger2(np.abs(B), np.abs(C)))

print("*" * 70)
print("hellinger distance between A, B is ", hellinger3(np.abs(A), np.abs(B)))
print("hellinger distance between A, C is ", hellinger3(np.abs(A), np.abs(C)))
print("hellinger distance between B, C is ", hellinger3(np.abs(B), np.abs(C)))
print("*" * 70)

if dim == 2:

    plt.scatter([x for x, _ in A], [y for _, y in A], label='distribution A')
    plt.scatter([x for x, _ in B], [y for _, y in B], label='distribution B')
    plt.scatter([x for x, _ in C], [y for _, y in C], label='distribution C')
    plt.legend()
    plt.show()
