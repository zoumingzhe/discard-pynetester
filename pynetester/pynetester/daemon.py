#!/usr/bin/env python3
# coding=utf-8
# ----------------------------------------------------------------------------------------------------
from concurrent.futures import ThreadPoolExecutor
import socket
import time
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
# ----------------------------------------------------------------------------------------------------
    @staticmethod
    def encode(item):
        # typestr = item['type'].upper()
        # if typestr not in ['TCP', 'UDP']:
        #     err = "type {0} not TCP or UDP".format(typestr)
        #     raise Exception(err)
        info = {
            # 'type':{'TCP':socket.SOCK_STREAM,'UDP':socket.SOCK_DGRAM}[typestr],
            'addr':(item['host'], int(item['port']))
        }
        print(info)
        return info
# ----------------------------------------------------------------------------------------------------
    @staticmethod
    def listen(info, threadpool):
        try:
            addr = info['addr']
            print("Listening {}:{}".format(addr[0], addr[1]))
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # bind
            try:
                sock.bind(addr)         # 绑定端口
            except Exception as e:
                err = "Port {} is used".format(addr[1])
                raise Exception('exit_listen', err)
            # listen
            while True:
                sock.listen(5)          # 等待客户端连接
                c,addr = sock.accept()  # 建立客户端连接
                # todo：测试
                print("Connect {0}".format(addr))
        except Exception as e:
            sock.close()
            if e.args[0] != 'exit_listen':
                print(str(type(e)) + str(e))
                daemon.listen(info, threadpool)
            else:
                print(e.args[1])
                raise e
# ----------------------------------------------------------------------------------------------------
    @staticmethod
    def server(config):
        info = []
        bind = config['bind']
        for item in bind:
            item['host'] = '0.0.0.0'
            info.append(daemon.encode(item))
        thd_num = len(info) * 5
        thdpool = ThreadPoolExecutor(max_workers=thd_num, thread_name_prefix="Server")
        for i in info:
            future = thdpool.submit(daemon.listen, i, thdpool)
            time.sleep(1)
        thdpool.shutdown(wait=True)
# ----------------------------------------------------------------------------------------------------
    @staticmethod
    def client(config = {'connect':[{'type':'TCP','host':'127.0.0.1','port':10517}]}):
        info = []
        for item in config['connect']:
            info.append(daemon.encode(item))
        # thd_num = len(info) * 5
        # thdpool = ThreadPoolExecutor(max_workers=thd_num, thread_name_prefix="Client")
        for i in info:
            # future = thdpool.submit(daemon.listen, i, thdpool)
            # sock = socket.socket(socket.AF_INET, i['type'])
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(i['addr'])
# ----------------------------------------------------------------------------------------------------
