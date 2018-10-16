import pickle
import numpy as np 
from sys import exit 
from time import time, clock

start = time()
# a = np.random.rand(10000,1000)
# np.savetxt('infile.txt', a, fmt='%15.9f')

# pickle_out = open('arr.pickle', 'wb')
# pickle.dump(a, pickle_out)
# pickle_out.close()

pickle_in = open('infile.txt', 'r')
example_ar = pickle.load(pickle_in)
print example_ar.shape

# a = np.genfromtxt('infile.txt')
# print a.shape
print 'Time: ',time()-start, 'seconds'



exit(0)
example_dict = {1: "6", 2: "2", 3: "f"}
pickle_out = open('dict.pickle', 'wb')
pickle.dump(example_dict, pickle_out)
pickle_out.close()


pickle_in = open('dict.pickle', 'rb')
example_dict = pickle.load(pickle_in)
print example_dict
print example_dict[2]
