import pandas as pd 
import numpy as np 
from sys import exit 
import h5py 



ofile = h5py.File("file.h5", 'w')
a = range(10)
dset = ofile.create_dataset('a', data=a)
for i in range(2):
    data = (i+1)*0.1
    c = ofile.create_dataset('c/t-'+str(i), data=data)
    c.attrs['t'] = i


print ofile.keys()
print ofile['c'].keys()
# print ofile['a']
b = np.asarray(ofile.get('a'))
d1 = np.asarray(ofile.get('c/t-0'))
print d1
print b