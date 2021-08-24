class Root(object) :
    """docstring for Root"""

    def __init__(self) :
        self.attribute = '这是属性'

    def fun(self) :
        print(self.attribute)
        print('方法名{}'.format(self.fun.__name__))


# 继承
class A(Root) :
    """docstring for A"""

    def __init__(self) :
        super(A, self).__init__() # 能够访问父类的属性
        print("实例化时执行")


if __name__ == '__main__' :
    test = A()  # 实例化类
    test.fun()  # 调用继承自Root的fun()方法
    a = test.attribute  # 调用继承自Root的attribute属性
    print(a)
'''
##################################################################################
# 未知参数指的是调用函数是，参数顺序相一致
# 接受任意数量的位置参数,可以使用一个*参数
def avg(first, *rest):
    return first + sum(rest)


# 关键字参数指的是使用键值对 key=value 的方式调用程序
# 接受任意数量的关键字参数,使用**开头的参数


# 同时接受任意数量的未知参数和关键字参数
def anyargs(x, *args, y, **kwargs):
    print(x)
    print(y)
    print(args)  # 元组
    print(kwargs)  # 字典


####################################################################
# 函数的某些参数强制使用关键字参数传递
# 将强制关键字参数放到某个 *参数或者单个*后面就能达到这种效果
def recv(maxsize, *, block):
    "Receive a message"
    pass


# 利用强制关键字参数，还能在接受任意多个未知参数的函数中指定关键字参数
def minimum(*values, clipe=None):
    "最小值"
    m = min(values)
    if clipe is not None:
        m = clipe if clipe > m else m
    return m


# 很多情况下，使用强制关键字参数比使用位置参数表一更加清晰
def caculate(zheng, fu):
    "计算相加"
    print(zheng + fu)


# 给函数参数添加元信息
def add_numbers(x: int, y: int) -> int:
    return x + y


#################################################################
# 定义有默认参数的函数
def spam(a, b=2):
    print(a, b)


# 如果默认参数是一个可以修改的容器,可以使用None作为默认值
# 在测试None值时使用is操作符很重要
def spam_1(a, b=None):
    if b is None:
        b = []
        b.append(a)
    print(a, b)


#####################################################
# lambda表达式典型的使用场景是排序或数据reduce
# names = ["David Beazley", "Brian Jones", "Raymond Hettinger", "Ned Batchelder"]
# result = sorted(names,key=lambda name:name.split()[-1].lower())
# print(result)

#####################################################
# 带额外状态信息的回调函数
def apply_async(func, args, *, callback):
    # compute the result
    result = func(*args)

    # Invoke the callback with the result
    callback(result)


def print_result(result):
    print("Got: ", result)


def add_numbers(x, y):
    return x + y


# 为了让回调函数访问外部信息，一种方法是使用一个绑定方法来代替一个简单函数
class ResultHandler:
    def __init__(self):
        self.sequence = 0

    def handler(self, result):
        self.sequence += 1
        print("[{}] Got: {}".format(self.sequence, result))


# 作为类的替代，可以使用一个闭包补货状态值
def make_handler():
    sequence = 0

    def handler(result):
        nonlocal sequence
        sequence += 1
        print("[{}] Got: {}".format(sequence, result))

    return handler


# 更高级的方法，使用携程来完成上面要实现的功能
def make_handler_xiecheng():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print("[{}] Got: {}".format(sequence, result))


# 对于协程需要使用send()方法作为回调函数，如下所示
make_handler_xiecheng = make_handler_xiecheng()
next(make_handler_xiecheng)
apply_async(add_numbers, (1, 2), callback=make_handler_xiecheng.send)

# if __name__ == "__main__":
#     handler = make_handler()
#     apply_async(add_numbers,(1,2),callback=handler)
'''