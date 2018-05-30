#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/30 11:43
# @Author : juingzhou
# @Site : 
# @File : threadingsafe.py
# @Software: PyCharm

import threading, time

g_num = 0

'''
g_num +=1
g_num = g_num+1
g_num原来存放在内存中

操作为成三步：
1.cpu先从内存中将g_num的值读到寄存器
2.在寄存器中对g_num的值读出来加1
3.将寄存器中的值写回到内存
'''
def func1():
    global g_num
    for i in range(20):
        mutxFlag = mutx.acquire(True)
        if mutxFlag:
            g_num += 1
            mutx.release()
def func2():
    global g_num
    for i in range(200):
        mutxFlag = mutx.acquire(True)
        if mutxFlag:
            g_num += 1
            mutx.release()
#创建锁
mutx = threading.Lock()
t1 = threading.Thread(target=func1)
t1.start()
t2 = threading.Thread(target=func2)
t2.start()
print("main thread g_num:%s" % g_num)
