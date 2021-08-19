# -*- coding: utf-8 -*-
# author:jiayanzi

import time
import os
import unittest
import common.driver as Driver
from common.log import logger
from selenium.common.exceptions import NoSuchElementException


class PassageRecord(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver.get_driver()

    # 通行记录-通过人员编号搜索
    def test_501_search_by_personNo(self):
        try:
            self.driver.find_element_by_name("data").click()
            time.sleep(1)
            self.driver.find_element_by_name("recordmanage").click()
            time.sleep(2)
            self.driver.find_element_by_name("personNo").send_keys("abcde")
            time.sleep(1)
            self.driver.find_element_by_name("searchBtn").click()
            time.sleep(2)
            self.assertEqual(self.driver.find_element_by_xpath("//*[contains(text(),'暂无数据')]").text,
                            "暂无数据", "According to person number: abcde search result error")
            self.driver.find_element_by_name("personNo").click()
            self.driver.find_element_by_name("personNo").clear()
            time.sleep(1)
            self.driver.find_element_by_name("personNo").send_keys("1225")
            time.sleep(1)
            self.driver.find_element_by_name("searchBtn").click()
            time.sleep(1)
            search_list=self.driver.find_elements_by_class_name("el-table__row")
            num=len(search_list)
            result=''
            for i in range(0,num):
                if self.driver.find_element_by_name("personinfoNo"+str(i)).text=="1225":
                    result=True
                    self.assertEqual(result, True, "Wrong  Result by PersonNo Search")
                else:
                    result = False
                    self.assertEqual(result, True, "Wrong  Result by PersonNo Search")
                    break
            time.sleep(2)
            logger.info("根据人员编号查询结果正确")
        except Exception as ex:
            logger.error(ex)
            raise ex
        time.sleep(2)

    # 通行记录-查看详情
    def test_502_view_record_detail(self):
        try:
            self.driver.find_element_by_name("detailBtn0").click()
            time.sleep(2)
            self.assertEqual(self.driver.find_element_by_xpath("//*[contains(text(),'识别记录详情')]").text,
                             "识别记录详情", "Failed to view details")
            logger.info("查看识别记录详情页成功")
            time.sleep(1)
            self.driver.find_element_by_xpath("//span[contains(text(),'识别记录详情')]//following::button").click()
            time.sleep(2)
        except Exception as ex:
            logger.error(ex)
            raise ex
        time.sleep(2)

    # 通行记录-删除识别记录
    def test_503_delete_view_record(self):
        try:
            self.driver.find_element_by_name("deleteBtn0").click()
            time.sleep(2)
            self.driver.find_element_by_xpath('//div[@class="el-message-box__btns"]//'\
                                              'following::span[contains(text(),"删除")]').click()
            time.sleep(2)
            text=''
            try:
                elements=self.driver.find_element_by_xpath("//[contains(text(),'确定进行删除吗？')]")
            except NoSuchElementException as e:
                text =False
            self.assertEqual(text, False, 'Failure to return view record page')
            logger.info("删除失败记录成功")
            time.sleep(2)
        except Exception as ex:
            logger.error(ex)
            raise ex

    '''
        @classmethod
        def tearDownClass(cls):
            cls.driver.quit()
    '''


