# -*- coding: utf-8 -*-
# @Time : 2021/07/08 09:25
# @Author : yunshan
# @File : decoration.py
import time

class Decoration:
    def __init__(self):
        super(Decoration, self).__init__()

    def logger(self,func):
        def wrapper(*args,**kwargs):
            now = time.ctime()
            print(f'{now}')
            func(*args,**kwargs)
            print('执行{}结束.'.format(func.__name__))
        return wrapper

    def timer(self,func):
        def wrapper(*args,**kwargs):
            start_time = time.time()
            func(*args,**kwargs)
            end_time = time.time()
            print('执行{}函数花费时间{:.5}秒.'.format(func.__name__,round(end_time-start_time,5)))
        return wrapper

if __name__ == '__main__':
    decoration = Decoration()


    @decoration.logger
    def time_sleep(seconds:int):
        time.sleep(seconds)
        print('over...')

    time_sleep(2)















