#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/30 19:44
# @Author : juingzhou
# @Site : 
# @File : socket_udp.py
# @Software: PyCharm
import socket
from time import ctime

udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
send_addr = ('127.0.0.1', 9999)
while True:
    send_info = input("请输入:").encode()
    if send_info == "q":
        break
    else:
        udp.sendto(send_info, send_addr)
        print("已发送    %s" % ctime())

udp.close()
