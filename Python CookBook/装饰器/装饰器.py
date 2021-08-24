# -*- coding: utf-8 -*-
# @Time : 2021/06/21 10:22
# @Author : yunshan
# @File : 装饰器.py

# 日志打印器
import time


def logger(func):
    def wrapper(*args,**kwargs):
        now = time.ctime()
        print(f'{now}')
        func(*args,**kwargs)
        print("执行以上函数结束")
    return wrapper

@logger
def add(x,y):
    print('{}+{}={}'.format(x,y,x+y))

add(2,3)


# 时间计时器
def timer(func):
    def wrapper(*args,**kwargs):
        t1 = time.time()
        func(*args,**kwargs)
        t2 = time.time()
        cost_time = t2 - t1
        print("执行{}函数花费时间{:.5}秒".format(func.__name__,cost_time))
    return wrapper

@timer
def want_sleep(sleep_time):
    time.sleep(sleep_time)

want_sleep(3)

'''

# 带参数的函数装饰器
def say_hello(contry):
    def wrapper(func):
        def deco(*args,**kwargs):
            if contry == "China":
                print("你好！")
            elif contry == "America":
                print("Hello!")
            else:
                return "nothing"

            func(*args,**kwargs)

        return deco
    return wrapper

@say_hello("China")
def xiaoming():
    pass

# xiaoming()


# 不带参数的类装饰器
# 基于类装饰器的实现，必须实现__call__ 和 __init__ 两个内置函数。
# __init__:接受被装饰函数
# __call__:实现装饰逻辑

class Logger(object):
    def __init__(self,func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("[INFO]:The function [{func}] is running......"\
              .format(func = self.func.__name__))
        return self.func(*args,**kwargs)

@Logger
def say(something):
    print("Say {}".format(something))

#say("Hello")

# 带参数的类装饰器
# 此时__init__:不再接收被装饰函数，而是接收传入参数
# 此时__call__:接收被装饰的函数，实现装饰逻辑（多了一层嵌套）

class logger(object):
    def __init__(self,message:str):
        self.message= message

    def __call__(self, func):
        def wrapper(*args,**kwargs):
            print("[{level}]:The function [{func}] is running"\
                .format(level= self.message,func = func.__name__)
                  )
            func(*args,**kwargs)
        return wrapper

@logger(message="Information")
def say(something):
    print("Say {}!".format(something))

# say("Hello")

# wraps装饰器,将被修饰的函数wrapped的一些属性值赋值给修饰器函数wrapper

from functools import wraps
def wrapper(func):
    @wraps(func)
    def inner__function():
        pass
    return inner__function

@wrapper
def wrapped():
    pass

print(wrapped.__name__)

# 内置装饰器：property
# property 通常存在与类中，将一个函数定义成一个属性，属性的值就是该\
# 函数return的内容

class Student(object):
    def __init__(self,name:str):
        self.name = name

    @property
    def age(self):
        return self._age

    @age.setter #只能传入一个参数
    def age(self,value):
        if not isinstance(value,int):
            raise ValueError("年龄必须是数值")
        if not 0 <value<100:
            raise ValueError("年龄范围必须为0-100")

        self._age = value

    @age.deleter
    def age(self):
        del self._age

# xiaoming = Student("小明")
# xiaoming.age = 18
# print(xiaoming.age)
#
# del xiaoming.age
#
# print(xiaoming.age)


'''





