#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/30 21:37
# @Author : juingzhou
# @Site : 
# @File : socket_echo1.py
# @Software: PyCharm

import socket
from time import ctime

socket_echo1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bind_addr = ('', 9999)
socket_echo1.bind(bind_addr)
send_addr = ('127.0.0.1', 9900)
while True:
    send_info = input("请输入:").encode()
    if send_info == "q":
        break
    else:

        recv_data = socket_echo1.recvfrom(1024)
        s = bytes.decode(recv_data[0])
        print("收到   %s  %s    %s" % (recv_data[1][0], s, ctime()))

        socket_echo1.sendto(send_info, send_addr)
        print("已发送    %s" % ctime())


socket_echo1.close()
