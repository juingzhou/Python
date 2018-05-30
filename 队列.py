#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/29 19:09
# @Author : juingzhou
# @Site : 
# @File : 队列.py
# @Software: PyCharm
from multiprocessing import Manager, Process, Queue, Pool
import time, os, random


def write(q):
    for item in range(100):
        print("正在往消息队列写入%s" % item)
        q.put(item)
        time.sleep(random.random())


def reader(q):
    while True:
        if not q.empty():
            item = q.get()
            print("从消息队列读出%s" % item)
            time.sleep(random.random())
        else:
            break


# if __name__ =="__main__":
#     q = Queue()
#     print("开始读数据")
#     pw = Process(target=write,args=(q,))
#     pw.start()
#     pw.join()
#     pr = Process(target=reader,args=(q,))
#     pr.start()
#     pr.join()
#     print("所有数据已读完")
if __name__ == "__main__":
    q = Manager().Queue()
    pool = Pool(5)
    pool.apply(write, (q,))
    pool.apply(reader, (q,))
    pool.close()
    pool.join()
    print("所有数据已读完")
