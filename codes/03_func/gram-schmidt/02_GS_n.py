import numpy as np 
from numpy import dot
from numpy.linalg import norm

def proj(a,b):
    """
    calculate the projection of a along b
    it does not apply the normalization
    """
    result = dot(a,b) * b
    
    return result

def gram_schmidt(A):
        ''' 
        calculate the norm of orthogonalized vectors
        it suppose vectors are in columns of A
        '''
        A = np.asarray(A)
        N, M = A.shape
        assert(N==M), "input matrix should be square (nxn)"
        
        B = np.zeros((N, N))
        znorm = np.zeros(N)

        bp = A[:,0]
        znorm[0] = norm(bp)
        B[:,0] = bp/znorm[0]


        for k in range(1,N):
            sumj = 0
            for j in range(k):
                # print k , j
                sumj += proj(A[:,k], B[:,j])
            
            bp = A[:,k] - sumj
            znorm[k] = norm(bp)

            B[:,k] = bp / znorm[k]

        print dot(B[:,0], B[:,1])
        print dot(B[:,0], B[:,2])
        print dot(B[:,1], B[:,2])
            
        return znorm

A = np.asarray([[1,1,-2],[1,2,-3],[0,1,1]]).T 
# A = np.asarray([[1,1,-2,1],[1,2,-3,0],[0,1,1,2], [1,-5,2,0]]).T 

# print "A: \n", A
znorm = gram_schmidt(A)
print "znorm \n", znorm

