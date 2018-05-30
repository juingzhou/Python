#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/29 21:51
# @Author : juingzhou
# @Site : 
# @File : 查看线程数量.py
# @Software: PyCharm

import threading,time

def sing():
    for i in range(10):
        print("I am singing...")
        time.sleep(1)

def dance():
    for i in range(10):
        print("I am dancing...")
        time.sleep(1)

if __name__ == "__main__":

    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()
    while True:
        length = len(threading.enumerate())
        print("当前线程数量为:%s"%length)
        if len(threading.enumerate())<=1:
            break
        time.sleep(0.5)
