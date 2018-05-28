#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/26 16:10
# @Author : juingzhou
# @Site : 
# @File : create_list.py
# @Software: PyCharm
import random
import sys


def creat_set_list(n):
    results = []
    while True:
        randNum = random.randint(1, n)
        if not (randNum in results):
            results.append(randNum)
        if len(results) == n:
            break
    return results


if __name__ == "__main__":
    print(creat_set_list(20))
