# -*- coding: utf-8 -*-
# author:jiayanzi

import time
import os
import unittest
import common.driver as Driver
from common.log import logger
from common.readconfig import ReadConfig
from common.analysexml import AnalyseXml
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


class DeviceManager(unittest.TestCase):
    # 获取文件夹路径
    proDir = os.getcwd()
    # 找到配置文件
    config = ReadConfig()

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver.get_driver()

    time.sleep(3)

    # 设备管理-设备激活码点击并判断设备激活码页面的平台IP文字是否显示
    def test_301_device_active_code(self):
        try:
            self.driver.find_element_by_name("device").click()
            time.sleep(1)
            self.driver.find_element_by_name("devicemanage").click()
            time.sleep(2)
            self.driver.find_element_by_name("activationCodeBtn").click()
            time.sleep(2)
            active_code_web = self.driver.find_elements_by_class_name("titleName")
            self.assertEqual(active_code_web[1].text, "平台IP", "Active code IP is Error")
            time.sleep(2)
            self.driver.find_element_by_xpath(AnalyseXml("device_manager_code_X_button")).click()
            time.sleep(2)
            logger.info("打开设备激活码页面成功")
        except Exception as ex:
            logger.error(ex)
            raise ex
        time.sleep(2)

    # 设备管理，根据SN号查询，判断查询结果是否正确
    def test_302_device_manager_search(self):
        try:
            time.sleep(2)
            self.driver.find_element_by_name("SN").send_keys("12345")
            time.sleep(1)
            self.driver.find_element_by_name("searchBtn").click()
            time.sleep(1)
            self.assertEqual(self.driver.find_element_by_xpath("//*[contains(text(),'暂无数据')]").text,
                                "暂无数据", "According to SN number: 12345 search result error")
            time.sleep(1)
            self.driver.find_element_by_name("SN").click()
            self.driver.find_element_by_name("SN").clear()
            time.sleep(1)
            self.driver.find_element_by_name("SN").send_keys(self.config.get_device('SN'))
            time.sleep(2)
            self.driver.find_element_by_name("searchBtn").click()
            time.sleep(2)
            self.assertEqual(self.driver.find_element_by_xpath(AnalyseXml("device_manager_list_first_sn")).text,
                                self.config.get_device('SN'), "Device manager search has result")
            time.sleep(1)
            logger.info("根据SN号搜索成功")
        except Exception as ex:
            logger.error(ex)
            raise ex
        time.sleep(2)

    # 设备管理-获取设备A设置-在下发页面根据设备SN搜索
    def test_303_send_device_settings_search(self):
        try:
            checkbox = self.driver.find_elements_by_class_name("el-checkbox")
            checkbox[1].click()
            time.sleep(1)
            self.driver.find_element_by_name("sendBtn").click()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "marginLeft10")))
            time.sleep(1)
            self.driver.find_element_by_name("sendDownBtn").click()
            time.sleep(2)
            self.driver.find_element_by_name("deviceSN").send_keys("12345")
            time.sleep(2)
            button_list=self.driver.find_elements_by_name("searchBtn")
            button_list[1].click()
            time.sleep(2)
            self.assertEqual(self.driver.find_element_by_xpath("//*[contains(text(),'暂无数据')]").text,
                            "暂无数据", "According to SN number: 12345 search result error")
            time.sleep(2)
            self.driver.find_element_by_name("deviceSN").click()
            time.sleep(1)
            self.driver.find_element_by_name("deviceSN").clear()
            time.sleep(1)
            self.driver.find_element_by_name("deviceSN").send_keys(self.config.get_device('SN'))
            time.sleep(1)
            button_list1 = self.driver.find_elements_by_name("searchBtn")
            button_list1[1].click()
            time.sleep(2)
            self.assertEqual(self.driver.find_element_by_name("sendDownSNIndex0").text,self.config.get_device('SN'))
            logger.info("获取设置参数成功,根据SN号查询结果正确")
            time.sleep(3)
        except Exception as ex:
            logger.error(ex)
            raise ex

    #下发设备配置到另外一台设备
    def test_304_get_and_send_device_settings(self):
        try:
            self.driver.find_element_by_name("deviceSN").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//input[@name='deviceSN']//following-sibling::span").click()
            time.sleep(1)
            button_num=self.driver.find_elements_by_name("searchBtn")
            button_num[1].click()
            time.sleep(2)
            self.driver.find_element_by_xpath(AnalyseXml("send_device_settings_checkbox")).click()
            time.sleep(1)
            self.driver.find_element_by_name("sendDownInnerBtn").click()
            WebDriverWait(self.driver,10).\
                until(EC.presence_of_element_located((By.CLASS_NAME,"el-message-box__content")))
            time.sleep(1)
            self.driver.find_element_by_xpath(AnalyseXml("send_device_settings_sure")).click()
            time.sleep(1)
            logger.info("下发A设备设置到B设备成功")
            time.sleep(1)
        except Exception as  ex:
            logger.error(ex)
            raise ex

    '''
        @classmethod
        def tearDownClass(cls):
            cls.driver.quit()
    '''
