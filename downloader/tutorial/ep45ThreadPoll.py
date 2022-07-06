#!/usr/bin/env python

import logging
import threading
from concurrent.futures import ThreadPoolExecutor 
import time
import random


def test(item):
    sec = random.randrange(1,10)
    logging.info(f"thread {item}: id = {threading.get_ident()}")
    logging.info(f"thread {item}: name = {threading.current_thread().name}")
    logging.info(f"thread {item}: sleeping for {sec}")
    time.sleep(sec)
    logging.info(f"thread {item} finished")

def main():
    logging.basicConfig(format="%(levelname)s - %(asctime)s: %(message)s",datefmt="%H:%M:%S", level=logging.DEBUG)
    logging.info("start")

    workersNum = 5
    itemsNum = 15

    with ThreadPoolExecutor(max_workers=workersNum) as executor:
        executor.map(test,range(itemsNum))

    logging.info("finished")

if __name__ == "__main__":
    main()
