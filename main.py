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
import unittest, time, sys
from lib.BSTestRunner import BSTestRunner
from lib.SendMail import SendEmail
from lib.config_operate import ConfigOperate
from lib.log import LOG

send_mail_off = sys.argv[1]

test_dir = './case/'
now = time.strftime('%Y-%m-%d %H_%M_%S')
report_file_name = './report/' + now + 'result.html'

def create_suite():
    test_suite = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py', top_level_dir=None)
    for suite in discover:
        for case in suite:
            test_suite.addTest(case)
            print(test_suite)
    return test_suite


def test_runner():
    all_case_name = create_suite()
    fp = open(report_file_name, 'wb')
    runner = BSTestRunner(stream=fp, title='接口自动化测试报告', description='用例执行情况如下')
    m = runner.run(all_case_name)
    fp.close()
    return m

def send_mail():
    suite_result = test_runner()
    to_list = ConfigOperate('global').get_config('email_send', 'to_list').split(';')
    cc_list = ConfigOperate('global').get_config('email_send', 'cc_list').split(';')
    file_path_tuple = (report_file_name,)
    email_username = ConfigOperate('global').get_config('email_base', 'username')
    email_passwd = ConfigOperate('global').get_config('email_base', 'passwd')
    email_smtp = ConfigOperate('global').get_config('email_base', 'smtp')
    send_conf = SendEmail(email_smtp, email_username, email_passwd)
    content = 'http接口自动化测试完成，测试通过:%s,测试失败：%s，未知错误：%s,详情见附件' % (suite_result.success_count, suite_result.failure_count, suite_result.error_count)
    if send_conf.send_email(to_list, cc_list, sub='接口自动化测试报告' + now, content=content, file_path=file_path_tuple):  # content=open(report_file_name, 'rb').read()
        LOG.info('测试报告邮件发送成功')
    else:
        LOG.info('邮件发送失败')

if __name__ == '__main__':
    if send_mail_off == 'sendmail':
        send_mail()
    elif send_mail_off == 'runcase':
        test_runner()
    else:
        raise Exception('参数输入错误')





