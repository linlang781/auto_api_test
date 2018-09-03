#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: liuyu
@license: None
@file: HttpRequest.py
@time: 17-4-28 下午2:16
"""

import requests
# import socket
# import json
from lib.log import LOG

METHODS = ['GET', 'POST', 'HEAD', 'TRACE', 'PUT', 'DELETE', 'OPTIONS', 'CONNECT']


class UnSupportMethodException(Exception):
    """当传入的method的参数不是支持的类型时抛出此异常。"""
    pass


class RequestSession(object):
    """
    http请求的client。初始化时传入url、method等，可以添加headers和cookies，但没有auth、proxy。
    """
    def __init__(self, ua=None, verify=False, timeout=10):
        """headers: 字典。 例：headers={'Content_Type':'text/html'}，cookies也是字典。"""
        self.session = requests.session()
        self.verify = verify
        self.timeout = timeout
        self.ua = ua if ua else 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.79 Safari/537.36'

    def set_headers(self, headers):
        if headers:
            self.session.headers.update(headers)

    def set_cookies(self, cookies):
        cookies_dict = {}
        cookies_type = type(cookies)
        if cookies_type not in [str, dict, requests.sessions.cookielib.CookieJar]:
            raise Exception('cookie参数类型错误')
        if cookies_type == str:
            cookie_pairs = cookies.split('；')
            for cookie_pair in cookie_pairs:
                k, v = cookie_pair.split('=', maxsplit=1)
                cookies_dict[k] = v
        if cookies_type in [dict, requests.sessions.cookielib.CookieJar]:
                cookies_dict = cookies
        self.session.cookies = requests.sessions.merge_cookies(self.session.cookies, cookies_dict)

    def send(self, url, method, params=None, data=None, header=None, cookie=None, **kwargs):
        method = method.upper()
        if method not in METHODS:
            raise UnSupportMethodException('不支持的method:{0}，请检查传入参数！'.format(method))
        if header is not None:
            self.set_headers(header)
        if cookie is not None:
            self.set_cookies(cookie)
        response = self.session.request(method=method, url=url, params=params, data=data, headers=header, cookies=cookie, verify=self.verify, timeout=self.timeout, **kwargs)
        response.encoding = 'utf-8'
        LOG.debug('{0} {1}'.format(method, url))
        LOG.debug('请求成功: {0}\n{1}'.format(response, response.text))
        return response

# class TCPClient(object):
#     """用于测试TCP协议的socket请求，对于WebSocket，socket.io需要另外的封装"""
#     def __init__(self, domain, port, timeout=30, max_receive=102400):
#         self.domain = domain
#         self.port = port
#         self.connected = 0  # 连接后置为1
#         self.max_receive = max_receive
#         self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self._sock.settimeout(timeout)
#
#     def connect(self):
#         """连接指定IP、端口"""
#         if not self.connected:
#             try:
#                 self._sock.connect((self.domain, self.port))
#             except socket.error as e:
#                 LOG.exception(e)
#             else:
#                 self.connected = 1
#                 LOG.debug('TCPClient connect to {0}:{1} success.'.format(self.domain, self.port))
#
#     def send(self, data, dtype='str', suffix=''):
#         """向服务器端发送send_string，并返回信息，若报错，则返回None"""
#         if dtype == 'json':
#             send_string = json.dumps(data) + suffix
#         else:
#             send_string = data + suffix
#         self.connect()
#         if self.connected:
#             try:
#                 self._sock.send(send_string.encode())
#                 LOG.debug('TCPClient Send {0}'.format(send_string))
#             except socket.error as e:
#                 LOG.exception(e)
#
#             try:
#                 rec = self._sock.recv(self.max_receive).decode()
#                 if suffix:
#                     rec = rec[:-len(suffix)]
#                 LOG.debug('TCPClient received {0}'.format(rec))
#                 return rec
#             except socket.error as e:
#                 LOG.exception(e)
#
#     def close(self):
#         """关闭连接"""
#         if self.connected:
#             self._sock.close()
#             LOG.debug('TCPClient closed.')
