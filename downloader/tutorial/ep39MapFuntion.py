#!/usr/bin/env python

peopleList = ["Matt","Bryan","Tammy","Markus"]

counts = []
for x in peopleList:
    counts.append(len(x))
print(f"Old way: {counts}")


# map(funtion , list of args)
# send one arg in args to funtion one time
print(f"Mapped: {list(map(len,peopleList))}")


firstNames = {"Apple","Choclate","Fudge","Pizza"} # pizza failed silently
lastNames = {"Pie","Cake","Brownies"}

def merge(a,b):
    return a + " " + b

x = map(merge,firstNames,lastNames)
print(list(x))


def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

def doAll(func,num):
    return func(num[0],num[1])

f = (add,sub,mul,div)
v = [[5,3]]
n = list(v) * len(f)
print(f"f:{f}, n:{n}")

print(list(map(doAll,f,n)))
















