#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/29 11:01
# @Author : juingzhou
# @Site : 
# @File : 多进程.py
# @Software: PyCharm
'''
多进程Process
1.创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例
用start()方法启动，这样创建进程比fork()还要简单

2.Process([group[,target[,name[,args[,kwargs]]]]])
target:表示这个进程实例所调用对象
args:表示调用对象的位置参数元祖
kwargs:表示调用对象的关键字参数字典
name:为当前进程实例的别名
group:大多数情况下用不到

3.join()方法可以等待子进程结束再继续往下执行，通常用于子进程间的同步
4.is_alive()判断进程是否还执行
5.join([timeout])是否等待进程实例执行结束，或者等待多少秒
6.start()启动进程
7.run()如果没有给定target参数，对这个对象调用start()方法，就将要执行对象中的run()方法
8.terminate()不管方法是否完成，立即终止

pid当前进程实例的PID值
'''

from multiprocessing import Process
import os, time


#
# def run_doc(name):
#     time.sleep(5)
#     print("子进程运行中，name = %s,pid = %d，父进程为%s"% (name, os.getpid(),os.getppid()))
# if __name__ =="__main__":
#
#     print("父进程%d."%(os.getpid()))
#     #创建子进程
#     p = Process(target=run_doc, args=('test',))
#     print("子进程 将要执行")
#     #开始执行子进程
#     p.start()
#     #等待子进程执行结束，父进程才开始执行
#     p.join()
#     print("子进程已结束")

def func(name, num, **kwargs):
    time.sleep(2)
    print("子进程：%s, name:%s,num:%s" % (os.getpid(), name, num))
    for k, v in kwargs.items():
        print("%s:%s" % (k, v))


if __name__ == "__main__":
    print("父进程：%s" % os.getpid())
    p = Process(target=func, name="p1", args=('test', 10), kwargs={'a': 30, 'b': 20})
    p.start()
    p.join()
