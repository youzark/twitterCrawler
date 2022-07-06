#!/usr/bin/env python

"""
Daemon:
    run background and quit when app quit
"""

import logging
import threading
from threading import Thread,Timer
from concurrent.futures import ThreadPoolExecutor 
import time


def test():
    threadname = threading.current_thread().name
    logging.info(f"Starting: {threadname}")
    for x in range(60):
        logging.info(f"Working: {threadname}")
        time.sleep(1)
    logging.info(f"Finished: {threadname}")

def stop():
    logging.info("Exiting the application")
    exit(0)


def main():
    logging.basicConfig(format="%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s",datefmt="%H:%M:%S", level=logging.DEBUG)
    logging.info("Main thread started")

    timer = Timer(3,stop)
    timer.start()
    
    # t = Thread(target=test,daemon=False) # thread continue after app exit
    # t.start()

    t = Thread(target=test,daemon=True) # thread shut down when app shut down
    t.start()

    logging.info("Main thread finished")


if __name__ == "__main__":
    main()
