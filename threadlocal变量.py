#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/30 13:48
# @Author : juingzhou
# @Site : 
# @File : threadlocal变量.py
# @Software: PyCharm

'''
ThreadLocal变量
1.一个ThreadLocal变量虽然时全局变量，大师每个线程都只是读写自己线程的独立副本
  ，互不干扰。ThreadLocal解决了参数在一个线程中各个参数之间互相传递的问题
2.可以理解为全局变量local_school是一个dict，可以绑定其他变量
3.ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份
   信息等，这样一个线程的所有调用到的处理函数都可以非常方便地区访问这些资源
'''

import threading

# 创建threadlocal变量
local_school = threading.local()


def process_student():
    std_name = local_school.student
    std_age = local_school.age
    print("hello %s %s in %s" % (std_name, std_age, threading.current_thread().name))


def processThread(name, age):
    local_school.student = name
    local_school.age = age
    process_student()


t1 = threading.Thread(target=processThread, args=("hh", 14,), name="t1")
t2 = threading.Thread(target=processThread, args=("ss", 15,), name="t2")
t1.start()
t2.start()
