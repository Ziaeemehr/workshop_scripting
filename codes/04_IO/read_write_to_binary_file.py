import numpy as np 

a = np.arange(0,10,0.125)
# print a
print len(a)
a.tofile("a.bin")

b = np.fromfile("a.bin", dtype=float, count=-1)
print b

print a==b
