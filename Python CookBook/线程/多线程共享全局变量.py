# -*- coding: utf-8 -*-
# @Time : 2021/07/05 17:13
# @Author : yunshan
# @File : 多线程共享全局变量.py
import threading
import time

g_num = 100
def work1():
    global g_num
    for i in range(3):
        g_num += 1
    print(f'in work1 g_num is :{g_num}')

def work2():
    global g_num
    print(f'in work2 g_num is {g_num}')

if __name__ == '__main__':
    t1 = threading.Thread(target=work1)
    t1.start()
    time.sleep(1)

    t2 = threading.Thread(target=work2)
    t2.start()