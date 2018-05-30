#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/29 21:37
# @Author : juingzhou
# @Site : 
# @File : thread.py
# @Software: PyCharm
import time, threading


def func(num):
    print("这是线程%s执行" % num)
    time.sleep(2)


if __name__ == "__main__":
    for i in range(5):
        t = threading.Thread(target=func, args=(i+1,))
        t.start()
    print("主线程结束")
