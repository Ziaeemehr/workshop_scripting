class MyClass(object):
    counter = 0
    def __init__(self, name):
        self.name = name 
        MyClass.counter +=1
    @staticmethod
    def count():
        return MyClass.counter

t = MyClass("some")
print(MyClass.count())
t1 = MyClass("other")
print(MyClass.count())

