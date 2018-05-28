#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/27 21:06
# @Author : juingzhou
# @Site : 
# @File : 闭包.py
# @Software: PyCharm

# 闭包：内部函数对外部函数作用域里变量的引用(菲全局变量)，则称内部函数为闭包
# 定义一个函数
# def fun4():
#     # 在函数内部再定义一个函数，并且这个函数用到了外部函数的变量
#     def fun5():
#         print("fun5")
#
#     return fun5
#
# res = fun4()
# res()
def outter(num):
    def inner(num1):
        return num+num1
    return inner

outter1 = outter(10)(20)

print(outter1)