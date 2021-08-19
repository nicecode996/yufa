# -*- coding: utf-8 -*-
# author:jiayanzi

import time
import os
import unittest
import common.driver as Driver
from common.log import logger
from common.analysexml import AnalyseXml


class DeviceGroup(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver.get_driver()

    # 添加设备组
    def test_305_add_device_group(self):
        try:
            # 设备管理菜单定位
            #self.driver.find_element_by_name("device").click()
            time.sleep(1)
            # 设备分组菜单定位
            self.driver.find_element_by_name("devicegroup").click()
            time.sleep(2)
            # 点击创建设备组按钮
            self.driver.find_element_by_name("createBtn").click()
            time.sleep(2)
            # 在设备组名输入框输入组名
            self.driver.find_element_by_name("groupName").send_keys("test_device_group")
            time.sleep(2)
            # 选择左侧未分组设备列表中的一个设备
            self.driver.find_element_by_xpath(AnalyseXml("add_group_device_select")).click()
            time.sleep(2)
            # 点击右移按钮
            self.driver.find_element_by_xpath(AnalyseXml("add_group_device_right_move")).click()
            time.sleep(2)
            # 点击确定按钮进行提交
            self.driver.find_element_by_name("submitBtn").click()
            time.sleep(2)
            # 验证设备分组列表中是否存在添加的分组信息
            self.assertEqual(self.driver.find_element_by_xpath(AnalyseXml("device_group_name_exist")).text,
                         "test_device_group", '添加设备组失败')
            time.sleep(3)
            logger.info("添加设备组成功")
        except Exception as ex:
            logger.error(ex)
            raise ex
        time.sleep(2)

    # 测试删除设备组
    def test_306_delete_device_group(self):
        try:
            # 点击设备组删除按钮
            self.driver.find_element_by_name("deleteBtn0").click()
            time.sleep(2)
            # 删除设备组确认按钮
            self.driver.find_element_by_xpath(AnalyseXml("device_group_delete_sure_button")).click()
            time.sleep(3)
            self.assertNotEqual(self.driver.find_element_by_xpath(AnalyseXml("device_group_name_exist")).text,
                             "test_device_group", '删除设备组失败')
            logger.info("删除设备组成功")
        except Exception as ex:
            logger.error(ex)
            raise ex
        time.sleep(2)

    '''
        @classmethod
        def tearDownClass(cls):
            cls.driver.quit()
    '''
