#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/30 20:01
# @Author : juingzhou
# @Site : 
# @File : socket_echo.py
# @Software: PyCharm

import socket
from time import ctime
import threading,sys


def send():
    while True:
        send_info = input("请输入:").encode()
        if send_info =="q":
            sys.exit()
        else:
            socket_echo.sendto(send_info, send_addr)
            print("已发送    %s" % ctime())


def recv():
    while True:
        recv_data = socket_echo.recvfrom(1024)
        s = bytes.decode(recv_data[0])
        print("收到%s    %s    %s" % (recv_data[1][0], s, ctime()))
if __name__ =="__main__":
    socket_echo = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bind_addr = ('', 9900)
    socket_echo.bind(bind_addr)
    send_addr = ('127.0.0.1', 9999)
    s = threading.Thread(target=send)
    r = threading.Thread(target=recv)
    s.start()
    r.start()
    socket_echo.close()
