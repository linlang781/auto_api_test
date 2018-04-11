#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: liuyu
@license: None
@file: sendmail.py
@time: 17-4-1 上午1:03
"""
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

        server = smtplib.SMTP()
        server.connect(host)
        server.login(self._account, passwd)
        self._server = server

        # 发送文件或html邮件

    def send_email(self, to_list, cc_list, sub = None, content = None, file_path = None, subtype='html'):
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
            print(str(e))
            return False

    # 析构函数：释放资源
    def __del__(self):
        self._server.quit()
        self._server.close()

# if __name__ == '__main__':
#
#     mailto_list = ['liuyu@yyhudong.com']
#     cc_list = ['781456868@qq.com']
#     mail = SendEmail('smtp.163.com', '18724353405@163.com', 'qq123123')
#     file_path_tuple = ("./test.html", "./conig.ini", "./mylog.log")
#     if mail.send_email(mailto_list, cc_list, file_path=file_path_tuple):
#         print "发送成功"
#     else:
#         print "发送失败"


