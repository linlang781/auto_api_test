#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: liuyu
@license: None
@file: test_magic_box.py
@time: 17-4-13 下午2:57
"""

import unittest
from lib.config_operate import ConfigOperate
from lib.http_requests import HttpRequests
from config.get_base_parms import *


class TestMagicBox(unittest.TestCase):
    '''魔盒游戏测试'''

    def setUp(self):

        self.url = ConfigOperate('/home/liuyu/auto_api_test/config/global.ini').get_config('httpconf', 'game_baseurl')
        self.base_parms = get_base_parms()
        self.headers = {'content-type': 'application/json'}

    def test_update_info(self):
        '''获取升级信息'''

        rp = HttpRequests.do_post(self.url + '/api/get/latest-version-info', self.base_parms)
        if rp[0] is True:
            result = rp[1].json()
            print(result)
            self.assertEqual(result['rc'], 0)
        else:
            self.fail('接口请求出错,HTTP响应为%d' % rp[1])

    def test_plugin_version_info(self):
        ''' 获取视频插件升级信息 '''

        rp = HttpRequests.do_post(self.url + '/api/get/plugin-version-info', self.base_parms)
        if rp[0] is True:
            result = rp[1].json()
            print(result)
            self.assertEqual(result['rc'], 0)
        else:
            self.fail('接口请求出错,HTTP响应为%d' % rp[1])

    def test_recommond_game(self):
        '''获取下载页面推荐的游戏'''
        rp = HttpRequests.do_post(self.url + '/api/get/recommend-games', self.base_parms)
        if rp[0] is True:
            result = rp[1].json()
            print(result)
            self.assertEqual(result['rc'], 0)
            self.assertEqual(result['data']['showCount'], 6)
        else:
            self.fail('接口请求出错,HTTP响应为%d' % rp[1])

    def test_get_box_game(self):
        '''获取魔盒游戏详细信息'''
        list_apks = [
                    {
                        "pkgName": "com.invictus.impossiball",
                        "verCode": "1511300729",
                        "signatureSf": "cb82a5010dd28529ffa1e58116643335",
                        "signatureMf": "0f140a2381575ff2222e47e817a09b53",
                    }
            ]
        rp = HttpRequests.do_post(self.url + '/api/get/box-games', self.base_parms, apks=list_apks)
        if rp[0] is True:
            result = rp[1].json()
            print(result)
            self.assertEqual(result['rc'], 0)
        else:
            self.fail('接口请求出错,HTTP响应为%d' % rp[1])
    #
    # def test_get_upgrade_game(self):
    #
    #     pass

    def test_get_default_keyword(self):
        '''获取搜索框默认关键词'''
        rp = HttpRequests.do_post(self.url + '/api/get/default-keywords', self.base_parms)
        if rp[0] is True:
            result = rp[1].json()
            print(result)
            self.assertEqual(result['rc'], 0)
        else:
            self.fail('接口请求出错,HTTP响应为%d' % rp[1])

    def test_hot_games(self):
        '''获取搜索页推荐的游戏列表'''
        rp = HttpRequests.do_post(self.url + '/api/get/hot-games', self.base_parms)
        if rp[0] is True:
            result = rp[1].json()
            print(result)
            self.assertEqual(result['rc'], 0)
        else:
            self.fail('接口请求出错,HTTP响应为%d' % rp[1])

    def test_get_ad_config(self):
        '''测试获取广告位信息'''
        rp = HttpRequests.do_post(self.url + '/api/get/ad-config', self.base_parms)
        if rp[0] is True:
            result = rp[1].json()
            print(result)
            self.assertEqual(result['rc'], 0)
        else:
            self.fail('接口请求出错,HTTP响应为%d' % rp[1])

    def test_game_view_page(self):
        '''游戏详情页测试'''
        rp = HttpRequests.do_post(self.url + '/view/page', self.base_parms, id=2000, pa=str(get_random_gameid()[0]))
        if rp[0] is True:
            result = rp[1].json()
            print(result)
            self.assertEqual(result['rc'], 0)
        else:
            self.fail('接口请求出错,HTTP响应为%d' % rp[1])

    def test_duplicate_game(self):
        '''获取开小号游戏列表'''
        ext_params = [{"pkgName": "com.dreamsky.DiabloLOL", "verCode": 310}, {"pkgName": "com.sqage.Ogre.OgreInstance.uc", "verCode": 24}, {"pkgName": "com.windplay.mobius.dnv.uc", "verCode": 7}]
        rp = HttpRequests.do_post(self.url + '/api/get/duplicate-game-list', self.base_parms, apks=ext_params)
        if rp[0] is True:
            result = rp[1].json()
            print(result)
            self.assertEqual(result['rc'], 0)
        else:
            self.fail('接口请求出错,HTTP响应为%d' % rp[1])

    def test_get_game_list(self):
        '''获取魔盒游戏最热列表'''
        rp = HttpRequests.do_post(self.url + '/api/get/game-list', self.base_parms, gameType='boxGame',orderType='hottest' )
        if rp[0] is True:
            result = rp[1].json()
            print(result)
            self.assertEqual(result['rc'], 0)
        else:
            self.fail('接口请求出错,HTTP响应为%d' % rp[1])

    def test_get_float(self):
        '''获取悬浮窗数据'''
        rp = HttpRequests.do_post(self.url + '/api/get/float', self.base_parms)
        if rp[0] is True:
            result = rp[1].json()
            print(result)
            self.assertEqual(result['rc'], 0)
        else:
            self.fail('接口请求出错,HTTP响应为%d' % rp[1])

    def test_get_red_point(self):
        '''测试小红点显示及数量'''
        rp = HttpRequests.do_post(self.url + '/api/get/page_id_status', self.base_parms)
        if rp[0] is True:
            result = rp[1].json()
            print(result)
            self.assertEqual(result['rc'], 0)
        else:
            self.fail('接口请求出错,HTTP响应为%d' % rp[1])

    def test_game_play_time(self):
        '''获取魔盒游戏时长'''
        rp = HttpRequests.do_post(self.url + '/api/get/game_play_info', self.base_parms, gameId=get_random_gameid())
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

