#!/usr/bin/env python3
# coding=utf-8
# ----------------------------------------------------------------------------------------------------
import time
import socket
# ----------------------------------------------------------------------------------------------------
def listen_handle(addr, threadpool):
    '''
    监听处理主函数
    '''
    try:
        time.sleep(1)
        # addr = info['addr']
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
            listen_handle(info, threadpool)
        else:
            print(e.args[1])
            raise e
# ----------------------------------------------------------------------------------------------------
