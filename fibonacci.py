#!/usr/bin/env python
#-*- coding: utf-8 -*-

class Fibonacci(object):

    def __init__(self):
        self.fList = [0,1]
        # print(self.fList[-1],self.fList[-2])
        self.main()

    def main(self):
        listLen = input('请输入fibonacci数列的长度(3-50):')
        self.checkLen(listLen)
        while len(self.fList) < int(listLen):
            self.fList.append(self.fList[-1]+self.fList[-2])
            print(self.fList)
        print('得到的Fibonacci数列为:\n %s ' %self.fList)
    def checkLen(self,length):
        lengthlist = map(str,range(3,51))
        if length in lengthlist:
            print('输入长度符合标准，继续运行')
        else:
            print('只能输入3-50，太长不是算不出，只是没必要')
            exit()


if __name__ =='__main__':
    fi = Fibonacci()

