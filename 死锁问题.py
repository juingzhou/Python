#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/30 12:40
# @Author : juingzhou
# @Site : 
# @File : 死锁问题.py
# @Software: PyCharm


import threading,time
class MyThraed1(threading.Thread):
    def run(self):
        if mutxA.acquire(True):
            print("thread1 do something....")
            time.sleep(1)
            if mutxB.acquire(True):
                print("thread2 do something..")
                mutxB.release()
            mutxA.release()


class MyThraed2(threading.Thread):
    def run(self):
        if mutxB.acquire(True):
            print("thread2 do something....")
            time.sleep(1)
            if mutxA.acquire(True):
                print("thread2 do something..")
                mutxA.release()
            mutxB.release()

mutxA = threading.Lock()
mutxB = threading.Lock()
mythread1 = MyThraed1()
mythread1.start()
mythread2 = MyThraed2()
mythread2.start()


