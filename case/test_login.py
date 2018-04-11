#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: liuyu
@license: None
@file: test_login.py.py
@time: 17-4-6 上午1:42
"""
import unittest
from lib.config_operate import ConfigOperate
import request
from lib.printlog import PrintLog

class TestLogin(unittest.TestCase):
    '''登录模块测试'''

    def setUp(self):

        self.url = ConfigOperate(r'C:\Users\Administrator\Desktop\auto_api_test-master\config\global.ini').get_config('common', 'url')
        self.port = ConfigOperate(r'C:\Users\Administrator\Desktop\auto_api_test-master\config\global.ini').get_config('common', 'port')
        self.data = {}

    def test_login(self):
        ''' 测试登录 '''
        r= request.
        rp = HttpRequests.do_post(self.url+'/user/reg', self.data)
        if
        # if rp[0] is True:
        #     result = rp[1].json()
        #     print(result)
        #     PrintLog.print_log_info('登录接口测试通过' + '\n' + str(result))
        #     self.assertEqual(result['rc'], 0)
        # else:
        #     self.fail('接口请求出错,HTTP响应为%d' % rp[1])

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()


