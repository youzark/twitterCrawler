#!/usr/bin/env python
from multiprocessing import Pool,Queue
import multiprocessing
import logging
import time
import random

def worker(item,Queue):
    display(f"start working on item : {item}")
    time.sleep(random.randrange(1,6))
    display(f"finish working on item : {item}")
    return f"finish {item}"

def display(msg):
    processName = multiprocessing.current_process().name
    logging.info(f"{processName} : {msg}")
    
def main():
    display("App start")
    pool = Pool(4)
    items = [1,2,3,4,5,6,7,8]
    print(pool.map_async(func=worker,iterable=items))
    display("App finished")



logging.basicConfig(format="%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s",datefmt="%H:%M:%S", level=logging.DEBUG)
if __name__ == "__main__":
    main()
