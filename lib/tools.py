#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: liuyu
@license: None
@file: tools.py.py
@time: 17-4-5 下午10:51
"""
import base64
import hashlib
import time
import gzip
import json


def get_md5(data):
    '''
    md5加密
    '''
    m = hashlib.md5()
    m.update(data)
    return m.hexdigest()


def get_sha1(data):
    '''
    sha1加密
    '''
    s = hashlib.sha1()
    s.update(data)
    return s.hexdigest()


def get_base64(data):
    '''
    base64加密
    '''
    str = data.encode('utf-8')  # 把原始字符串转换成byte类型
    b64 = base64.b64encode(str)
    return b64.decode('utf-8')  # 把返回值解码成字符串并返回


def getde_base64(encrypted):
    '''
    base64解密
    '''

    data = base64.b64decode(encrypted)
    return data.decode('utf-8')  # 返回str类型数据


def getnowtime():
    """
    :return: 返回当前时间y-m-d
    """

    nows = time.strftime("%Y-%m-%d %H:%M:%S")
    return nows


def getnowstamp():
    """
    返回当前时间戳
    :return:
    """
    return int(time.time())


def gzdecode(self, data):
    compressedstream = io.StringIO(data)
    gziper = gzip.GzipFile(fileobj=compressedstream)
    data2 = gziper.read()  # 读取解压缩后数据
    return data2


if __name__ == '__main__':
    pass
