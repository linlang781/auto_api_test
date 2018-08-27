#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: liuyu
@license: None
@file: main.py.py
@time: 17-3-31 下午9:34
"""

# 基础包：接口测试的封装
import unittest, time
from lib.BSTestRunner import BSTestRunner
from lib.SendMail import SendEmail
from lib.config_operate import ConfigOperate
from lib.log import LOG

test_dir = './case/'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    report_file_name = './report/' + now + 'result.html'
    fp = open(report_file_name, 'wb')
    runner = BSTestRunner(stream=fp, title='接口自动化测试报告', description='用例执行情况如下')
    m = runner.run(discover)
    fp.close()
    to_list = ConfigOperate('global').get_config('email_send', 'to_list').split(';')
    cc_list = ConfigOperate('global').get_config('email_send', 'cc_list').split(';')
    file_path_tuple = (report_file_name,)
    email_username = ConfigOperate('global').get_config('email_base', 'username')
    email_passwd = ConfigOperate('global').get_config('email_base', 'passwd')
    email_smtp = ConfigOperate('global').get_config('email_base', 'smtp')
    send_conf = SendEmail(email_smtp, email_username, email_passwd)
    content = 'http接口自动化测试完成，测试通过:%s,测试失败：%s，未知错误：%s,详情见附件' % (m.success_count, m.failure_count, m.error_count)
    try:
        send_conf.send_email(to_list, cc_list, sub='接口自动化测试报告' + now, content=content, file_path=file_path_tuple)  # content=open(report_file_name, 'rb').read()
        LOG.info('测试报告邮件发送成功')
    except Exception as e:
        LOG.info('邮件发送失败，错误原因为{0}'.format(e))
