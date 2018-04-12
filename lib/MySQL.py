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
        conf = ConfigOperate()
        self.host = conf.get_config('db_config', 'host')
        print(self.host)
        self.port = int(conf.get_config('db_config', 'port'))
        self.user = conf.get_config('db_config', 'user')
        self.passwd = conf.get_config('db_config', 'passwd')
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
    result = con.do_update("insert into testinfo.login_data VALUES ('ffff6','hhh9')")
    if result:
        print('0')
    else:
        print(result)
