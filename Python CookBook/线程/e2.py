# -*- coding: utf-8 -*-
# @Time : 2021/07/05 17:33
# @Author : yunshan
# @File : e2.py
import threading
import time

event = threading.Event()

def lighter():
    count = 0
    event.set()
    while True:
        if 5 < count <=10:
            event.clear()
            print("clear")
        elif count >10:
            event.set()
            count = 0
        else:
            print('aksd')

        time.sleep(1)
        count += 1

def car(name):
    while True:
        if event.is_set():
            print('running...{}'.format(name))
            time.sleep(1)
        else:
            print('red light,...{}'.format(name))
            event.wait()
            print('green light is on,start going...{}'.format(name))


light = threading.Thread(target=lighter,)
light.start()

car = threading.Thread(target=car("MINI",))
car.start()
endTime = time.time()
