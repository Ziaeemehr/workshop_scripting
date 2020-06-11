"""
Decorator pattern allows a user to add new functionality to an existing object without altering its structure. This type of design pattern comes under structural pattern as this pattern acts as a wrapper to existing class.

This pattern creates a decorator class, which wraps the original class and provides additional functionality keeping the class methods signature intact.

The motive of a decorator pattern is to attach additional responsibilities of an object dynamically.
"""

import coffeeshop

myCoffee = coffeeshop.Concrete_Coffee()
print('Ingredients: '+myCoffee.get_ingredients() +
      '; Cost: '+str(myCoffee.get_cost())+'; sales tax = '+str(myCoffee.get_tax()))

myCoffee = coffeeshop.Milk(myCoffee)
print('Ingredients: '+myCoffee.get_ingredients() +
      '; Cost: '+str(myCoffee.get_cost())+'; sales tax = '+str(myCoffee.get_tax()))

myCoffee = coffeeshop.Vanilla(myCoffee)
print('Ingredients: '+myCoffee.get_ingredients() +
      '; Cost: '+str(myCoffee.get_cost())+'; sales tax = '+str(myCoffee.get_tax()))

myCoffee = coffeeshop.Sugar(myCoffee)
print('Ingredients: '+myCoffee.get_ingredients() +
      '; Cost: '+str(myCoffee.get_cost())+'; sales tax = '+str(myCoffee.get_tax()))
