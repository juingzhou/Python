#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/28 11:35
# @Author : juingzhou
# @Site : 
# @File : garbage_collection.py
# @Software: PyCharm

'''
Garbage Collection(垃圾回收)
1.为新生成的对象分配内存
2.识别那些垃圾对象
3.从垃圾对象那回收内存

python采用的是引用技术机制为主，标记-清除和分代收集两种机制为辐的策略

引用计数机制的缺陷是循环引用的问题
import gc
gc.disable()可以关闭gc内存

有三种情况会触发垃圾回收:
1.调用gc.collect()
2.gc模块的计数器达到阈值的时候
3.程序推出的时候

gc模块唯一处理不了的是循环引用的类都有__del__方法，
所以项目要避免定义__del__方法
'''

import sys
a = 1223211
print(sys.getrefcount(a))


