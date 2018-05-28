#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/28 0:07
# @Author : juingzhou
# @Site : 
# @File : deco_example.py
# @Software: PyCharm
from time import ctime, sleep


def makeBold(func):
    def wrapper():
        return "<b>" + func() + "</b>"

    return wrapper


def makeItalic(func):
    def wrapper():
        return "<i>" + func() + "</i>"

    return wrapper


@makeBold
def test1():
    return "hello world-1"


@makeItalic
def test2():
    return "hello world-2"


@makeBold
@makeItalic
def test3():
    return "hello world-3"


# print(test1())
# print(test2())
# print(test3())

#通用装饰器
 #不定长参数
 #有返回值
def timefunc(func):
    def wrqpperfunc(a, b):
        print("%s called at %s" % (func.__name__, ctime()))
        print(a, b)
        ret = func(a, b)
        return ret

    return wrqpperfunc


@timefunc
def test(a, b):
    print(a + b)


test(1, 3)
