import numpy as np
import pandas as pd 

np.random.seed(123)
a = np.array([3,1,1,2,2,3])
b = np.array([0.2,0.1,0.2,0.1,0.2,0.1])
c = a+b

d = pd.DataFrame(zip(a,b,c), columns=['a','b','sum'])
print d

d1 = d.sort(['a', 'b'], ascending=[True, True])
# df.sort_values(by=['col1', 'col2'])

print d1 
print np.asarray(d1['sum'].reshape(3,2))