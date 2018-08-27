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
    LOG.info('test')
    ConfigOperate('DB_config.ini').get_config('mysql_conf','ip')