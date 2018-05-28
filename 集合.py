#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/26 15:40
# @Author : juingzhou
# @Site : 
# @File : 集合.py
# @Software: PyCharm

s1 = "jkasjdkiuwbd"
results = {}
for i in set(s1):
    results[i] = s1.count(i)
print(sorted(results.items(), key=lambda item: item[1], reverse=True)[0:3])
