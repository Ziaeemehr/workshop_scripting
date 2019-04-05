import numpy as np 
import h5py


f = h5py.File('asy_pat.h5', 'r')
print list(f.keys())

a = [0.35, 0.5, 0.75]
l = ['vol', 'Q', 'snr']

# for i in f.keys():
    # print i, type(i)
    # print np.asarray(f.get(i)).shape
print np.asarray(f.get('vol-'+str('%.6f'%a[0])))