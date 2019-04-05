# https://jakevdp.github.io/PythonDataScienceHandbook/02.09-structured-data-numpy.html
import numpy as np 

name = ['Alice', 'Bob', 'Cathy', 'Doug']
age = [25, 45, 37, 19]
weight = [55.0, 85.5, 68.0, 61.5]

 # Use a compound data type for structured arrays
data = np.zeros(4, dtype={'names':('name', 'age', 'weight'),
                          'formats':('U10', 'i4', 'f8')})
print(data.dtype)


data['name'] = name
data['age'] = age
data['weight'] = weight
print(data)

print data['name']
print data[0]
# Get names where age is under 30
data[data['age'] < 30]['name']


np.dtype({'names':('name', 'age', 'weight'),
          'formats':((np.str_, 10), int, np.float32)})
np.dtype([('name', 'S10'), ('age', 'i4'), ('weight', 'f8')])
# If the names of the types do not matter to you, 
# you can specify the types alone in a 
# comma-separated string:
np.dtype('S10,i4,f8')