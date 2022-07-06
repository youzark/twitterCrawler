#!/usr/bin/env python

import multiprocessing
import time
import random
import sys

def calculate(func,args):
    result = func(*args)
    return '{} says that {}{} = {}'.format(
            multiprocessing.current_process().name,
            func.__name__,
            args,
            result
            )

def calculatestar(args):
    return calculate(*args)

def mul(a,b):
    time.sleep(0.5 * random.random())
    return a * b

def plus(a,b):
    time.sleep(0.5 * random.random())
    return a + b

def f(x):
    return 1.0 / (x - 5.0)

def pow3(x):
    return x ** 3

def noop(x):
    pass

def test():
    PROCESSES = 4
    print(f"Creating pool with {PROCESSES} processes")

    with multiprocessing.Pool(PROCESSES) as pool:

        TASKS = [(mul,(i,7)) for i in range(10)] + [(plus,(i,8)) for i in range(10)]

        results = [ pool.apply_async(calculate , t) for t  in TASKS ]
        imap_it = pool.imap(calculatestar, TASKS)
        imap_unordered_it = pool.imap_unordered(calculatestar, TASKS)

        print("Ordered results using pool.apply_async():")
        for r in results:
            print("\t", r.get())
        print()
            

if __name__ == "__main__":
    test()
