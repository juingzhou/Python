#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/28 21:28
# @Author : juingzhou
# @Site : 
# @File : 进程.py
# @Software: PyCharm

'''
多进程：
程序(program)是一个指令的集合
进程(Process正在执行中的程序)是一个静态的概念
1.进程是程序的一侧静态执行过程，占用特定的地址空间
2.每个进程都是独立的，由3部分组成cpu，data，code
3.缺点：内存的浪费，cpu的负担
4.数据区，代码区，堆，栈
'''

import os

pid = os.fork()

if pid < 0:
    print("fork()调用失败")
elif pif == 0:
    print("我是子进程(%s),我的父进程是(%s)" % (os.getpid(), os.getppid()))
    x += 1
else:
    print("我是父进程(%s),子进程(%s)" % (os.getpid(), pid))
