import numpy as np 

a = np.asarray([[1.1,2,3],[4,5,6]])
# a = np.asarray([1,2,3])
np.savetxt("out.txt", a.T, fmt='%.9g')