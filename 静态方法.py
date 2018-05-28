#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/25 19:15
# @Author : juingzhou
# @Site : 
# @File : 静态方法.py
# @Software: PyCharm


class A(object):

    name = "aa"

    @staticmethod
    def test():#属于类，没有默认传递的参数，可以通过类对象来说明，也可以通过类名来调用
        A.name = "zjj"
        print("A.test类的静态方法")
A.test()
print(A.name)