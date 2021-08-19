# -*- coding: utf-8 -*-
# author:jiayanzi

import time
import os
import unittest
import common.driver as Driver
from common.log import logger
from common.readconfig import ReadConfig
from common.analysexml import AnalyseXml
from selenium.common.exceptions import NoSuchElementException


class ConfigManager(unittest.TestCase):
    # 获取文件夹路径
    proDir = os.getcwd()
    # 找到配置文件
    config = ReadConfig()

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver.get_driver()

    # 配置管理-设备基础设置-参数设置
    def test_312_device_base_config(self):
        try:
            #self.driver.find_element_by_name("device").click()
            time.sleep(1)
            self.driver.find_element_by_name("configmanage").click()
            time.sleep(1)
            self.driver.find_element_by_name("setBaseConfigBtn0").click()
            time.sleep(2)
            self.driver.find_element_by_xpath(AnalyseXml("quality_judge_switch")).click()
            time.sleep(2)
            self.driver.find_element_by_name("submitBtn").click()
            time.sleep(2)
            self.driver.find_element_by_name("setBaseConfigBtn0").click()
            time.sleep(2)
            self.assertEqual(self.driver.find_element_by_xpath(AnalyseXml("quality_judge_switch")). \
                             get_attribute("class"), "el-switch", "Failure in parameter configuration")
            time.sleep(1)
            self.driver.find_element_by_xpath(AnalyseXml("quality_judge_switch")).click()
            time.sleep(2)
            self.driver.find_element_by_name("submitBtn").click()
            logger.info("设备基础设置参数设置成功")
            time.sleep(2)
        except Exception as ex:
            logger.error(ex)
            raise ex
        time.sleep(2)

    # 配置管理-添加参数库
    def test_313_add_parameter_library(self):
        try:
            self.driver.find_element_by_name("createFeatureBtn").click()
            time.sleep(2)
            self.driver.find_element_by_name("featureFormName").send_keys("圆脸长头发")
            time.sleep(1)
            self.driver.find_element_by_name("featureFormDes").send_keys("test")
            time.sleep(2)
            self.driver.find_element_by_name("submitBtn").click()
            time.sleep(2)
            self.assertEqual(self.driver.find_element_by_xpath(AnalyseXml("param_library_list")).text,
                             "圆脸长头发", "Failure to add parameter library")
            time.sleep(1)
            logger.info("新增参数库成功")
        except Exception as ex:
            logger.error(ex)
            raise ex
        time.sleep(2)

    # 配置管理-编辑参数库名称
    def test_314_edit_parameter_library_name(self):
        try:
            self.driver.find_element_by_name("editBtn2").click()
            time.sleep(2)
            self.driver.find_element_by_name("featureFormName").clear()
            time.sleep(1)
            self.driver.find_element_by_name("featureFormName").send_keys("test")
            time.sleep(2)
            self.driver.find_element_by_name("submitBtn").click()
            time.sleep(2)
            self.assertEqual(self.driver.find_element_by_xpath(AnalyseXml("param_library_list")).text,
                             "test", "Failure to edit parameter library")
            time.sleep(1)
            logger.info("编辑参数库成功")
            time.sleep(1)
        except Exception as ex:
            logger.error(ex)
            raise ex

    # 配置管理-选择设备并同步-根据SN号搜索
    def test_315_search_by_deviceSN(self):
        try:
            self.driver.find_element_by_name("selectDeviceBtn").click()
            time.sleep(2)
            self.driver.find_element_by_name("deviceSN").send_keys("12345")
            time.sleep(2)
            self.driver.find_element_by_name("searchBtn").click()
            time.sleep(1)
            self.assertEqual(self.driver.find_element_by_xpath("//*[contains(text(),'暂无数据')]").text,
                             "暂无数据", "According to SN number: 12345 search result error")
            time.sleep(1)
            self.driver.find_element_by_name("deviceSN").click()
            time.sleep(1)
            self.driver.find_element_by_name("deviceSN").clear()
            time.sleep(2)
            self.driver.find_element_by_name("deviceSN").send_keys(self.config.get_device('SN'))
            time.sleep(2)
            self.driver.find_element_by_name("searchBtn").click()
            time.sleep(2)
            search_list_sn = self.driver.find_element_by_name("selectDeviceAndSyncDetailSN0")
            self.assertEqual(search_list_sn.text, self.config.get_device('SN'), "Search result is error")
            time.sleep(1)
            logger.info("根据SN号搜索结果正确")
            time.sleep(1)
        except Exception as ex:
            logger.error(ex)
            raise ex
        time.sleep(2)

    # 配置管理-下发参数库到设备A
    def test_316_download_parameter_library(self):
        try:
            checkbox_list = self.driver.find_elements_by_class_name("el-checkbox__inner")
            checkbox_list[1].click()
            time.sleep(1)
            self.driver.find_element_by_name("submitBtn").click()
            time.sleep(2)
            text = ''
            try:
                element = self.driver.find_element_by_xpath("//div[contains(text(),'选择设备并同步')]")
            except NoSuchElementException as e:
                text = False
            self.assertEqual(text, False, 'Failure to download parameter library')
            logger.info("下发参数库成功")
            time.sleep(2)
        except Exception as ex:
            logger.error(ex)
            raise ex
        time.sleep(2)

    # 配置管理-删除参数库
    def test_317_delete_paramater_library(self):
        try:
            self.driver.find_element_by_name("deleteBtn2").click()
            time.sleep(2)
            self.driver.find_element_by_xpath(AnalyseXml("param_delete_sure_button")).click()
            time.sleep(2)
            text2 = ''
            try:
                element2 = self.driver.find_element_by_xpath(AnalyseXml("param_library_list"))
            except NoSuchElementException as e:
                text2 = False
            self.assertEqual(text2, False, "Failure to delete parameter library")
            time.sleep(1)
            logger.info("删除参数库成功")
            time.sleep(1)
        except Exception as ex:
            logger.error(ex)
            raise ex

    '''
        @classmethod
        def tearDownClass(cls):
            cls.driver.quit()
    '''
