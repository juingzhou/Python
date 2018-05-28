#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/28 14:53
# @Author : juingzhou
# @Site : 
# @File : 属性拦截器.py
# @Software: PyCharm

class School(object):
    def __init__(self, subject1):
        self.subject1 = subject1
        self.subject2 = "cpp"
    #重写属性访问拦截器
    def __getattribute__(self, obj):
        if obj == "subject1":
            print(obj)
            print("log subject1")
            return "redirect python"
        else:#注意，如果注释后面两行，其他属性就会不能正常访问
            return object.__getattribute__(self, obj)
school = School("Python")
print(school.subject1)
print(school.subject2)

