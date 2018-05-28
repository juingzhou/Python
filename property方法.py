#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/27 14:45
# @Author : juingzhou
# @Site : 
# @File : property方法.py
# @Software: PyCharm
class Test(object):
    def __init__(self):
        self.__num = 100

    @property
    def num(self):  # getter
        return self.__num

    @num.setter
    def num(self, num):  # setter
        if num < 100:
            self.__num = num

    # num = property(getNum, setNum)


t = Test()
t.num = 20
print(t.num)
