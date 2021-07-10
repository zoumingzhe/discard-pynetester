#!/usr/bin/env python3
# coding=utf-8
# ----------------------------------------------------------------------------------------------------
import time
import socket
from .core.server import listen_handle
from .util.common import decode_ip_port
from concurrent.futures import ThreadPoolExecutor
# ----------------------------------------------------------------------------------------------------
# 类 daemon
# ----------------------------------------------------------------------------------------------------
# 变更履历：
# 2021-05-17 | Zou Mingzhe   | Ver0.1  | 初始版本
# ----------------------------------------------------------------------------------------------------
# MAP：
# 未开发 | server(self, ...)            | 压缩文件
# ----------------------------------------------------------------------------------------------------
class daemon:
    """
    daemon类守护线程。
    """
# # ----------------------------------------------------------------------------------------------------
#     @staticmethod
#     def encode(item):
#         # typestr = item['type'].upper()
#         # if typestr not in ['TCP', 'UDP']:
#         #     err = "type {0} not TCP or UDP".format(typestr)
#         #     raise Exception(err)
#         info = {
#             # 'type':{'TCP':socket.SOCK_STREAM,'UDP':socket.SOCK_DGRAM}[typestr],
#             'addr':(item['host'], int(item['port']))
#         }
#         print(info)
#         return info
# ----------------------------------------------------------------------------------------------------
    @staticmethod
    def server(config):
        info = []
        for item in config['port']:
            ip_port = '0.0.0.0:' + str(item)
            address = decode_ip_port(ip_port)
            info.append((address.host, address.port))
        thd_num = len(info) * 10
        thdpool = ThreadPoolExecutor(max_workers=thd_num, thread_name_prefix="Server")
        for i in info:
            future = thdpool.submit(listen_handle, i, thdpool)
            # time.sleep(0.01)
        thdpool.shutdown(wait=True)
# ----------------------------------------------------------------------------------------------------
    @staticmethod
    def client(config = {'connect':[{'type':'TCP','host':'127.0.0.1','port':10517}]}):
        info = []
        for item in config['connect']:
            addr = decode_ip_port(item)
            info.append((addr.host, addr.port))
        # thd_num = len(info) * 5
        # thdpool = ThreadPoolExecutor(max_workers=thd_num, thread_name_prefix="Client")
        for i in info:
            # future = thdpool.submit(daemon.listen, i, thdpool)
            # sock = socket.socket(socket.AF_INET, i['type'])
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(i)
# ----------------------------------------------------------------------------------------------------
