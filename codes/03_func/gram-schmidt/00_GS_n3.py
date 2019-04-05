import numpy as np 
from numpy import dot
from numpy.linalg import norm


def gram_schmidt(A):
        ''' 
        calculate the norm of orthogonalized vectors
        y is updated by reference
        '''
        znorm = np.zeros(3)
        
        a1 = (A[:,0])
        a2 = (A[:,1])
        a3 = (A[:,2])

        znorm[0] = norm(a1)
        b1 = a1/znorm[0]

        b2p = a2 - dot(b1, a2) * b1
        znorm[1] = norm(b2p)
        b2 = b2p/znorm[1]

        b3p = a3-dot(b1, a3)*b1-dot(b2, a3)*b2
        znorm[2] = norm(b3p)
        b3 = b3p/znorm[2]

        
        B = np.zeros((3,3))
        B[:,0] = b1
        B[:,1] = b2 
        B[:,2] = b3
        print "B \n", B, "\n"
        print dot(b1,b2), dot(b1,b3), dot(b2,b3)

        return znorm

A = np.asarray([[1,1,-2],[1,2,-3],[0,1,1]]).T 
print "A: \n", A
znorm = gram_schmidt(A)
print "znorm \n", znorm

