#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: liuyu
@license: None
@file: printlog.py
@time: 17-4-7 上午2:03
"""
import os
import logbook
from logbook.more import ColorizedStderrHandler
from functools import wraps

LOG_DIR = os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__))), 'log')
file_stream = False

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)
    file_stream = True


def get_logger(name='Interface', file_log=file_stream, level=''):
    """ get logger Factory function """
    logbook.set_datetime_format('local')
    ColorizedStderrHandler(bubble=False, level=level).push_thread()
    logbook.TimedRotatingFileHandler(
        os.path.join(LOG_DIR, '%s.log' % name),
        date_format='%Y-%m-%d-%H', bubble=True, encoding='utf-8').push_thread()
    return logbook.Logger(name)


LOG = get_logger(file_log=file_stream, level='INFO')


def logger(param):
    """ fcuntion from logger meta """

    def wrap(function):
        """ logger wrapper """

        @wraps(function)
        def _wrap(*args, **kwargs):
            """ wrap tool """
            LOG.info("当前模块 {}".format(param))
            LOG.info("全部args参数参数信息 , {}".format(str(args)))
            LOG.info("全部kwargs参数信息 , {}".format(str(kwargs)))
            return function(*args, **kwargs)

        return _wrap

    return wrap


if __name__ == '__main__':
    LOG.info('3333')

