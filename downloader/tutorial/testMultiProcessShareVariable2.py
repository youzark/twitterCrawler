#!/usr/bin/env python
import logging
import multiprocessing
import time
import random

msgList = []

#For Worker Process
def work(msg,max):
    name = multiprocessing.current_process().name
    logging.info(f"Started: {name}")
    for x in range(max):
        logging.info(f"{name} : {msg}  {x}")
        time.sleep(random.randrange(1,6))
    logging.info(f"Finished: {name}")
    return msg + " is returned"

def procResult(result):
    msgList.append(result)
    logging.info(f"Result : {result}")

# Main Process
def main():
    logging.info("Main thread started")

    maxValue = 5
    pool = multiprocessing.Pool(maxValue)

    results = []

    for x in range(maxValue):
        item = "Item" + str(x)
        count = random.randrange(1,5)
        r = pool.apply_async(func=work,args=[item,count])
        results.append(r)

    for result in results:
        print(result.get(10))


    # pool.close() or pool.terminate() close is safer
    pool.join()
    pool.close()

    for info in msgList:
        print(info)

    logging.info("Finished")

logging.basicConfig(format="%(levelname)s - %(asctime)s.%(msecs)03d: %(message)s",datefmt="%H:%M:%S", level=logging.DEBUG)
if __name__ == "__main__":
    main()
