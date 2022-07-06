#!/usr/bin/env python

import logging
import multiprocessing
from multiprocessing.context import Process
import time

#For Worker Process
def work(msg,max):
    name = multiprocessing.current_process().name
    logging.info(f"Started: {name}")
    for x in range(max):
        logging.info(f"{name} : {msg}  {x}")
        time.sleep(1)
    logging.info(f"Finished: {name}")

# Main Process
def main():
    logging.info("Main thread started")
    maxValue = 3
    worker = Process(target=work,args=("working",maxValue),daemon=True,name="Worker")
    worker.start()
    time.sleep(5)
    # if the process is running , stop it
    if worker.is_alive:
        worker.terminate()  # pretty dangerous 
    worker.join()

    logging.info(f"Main thread finished {worker.exitcode}")


logging.basicConfig(format="%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s",datefmt="%H:%M:%S", level=logging.DEBUG)
if __name__ == "__main__":
    main()
