#!/usr/bin/env python

## 
import time
from threading import Timer
##

## 
def display(msg):
    print(msg + " " + time.strftime("%H:%M:%S"))

def runOnce():
    display("Run once:")
    t = Timer(5,display,['Time out!'])
    t.start()
##

## 
runOnce()
print("waiting...")
##


## interval timer
class repeatTimer(Timer):
    # run is called automatically when start() is called
    def run(self):
        while not self.finished.wait(self.interval):  # type: ignore
            self.function(*self.args,**self.kwargs)  # type: ignore
        print("Done")

##

## 
timer = repeatTimer(1,display,['Repeating'])
timer.start()

print("threading started")
time.sleep(10)
print("threading finishing")

timer.cancel()
##
