#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/26 0:04
# @Author : juingzhou
# @Site : 
# @File : 工厂方法模式.py
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
        aex = Stone_Axe_Factory().creat_axe(axe_type)
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


# 工厂类
class Factory(object):
    # 生产斧头，根据用户指定的类型来生产
    def creat_axe(self,type):
        pass


class Stone_Axe_Factory(Factory):
    def creat_axe(self,type):
        return StoneAxe(type)


class Steel_Aex_Factory(Factory):
    def creat_axe(self,type):
        return SteelAxe(type)


p1 = Person("小明")
# p1.work("stone")
p1.work("stone")
