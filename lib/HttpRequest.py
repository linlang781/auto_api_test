#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: liuyu
@license: None
@file: HttpRequest.py
@time: 17-4-28 下午2:16
"""
import json
import requests
from lib.tools import *


class HttpRequests(object):
    @staticmethod
    def do_post(url, params, **kwargs):

        if kwargs is not None:
            params.update(kwargs)
            response = requests.post(url, data=json.dumps(params))
            if response.status_code == 200:
                return True, response
            else:
                return False, response.status_code
        else:
            response = requests.post(url, data=json.dumps(params))
            if response.status_code == 200:
                return True, response
            else:
                return False, response.status_code


if __name__ == '__main__':
    header = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    }

    data_params = {
        "fmuserName": "15601128781",
        "isAuto": 'false',
        "password": '57BC148FD3FBDF8BD8A306B007E3F312'
    }
    reg_params = {"account": "781456868@qq.com", "validCode": "", "geetest_challenge": "", "geetest_validate": "",
                  "geetest_seccode": "", "type": "1", "ctype": "pc"}
    # cookies = 'JSESSIONID=79F94A9DDC5D60D0A56FCCD65BFC577C.tomcat94; Hm_lvt_79f1636012c7c583a8d9e22d74665c58=1522831007; undefined=false; Hm_lpvt_79f1636012c7c583a8d9e22d74665c58=1522831683'
    # r = requests.post('https://192.168.1.94/FMCloud/user/reg', data=json.dumps(data_params), verify=False)
    cookies = {
        "JSESSIONID": "F9996F4FD6E598C6EA062FCCC91F209F.tomcat94",
        "Hm_lvt_79f1636012c7c583a8d9e22d74665c58": "1522831007",
        'undefined': 'false',
        'Hm_lpvt_79f1636012c7c583a8d9e22d74665c58': '1522831683',
    }
    timestrap = getnowstamp()
    # key = requests.get('https://192.168.1.94/FMCloud/user/dk?_=1523174632297', verify=False)
    r = requests.post('https://192.168.1.94/FMCloud/user/login' + '?' + str(timestrap),
                      json=data_params,
                      cookies=cookies,
                      # cert=r'C:\Users\Administrator\Desktop\b64cer.cer',
                      verify=False
                      )
    # https://192.168.1.94/FMCloud/validcode/reg?timestamp=1523174860489
    reg = requests.post('https://192.168.1.94/FMCloud/validcode/reg',
                        json=reg_params,
                        verify=False
                        )

    # print(key.text)

    print(r.text)
    print(reg.text)
