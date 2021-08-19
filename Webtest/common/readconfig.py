# -*- coding: utf-8 -*-
# author:jiayanzi

import configparser
from os import path


class ReadConfig:

    def __init__(self):
        proDir = path.dirname(__file__)
        parent_path = path.abspath(path.dirname(proDir))
        configPath = path.join(parent_path, "data\config.ini")
        fd = open(configPath,encoding='UTF-8')
        data = fd.read()

        #读取&解析配置文件
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath,encoding='UTF-8')


    # 读取config.ini中【HTTP】中内容的方法
    def get_http(self, name):
        value = self.cf.get("HTTP", name)
        return value

    def get_device(self, name):
        value = self.cf.get("DEVICE", name)
        return value

    def get_interface(self,name):
        value = self.cf.get("INTERFACE",name)
        return value
