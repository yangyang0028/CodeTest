import os
from threading import Thread, Lock
import time
from cupshelpers import Printer
import serial

data_mutex = Lock()
data = ""

def FunctionA() :

    while True :
        global data_mutex
        data_mutex.acquire()
        global data
        data = data + "FunctionA\n"
        data_mutex.release()
        time.sleep(1)


def FunctionB() :

    while True :
        global data_mutex
        data_mutex.acquire()
        global data
        data = data + "FunctionB\n"
        data_mutex.release()
        time.sleep(1)

try:
    TA = Thread(target=FunctionA)
    TB = Thread(target=FunctionB)
    TA.start()
    TB.start()
except:
   print("error")
   exit()

print("Start.")

while True :
    try:
        with open( 'log.txt', 'a+' ) as fd:
            data_mutex.acquire()
            fd.write(data)
            data = ""
            data_mutex.release()
        time.sleep(1)
    except:
        exit()
