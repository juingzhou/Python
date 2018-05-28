#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/28 15:41
# @Author : juingzhou
# @Site : 
# @File : 偏函数.py
# @Software: PyCharm

import functools


def showarg(*args, **kwargs):
    print(args)
    print(kwargs)


l = [1, 2, 3]
p1 = functools.partial(showarg, 1, 2, 3)
p1()
p1(l)
p1(a='123', b='456')
