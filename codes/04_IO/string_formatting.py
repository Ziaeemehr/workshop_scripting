#!/usr/bin/env python
# coding: utf-8

# In[5]:


# STRING FORMATTING AND FORMAT SPECIFICATIONS
#Insert values into a string in order:
continents = "France is in {} and China is in {}".format("Europe", "Asia")
print continents

# Insert values into a string by position:
squares = "{0} times {0} equals {1}".format(3,9)
print squares

# Insert values into a string by name:
population = "{name}'s population is {pop} million".format(name="Brazil", pop=209)
print population

# Format specification for precision of two decimal places:
two_decimal_places = "I own {:.2f}% of the company".format(32.5548651132)
print two_decimal_places

# Format specification for comma separator:
india_pop = "The approximate population of {} is {}".format("India",1324000000)
print india_pop

# Order for format specification when using precision and comma separator:
balance_string = "Your bank balance is {:,.2f}".format(12345.678)
print balance_string


# In[ ]:




