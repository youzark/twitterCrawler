#!/usr/bin/env python
"""
Async Code:
    CoRoutines in the same thread
"""

import logging
import threading
import multiprocessing
import asyncio
import random

#For Worker Process
def display(msg):
    threadName = threading.current_thread().name
    processName = multiprocessing.current_process().name
    logging.info(f"thread name: {threadName}  ---  proc Name: {processName} : {msg}")

async def work(name):
    display(name + " starting")
    await asyncio.sleep(random.randrange(1,5))
    display(name + " finished")

async def runAsync(maxValue):
    tasks = []
    for x in range(maxValue):
        name = "Item" + str(x)
        tasks.append(asyncio.ensure_future(work(name))) # ensure_future make function awaitable

    await asyncio.gather(*tasks)

# Main Process
def main():
    display("Main started")

    loop = asyncio.get_event_loop()

    loop.run_until_complete(runAsync(50))
    
    loop.close()

    display("Main finished")

logging.basicConfig(format="%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s",datefmt="%H:%M:%S", level=logging.DEBUG)
if __name__ == "__main__":
    main()
