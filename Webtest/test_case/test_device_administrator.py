# -*- coding: utf-8 -*-
# author:jiayanzi

import time
import os
import unittest
import common.driver as Driver
from common.log import logger
from common.analysexml import AnalyseXml


class Administrator(unittest.TestCase):
    proDir = os.getcwd()
    photoPath = os.path.join(proDir, "file\\2.jpg")
    photoFilePath = eval(repr(str(photoPath)).replace("\\", "/"))
    global photoResult
    photoResult = photoFilePath.replace("//", "/")

    # 获取当前driver
    @classmethod
    def setUpClass(cls):
        cls.driver = Driver.get_driver()

    # 设备管理-管理员
    def test_307_device_administrator(self):
        try:
            #self.driver.find_element_by_name("device").click()
            time.sleep(1)
            self.driver.find_element_by_name("adminmanage").click()
            time.sleep(2)
            self.driver.find_element_by_name("addManageBtn").click()
            time.sleep(2)
            name_list = self.driver.find_elements_by_name("name")
            name_list[1].send_keys("abc")
            time.sleep(1)
            password_list = self.driver.find_elements_by_name("password")
            password_list[1].send_keys("1234")
            time.sleep(1)
            pthone_list = self.driver.find_elements_by_name("phone")
            pthone_list[1].send_keys("15000010001")
            time.sleep(1)
            self.driver.find_element_by_name("photo").send_keys(photoResult)
            time.sleep(5)
            self.driver.find_element_by_name("submitBtn").click()
            time.sleep(3)
            self.assertEqual(self.driver.find_element_by_xpath(AnalyseXml("administrator_name")).text,
                             "abc", "Add administrator fail")
            logger.info("添加管理员成功")
            time.sleep(1)
        except Exception as ex:
            logger.error(ex)
            raise ex
        time.sleep(2)

    # 设备管理-管理员-编辑管理员姓名
    def test_308_edit_administrator(self):
        try:
            self.driver.find_element_by_name("editBtn0").click()
            time.sleep(2)
            edit_name_list = self.driver.find_elements_by_name("name")
            edit_name_list[1].clear()
            time.sleep(1)
            edit_name_list[1].send_keys("abcd")
            time.sleep(1)
            self.driver.find_element_by_name("submitBtn").click()
            time.sleep(2)
            self.assertEqual(self.driver.find_element_by_xpath(AnalyseXml("administrator_name")).text,
                             "abcd", "Edit administrator fail")
            logger.info("编辑管理员成功")
            time.sleep(1)
        except Exception as ex:
            logger.error(ex)
            raise ex
        time.sleep(2)

    # 设备管理-管理员-关联设备
    def test_309_related_device(self):
        try:
            self.driver.find_element_by_name("relateBtn0").click()
            time.sleep(1)
            self.driver.find_element_by_xpath(AnalyseXml("related_device_list_first_select")).click()
            time.sleep(1)
            self.driver.find_element_by_name("relanceBtn").click()
            time.sleep(1)
            self.assertEqual(self.driver.find_element_by_xpath(AnalyseXml("relate_device_num")).text, "1",
                             'Related device fail')
            logger.info("关联设备成功")
            time.sleep(1)
        except Exception as ex:
            logger.error(ex)
            raise ex
        time.sleep(2)

    # 设备管理-管理员-通过手机号搜索
    def test_310_search_by_phoneNo(self):
        try:
            self.driver.find_element_by_name("phone").send_keys("15000010001")
            time.sleep(1)
            self.driver.find_element_by_name("searchBtn").click()
            time.sleep(1)
            self.assertEqual(self.driver.find_element_by_xpath(AnalyseXml("administrator_name")).text,
                             "abcd", "Search administrator by phone is fail")
            logger.info("根据手机号搜索结果正确")
            time.sleep(1)
        except Exception as ex:
            logger.error(ex)
            raise ex
        time.sleep(2)

    # 设备管理-管理员-删除管理员
    def test_311_delete_administrator(self):
        try:
            self.driver.find_element_by_name("deleteBtn0").click()
            time.sleep(1)
            self.driver.find_element_by_xpath(AnalyseXml("delete_administratoe_sure_button")).click()
            time.sleep(1)
            self.assertNotEqual(self.driver.find_element_by_xpath(AnalyseXml("administrator_name")).text,
                                "abcd", "Delete administrator fail")
            logger.info("删除管理员成功")
        except Exception as ex:
            logger.error(ex)
            raise ex
        time.sleep(3)

    '''
        @classmethod
        def tearDownClass(cls):
            cls.driver.quit()
    '''
