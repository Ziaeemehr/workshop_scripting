import numpy as np 

arr = np.arange(10)
np.save('some_array', arr)
a = np.load('some_array.npy')
# print a
a1 = np.arange(5)
a2 = np.arange(10)
np.savez('array_archive.npz', a=a1, b=a2)
# arch = np.load('array_archive.npz')
# print arch['a']
# print arch['b']
np.savez_compressed('array_compressed.npz', a=a1, b=a2)
arch = np.load('array_compressed.npz')
print arch['a']
print arch['b']
