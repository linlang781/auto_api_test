#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuyu
@file: SwitchHost
@time: 2018/9/3
"""


class SwitchHost(object):
    def __init__(self):
        # 内网host地址
        self.inner_network = ['172.16.60.71 cms.tuanche.net',
                              '172.16.60.71 console.tuanche.com',
                              '172.16.60.71 www.tuanche.com',
                              '172.16.60.71 bj.tuanche.com',
                              '172.16.60.71 ebsconsole.tuanche.com'
                              '127.0.0.1 localhost'
                              ]

        # 外网host地址
        self.outer_network = ['127.0.0.1 localhost']
        self.host_path = r'C:\Windows\System32\drivers\etc\hosts'

    def inner_network(self):
        output = open(self.host_path, 'w')
        for inner in self.inner_network:
            output.write(inner)
            output.write("\n")
        output.close()

    def outer_network(self):
        output = open(self.host_path, 'w')
        for outer in self.outer_network:
            output.write(outer)
            output.write("\n")
        output.close()
