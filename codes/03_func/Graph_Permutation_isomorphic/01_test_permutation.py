"""
A_G = P A_H P.T

P is permutation matrix
P.T is the transpose matrix of T
"""

import numpy as np
import networkx as nx


def permutation(alpha, n):
    P = np.zeros((n, n), dtype=int)
    for i in range(n):
        P[i][alpha[i]] = 1

    return P


A_G = np.array([[0, 1, 0, 0, 0],
                [1, 0, 1, 0, 1],
                [0, 1, 0, 1, 1],
                [0, 0, 1, 0, 1],
                [0, 1, 1, 1, 0]])


A_H = np.array([[0, 1, 1, 1, 0],
                [1, 0, 1, 0, 0],
                [1, 1, 0, 1, 0],
                [1, 0, 1, 0, 1],
                [0, 0, 0, 1, 0]])

# arbitrary permutation of nodes.
alpha = [4, 3, 0, 1, 2]
P = permutation(alpha, 5)

A_Gp = np.matmul(np.matmul(P, A_H), P.T)

# check if it works?
print(np.array_equal(A_Gp, A_G))
