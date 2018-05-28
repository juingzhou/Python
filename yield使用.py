#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/27 17:26
# @Author : juingzhou
# @Site : 
# @File : yield使用.py
# @Software: PyCharm

from collections import Iterable
from collections import Iterator

# 生成器
#
# def fib(num):
#     a, b = 0, 1
#     n = 0
#     while n < num:
#         yield b  # yield函数执行到这里就会交出CPU控制权，停止执行，调用next再继续执行
#         a, b = b, a + b
#         n += 1
#
#
# if isinstance(fib(10), Iterable):  # 判断是否可迭代
#     for i in fib(10):
#         print(i)

l = [x for x in range(10)]
it = iter(l)#生成迭代器   #将可迭代对象转换成迭代器
print(isinstance(it, Iterator))#判断是否为迭代器
