#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/28 15:10
# @Author : juingzhou
# @Site : 
# @File : 内建函数.py
# @Software: PyCharm
# map 返回迭代器
for i in map(lambda x: x ** 2, [1, 2, 3]):
    print(i, end='  ')
print()
for i in map(lambda x, y: x + y, [1, 2, 3], [4, 5, 6]):
    print(i, end='  ')
print()


def fun(x, y):
    return x + y


l1 = [1, 2, 3]
l2 = [4, 5, 6]

for i in map(fun, l1, l2):
    print(i, end='  ')
print()
print('-' * 50)

# 过滤器
f = filter(lambda x: x % 2, [1, 2, 3, 4])
for i in f:
    print(i, end='  ')
print()
for i in filter(None, "Hello"):
    print(i, end='  ')
print()
print('-' * 50)


#functools是python2.5被引入的，一些工具函数放在此包里
from functools import reduce

print(reduce(lambda x, y: x + y, [1, 2, 3, 4]))

print(reduce(lambda x, y: x + y, [1, 2, 3, 4], 5))

print(reduce(lambda x, y: x + y, ['aa', 'bb', 'cc'], 'dd'))
print(('-'*50).center(50))
