#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/29 17:10
# @Author : juingzhou
# @Site : 
# @File : 进程池.py
# @Software: PyCharm

from multiprocessing import Pool
import random, time, os


def worker(msg):
    start_time = time.time()
    print("%s开始执行，进程号为:%s" % (msg, os.getpid()))
    time.sleep(random.random() * 2)
    stop_time = time.time()
    print("%s执行完毕，耗时为：%s" % (msg, stop_time - start_time))


if __name__ == "__main__":
    # 定义进程池，最大进程数为3
    pool = Pool(3)
    for i in range(10):
        # pool.apply_async(要调用的目标，(传递给目标的参数元祖))
        # 每次循环将会用空闲出来的子进程去调用目标
        # pool.apply_async(worker, (i,))#异步并发，非阻塞方式并行执行
        pool.apply(worker, (i,))#同步并发，阻塞方式
    print("start")
    pool.close()  # 关闭进程池，关闭后pool不再接收新的请求
    pool.join()  # 等待pool所有子进程执行完成，必须放在close语句之后
    # 父进程等待进程池的结束
    print("end")
