#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/25 19:36
# @Author : juingzhou
# @Site :
# @File : _new_方法.py
# @Software: PyCharm

class User(object):
    def __init__(self, name, password):
        # pass
        self.name = name
        self.password = password
        print("对象已经构建好了，由解释器自动回调，对对象已经初始化")
    #new方法是当对象构建的时候由解释器自动回调的方法，该方法必须返回当前类的对象。
    def __new__(cls, username, password):
        # pass
        print("User类的对象开始构建")
        return object.__new__(cls)
    def __str__(self):
        return "用户名:%s,密码:%s" % (self.name, self.password)
u = User("123", "234")
print(u)
# print(u.name)
# print(u.password)
