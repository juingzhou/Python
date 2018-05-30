#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/30 13:09
# @Author : juingzhou
# @Site : 
# @File : 线程执行控制.py
# @Software: PyCharm

import threading,time
class Task1(threading.Thread):
    def run(self):
        while True:
            if task1.acquire():
                print("task1'''")
                task2.release()
class Task2(threading.Thread):
    def run(self):
        while True:
            if task2.acquire():
                print("task2'''")
                task3.release()
class Task3(threading.Thread):
    def run(self):
        while True:
            if task3.acquire():
                print("task3'''")
                task1.release()




if __name__ =="__main__":
    task1 = threading.Lock()
    task2 = threading.Lock()
    task2.acquire()
    task3 = threading.Lock()
    task3.acquire()
    t1 = Task1()
    t2 = Task2()
    t3 = Task3()
    t1.start()
    t2.start()
    t3.start()