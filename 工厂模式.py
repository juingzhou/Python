#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/25 23:06
# @Author : juingzhou
# @Site : 
# @File : 工厂模式.py
# @Software: PyCharm
class Person(object):
    def __init__(self, name):
        self.name = name

    def work(self, axe_type):
        print("%s开始工作了" % (self.name))
        # person完成work,需要使用一把斧头
        # aex = Aex("石斧")
        # aex = StoneAxe("石岗岩")
        # aex = SteelAxe("钢铁斧头")
        aex = Factory.creat_axe(axe_type)
        aex.cut_tree()
        # 在原始社会，人类需要一把石斧


class Aex(object):
    def __init__(self, name):
        self.name = name

    def cut_tree(self):
        print("%s斧头开始砍树" % (self.name))


class StoneAxe(Aex):
    def cut_tree(self):
        print("使用石头做的斧头砍树")


class SteelAxe(Aex):
    def cut_tree(self):
        print("使用钢铁做的斧头砍树")


class Factory(object):
    @staticmethod
    def creat_axe(type):
        if type == "stone":
            return StoneAxe(type)
        elif type == "steel":
            return SteelAxe(type)
        else:
            print("传入的斧头类型有错误")


p1 = Person("小明")
# p1.work("stone")
p1.work("steel")
