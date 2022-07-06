#!/usr/bin/env python
"""
Serializing objects
Saving and loading objects and their states
"""

import pickle

def outline(func):
    def inner(*args,**kwargs):
        print("-"*20)
        print(f"Function: {func.__name__}")
        func(*args,**kwargs)
        print("-"*20)
    return inner


class Cat:
    def __init__(self,name,age,info):
        self._name = name
        self._age = age
        self._info = info

    @outline
    def display(self,msg=""):
        print(msg)
        print(f"{self._name} is a {self._age} years old cat")
        for k,v in self._info.items():
            print(f"{k} = {v}")


othello = Cat("Othello",15,dict(color="Black",weight=15,loves="Eating"))
othello.display()

serializeCat = pickle.dumps(othello)
print(serializeCat)

# with open("Cat.txt","wb") as f:
#     pickle.dump(othello,f)

myCat = pickle.loads(serializeCat)
myCat.display("From string")

