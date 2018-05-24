import pandas as pd 
import numpy as np 
from sys import exit 
import h5py 

frame = pd.DataFrame({'a': np.random.randn(100)})
store = pd.HDFStore('mydata.h5')
store['obj1'] = frame
store['obj1_col'] = frame['a']
# print store
# print store['obj1']
store.put('obj2', frame, format='table')
# print store.select('obj2', where=['index >=10 and index <=15'])
store.close()

# The put is an explicit version of the 
# store['obj2'] = frame method but allows us to
# set other options like the storage format.
# The pandas.read_hdf function gives you a shortcut to these tools:
frame.to_hdf('mydata.h5', 'obj3', format='table')
# print pd.read_hdf('mydata.h5', 'obj3', where=['index<5'])
# print pd.read_hdf('mydata.h5', key=None)
f = h5py.File('mydata.h5', 'r')
# print f.keys()
# print f['obj1']
print list(f.items())