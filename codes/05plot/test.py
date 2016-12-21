import numpy as np
import matplotlib.pyplot as plt

ifile = open('xyz_v.txt','r')
data = np.genfromtxt(ifile,dtype='float')
x = data[:,0]
y = data[:,1]
z = data[:,2]

plt.plot(x,y,'ro')
plt.show()
