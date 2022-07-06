#!/usr/bin/env python
"""
Queue:
    Mail box
Future : 
    synchronizing program execution
"""

import logging
import threading
from threading import Thread
from queue import Queue
from concurrent.futures import ThreadPoolExecutor 
import time
import random


def testQueue(name,que):
    threadname = threading.current_thread().name
    logging.info(f"Starting: {threadname}")
    time.sleep(random.randrange(1,5))
    logging.info(f"Finished: {threadname}")
    ret = "Hello " + name + " your random number is " + str(random.randrange(1,10))
    que.put(ret) # you should lock it actually 

def queued():
    que = Queue()
    t = Thread(target=testQueue,args=["Bryan",que])
    t.start()
    logging.info("Do something on the main thread")

    # when use queue you need to asyc by hand
    t.join()
    ret = que.get()
    logging.info(f"Returned: {ret}")


#Futures
#User Futures to handle message passing
def testFuture(name):
    threadname = threading.current_thread().name
    logging.info(f"Starting: {threadname}")
    time.sleep(random.randrange(1,5))
    logging.info(f"Finished: {threadname}")
    ret = "Hello " + name + " your random number is " + str(random.randrange(1,100))
    return ret


def pooled():
    workers = 20
    ret = []
    with ThreadPoolExecutor(max_workers=workers) as ex:
        for x in range(workers):
            v = random.randrange(1,5)
            future = ex.submit(testFuture,"Bryan" + str(x))
            ret.append(future)
    logging.info("Do something on the main thread")
    for r in ret:
        logging.info(f"Returned: {r.result()}")


def main():
    logging.basicConfig(format="%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s",datefmt="%H:%M:%S", level=logging.DEBUG)
    logging.info("Main thread started")
    # queued()
    pooled()
    logging.info("Main thread finished")


if __name__ == "__main__":
    main()
