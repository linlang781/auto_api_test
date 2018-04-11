#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: liuyu
@license: None
@file: test_forum.py
@time: 17-4-19 上午10:41
"""
import unittest
from lib.config_operate import ConfigOperate
from lib.http_requests import HttpRequests
from config.get_base_parms import *

class TestForum(unittest.TestCase):
    '''社区相关接口测试'''

    def setUp(self):
        self.url = ConfigOperate('/home/liuyu/auto_api_test/config/global.ini').get_config('httpconf', 'forum_baseurl')
        self.base_parms = get_base_parms()
        self.headers = {' content-type': 'application/json'}

    def test_forum_index(self):
        '''测试社区首页'''
        page = random.choice(range(5, 20))
        offset = random.choice(range(5, 30))
        rp = HttpRequests.do_post(self.url + '/api/get/latest-version-info', self.base_parms, group_id=get_random_group_id(), page=page, offset=offset)
        if rp[0] is True:
            result = rp[1].json()
            print(result)
            self.assertEqual(result['rc'], 0)
        else:
            self.fail('接口请求出错,HTTP响应为%d' % rp[1])

    def test_forum_group_new(self):
        '''测试话题详情页最新页面'''
        rp = HttpRequests.do_post(self.url + '/forum_app/group4', self.base_parms, group_id=get_random_group_id(), sort_rule=0)
        if rp[0] is True:
            result = rp[1].json()
            print(result)
            self.assertEqual(result['rc'], 0)
        else:
            self.fail('接口请求出错,HTTP响应为%d' % rp[1])

    def test_forum_group_hot(self):
        '''测试话题详情页精选页面'''
        rp = HttpRequests.do_post(self.url + '/forum_app/group4', self.base_parms, group_id=get_random_group_id(), sort_rule=1)
        if rp[0] is True:
            result = rp[1].json()
            print(result)
            self.assertEqual(result['rc'], 0)
        else:
            self.fail('接口请求出错,HTTP响应为%d' % rp[1])

    def test_forum_topic(self):
        '''测试图文帖子详情页'''
        type_id = list(range(0, 7))
        for i in type_id:
            rp = HttpRequests.do_post(self.url + '/forum_app/topic', self.base_parms, group_id=get_random_topic(), type_id=int(i))
            if rp[0] is True:
                result = rp[1].json()
                print(result)
                self.assertEqual(result['rc'], 0)
            else:
                self.fail('接口请求出错,HTTP响应为%d' % rp[1])

    def test_xxx(self):
        pass

    def tearDown(self):
        pass


if __name__ == '__main__':
    # 构造测试集
    suite = unittest.TestSuite()
    suite.addTest(TestForum("test_forum_index"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)