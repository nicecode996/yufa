# -*- coding: utf-8 -*-
# author:jiayanzi

import requests
from common.readconfig import ReadConfig
#from common.log import logger


class InterFace:

    def __init__(self):

        global host,port,timeout
        localConfig = ReadConfig()
        host=localConfig.get_interface("baseurl")
        port=localConfig.get_interface("port")
        #self.log=logger.get_logger()
        self.headers={}
        self.data={}
        self.url=None
        self.files={}

    def set_url(self,url):
        self.url=host + port+url

    def set_header(self,headers):
        self.headers=headers

    def set_data(self,data):
        self.data=data

    def set_files(self,files):
        self.files=files

    #定义get函数
    def get(self,url,headers):
        try:
            response=requests.get(self.url,headers=self.headers)
            return response
        except TimeoutError:
            #self.log.error("Time out!")
            return None

    #定义post方法
    def post(self):
        try:
            response=requests.post(self.url,headers=self.headers)
            return response
        except TimeoutError:
            #self.log.error("Time out!")
            return None


