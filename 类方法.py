#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/25 18:58
# @Author : juingzhou
# @Site : 
# @File : 类方法.py
# @Software: PyCharm
class A(object):
    name = "aa"
    def test1(self):
        print("A.test1的方法")
    @classmethod
    def test2(cls):#类方法一定要在类方法上面加上一个修饰器，类方法的参数cls，代表当前的类
        cls.name = "ss"
        print("A.test2的方法")

#A.test1()
A.test2()

a = A()
a.test1()
a.test2()
a.name
