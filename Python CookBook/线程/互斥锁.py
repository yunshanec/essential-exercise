# -*- coding: utf-8 -*-
# @Time : 2021/07/05 17:21
# @Author : yunshan
# @File : 互斥锁.py
import threading
import time
from threading import Lock



def work():
    global n
    lock.acquire()
    temp = n
    time.sleep(0.1)
    n = temp - 1
    lock.release()

if __name__ == '__main__':

    lock = Lock()
    n = 100
    l = []
    for i in range(100):
        p = threading.Thread(target=work)
        l.append(p)
        p.start()
    for p in l:
        p.join()