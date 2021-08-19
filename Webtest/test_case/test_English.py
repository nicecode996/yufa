# -*- coding: utf-8 -*-
# author:caiying

import time
import os
import unittest
import common.driver as Driver
from common.readconfig import ReadConfig
from common.log import logger


class English_tab(unittest.TestCase):

    # 获取文件夹路径
    proDir = os.getcwd()
    # 找到配置文件
    config = ReadConfig()

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver.get_driver()

    def test_1001_english(self):
        try:
            self.driver.find_element_by_xpath( '/html/body/div[1]/div/div/div/header/div[3]/div[1]/div[2]/span' ).click()
            time.sleep( 5 )
            self.driver.find_element_by_xpath( "//*[contains(text(),'English')]" ).click()
            time.sleep(3)
            self.assertEqual(self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/header/div[3]/div[1]/div[2]/span').text,'English','A')
            logger.info("切换到英文成功")
        except Exception as ex:
            logger.error('切换到英文失败')
            raise ex

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()