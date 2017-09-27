import zoo
# In zoo.cpp we expose hello() function, and it now exists in the zoo module.
assert 'hello' in dir(zoo)
# zoo.hello is a callable.
assert callable(zoo.hello)
# Call the C++ hello() function from Python.
print zoo.hello()

# Create an animal.
animal = zoo.Animal("dog")
# The Python object.
print animal
# Use the exposed method to show the address of the C++ object.
print "The C++ object is at 0x%016x" % animal.get_address()
# Use the exposed property accessor.
print "I see a \"%s\"" % animal.name
animal.name = "cat"
print "I see a \"%s\"" % animal.name