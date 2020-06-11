import numpy as np
import networkx as nx
from random import shuffle

def permutation(alpha):
    
    n = len(alpha)
    P = np.zeros((n, n), dtype=int)
    for i in range(n):
        P[i][alpha[i]] = 1

    return P

N, p = 5, 0.5
G_H = nx.gnp_random_graph(N, p, seed=1)
A_H = nx.to_numpy_array(G_H, dtype=int)

alpha = list(range(N))
shuffle(alpha)
P = permutation(alpha)

A_G = np.matmul(np.matmul(P, A_H), P.T)
G_G = nx.from_numpy_array(A_G)

print("is isomorphic : ", nx.is_isomorphic(G_G, G_H))

A = nx.to_numpy_array(G_G, dtype=int)
print("same adj : ", np.array_equal(A, A_G))