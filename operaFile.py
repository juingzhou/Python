#!/usr/bin/env python
#-*- coding: utf-8 -*-


import os
def operaFile():
    print('创建一个名字为text.txt的文件，并在其中写入Hello Python')
    print('先得保证 text.txt不存在')

    fp = open('text.txt','w')
    str = input('请输入文字:')
    fp.write(str)
    fp.close()
    print('不要忘记用close关闭文件')



    print('使用with as就可以了')
    with open('text.txt','r') as fp:
        st = fp.read()
    print('text.txt的内容为：%s' %st)

if __name__ == '__main__':
    operaFile()
