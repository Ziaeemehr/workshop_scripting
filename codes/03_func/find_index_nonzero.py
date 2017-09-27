import numpy

# index of zero elements in a numpy array

x = numpy.array([1,0,2,0,3,0,4,5,6,7,8])
numpy.where(x == 0)[0]

Out: array([1, 3, 5])

import numpy as np
arr = np.array([[1,2,3], [0, 1, 0], [7, 0, 2]])
np.argwhere(arr == 0)

Out:
     array([[1, 0],    # indices of the first zero
            [1, 2],    # indices of the second zero
            [2, 1]],   # indices of the third zero
            dtype=int64)

#If you are working with 1d array there is a sugar syntax 
x = numpy.array([1,0,2,0,3,0,4,5,6,7,8])
numpy.flatnonzero(x == 0)
Out: array([1, 3, 5])



#some thing else
import numpy as np
x = np.array([1,0,2,3,6])
non_zero_arr = np.extract(x>0,x)

min_index = np.amin(non_zero_arr)
min_value = np.argmin(non_zero_arr)


# index of zero elements in a list
a = [0, 1, 0, 1, 0, 0, 0, 0]
[i for i, e in enumerate(a) if e != 0]

import numpy as np
a = [0, 1, 0, 1, 0, 0, 0, 0]
nonzeroind = np.nonzero(a) 
print nonzeroind[0]
Out: [1, 3]
