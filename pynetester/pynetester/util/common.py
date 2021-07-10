#!/usr/bin/env python3
# coding=utf-8
# ----------------------------------------------------------------------------------------------------
from collections import namedtuple
import re
# ----------------------------------------------------------------------------------------------------
t_addr = namedtuple('addr', ['host', 'port'])
# ----------------------------------------------------------------------------------------------------
def decode_ip_port(ip_port):
    '''
    解析IP:PORT格式
    '''
    if type(ip_port) == str:
        rule = '''^(?P<ip>\d+\.\d+\.\d+\.\d+):(?P<port>\d+)'''
        rset = re.search(rule, ip_port)
        if rset:
            ip = rset.group('ip')
            port = rset.group('port')
            return t_addr(ip, int(port))
# ----------------------------------------------------------------------------------------------------
