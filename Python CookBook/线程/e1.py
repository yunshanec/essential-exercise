# -*- coding: utf-8 -*-
# @Time : 2021/07/05 17:03
# @Author : yunshan
# @File : e1.py
import threading
import time
from threading import Thread,Lock

def run(n):
    print('task',n)
    time.sleep(1)
    print('2s')
    time.sleep(1)
    print('1s')
    time.sleep(1)
    print('0s')
    time.sleep(1)

if __name__ == '__main__':
    t1 = threading.Thread(target=run,args=('t1',))
    t1.setDaemon(True) # 把子线程设置成守护线程（必须在start()之前设置）
    t1.start()
    t1.join() # 设置主线程等待子线程结束
    print('end')
