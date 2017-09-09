from sys import exit

class Parent(object):
    def __init__(self):
        self.a = 10

    foobar = ["hello"]

    def print_sth(self):
        print "Parent class"

class Child(Parent):
    # def __init__(self):
    #     self.a = 20

    foobar = Parent.foobar + ['world']
    def print_sth(self):
        print "Child class"


A = Parent()
# print A.foobar
# A.print_sth()
print A.a



B = Child()
# print B.foobar
# B.print_sth()
print B.a


# print A.foobar
# A.print_sth()
print A.a