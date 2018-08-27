#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuyu
@file: test_log
@time: 2018/8/27
"""

from lib.log import LOG
from lib.config_operate import ConfigOperate
if __name__ == '__main__':
    LOG.info('testqqq')
    LOG.info('testppp')
    print(ConfigOperate('DB_config').get_config('mysql_conf','ip').split(';'))
    to_list = ConfigOperate('global').get_config('email_send', 'to_list').split(';')
    cc_list = ConfigOperate('global').get_config('email_send', 'cc_list').split(';')
    print(to_list, cc_list)
