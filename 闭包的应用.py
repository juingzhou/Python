#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/27 23:11
# @Author : juingzhou
# @Site : 
# @File : 闭包的应用.py
# @Software: PyCharm


def line_conf(a, b):
    def line(x):
        return a * x + b

    return line

fun = line_conf(1, 2)
print(fun(4))
