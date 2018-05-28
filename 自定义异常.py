#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/26 10:29
# @Author : juingzhou
# @Site : 
# @File : 自定义异常.py
# @Software: PyCharm

class PersonException(Exception):
    def __init__(self, pw, mini_length):
        self.password = pw
        self.mini_length = mini_length

    def __str__(self):
        return "%s密码是错误的，密码的最小长度为%s" % (self.password, self.mini_length)


def reg(username, password):
    if len(password) < 6:
        raise PersonException(password, 6)  # 抛出你指定的异常
    else:
        print("用户名为:%s,密码为:%s" % (username, password))


try:
    reg("hh", "123123")
except Exception as ex:
    print(ex)
