#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/26 15:59
# @Author : juingzhou
# @Site : 
# @File : list去重.py
# @Software: PyCharm
l = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5,7,3,3,1,3,5,2]



def change_list(l1):
    result = []
    for i in l1:
        if not (i in result):
            result.append(i)
    return result

if __name__ =="__main__":
    print(change_list(l))