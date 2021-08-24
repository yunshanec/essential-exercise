# -*- coding: utf-8 -*-
# @Time : 2021/06/21 09:09
# @Author : yunshan
# @File : 内联回调函数.py

# 通过使用生成器和协程可以使得回调函数内联在某个函数中

# 函数的某些参数强制使用关键字参数传递
# 将强制关键字参数放到某个 *参数或者单个*后面就能达到这种效果
def apply_async(function, args, *, callback):
    result = function(*args)
    callback(result)


from queue import Queue
from functools import wraps


class Async:
    def __init__(self, function, args):
        self.function = function
        self.args = args


# 装饰器
# wraps 将被修饰函数的一些属性值赋值给修饰器函数
def inlined_async(function):
    @wraps(function)
    def wrapper(*args):
        f = function(*args)
        result_queue = Queue()
        # 写入队列
        result_queue.put(None)
        while True:
            # 获取队列
            result = result_queue.get()
            try:
                a = f.send(result)
                apply_async(a.function, a.args, callback=result_queue.put)
            except StopIteration:
                break

    return wrapper


# 回调函数1
def add(x, y):
    return x + y


# 回调函数2
def subtract(x,y):
    return x-y


@inlined_async
def test():
    r = yield Async(add, (1, 2))
    print(r)
    r = yield Async(add, ("hello", "world"))
    print(r)

    for n in range(10):
        r = yield Async(subtract,(n,n))
        print(r)

    print("END")

test()
