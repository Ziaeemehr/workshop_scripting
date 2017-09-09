import glob
import pylab as pl
import numpy as np 

for name in glob.glob('./Cor-0.300000-*'):
     data = np.genfromtxt(name)
     pl.imshow(data)
     pl.show()
