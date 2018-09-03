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
from lib.log import LOG
import pymysql


class ConnMysql(object):

    def __init__(self):
        conf = ConfigOperate('DB_config')
        self.host = conf.get_config('mysql_conf', 'host')
        self.port = int(conf.get_config('mysql_conf', 'port'))
        self.user = conf.get_config('mysql_conf', 'username')
        self.passwd = conf.get_config('mysql_conf', 'password')
        try:
            self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd)
            self.cur = self.conn.cursor()
        except Exception as e:
            LOG.error('数据库连接错误', e)

    def do_select(self, query):
        try:
            result_db = self.cur.execute(query)
        except Exception as e:
            LOG.error('查询命令错误', e)
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
            LOG.error('查询命令错误', e)
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
    con.do_select("SELECT * FROM che100.tc_carstyle ORDER BY id DESC LIMIT 10")
    for i in con.fetch_all_rows():
        if i[1] == '测试车型0830':
            print(i)
