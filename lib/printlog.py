#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: liuyu
@license: None
@file: printlog.py
@time: 17-4-7 上午2:03
"""
import logging

# 第一步，创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)  # Log等级总开关

# 第二步，创建一个handler，用于写入日志文件
logfile = r'C:\Users\Administrator\Desktop\auto_api_test-master\log\log.txt'
fh = logging.FileHandler(logfile, mode='a+')
fh.setLevel(logging.INFO)  # 输出到file的log等级的开关

# 第三步，再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)  # 输出到console的log等级的开关

# 第四步，定义handler的输出格式
formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 第五步，将logger添加到handler里面
logger.addHandler(fh)
logger.addHandler(ch)


# 日志
class Logger(object):

    @staticmethod
    def info(msg):
        return logger.info(msg)

    @staticmethod
    def debug(msg):
        return logger.debug(msg)

    @staticmethod
    def error(msg):
        return logger.error(msg)

    @staticmethod
    def critical(msg):
        return logger.critical(msg)


if __name__ == '__main__':
    Logger.error('test')





