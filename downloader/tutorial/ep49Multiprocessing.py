#!/usr/bin/env python
"""
When we try to do multiprocessing in python:
    we copy the script multiple time and run together

"""

import logging
import multiprocessing
from multiprocessing import process
import time

# config globally for different os has different __name__
logging.basicConfig(format="%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s",datefmt="%H:%M:%S", level=logging.DEBUG)

# process entry point
def run(num):
    name = process.current_process().name
    logging.info(f"Running {name} as {__name__}")
    time.sleep(num * 2)
    logging.info(f"finish {name}")


# Basic usage

def main():
    name = process.current_process().name
    logging.info(f"Running {name} as {__name__}")

    processes = []
    for x in range(5):
        p = multiprocessing.Process(target=run,args=[x],daemon=True) # cause it daemon might be killed prematurely 
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
    logging.info(f"finish {name}")

if __name__ == "__main__":
    main()















