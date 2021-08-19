# -*- coding: utf-8 -*-
# author:jiayanzi

import time
import os
import unittest
import common.driver as Driver
from common.log import logger
from common.readconfig import ReadConfig


class CommandRecord(unittest.TestCase):
    # 获取文件夹路径
    proDir = os.getcwd()
    # 找到配置文件
    config = ReadConfig()

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver.get_driver()

    def test_318_command_sent_down_record_search(self):
        try:
            #self.driver.find_element_by_name("device").click()
            time.sleep(1)
            self.driver.find_element_by_name("commandmanage").click()
            time.sleep(2)
            self.driver.find_element_by_name("commandSN").send_keys("12345")
            time.sleep(2)
            self.driver.find_element_by_name("searchBtn").click()
            time.sleep(1)
            self.assertEqual(self.driver.find_element_by_xpath("//*[contains(text(),'暂无数据')]").text,
                             "暂无数据", "According to SN number: 12345 search result error")
            time.sleep(2)
            self.driver.find_element_by_name("commandSN").click()
            time.sleep(1)
            self.driver.find_element_by_name("commandSN").clear()
            time.sleep(2)
            self.driver.find_element_by_name("commandSN").send_keys(self.config.get_device('SN'))
            time.sleep(1)
            self.driver.find_element_by_name("searchBtn").click()
            time.sleep(2)
            record_list = self.driver.find_elements_by_class_name("el-table__row")
            num = len(record_list)
            t = ''
            # 判断根据SN号搜索后的列表中，第一页记录SN号正确
            for i in range(0, num):
                if self.driver.find_element_by_name("selectDeviceAndSyncSN"+str(i)).text == self.config.get_device('SN'):
                    t = True
                    self.assertEqual(t, True, "Wrong Recording Result by SN Search Command")
                else:
                    t = False
                    self.assertEqual(t, True, "Wrong Recording Result by SN Search Command")
                    break

            time.sleep(2)
            logger.info("根据SN号搜索命令下发记录结果正确")
        except Exception as ex:
            logger.error(ex)
            raise ex
        time.sleep(2)

'''
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
'''