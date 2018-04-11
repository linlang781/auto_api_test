#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: liuyu
@license: None
@file: test_game_page.py
@time: 17-4-13 下午2:57
"""
import unittest
from lib.config_operate import ConfigOperate
from lib.http_requests import HttpRequests
from config.get_base_parms import *

class TestGamePage(unittest.TestCase):
    '''游戏-发现相关接口测试'''

    def setUp(self):

        self.url = ConfigOperate('/home/liuyu/auto_api_test/config/global.ini').get_config('httpconf', 'game_baseurl')
        self.base_parms = get_base_parms()
        self.headers = {'content-type': 'application/json'}

    def test_game_page(self):
        '''游戏详情页测试'''
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
