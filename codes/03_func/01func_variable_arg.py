#!/usr/bin/python
import numpy as np
# Function definition is here
def printinfo( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print "Output is: "
   print arg1
   for var in vartuple:
      print var
   

printinfo( 10 )
printinfo( 70, 60, 50 )

def add(x,y):
    return x+y

print add(1,2)
a = np.array([1,1,1])
b = np.array([1,2,3])
print add(a,b)
print add([1,1,1],[1,2,3])




