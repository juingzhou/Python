#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/28 11:04
# @Author : juingzhou
# @Site : 
# @File : decorator_class.py
# @Software: PyCharm

class deco(object):
    def __init__(self, func):
        print("---初始化---")
        print("func name is %s" % func.__name__)
        self.__func = func

    def __call__(self):
        print("---装饰器的功能---")
        self.__func()


@deco
def test():
    print("---test---")


test()
