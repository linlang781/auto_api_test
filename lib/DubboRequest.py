#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuyu
@file: DubboRequest
@time: 2018/8/27
"""

from pyhessian.client import HessianProxy
from pyhessian import protocol
from lib.log import LOG, logger


@logger('dubbo接口')
class DubboRequest(object):

    def __init__(self, url, interface, method, param, **kwargs):
        self.url = url
        self.interface = interface
        self.method = method
        self.param = param
        self.interface_param = protocol.object_factory(self.param, **kwargs)

    def getresult(self):
        try:
            result = HessianProxy(self.url + self.interface)
            return_result = getattr(result, self.method)(self.interface_param)
            LOG.info('测试返回结果:%s' % return_result)
            res = {'code': 0, 'result': return_result}
        except Exception as e:
            LOG.info('测试失败，原因：%s' % e)
            res = {'code': 1, 'result': e}
        return res

if __name__ == '__main__':
    ip = '10.0.2.99'
    port = '20081'
    method = 'com.tuanche.service.AutoshowSearchService.getById'
    params = '1046'

