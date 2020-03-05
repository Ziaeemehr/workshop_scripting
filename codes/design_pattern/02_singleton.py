# This pattern restricts the instantiation of a class to one object. It is a type of creational pattern and involves only one class to create methods and specified objects.


class Singleton:
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Singleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self


s = Singleton()
print (s)

s = Singleton.getInstance()
print (s)

s = Singleton.getInstance()
print (s)


# https://python-patterns.guide/gang-of-four/singleton/
print ("")

class Logger(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(Logger, cls).__new__(cls)
            # Put any initialization here.
        return cls._instance

log1 = Logger()
print (log1)

# But the second call returns the same instance. The message “Creating the object” does not print, nor is a different object returned:

log2 = Logger()
print(log2)
print('Are they the same object?', log1 is log2)