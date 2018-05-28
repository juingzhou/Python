#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/26 15:12
# @Author : juingzhou
# @Site : 
# @File : 列表推导世.py
# @Software: PyCharm


print([i for i in range(1, 10) if i % 2 == 0] )


print([i**2 for i in range(1, 10)])


print([x*y for x in range(1, 3) for y in range(1, 3) if x*y%2==0])

print([(x,y) for x in range(1, 3) for y in range(1, 3) if x*y%2==0])
a=[1, 2, 3]
print([[a[0]+x, a[1]+x, a[2]+x] for x in range(0, 99) if x%3==0])