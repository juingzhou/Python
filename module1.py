#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/26 11:08
# @Author : juingzhou
# @Site : 
# @File : module1.py
# @Software: PyCharm
# import test
__all__ = ["isnull"]
def isnull(str):
    if not str:
        return True
    elif str.strip() == '':
        return True
def test1():
    print("module1中的test1的方法")

if __name__ == "__main__":
    print(isnull(""))
