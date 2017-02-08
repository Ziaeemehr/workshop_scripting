#!/usr/bin/python
#-------------------------------------------------------------------

total = 0; # This is global variable.
def sum( arg1, arg2 ):
   total = arg1 + arg2; # Here total is local variable.
   print "Inside the function local total : ", total
   return total;

# Now you can call sum function
sum( 10, 20 );
print "Outside the function global total : ", total 

#-------------------------------------------------------------------
foo = 1
def test():
    foo = 2 # new local foo

def blub():
    global foo
    foo = 3 # changes the value of the global foo

print 'foo befor calling functions', foo
test()
print 'foo after calling test', foo
blub()
print 'foo after calling blub', foo
#-------------------------------------------------------------------

globvar = 0
def set_globvar_to_one():
    global globvar    # Needed to modify global copy of globvar
    globvar = 1

def print_globvar():
    print(globvar)     # No need for global declaration to read value of globvar

set_globvar_to_one()
print_globvar()       # Prints 1
