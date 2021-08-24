# -*- coding: utf-8 -*-
# @Time : 2021/06/25 09:33
# @Author : yunshan
# @File : 元编程.py

'''
# 9.1在函数上添加包装器
# 如果想使用额外的代码包装一个函数，可以定义一个装饰器函数
import time
from functools import wraps

# 装饰器
def timethis(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(func.__name__,"运行时间 {}".format(end-start))
        return result
    return wrapper
# 一个装饰器就是一个函数，它接受一个函数作为参数并返回一个新的函数
@timethis
def countdown(n):
    while n>0:
        n -= 1

countdown(10000000)

'''
from functools import wraps

def decorator1(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print("Decorator1")
        return func(*args,**kwargs)
    return wrapper

def decorator2(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print("Decorator2")
        return func(*args,**kwargs)
    return wrapper

@decorator1
@decorator2
def add(x,y):
    return x+y

print(add(2,3))



