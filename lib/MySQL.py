#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: liuyu
@license: None
@file: MySQL.py
@time: 17-4-12 下午2:01
"""
from lib.config_operate import ConfigOperate
import pymysql


class ConnMysql(object):

    def __init__(self):
        conf = ConfigOperate('C:\Users\Administrator\Desktop\auto_api_test-master\config/global.ini')
        self.host = conf.get_config('dbconfig', 'host')
        self.port = int(conf.get_config('dbconfig', 'port'))
        self.user = conf.get_config('dbconfig', 'user')
        self.passwd = conf.get_config('dbconfig', 'passwd')
        try:
            self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd)
            self.cur = self.conn.cursor()
        except Exception as e:
            print('数据库连接错误', e)

    def do_select(self, query):
        try:
            result_db = self.cur.execute(query)
        except Exception as e:
            print('查询命令错误', e)
            result_db = False
        return result_db

    def do_update(self, query):
        """
        update和delete\insert
        :param query:
        :return:
        """
        try:
            result_db = self.cur.execute(query)
            self.commit()
        except Exception as e:
            print('查询命令错误', e)
            result_db = False
        return result_db

    def fetch_all_rows(self):

        return self.cur.fetchall()

    def fetch_one_row(self):

        return self.cur.fetchone()

    def get_row_count(self):

        return self.cur.rowcount()

    def commit(self):

        self.conn.commit()

    def roll_back(self):

        self.conn.rollback()

    def __del__(self):
        self.cur.close()
        self.conn.close()


if __name__ == '__main__':
    con = ConnMysql()
    con.do_select("select * from ggserver.iplay_products where `name` like '%游戏助手%'")
    result = con.fetch_one_row()
    print(result[1])
