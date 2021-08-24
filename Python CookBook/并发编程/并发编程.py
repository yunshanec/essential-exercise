# -*- coding: utf-8 -*-
# @Time : 2021/06/25 10:17
# @Author : yunshan
# @File : 并发编程.py

'''
# 12.2启动与停止线程
import time
from threading import Thread

def add():
    print("loading...")
    time.sleep(3)

def mul():
    print('loading...')
    time.sleep(5)

if __name__ == "__main__":
    t1 = Thread(target = add)
    t2 = Thread(target = mul)

    t1.start()
    t2.start()

    # 等待子线程执行完 t2不执行完，谁也不准走
    t2.join()

    print(time.ctime())

import time
from threading import Thread

def countdown(n):
    while n>0:
        print("T-minus",n)
        n -= 1
        time.sleep(5)

t = Thread(target=countdown,args=(10,))
t.start()

# 查询线程对象的状态，看他是否在还在执行
if t.is_alive():
    print('Still runing')
else:
    print('Completed')

# import time
# from threading import Thread
#
# class CountdownTask:
#     def __init__(self):
#         self._running = True
#
#     def terminate(self):
#         self._running = False
#
#     def run(self,n):
#         while self._running and n>0:
#             print("T-minus",n)
#             n-=1
#             time.sleep(5)
#
# c = CountdownTask()
# t = Thread(target=c.run,args=(10,))
# t.start()
# c.terminate() # signal termination
# t.join() # Wait for actual termination (if needed)


# 12.2 判断线程是否已经启动
# Event 对象包含一个可有线程设置的信号标志，它允许等到某些事件的发生
# from threading import Thread,Event
# import time
#
# # code to execute in an independent thread
# def countdown(n,started_evt):
#     print('countdown starting')
#     started_evt.set()
#     while n>0:
#         print("T-minus",n)
#         n -=1
#         time.sleep(3)
#
# start_evt = Event()
# print("Launching countdown")
# t = Thread(target=countdown,args=(10,start_evt))
# t.start()
#
# # wait for the thread to start
# start_evt.wait()
# print("countdown is runing")

'''
# 12.3 线程间通信
# 从一个线程向另一个线程发送数据最安全的方式可能就是使用queue库中的队列
# 创建一个被多线程共享的Queue对象，这些线程通过使用put()和get()操作向队列中、
# 添加或删除元素

# A thread that produces data

