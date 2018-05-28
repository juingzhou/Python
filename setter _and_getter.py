#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/27 14:35
# @Author : juingzhou
# @Site : 
# @File : setter _and_getter.py
# @Software: PyCharm

class Test(object):
    def __init__(self):
        self.__num = 100
    def getNum(self):
        return self.__num
    def setNum(self,num):
        if num<100:
            self.__num = num

t = Test()
t.setNum(30)
print(t.getNum())

