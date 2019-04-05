#!/usr/bin/python

''''
Python is Interpreted
Python is Interactive
Python is Object-Oriented
'''


counter = 100          # An integer assignment
miles   = 1000.0       # A floating point
name    = "John"       # A string

print counter
print miles
print name

a = b = c = 1

#Standard Data Types

    #1.Numbers
    #2.String
    #3.List
    #4.Tuple
    #5.Dictionary

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
#tuple[2] = 1000    # Invalid syntax with tuple
list[2] = 1000     # Valid syntax with list


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


print '=================================================='

# append and extend


stack = ['a', 'b']
stack.append('c')
# stack
# ['a', 'b', 'c']

stack.append(['e', 'f'])
# stack
# ['a', 'b', 'c', ['e', 'f']]

stack.extend(['g', 'h'])
# stack
# ['a', 'b', 'c', ['e', 'f'], 'g', 'h']
