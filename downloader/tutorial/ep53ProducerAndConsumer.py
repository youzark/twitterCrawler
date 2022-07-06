#!/usr/bin/env python
import logging
import threading
import multiprocessing
from threading import Thread
from queue import Queue
from concurrent.futures import ThreadPoolExecutor 
import time
import random
logging.basicConfig(format="%(levelname)s - %(asctime)s: %(message)s",datefmt="%H:%M:%S", level=logging.DEBUG)

#For Worker Process
def display(msg):
    threadName = threading.current_thread().name
    processName = multiprocessing.current_process().name
    logging.info(f"{threadName} -- proc Name: {processName} : {msg}")


# Producer
def create_work(queue,finished,maxValue):
    finished.put(False)
    for x in range(maxValue):
        v = random.randrange(1,100)
        queue.put(v)
        display(f"Producing iter{x}: {v}")
    finished.put(True)

# Consumer
def work(workQueue,finished):
    counter = 0
    while True:
        if not workQueue.empty():
            v = workQueue.get()
            display(f"Consuming id{counter}: {v}")
            counter += 1
        else:
            q = finished.get()
            if q == True:
                break

def main():
    maxValue = 50
    workQueue = Queue()
    finished = Queue()

    producer = Thread(target=create_work,args=[workQueue,finished,maxValue],daemon=True)
    consumer = Thread(target=work,args=[workQueue,finished],daemon=True)

    producer.start()
    consumer.start()

    producer.join()
    display("Producer finished")
    consumer.join()
    display("Consumer finished")



if __name__ == "__main__":
    main()
