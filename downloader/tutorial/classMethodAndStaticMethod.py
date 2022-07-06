#!/usr/bin/env python
import datetime
"""
By Corey Schafer

@classmethod:
    deal with class property rather than object property
    provide way to modify static property
    also used to provide multiple ways to init a object(alternative constructor)

@staticmethod:
    nothing class related will be passed to the method.
    just a normal method in the class for they have some logical connection
"""

class Employee:
    numOfEmps = 0
    raiseAmount = 1.04

    def __init__(self,firstName,lastName,pay):
        self.firstName = firstName
        self.lastName = lastName
        self.pay = pay

    @staticmethod
    def isWorkDay(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    @classmethod
    def setRaiseAmount(cls,amount):
        cls.raiseAmount = amount

    @classmethod
    def fromString(cls,empString):
        firstName, lastName, pay = empString.split("-")
        return cls(firstName, lastName, pay)

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
        return len(self.firstName + self.lastName)


print(f"Test ststic : Is week day: {Employee.isWorkDay(datetime.datetime(2019,3,11))} ")
emp = Employee("you","zark",50000)
emp2 = Employee("you","zarking",50000)

print(Employee.raiseAmount)
print(emp.raiseAmount)
print(emp2.raiseAmount)
Employee.setRaiseAmount(1.6)
print(Employee.raiseAmount)
print(emp.raiseAmount)
print(emp2.raiseAmount)
# but pay attention , if you get self.raiseAmount in class specification , 
# a instance property will be created and emo.raiseAmount will only change value
# for one instance ,and Employee.raiseAmount works as a init/fallback value
emp.setRaiseAmount(1.9)
print(Employee.raiseAmount)
print(emp.raiseAmount)
print(emp2.raiseAmount)
