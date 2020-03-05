# Python program showing
# abstract base class work

import abc
from abc import ABC, abstractmethod


# Python program showing
# implementation of abstract
# class through subclassing


class parent:
    def geeks(self):
        pass


class child(parent):
    def geeks(self):
        print("child class")


# Driver code
print(issubclass(child, parent))
print(isinstance(child(), parent))


# Concrete Methods in Abstract Base Classes :

# Python program invoking a
# method using super()

class R(ABC):
    def rk(self):
        print("Abstract Base Class")


class K(R):
    def rk(self):
        super().rk()
        print("subclass ")


# Driver code
r = K()
r.rk()

exit(0)

# Abstract Properties :

# Python program showing
# abstract properties

class parent(ABC):
    @abc.abstractproperty
    def geeks(self):
        return "parent class"

class child(parent):
    @property
    def geeks(self):
        return "child class"

try:
    r = parent()
    print (r.geeks)

except Exception as err:
    print (err)

r = child()
print (r.geeks)
