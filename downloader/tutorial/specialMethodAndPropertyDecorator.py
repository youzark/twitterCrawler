#!/usr/bin/env python
"""
By Corey Schafer

Magic Methods: ( also called dunder method)
    overloading operator : len() str() repr() "+" ...

@property:
    make class method accessible as a attribute

@attribute.setter
    define method to assign property value

@attribute.deleter
    define method to delete property
"""

class Employee:
    
    numOfEmps = 0
    raiseAmount = 1.04

    def __init__(self,firstName,lastName,pay):
        self.firstName = firstName
        self.lastName = lastName
        self.pay = pay

    @property
    def email(self):
        return f"{self.firstName}{self.lastName}@email.com"

    @property
    def fullname(self):
        return f"{self.firstName} {self.lastName}"

    @fullname.setter
    def fullname(self,name):
        firstName, lastName = name.split(" ")
        self.firstName = firstName
        self.lastName = lastName

    @fullname.deleter
    def fullname(self):
        self.firstName = None
        self.lastName = None

    # served as a fall back for __str__() method
    # as return value when repr(Employee) is call
    # Meant to be used by developer as a debug method
    # return a string that can be used to recreate the object
    def __repr__(self):
        return f"Employee('{self.firstName}','{self.lastName}',{self.pay})"

    def __str__(self):
        return f"{self.firstName} {self.lastName} - {self.firstName}{self.lastName}@mail.ustc.edu.com"

    # only for example here: Really not a good example
    # overloading "+" for employ
    # return added payment 
    def __add__(self,other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.firstName+self.lastName)





emp = Employee("you","zark",50000)
print(repr(emp))
print(str(emp))
print(emp)
print("with property:" + emp.email)
emp.fullname = "White Bro"
print(emp.fullname)
del emp.fullname
print(emp.fullname)

emp1 = Employee("you","zark",50000)
emp2 = Employee("you","zark",62300)
# you can define your special dunder method for operator
print(int.__add__(1,2))
print(emp1 + emp2)
print(len(emp1))
