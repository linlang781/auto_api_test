#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: liuyu
@license: None
@file: SendMail.py
@time: 17-4-1 上午1:03
"""
from lib.log import LOG
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import smtplib


class SendEmail(object):
    # 构造函数：初始化基本信息
    def __init__(self, host, user, passwd):
        lInfo = user.split("@")
        self._user = user
        self._account = lInfo[0]
        self._me = self._account + "<" + self._user + ">"

        # server = smtplib.SMTP()
        server = smtplib.SMTP_SSL(host, 465)
        # server.connect(host, 25)
        server.login(self._user, passwd)
        self._server = server

        # 发送文件或html邮件

    def send_email(self, to_list, cc_list, sub=None, content=None, file_path=None, subtype='html'):
        msg = MIMEMultipart()
        if sub is None:
            msg['Subject'] = '无标题邮件'
        else:
            msg['Subject'] = sub
        msg['From'] = self._me
        msg['To'] = ";".join(to_list)
        msg['Cc'] = ";".join(cc_list)
        if content is None:
            puretext = MIMEText('该邮件未输入任何内容')
            msg.attach(puretext)
        else:
            puretext = MIMEText(content, _subtype=subtype, _charset='utf-8')
            msg.attach(puretext)
        if file_path is not None:
            for tuple_path in tuple(file_path):
                mail_file = MIMEApplication(open(tuple_path, 'rb').read())
                mail_file.add_header('Content-Disposition', 'attachment', filename='%s' % tuple_path.split('/')[-1])
                msg.attach(mail_file)
        try:
            self._server.sendmail(self._me, to_list, msg.as_string())
            return True
        except Exception as e:
            LOG.error(str(e))
            return False

    # 析构函数：释放资源
    def __del__(self):
        self._server.quit()
        self._server.close()


if __name__ == '__main__':
    pass
# mailto_list = ['liuyu01@fengmap.com']
# cc_list = ['liuyu01@fengmap.com']
# if mail.send_email(mailto_list, cc_list, sub='自动化测试详情', content='这是报告'):
#     print('0')
# else:
#     print('1')
