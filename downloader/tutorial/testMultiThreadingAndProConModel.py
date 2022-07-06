#!/usr/bin/env python
import logging
import threading
from concurrent.futures import ThreadPoolExecutor 
import time
from time import sleep
import random
from queue import Queue


def display(msg):
    threadName = threading.current_thread().name
    logging.info(f"thread name: {threadName} : {msg}")

def test(item):
    sec = random.randrange(1,10)
    display(f"item:{item} start")
    time.sleep(sec)
    display(f"item:{item} finished")

def Mexecutor(item):
    futures = []
    with ThreadPoolExecutor(max_workers=5) as ex:
        futures.append(ex.submit(test,item))
    display("Consumer finished")
    return futures

def itemSender():
    display("Start send item")
    for i in range(50):
        item = random.randrange(1,20)
        finishFlagQueue.put(False)
        itemQueue.put(f"{i}:{item}")
        interval = random.randrange(1,3)
        sleep(interval)
    finishFlagQueue.put(True)
    display("Finished send item")
        

def main():
    itemQueue = Queue()
    finishFlagQueue = Queue()
    logging.info("start")
    sender = threading.Thread(target=itemSender,daemon=True)
    receiver = threading.Thread(target=Mexecutor,daemon=True)
    sender.start()
    receiver.start()
    sender.join()
    display("sender return")
    receiver.join()
    display("receiver return")
    logging.info("finished")

logging.basicConfig(format="%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s",datefmt="%H:%M:%S", level=logging.DEBUG)
if __name__ == "__main__":
    main()
