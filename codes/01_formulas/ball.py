#!/usr/bin/python
#from math import *
import matplotlib.pyplot as plt
import numpy as np

v0 = 5
g = 9.81
t = [i*0.1 for i in range(20)]
    
y = [0]*len(t)# or np.zeros(len(t)) 

for i in range(len(t)):
    y[i] = v0*t[i] - 0.5 *g*t[i]**2

for i in range(len(t)):
    print "%4.3f \t %4.3f" % (t[i] , y[i])
    
    
plt.plot(t,y,'ro')
#plt.savefig("fig.png")
plt.show()



