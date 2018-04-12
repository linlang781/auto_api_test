#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: liuyu
@license: None
@file: test_login.py
@time: 17-4-19 上午10:41
"""
import unittest, requests
from lib.config_operate import ConfigOperate
from lib.tools import *
from lib.http_requests import HttpRequests
from config.get_base_parms import *

class TestUser(unittest.TestCase):
    '''用户相关接口测试'''

    def setUp(self):
        self.url = ConfigOperate().get_config('url_config', 'url')
        self.port = ConfigOperate().get_config('url_config', 'port')
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"
        }


    def test_reg(self):
        '''用户注册'''
        params = {
            "account": "781456868@qq.com",
            "validCode": "",
            "geetest_challenge": "",
            "geetest_validate": "",
            "geetest_seccode": "",
            "type": "1",
            "ctype": "pc"
        }
        response = requests.post(self.url + ':' + self.port + '/FMCloud/validcode/reg?timestamp=' + str(getnowstamp()), json=params, verify=False, headers=self.headers)
        # self.assertEqual(response.status_code, 200, '断言状态码为200')
        print(response.text)

    def tearDown(self):
        pass

if __name__ == '__main__':
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(TestForum("test_reg"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)


