#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0
@author: liuyu
@license: None
@file: get_base_parms.py
@time: 17-4-13 下午12:18
"""
from lib.MySQL import ConnMysql
from config.get_token import get_token
import random


def get_base_parms():

    data = {
        "device": {
            "mac": "unknown",
            "fingerprint": "Xiaomi/kenzo/kenzo:6.0.1/MMB29M/V8.2.1.0.MHOCNDL:user/release-keys",
            "model": "Redmi Note 3",
            "product": "kenzo",
            "vendor": "Xiaomi",
            "sdk": 23,
            "widthPixels": 1080,
            "heightPixels": 1920,
            "density": 480,
            "currentAndroidId": "1b8d2c5ea5c93c11",
            "firstAndroidId": "unknown",
            "firstBoot": 1491357039345,
            "firstImei": "unknown",
            "hasWeChat": "true",
            "hasqq": "true",
            "language": "zh",
            "country": "CN",
            "cpu": {
                "cpuimplementer": "0x41",
                "cpuarchitecture": "8",
                "cpurevision": "4",
                "revision": "4",
                "processorcnt": "5",
                "hardware": "Qualcomm Technologies, Inc MSM8956",
                "cpuvariant": "0x0",
                "features": "fp asimd evtstrm aes pmull sha1 sha2 crc32 wp half thumb fastmult vfp edsp neon vfpv3 tlsi vfpv4 idiva idivt",
                "cpupart": "0xd03"
            },
            "prop": {
                "ro.product.brand": "Xiaomi",
                "ro.product.name": "kenzo",
                "ro.product.model": "Redmi Note 3",
                "ro.build.fingerprint": "Xiaomi/kenzo/kenzo:6.0.1/MMB29M/V8.2.1.0.MHOCNDL:user/release-keys",
                "ro.build.version.sdk": "23",
                "ro.build.version.release": "6.0.1",
                "ro.build.date": "Tue Feb 14 20:19:12 CST 2017",
                "ro.build.date.utc": "1487074752",
                "ro.boot.cpuid": "",
                "ro.btconfig.vendor": "",
                "persist.sys.timezone": "Asia/Shanghai",
                "persist.sys.country": "",
                "persist.sys.language": "",
                "persist.sys.dalvik.vm.lib": "",
                "ro.build.description": "kenzo-user 6.0.1 MMB29M V8.2.1.0.MHOCNDL release-keys",
                "ro.runtime.firstboot": "1491357039345",
                "ro.serialno": "acccbe9c",
                "ro.product.device": "kenzo",
                "ro.kernel.qemu": "",
                "ro.hardware": "qcom",
                "ro.product.cpu.abi": "arm64-v8a"
            },
            "gpuVendor": "Adreno (TM) 510",
            "imei": "861735031851214",
            "connectionType": "WiFi",
            "carrier": "Unknown"
        },
        "caller": {
            "id": "ggclient",
            "sf": "A052F5F784A80A2A9B3AE97339C2C9C5",
            "rsa": "F08C552DA28E99672ACACFA7039F3560",
            "mf": "08D2F61DAD464B916FBFA11ADCC550A0",
            "regId": "D/sj08XtOhp/xqO61JeJ6rgt2bNqMfk47FJ2rNwdee8=",
            "pkgName": "com.iplay.assistant",
            "channel": "B1",
            "verCode": get_ver_code()[0],
            "token": str(get_token())
        },
        "token": str(get_token()),
        "reqTime": 1491470331215
    }
    return data


def create_req_time():
    # now =
    # reqtime =
    # return reqtime
    pass

def get_ver_code():
    db = ConnMysql()
    sql = "select max(vercode) from ggserver.iplay_products where name = '游戏助手'"
    # sql = "select max(vercode) from iplay_products limit 10"
    db.do_select(sql)
    result = db.fetch_one_row()
    return result


def get_random_gameid():
    db = ConnMysql()
    sql = "select game_id from ggserver.iplay_game_pkg order by update_timestamp desc limit 100"
    # sql = "select max(vercode) from iplay_products limit 10"
    db.do_select(sql)
    result = db.fetch_all_rows()
    return random.choice(result)


def get_gamepkg_code():
    db = ConnMysql()
    sql = "select pkg_name, ver_code from ggserver.iplay_game_pkg order by update_timestamp desc limit 100"
    # sql = "select max(vercode) from iplay_products limit 10"
    db.do_select(sql)
    result = db.fetch_all_rows()
    return random.choice(result)


def get_random_group_id():
    db = ConnMysql()
    sql = "select fid from forum_dev.fgroup where type = 'operation' order by fid desc "
    # sql = "select max(vercode) from iplay_products limit 10"
    db.do_select(sql)
    result = db.fetch_all_rows()
    return random.choice(result)[0]


def get_random_uid():
    db = ConnMysql()
    sql = "select uid from forum_dev.profile where lv >5"
    # sql = "select max(vercode) from iplay_products limit 10"
    db.do_select(sql)
    result = db.fetch_all_rows()
    return random.choice(result)[0]

def get_random_topic():
    db = ConnMysql()
    sql = "select tid from forum_dev.topic where typeid=0 order by lastpost limit 100"
    # sql = "select max(vercode) from iplay_products limit 10"
    db.do_select(sql)
    result = db.fetch_all_rows()
    return random.choice(result)[0]

 def get_random_plugin_topic():
    db = ConnMysql()
    sql = "select tid from forum_dev.topic where typeid=1 order by lastpost limit 100"
    # sql = "select max(vercode) from iplay_products limit 10"
    db.do_select(sql)
    result = db.fetch_all_rows()
    return random.choice(result)[0]




if __name__ == '__main__':
    print(get_random_uid())
