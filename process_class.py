#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/29 12:49
# @Author : juingzhou
# @Site : 
# @File : process_class.py
# @Software: PyCharm

from multiprocessing import Process
import time,os

class Process_class(Process):
    def __init__(self,interval):
        Process.__init__(self)
        self.interval = interval
    def run(self):
        time_start = time.time()
        print("子进程开始")
        time.sleep(self.interval)
        stop_time = time.time()
        print("子进程：%s,父进程：%s,消耗时间:%s"%(os.getpid(),os.getppid(),stop_time-time_start))

if __name__ =="__main__":
    for i in range(5):
        start_time = time.time()
        p = Process_class(i+1)
        p.start()
        # p.join()
        stop_time = time.time()
        print("子进程结束,消耗时间:%s"%(stop_time-start_time))

