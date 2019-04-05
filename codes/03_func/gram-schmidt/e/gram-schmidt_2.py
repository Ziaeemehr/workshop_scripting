import numpy as np 
from copy import deepcopy
from sys import exit

np.random.seed(1235)

def normalize(v):
    return v / np.sqrt(v.dot(v))

# after transpose vectors on columns
# A = np.asarray([[1.0,1.0],
#                 [2.0,-1.0]]).T

A = np.random.rand(3,3).T

a = A[:,0]
b = A[:,1]
c = A[:,2]

v1 = A[:,0]
v2 = b - np.dot(v1,b)/np.dot(v1, v1) * v1
v3 = c - np.dot(v1,c)/np.dot(v1, v1) * v1 - np.dot(v2,c)/np.dot(v2,v2)*v2

# print A 
# n = len(A)
# znorm = np.zeros(n)
# B = np.zeros((n,n))
# B[:,0] = A[:,0]
# znorm[0] = np.linalg.norm(A[:,0])

# for i in range(1,n):
#     vi = A[:,i]
#     for j in range(i):
#         vj = A[:,j]
#         vi = vi -np.dot(vi,vj)/np.dot(vj,vj)
#     B[:,i] = vi
#     znorm[i] = np.linalg.norm(vi)

# for i in range(n):
#     print normalize(B[:,i]), znorm[i]


# print A


q1 = normalize(v1)
q2 = normalize(v2)
q3 = normalize(v3)

for v in [v1,v2,v3]:
    print np.linalg.norm(v)
for q in [q1, q2, q3]:
    print np.linalg.norm(q)






# exit(0)
print "-------------"
q, r = np.linalg.qr(A)
print q
