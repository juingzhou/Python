#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/25 19:59
# @Author : juingzhou
# @Site : 
# @File : 单例模式.py
# @Software: PyCharm

# class User(object):
#     __instance = None
#     def __init__(self,name,pw):
#         self.name = name
#         self.password = pw
#     @classmethod
#     def get_instance(cls,name,password):
#         if not cls.__instance:
#             cls.__instance=User(name,password)
#         return cls.__instance
#
# # u1 = User("aa","123")
# # u2 = User("ww","234")
# # print(u1 is u2) #如果判断表达式返回True，这两个对象是一个对象，并且内存地址一样
# # print(id(u1))
# # print(id(u2))
# u1 = User.get_instance("aa","123")
# u2 = User.get_instance("ss","234")
# print(id(u1))
# print(id(u2))
# print(u1.name)
# print(u2.name)
class User(object):

    __instance = None
    def __init__(self, name):
        self.name = name
    # @classmethod
    def __new__(cls, name):
        if not cls.__instance: #保证Object.__new__（）方法只执行一次
            cls.__instance = object.__new__(cls)
        return cls.__instance
u1 = User("aa")
u2 = User("ss")
print(u1 is u2)
print(u1.name)
print(u2.name)