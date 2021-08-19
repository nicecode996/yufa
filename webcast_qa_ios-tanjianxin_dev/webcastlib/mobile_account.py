# -*- coding=utf8 -*-

"""
调用账号池
"""

import requests
import json
from shoots import logger
import random

headers = {'Content-Type': 'application/json'}
service_url='https://live-ci.apps.bytedance.net/account_pool'

class MobileRequest():
    def get_num(self, tags):
        if tags == 1128:
            url1 = '%s/app/1128/idle' % service_url
            url2 = '%s/app/1128/allocate/' % service_url
        elif tags == 1112:
            url1 = '%s/app/1112/idle' % service_url
            url2 = '%s/app/1112/allocate/' % service_url
        elif tags == 32:
            url1 = '%s/app/32/idle' % service_url
            url2 = '%s/app/32/allocate/' % service_url
        elif tags == 13:
            url1 = '%s/app/13/idle' % service_url
            url2 = '%s/app/13/allocate/' % service_url

        r = requests.get(url1, headers=headers)  # 获取空闲账号列表
        logger.info(r.text)
        map = json.loads(r.text)  # 把json转换成dict
        random.shuffle(map["account_list"])  #随机打乱数组顺序
        num = map["account_list"][0]["mobile"]  # 取第一个账号
        logger.info(num)

        '''
        data_map = {}  # 定义一个字典
        data_map["mobile"] = num  # 赋值
        mobile = json.dumps(data_map)  # 解析json,把字典转换为json字符串
        byte_mobile = str.encode(mobile)  # 字符串转字节流
        '''

        params = {
            'mobile': num
        }
        q = requests.post(url2, headers=headers, json=params)  # 分配账号
        logger.info(q.text)
        t = requests.get(url1, headers=headers)  # 获取空闲账号列表
        logger.info(t.text)
        return num


    def release_num(self, tags, num):
        '''
        data_map = {}  # 定义一个字典
        data_map["mobile"] = num  # 赋值
        mobile = json.dumps(data_map)  # 解析json,把字典转换为json字符串
        byte_mobile = str.encode(mobile)  # 字符串转字节流
        '''
        params = {
            'mobile': num
        }
        if tags == 1128:
            url3 = '%s/app/1128/free' % service_url
        elif tags == 1112:
            url3 = '%s/app/1112/free' % service_url
        elif tags == 32:
            url3 = '%s/app/32/free' % service_url
        elif tags == 13:
            url3 = '%s/app/13/free' % service_url

        p = requests.post(url3, headers=headers, json=params)  # 释放账号
        logger.info(p.text)
