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
        self.func = func

    def __call__(self):
        print("---装饰器的功能---")
        self.func()


@deco  # 调用并生成Test的一个对象，所以会调用__init__方法，比并且把下面装饰的函数作为参数传进去
def test():
    print("---test---")


test()  # 调用Test的一个对象的__call__方法
