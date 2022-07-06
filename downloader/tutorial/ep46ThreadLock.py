#!/usr/bin/env python

"""
GIL:
    Global interperter lock
    a mutex that allow only one thread to hold the control of the interpreter
    Python is true multi-threading , it means python will really create threads
    in system, but only one theard can use interpreter one time.


With GIL , no race condition is possible.
shared resources is protected because only one thread can use interpreter
"""

import logging
import threading
from concurrent.futures import ThreadPoolExecutor 
import time
import random


counter = 0
def test(count):
    global counter
    threadname = threading.current_thread().name
    logging.info(f"Starting: {threadname}")

    for x in range(count):
        logging.info(f"Count: {threadname} += {count}")

        
        # counter += 1 # race condition here ,But actually GIL will deal with that
    
        #Locking
        # lock = threading.Lock()
        # lock.acquire()
        # # lock.acquire()  # deadlock hear
        # try:
        #     counter += 1
        # finally:
        #     lock.release()


        # Locking Simplified 
        lock = threading.Lock()
        with lock:
            logging.info(f"Locked: {threadname}")
            counter += 1
            time.sleep(2)
            



    logging.info(f"Completed: {threadname}")

def main():
    logging.basicConfig(format="%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s",datefmt="%H:%M:%S", level=logging.DEBUG)
    logging.info("App Starting")
    workers = 2
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for x in range(workers*2):
            v = random.randrange(1,5)
            ex.submit(test,v)

    print(f"Counter: {counter}")
    logging.info("App Finished")

if __name__ == "__main__":
    main()
