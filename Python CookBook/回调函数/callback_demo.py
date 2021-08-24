# -*- coding: utf-8 -*-
# @Time : 2021/06/21 09:49
# @Author : yunshan
# @File : callback_demo.py

from even import *

# 中间函数
# 接受一个生成偶数的函数作为参数
# 返回奇数

def getOddNumber(k,getEvenNumber):
    return 1+getEvenNumber


def main():
    k = 1
    i = getOddNumber(k,getEvenNumber=double(x=3))
    print(i)

if "__name__" == "__main__":
    main()
