#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/30 13:32
# @Author : juingzhou
# @Site : 
# @File : thread_queue.py
# @Software: PyCharm
from queue import Queue
import time,threading


class Producter(threading.Thread):
    def run(self):
        while True:
            if q.qsize()<30:
                for i in range(50):
                    q.put("产品"+str(i))
                    print("生产了产品"+str(i))
                time.sleep(0.5)
class Comsumer(threading.Thread):
    def run(self):
        while True:
            if q.qsize()>10:
                for i in range(3):
                    print("%s消费了%s"%(self.name,q.get()))
                time.sleep(0.5)

if __name__ =="__main__":
    q = Queue()
    for i in range(20):
        q.put("产品%s"%str(i))
    for j in range(5):
        c = Comsumer()
        c.start()
    for k in range(2):
        p = Producter()
        p.start()
