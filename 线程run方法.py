#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/29 22:05
# @Author : juingzhou
# @Site : 
# @File : 线程run方法.py
# @Software: PyCharm
import threading, time


class MyThread(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num = num
    def run(self):
        for i in range(10):
            time.sleep(1)
            print("I am %s @ %s" % (self.name, str(i)),self.num)

for i in range(5):
    t = MyThread(i)
    t.start()
