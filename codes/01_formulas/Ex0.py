#!/usr/bin/python
'''
Write an script that do the following :
1. define x in range 0,4*pi with step 0.01
2. define a function to calculate 
   y = exp(-x)*1*cos(10*x-0.5)
3. save the x and y in a txt file with 6 decimal 
   place and in two coloumn 
4. plot the results
5. time the whole process
6. Do the same steps but with out for loops
   note: use numpy arrays and functions 
   for vectorization (look vectorization.py)
7. Compare the timing of using loop and vectorization 
   and calculate the speedup(look timer_example.py)
'''

import numpy as np
from math import exp,cos
import matplotlib.pyplot as plt
import time


x = np.arange(0,4*np.pi,0.00001)
def f(x1):
    r = exp(-x1)*1*cos(10*x1-0.5)
    return r
ofile = open("result.txt",'w')
#print len(x)
y = np.zeros(len(x))

t1 = time.clock()
for i in range(len(x)):
    y[i] = f(x[i])
    #ofile.write('%.6f %.6f \n'%(x[i],y[i]))
#ofile.close()
t2loop = time.clock()-t1
print 'loop timing',t2loop

t1= time.clock()
y = np.exp(-x)*1*np.cos(10*x-0.5)
t2vec = time.clock()-t1
print 'vec timing',t2vec

print 'speedup', t2loop/t2vec

#plt.plot(x,y)
#plt.show()


