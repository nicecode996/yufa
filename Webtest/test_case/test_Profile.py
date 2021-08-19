# -*- coding: utf-8 -*-
# author:caiying

import time
import os
import unittest
import common.driver as Driver
from common.readconfig import ReadConfig
from common.log import logger

class Profile(unittest.TestCase):
    # 获取文件夹路径
    proDir = os.getcwd()
    # 找到配置文件
    config = ReadConfig()

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver.get_driver()

    def test_901_usertitle(self):
        try:
            self.driver.find_element_by_xpath('/html/body/div[1]/div/div/div/header/div[3]/div[2]').click()
            time.sleep(5)
            self.driver.find_element_by_xpath("//*[contains(text(),'个人资料')]").click()
            time.sleep(5)
            self.assertEqual(self.driver.find_element_by_xpath('//*[@id="profile"]/ul/li[2]/p[1]').text,'superadmin')
            logger.info("账号是superadmin")
        except Exception as ex:
            logger.error('账号不是superadmin')
            raise ex