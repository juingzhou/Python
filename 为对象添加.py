#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/28 10:22
# @Author : juingzhou
# @Site : 
# @File : 为对象添加.py
# @Software: PyCharm
import types


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


def showInfo(self):
    print(self.name)
    print(self.age)

@classmethod
def fun1(cls):
    print("classmethod")


@staticmethod
def fun2(a,b):
    print(a+b)

Person.fun1 = fun1#添加类方法
Person.fun2 = fun2
p = Person("zjj", "27")
p.showInfo = types.MethodType(showInfo, p)  # 为对象添加实例方法
p.showInfo()
p.sex = "male"  # 为对象动态添加属性
print(p.sex)
p.fun1()
p.fun2(3,4)
Person.addr = "CD"  # 为类动态添加属性
p2 = Person("hh", "72")
print(p.addr)
print(p2.addr)
