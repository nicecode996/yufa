# -*- coding: utf-8 -*-
# author:caiying

from selenium import webdriver
import time
import os
import unittest
import common.driver as Driver
from common.readconfig import ReadConfig
from common.log import logger


class Wechatapps(unittest.TestCase):
    # 获取文件夹路径
    proDir = os.getcwd()
    # 找到配置文件
    config = ReadConfig()

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver.get_driver()

    def test_701_wechatauth(self):
        try:
            self.driver.find_element_by_name('apps').click()
            time.sleep( 1 )
            self.driver.find_element_by_name( 'wechatauth' ).click()
            time.sleep( 1 )
            self.driver.find_element_by_xpath( '//*[@id="wechatAuth"]/div/div[5]/div[2]/div/label[2]/span[1]' ).click()
            time.sleep( 1 )
            self.driver.find_element_by_name( 'submitBtn' ).click()
            time.sleep(1)
            self.assertEqual(self.driver.find_element_by_xpath('/html/body/div[3]/p').text,u'保存成功！')
            logger.info('保存成功')
        except Exception as ex:
            logger.error('保存成功')
            raise ex
