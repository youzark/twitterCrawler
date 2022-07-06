#!/usr/bin/env python

import logging
from threading import Thread
import time 
import random


def longTask(name):
    maxValue = random.randrange(1,10)
    logging.info(f"task: {name} performing {maxValue} times")
    for x in range(maxValue):
        logging.info(f"task: {name} -> {x}")
        time.sleep(random.randrange(1,3))
    logging.info(f"task: {name} complete")

def main():
    logging.basicConfig(format="%(levelname)s - %(asctime)s: %(message)s",datefmt="%H:%M:%S", level=logging.DEBUG)
    logging.info("starting")

    threads = []
    for i in range(10):
        t = Thread(target=longTask, args=["thread" + str(i)])
        threads.append(t)
        t.start()

    # tell the main thread wait until specified threads finished
    for t in threads:
        t.join()

    logging.info("Finished all threads")

if __name__ == "__main__":
    main()
