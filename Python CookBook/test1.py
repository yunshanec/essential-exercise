# -*- coding: utf-8 -*-
# @Time : 2021/06/18 13:23
# @Author : yunshan
# @File : test1.py

# 装饰器Decorators 修改其他函数的功能的函数
# 将函数作为参数传给另一个函数

from functools import wraps


def a_new_decorator(a_func):
    # @wraps 接受一个函数进行装饰，并加入了赋值函数名称、注释文档、参数列表等功能
    # 这可以让我们在装饰器里面访问在装饰之前的函数的属性
    @wraps(a_func)
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")
        a_func()
        print("I am doing some boring work after excuting a_func()")

    return wrapTheFunction


@a_new_decorator
def a_function_requiring_decoration():
    print("I an the function which needs some decoration to remove my foul smell")


# print(a_function_requiring_decoration.__name__)

###################################################################################
# 日志是装饰器的一大亮点
def logit(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + "was called")
        return func(*args, **kwargs)

    return with_logging


@logit
def addition_func(x):
    """do some math"""
    return x + x


# result = addition_func(12)
# print(result)

# 装饰器类
class Logit(object):
    def __init__(self, logfile="out.log"):
        self.logfile = logfile
        super(Logit, self).__init__()

    def __call__(self, func):
        @wraps(func)
        def wrapper_function(*args, **kwargs):
            log_string = func.__name__ + "was called"
            print(log_string)
            # open logfile and writing
            with open(self.logfile, "a") as opened_file:
                # 现在将日志打到指定的文件
                opened_file.write(log_string + "\n")
            # 现在，发送一个通知
            self.notify()
            return func(*args, **kwargs)

        return wrapper_function

    def notify(self):
        # logit只打日志 不做别的
        pass


# 给Logit创建子类，添加email功能
class email_logit(Logit):
    def __init__(self, email="yunshanec@163.com", *args, **kwargs):
        self.email = email
        super(email_logit, self).__init__(*args, **kwargs)

    def notify(self):
        pass


######################################################################
# 内联回调函数
from queue import Queue
from functools import wraps


def apply_async(func, args, *, callback):
    result = func(*args)
    callback(result)


class Async:
    def __init__(self, func, args):
        self.func = func
        self.args = args


# 装饰器
def inlined_async(func):
    @wraps(func)
    def wrapper(*args):
        f = func(*args)
        result_queue = Queue()
        result_queue.put(None)
        while True:
            result = result_queue.get()
            try:
                a = f.send(result)
                apply_async(a.func, a.args, callback=result_queue.put)
            except StopIteration:
                break

    return wrapper


# 两个代码片段允许使用yield语句内联回调步骤
def add_nums(x, y):
    return x + y


@inlined_async
def test():
    r = yield Async(add_nums, (2, 3))
    print(r)
    x = yield Async(add_nums, ("hello", "world"))
    print(x)


test()
