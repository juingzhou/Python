#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/29 22:34
# @Author : juingzhou
# @Site : 
# @File : 线程共享全局变量.py
# @Software: PyCharm
import threading,time

num = 0
def fun1():
    global num
    for i in range(10):
        num += 1
        print("这是线程fun1，num为:%d"%(num))


def fun2():
    global num
    print("这是线程fun2，num为:%d"%(num))

print("主线程启动")
t1= threading.Thread(target=fun1)
t1.start()
time.sleep(1)
t2= threading.Thread(target=fun2)
t2.start()