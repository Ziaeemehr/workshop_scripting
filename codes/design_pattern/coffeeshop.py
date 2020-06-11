"""
Decorator pattern allows a user to add new functionality to an existing object without altering its structure. This type of design pattern comes under structural pattern as this pattern acts as a wrapper to existing class.

This pattern creates a decorator class, which wraps the original class and provides additional functionality keeping the class methods signature intact.

The motive of a decorator pattern is to attach additional responsibilities of an object dynamically.
"""

import six
from abc import ABCMeta

@six.add_metaclass(ABCMeta)
class Abstract_Coffee(object):

    def get_cost(self):
        pass

    def get_ingredients(self):
        pass
    
    def get_tax(self):
        return 0.1 * self.get_cost()
    
class Concrete_Coffee(Abstract_Coffee):

    def get_cost(self):
        return 1.0
    
    def get_ingredients(self):
        return "coffee"
    
@six.add_metaclass(ABCMeta)
class Abstract_Coffee_Decorator(Abstract_Coffee):

    def __init__(self, decorated_coffee):
        self.decorated_coffee = decorated_coffee
    
    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients()

class Sugar(Abstract_Coffee_Decorator):

    def __init__(self, decorated_coffee):
        Abstract_Coffee_Decorator.__init__(self, decorated_coffee)
    
    def get_cost(self):
        return self.decorated_coffee.get_cost()
    
    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients() + ", sugare"

class Milk(Abstract_Coffee_Decorator):

    def __init__(self, decorated_coffee):
        Abstract_Coffee_Decorator.__init__(self, decorated_coffee)
    
    def get_cost(self):
        return self.decorated_coffee.get_cost() + 0.25
    
    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients() + ", milk"

class Vanilla(Abstract_Coffee_Decorator):

    def __init__(self, decorated_coffee):
        Abstract_Coffee_Decorator.__init__(self, decorated_coffee)
    
    def get_cost(self):
        return self.decorated_coffee.get_cost() + 0.75
    
    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients() + ", vanilla"
        
        
