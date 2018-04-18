#!/usr/bin/env python
#-*- coding: utf-8 -*-

from urllib import request
import time
import platform
import os

def clear():
    '''该函数用于清屏'''
    print('内容较多，显示3秒后翻页')
    time.sleep(3)
    OS = platform.system()
    if (OS =='Windows'):
        os.system('cls')
    else:
        os.system('clear')

def linkBaidu():
    url = 'https://www.baidu.com/'
    try:
        response = request.urlopen(url,timeout=3)

    except request.URLError:
        print('网络地址错误')
        exit()

    with open('baidu.txt','w') as fp:
        fp.write(str(response.read()))
    print("获取url信息，response.geturl() \n: %s" %response.geturl())
    print("获取返回代码，response.getcode() \n :%s" %response.getcode())
    print("获取返回信息，response.info() \n :%s" %response.info())

if __name__ =='__main__':
    linkBaidu()