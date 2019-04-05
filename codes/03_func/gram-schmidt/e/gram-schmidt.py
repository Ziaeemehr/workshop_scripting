import numpy as np


def gs(X):
    Q, R = np.linalg.qr(X)
    return Q

# A = np.array([[0, 1], 
#               [1, 1], 
#               [1, 1], 
#               [2, 1]])
# b = np.array([1, 0, 2, 1])
# q, r = np.linalg.qr(A)
# p = np.dot(q.T,b)
# result = np.dot(np.linalg.inv(r), p)

# vectors in rows
A = np.asarray([[1,1],
               [2,-1]])
q, r = np.linalg.qr(A.T)
u1 = q[:,0]
u2 = q[:,1]
print np.dot(u1, u2) 