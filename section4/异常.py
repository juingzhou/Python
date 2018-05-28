#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/26 0:19
# @Author : juingzhou
# @Site : 
# @File : 异常.py
# @Software: PyCharm
f = None
try:
    f = open("test1.txt", 'r')
    f.read()
except FileNotFoundError as ex:
    print("找不到文件")     #捕获到异常之后不会回头继续执行之前的代码
    print(ex.strerror)
else:
    print("无异常")
finally:
    if f:
        f.close()
   
    else:
        pass


