#!/usr/bin/env python

# Skipping
for _ in range(4): # the _ is ignored, when it's not used
    print("hello")

# Single Before , weak private for class ,scope
class Person:
    def __init__(self,name):
        self._name = name

    def __think(self):
        print("Thinking to my self")

    def work(self):
        self.__think()

class Child(Person):
    # Before and after
    def __init__(self):
        print("Constructor")

    def __test__(self):
        print("call someone")


    def testDouble(self):
        self.__think()

# You can access and modify _ variable , but don't , it's assumed that is local 
p = Person("youzark")
print(f"Weak private: {p._name}")


# Double underscore before : use internally by automatically change name outside of the scope
p.work()
c = Child()
c.__test__()
c.testDouble()

# After any number: avoid naming conflicts
class_ = Person("test")


