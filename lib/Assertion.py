#!/usr/bin/env python
# encoding: utf-8

"""
@author: liuyu
@file: Assertion
@time: 2018/8/27
"""


def res(d, code):
    result = []
    if isinstance(d, dict) and code in d.keys():
        value = d[code]
        result.append(value)
        return result
    elif isinstance(d, (list, tuple)):
        for item in d:
            value = res(item, code)
            if value == "None" or value is None:
                pass
            elif len(value) == 0:
                pass
            else:
                result.append(value)
        return result
    else:
        if isinstance(d, dict):
            for k in d:
                value = res(d[k], code)
                if value == "None" or value is None:
                    pass
                elif len(value) == 0:
                    pass
                else:
                    for item in value:
                        result.append(item)
            return result


def assert_in(asserqiwang, fanhuijson):
    if len(asserqiwang.split('=')) > 1:
        data = asserqiwang.split('&')
        result = dict([(item.split('=')) for item in data])
        value1 = ([(str(res(fanhuijson, key))) for key in result.keys()])
        value2 = ([(str(value)) for value in result.values()])
        if value1 == value2:
            return {'code': 0, "result": 'pass'}
        else:
            return {'code': 1, 'result': 'fail'}
    else:
        return {"code": 2, 'result': '填写测试预期值'}


def assertre(asserqingwang):
    if len(asserqingwang.split('=')) > 1:
        data = asserqingwang.split('&')
        result = dict([(item.split('=')) for item in data])
        return result
    else:
        raise {"code": 1, 'result': '填写测试预期值'}
