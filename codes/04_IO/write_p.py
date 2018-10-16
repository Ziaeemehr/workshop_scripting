import numpy as np 


f = open('file.txt', 'w')
for i in range(10):
    f.write("%g %g \n"%(i, i**2))

f.close()