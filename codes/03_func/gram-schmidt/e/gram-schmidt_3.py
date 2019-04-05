# L-20 MCS 507 Fri 11 Oct 2013 : gramschmidt.py
import numpy as np

"""
Given pseudo code for the Gram-Schmidt method,
define Python code.
"""

import numpy as np

def gramschmidt(A):
    """
    Applies the Gram-Schmidt method to A
    and returns Q and R, so Q*R = A.
    """
    R = np.zeros((A.shape[1], A.shape[1]))
    Q = np.zeros(A.shape)
    for k in range(0, A.shape[1]):
        R[k, k] = np.sqrt(np.dot(A[:, k], A[:, k]))
        Q[:, k] = A[:, k]/R[k, k]
        for j in range(k+1, A.shape[1]):
            R[k, j] = np.dot(Q[:, k], A[:, j])
            A[:, j] = A[:, j] - R[k, j]*Q[:, k]
    return Q, R

def main():
    """
    Prompts for n and generates a random matrix.
    """
    # cols = input('give number of columns : ')
    # rows = input('give number of rows : ')
    # A = np.random.rand(rows, cols)
    A = np.array([[1,1,0],[1,2,1],[-2,-3,1]])
    print 'A = '
    print A
    Q, R = gramschmidt(A)
    print 'Q = '
    print Q
    print 'R = '
    print R
    print 'Q^T*Q = '
    print np.dot(Q.transpose(), Q)
    print 'Q*R ='
    print np.dot(Q, R)

main()
