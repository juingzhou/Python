#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/28 10:42
# @Author : juingzhou
# @Site : 
# @File : 限制修改对象属性.py
# @Software: PyCharm

class student(object):
    __slots__ = ("name", "age")#限制修改对象属性

stu = student()
stu.name = "hh"
stu.age = 12
print(stu.name)
print(stu.age)
stu.sex = "male"
