#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: liuyu
@license: None
@file: test_mine.py
@time: 17-4-13 下午2:57
"""

import unittest
from lib.config_operate import ConfigOperate
from lib.http_requests import HttpRequests
from config.get_base_parms import *
import random

class TestMine(unittest.TestCase):
    '''测试我的相关接口'''

    def setUp(self):
        self.url = ConfigOperate('/home/liuyu/auto_api_test/config/global.ini').get_config('httpconf', 'forum_baseurl')
        self.base_parms = get_base_parms()
        self.headers = {' content-type': 'application/json'}

    def test_my_post_topic(self):
        '''我发布的帖子'''
        rp = HttpRequests.do_post(self.url + '/forum_app/my_post_topics', self.base_parms)
        if rp[0] is True:
            result = rp[1].json()
            print(result)
            self.assertEqual(result['rc'], 0)
        else:
            self.fail('接口请求出错,HTTP响应为%d' % rp[1])

    def test_my_replay_topic(self):
        '''我回复的帖子'''
        rp = HttpRequests.do_post(self.url + '/forum_app/my_reply_topics', self.base_parms)
        if rp[0] is True:
            result = rp[1].json()
            print(result)
            self.assertEqual(result['rc'], 0)
        else:
            self.fail('接口请求出错,HTTP响应为%d' % rp[1])


    def test_my_collection(self):
        '''我的收藏'''
        rp = HttpRequests.do_post(self.url + '/forum_app/my_collection', self.base_parms)
        if rp[0] is True:
            result = rp[1].json()
            print(result)
            self.assertEqual(result['rc'], 0)
        else:
            self.fail('接口请求出错,HTTP响应为%d' % rp[1])

    def test_share_qq_wechat_add_score(self):
        '''分享QQ\微信加积分(随机)'''
        subtype = random.choice(['qq', 'wechat'])
        rp = HttpRequests.do_post(self.url + '/user/add_score', self.base_parms, sub_type=subtype, type='share_one')
        if rp[0] is True:
            result = rp[1].json()
            print(result)
            self.assertEqual(result['rc'], 0)
        else:
            self.fail('接口请求出错,HTTP响应为%d' % rp[1])

    def test_share_qzone_add_score(self):
        '''分享空间\朋友圈加积分(随机)'''
        subtype = random.choice(['qq', 'wechat'])
        rp = HttpRequests.do_post(self.url + '/user/add_score', self.base_parms, sub_type=subtype, type='share_group')
        if rp[0] is True:
            result = rp[1].json()
            print(result)
            self.assertEqual(result['rc'], 0)
        else:
            self.fail('接口请求出错,HTTP响应为%d' % rp[1])

    def test_edit_profile_nickname(self):
        '''修改用户昵称'''
        rp = HttpRequests.do_post(self.url + '/user/edit_profile', self.base_parms, key='nickname', value='xxppe')
        if rp[0] is True:
            result = rp[1].json()
            print(result)
            self.assertEqual(result['rc'], 0)
        else:
            self.fail('接口请求出错,HTTP响应为%d' % rp[1])

    def test_edit_profile_header(self):
        '''修改用户头像'''
        rp = HttpRequests.do_post(self.url + '/user/edit_profile', self.base_parms, key='header_img', value='http://pic6.huitu.com/res/20130116/84481_20130116142820494200_1.jpg')
        if rp[0] is True:
            result = rp[1].json()
            print(result)
            self.assertEqual(result['rc'], 0)
        else:
            self.fail('接口请求出错,HTTP响应为%d' % rp[1])

    def test_edit_profile_gender(self):
        '''修改用户性别'''
        rp = HttpRequests.do_post(self.url + '/user/edit_profile', self.base_parms, key='gender', value=0)
        if rp[0] is True:
            result = rp[1].json()
            print(result)
            self.assertEqual(result['rc'], 0)
        else:
            self.fail('接口请求出错,HTTP响应为%d' % rp[1])

    def test_my_home_page_paly_games(self):
        '''测试个人主页-玩过的游戏'''
        rp = HttpRequests.do_post(self.url + '/user/home_page', self.base_parms, user_id=get_random_uid(), home_type='play_games')
        if rp[0] is True:
            result = rp[1].json()
            print(result)
            self.assertEqual(result['rc'], 0)
        else:
            self.fail('接口请求出错,HTTP响应为%d' % rp[1])

    def test_my_home_page_post_games(self):
        '''测试个人主页-评论过的游戏'''
        rp = HttpRequests.do_post(self.url + '/user/home_page', self.base_parms, user_id=get_random_uid(), home_type='game_posts')
        if rp[0] is True:
            result = rp[1].json()
            print(result)
            self.assertEqual(result['rc'], 0)
        else:
            self.fail('接口请求出错,HTTP响应为%d' % rp[1])

    def test_my_home_page_post_topic(self):
        '''测试个人主页-发布的帖子'''
        rp = HttpRequests.do_post(self.url + '/user/home_page', self.base_parms, user_id=get_random_uid(), home_type='topics')
        if rp[0] is True:
            result = rp[1].json()
            print(result)
            self.assertEqual(result['rc'], 0)
        else:
            self.fail('接口请求出错,HTTP响应为%d' % rp[1])


    def test_my_played_game(self):
        '''我的游戏,我玩过的游戏'''
        rp = HttpRequests.do_post(self.url + '/user/my_game', self.base_parms, my_type='play_games')
        if rp[0] is True:
            result = rp[1].json()
            print(result)
            self.assertEqual(result['rc'], 0)
        else:
            self.fail('接口请求出错,HTTP响应为%d' % rp[1])

    def test_my_comment_game(self):
        '''我的游戏,我评论过的游戏'''
        rp = HttpRequests.do_post(self.url + '/user/my_game', self.base_parms, my_type='game_posts')
        if rp[0] is True:
            result = rp[1].json()
            print(result)
            self.assertEqual(result['rc'], 0)
        else:
            self.fail('接口请求出错,HTTP响应为%d' % rp[1])

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()

