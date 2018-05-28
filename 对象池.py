#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/28 11:21
# @Author : juingzhou
# @Site : 
# @File : 对象池.py
# @Software: PyCharm
"""
1.Python为了优化速度，使用了小整数【-5，257）对象池，避免为整数频繁申请和销毁
  内存空间
2.同理，单个字符也提供对象池，常驻内存
3.每个大整数，均创建一个新的对象
4.对于字符串，单个单词，不可修改，默认开启intern机制，采用引用技术机制引用对象，
  引用计数为0，则销毁
"""


