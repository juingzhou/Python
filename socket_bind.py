#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2018/5/30 19:56
# @Author : juingzhou
# @Site : 
# @File : socket_bind.py
# @Software: PyCharm
import socket

udp_bind = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
bind = ('',9999)
udp_bind.bind(bind)

recv_data = udp_bind.recvfrom(1024)
print(recv_data)
udp_bind.close()