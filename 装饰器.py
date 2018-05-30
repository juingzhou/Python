#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/27 23:34
# @Author : juingzhou
# @Site : 
# @File : 装饰器.py
# @Software: PyCharm
# 装饰器
##装饰器其实就是一个闭包，把一个函数当作参数然后返回一个替代版函数
##装饰器有两个特性：
###一是可以把被装饰的函数换成其他函数
###二是可以在加载模块时候立即执行
import decorator

def deco(func):
    def wrapper():
        print(func.__name__)
        return func()
    return wrapper

def fun():
    print("---1---")
ret = deco(fun)
ret()

#语法糖
@deco
def fun2():
    print("---2---")
fun2()
print(fun2)
print('-'*50)

import functools

def note(func):
    "note function"
    @functools.wraps(func)
    def wrapper():
        print(func.__name__)
        return func()
    return wrapper


@note
def test():
    print("I am test function")
test()
print(test.__doc__)