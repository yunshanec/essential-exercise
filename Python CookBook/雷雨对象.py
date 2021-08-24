# -*- coding: utf-8 -*-
# @Time : 2021/06/18 14:47
# @Author : yunshan
# @File : 雷雨对象.py

"""
_formats = {
    "ymd": "{d.year}-{d.month}-{d.day}",
    "mdy": "{d.month}/{d.day}/{d.year}",
    "dmy": "{d.day}/{d.month}/{d.year}",
}


class Data:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, format_spec):
        if format_spec == "":
            format_spec = "ymd"
        fmt = _formats[format_spec]
        return fmt.format(d=self)


#
# d = Data(2021,6,18)
# print(format(d)+'what?{}'.format("yes"))
###################################################################

# 在类中封装属性名（私有数据）
class A:
    def __init__(self):
        self._internal = 3
        self.public = 1

    def _internal_method(self, method):
        print("I am an {} method".format(method))

    def public_method(self):
        print("I am a public method")

    def __what_method(self):
        print("what method")


# a = A()
# print(a._internal_method('internal'))
# ##############################################################3
# 创建可管理的属性
# 自定义某个属性的一种简单方法是将它定义为一个property
# property 一个可以使实例方法用起来像实例属性一样的特殊关键字
# 调用时，无需括号；并且仅有一个self参数


class Person:
    def __init__(self, first_name):
        self._first_name = first_name

    @property
    def first_name(self):
        return self._first_name

    # 方法名.setter
    @first_name.setter  # 设置，进可接收除self外的一个参数
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected a string")
        self._first_name = value

    # 方法名.deleter
    @first_name.deleter  # 删除
    def first_name(self):
        # raise AttributeError("Can't delete attribute")
        del self._first_name

# person = Person("Yun Shan")
# print(person.first_name)
# person.first_name = "yunshan"
# print(person.first_name)
# del person.first_name

###################################################################

# 调用父类的方法
class C:
    def spam(self):
        print('A.spam')

class D(C):
    def spam(self):
        print('B.spam')
        super().spam() # call parent spam()

d = D()
d.spam()

# super()函数的一个常见用法是在__init__()方法中确保父类被正常的初始化


class A:
    def __init__(self):
        self.x = 0

class B(A):
    def __init__(self):
        # 确保父类被正确的初始化
        super(B, self).__init__()
        self.y =1


###############################
# 8.8子类中扩展property
class Person:
    def __init__(self,name):
        self.name = name

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self,value):
        if not isinstance(value,str):
            raise TypeError("Expected a string")
        self._name = value

    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")


class SubPerson(Person):
    #只扩展property的getter方法
    @Person.name.getter
    def name(self):
        print('Getting name')
        return super().name

    # 子类修改父类中的setter方法
    @Person.name.setter
    def name(self,value):
        print("Setting name to",value)
        super(SubPerson,SubPerson).name.__set__(self,value)

    @name.deleter
    def name(self):
        print("Deleting name")
        super(SubPerson,SubPerson).name.__delete__(self)

s = SubPerson('云杉')
s.name = 'Larry'
print(s.name)


# 8.9 创建新的类或实例属性
# 如果想创建一个全新的实力属性，可以通过一个描述其的形式来定义他的功能

# Descriptor attribute for an intenger type-checked attribute
class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("Expected an int")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


# 为了使用描述器，需要将这个描述器的实例作为雷属性放到一个类的定义中
class Point:
    x = Integer("x")
    y = Integer("y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

point = Point(2,3)
print(point.x)
point.y = 5
print(point.y)
del point.x
print(point.x)

"""
# 8.16在类重定义多个构造器,使用类方法
import time
class Date:
    def __init__(self,year,month,day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year,t.tm_mon,t.tm_mday)

a = Date(2021,6,25)
b = Date.today()
print(a)
print(b)