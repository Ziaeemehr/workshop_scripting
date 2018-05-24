import pandas as pd 
from pandas import Series, DataFrame
import numpy as np
#Series
obj = pd.Series([4,7,-5,3])
# print obj
# print type(obj.values)
# print obj.index

obj2 = pd.Series([4, 7, -5, 3], 
        index=['d', 'b', 'a', 'c'])
# print obj2
# print obj2.index
# print obj2['d']
# print obj2[['c','a']]
# print obj2*2
# print ('b' in obj2)
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = pd.Series(sdata)
# print obj3
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4=pd.Series(sdata, index=states)
# print obj4
# print pd.isnull(obj4)
# print pd.notnull(obj4)
# print obj4[pd.notnull(obj4)]
obj4.name = 'population'
obj4.index.name = 'state'
# print obj4

#DataFrame
data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)
# print frame
# print frame.head()
# print pd.DataFrame(data, columns=['year', 'state', 'pop'])
frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                      index=['one', 'two', 'three', 'four', 'five', 'six'])
# print frame2
# print frame2.columns
# print frame2['state']
# print frame2.loc['three']
# frame2['debt'] = 16.5
frame2['debt'] = np.arange(6.)
val = pd.Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame2['debt'] = val
frame2['eastern'] = frame2.state == 'Ohio'
del frame2['eastern']
# print frame2

# Another common form of data is a nested dict of dicts:
pop = {'Nevada': {2001: 2.4, 2002: 2.9},
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = pd.DataFrame(pop)
# print frame3
# print frame3.T
# print pd.DataFrame(pop, index=[2001, 2002, 2003])
pdata = {'Ohio': frame3['Ohio'][:-1],
         'Nevada': frame3['Nevada'][:2]}
# print pdata

# Reindexing
obj = pd.Series([4.5, 7.2, -5.3, 3.6], 
index=['d', 'b', 'a', 'c'])
obj2 = obj.reindex(['a', 'b', 'c', 'd', 'e'])
# print obj 
# print obj2

frame = pd.DataFrame(np.arange(9).reshape((3, 3)),
        index=['a', 'c', 'd'],
        columns=['Ohio', 'Texas', 'California'])
print frame
frame2 = frame.reindex(['a', 'd', 'c'])
print frame2
states = ['Texas', 'Utah', 'California']
print frame.reindex(columns=states)
