
# coding: utf-8

# # <font color='blue'>Why Python</font>
# 
# -  easy to learn
# -  huge library
# -  excellent science support
# -  quick development turnaround
# 
# 
# 
# 
# note: using some David Grellscheid slides (Thanks!)

# ## <font color='blue'>Growth of major programming languages </font>
# #### Based on Overflow question views in World Bank high-income countries
# 
# <img src="img/01.png" alt="Alt text that describes the graphic" title="Title text" width="600" height="600" />

# <img src="img/02.png" alt="Alt text that describes the graphic" title="Title text" />

# ## <font color='blue'> Zen of Python, by Tim Peters ( import this )</font>
# -  Beautiful is better than ugly.
# -  Explicit is better than implicit.
# -  Simple is better than complex.
# -  Complex is better than complicated.
# -  Readability counts.
# -  There should be one—and preferably only one— obvious way to do it.
# -  If the implementation is hard to explain, it's a bad idea.
# 
# 

# # <font color='blue'> Design choices </font>
# 
# -  Multi-paradigm language:
# -  structured, object oriented & functional
# -  styles are all supported
# -  clean syntax, fun to use
# -  Highly extensible:
#  small core, large standard lib
Python is Interpreted
Python is Interactive
Python is Object-Oriented
# ## <font color='blue'> Standard Data Types </font>
# 
# 1. Numbers
# 2. String
# 3. List
# 4. Tuple
# 5. Dictionary

# In[3]:


counter = 100          # An integer assignment
miles   = 1000.0       # A floating point
name    = "John"       # A string

print counter
print miles
print name

a = b = c = 1


# In[4]:


#String
str = 'Hello World!'
#List
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print list          # Prints complete list
print list[0]       # Prints first element of the list
print list[1:3]     # Prints elements starting from 2nd till 3rd 
print list[2:]      # Prints elements starting from 3rd element
print tinylist * 2  # Prints list two times
print list + tinylist # Prints concatenated lists


# In[2]:


#Tuple
tup1 = (50,);
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print tuple           # Prints complete list
print tuple[0]        # Prints first element of the list
print tuple[1:3]      # Prints elements starting from 2nd till 3rd 
print tuple[2:]       # Prints elements starting from 3rd element
print tinytuple * 2   # Prints list two times
print tuple + tinytuple # Prints concatenated lists

tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
list = [ 'abcd', 786 , 2.23, 'john', 70.2  ]
# tuple[2] = 1000    # Invalid syntax with tuple
list[2] = 1000     # Valid syntax with list


# In[6]:


#Dictionary
dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"
tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

print dict['one']       # Prints value for 'one' key
print dict[2]           # Prints value for 2 key
print tinydict          # Prints complete dictionary
print tinydict.keys()   # Prints all the keys
print tinydict.values() # Prints all the values


# # <font color='blue'> Syntax </font>
# ### Control flow
# -  for
# -  if else elif
# -  while
# -  pas/break/continue

# In[8]:


A = [1.5,3,2]
for a in A:
    print a*2
    
# for i in range(3):
#     print A[i]
    
# for (int i=0; i<3; i++)
#     cout << A[i]<< endl;


# In[23]:


if 3 in list:
    print '3 is in the list'
if 20 not in list:
    print '20 is not in the list' 


# ## <font color='blue'> Functions and libraries </font>
# -  importing libraries
# -  Function definition
# 
# 

# In[1]:


from numpy import *
import numpy
import numpy as np 
from numpy import sin, cos


# In[3]:


def f(a,b):
    return a+b
# scalar
x,y = 2,5
print 'on scalar: ', f(x,y)
# on array
x = array([1,2])
y = array([3,4])
print 'on arrays: ', f(x,y)
#on list
x = [1,2]
y = [3,4]
print 'on lists : ', f(x,y)

