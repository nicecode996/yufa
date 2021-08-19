# -*- coding: utf-8 -*-
#author:jiayanzi

import time
import unittest
import os
from selenium.webdriver.common.by import By
import common.driver as Driver
from common.log import logger
from common.analysexml import AnalyseXml


class PersonManager(unittest.TestCase):
    proDir = os.getcwd()
    # 找到配置文件-照片
    photoPath = os.path.join(proDir, "file\\1.jpg")
    #找到配置文件-导入的excel
    #excelPath =os.path.join(proDir,"file\\importPersons.xlsx")
    #替换双反斜线
    photoFilePath = eval(repr(str(photoPath)).replace("\\", "/"))
    #excelFilePath = eval(repr(str(excelPath)).replace("\\", "/"))
    #定义全局变量
    global photoResult
    #global excelResult
    #替换双斜线为单斜线
    photoResult=photoFilePath.replace("//", "/")
    #excelResult=excelFilePath.replace("//", "/")

    @classmethod
    def setUpClass(cls):
        cls.driver=Driver.get_driver()

    # 人员管理-新增人员
    def test_201_add_person(self):
        try:
            self.driver.find_element_by_name("people").click()
            time.sleep(2)
            self.driver.find_element_by_name("peoplemanage").click()
            time.sleep(2)
            self.driver.find_element_by_name("createBtn").click()
            time.sleep(3)
            self.driver.find_element_by_name("personName").send_keys('test')
            time.sleep(1)
            self.driver.find_element_by_name("personNo").send_keys('0001')
            time.sleep(1)
            self.driver.find_element_by_name("imgUpload").send_keys(photoResult)
            time.sleep(5)
            person_org=self.driver.find_elements(By.XPATH,"//*[@class='el-input__inner']")
            person_org[7].click()
            time.sleep(1)
            person_org_list=self.driver.find_elements(By.XPATH,"//*[@class='custom-tree-node']")
            person_org_list[4].click()
            time.sleep(1)
            self.driver.find_element_by_name("submitBtn").click()
            time.sleep(2)
            person_list=self.driver.find_elements_by_name("personName0")
            self.assertEqual(person_list[1].text,  "test", 'add person fail')
            time.sleep(2)
            logger.info("新增人员成功")
        except Exception as ex:
            logger.error(ex)
            raise ex
        time.sleep(2)

    #人员管理-按组织搜索
    def test_202_person_search_by_Organization(self):
        try:
            time.sleep(2)
            orga_list=self.driver.find_elements(By.XPATH,"//*[@class='el-input__inner']")
            orga_list[2].click()
            time.sleep(1)
            orga=self.driver.find_elements(By.XPATH,"//*[@class='custom-tree-node']")
            orga[1].click()
            time.sleep(2)
            self.driver.find_element_by_name("searchBtn").click()
            time.sleep(2)
            search_person_list = self.driver.find_elements_by_name("personName0")
            self.assertEqual(search_person_list[1].text, "test", 'Search person fail by Organization')
            time.sleep(2)
            logger.info("根据组织搜索成功")
            aa=self.driver.find_elements_by_class_name("el-input__suffix-inner")
            aa[0].click()
            time.sleep(1)
            self.driver.find_element_by_name("searchBtn").click()
            time.sleep(2)
        except Exception as ex:
            logger.error(ex)
            raise ex
        time.sleep(2)

    #人员管理-编辑人员姓名
    def test_203_edit_person_name(self):
        try:
            edit_button=self.driver.find_elements(By.NAME,"editBtn0")
            edit_button[2].click()
            time.sleep(1)
            self.driver.find_element_by_name("personName").clear()
            time.sleep(1)
            self.driver.find_element_by_name("personName").send_keys("test1")
            time.sleep(1)
            self.driver.find_element_by_name("submitBtn").click()
            time.sleep(2)
            edit_person_list=self.driver.find_elements_by_name("personName0")
            self.assertEqual(edit_person_list[1].text,  "test1",  'Edit person fail')
            logger.info("编辑人员成功")
        except Exception as ex:
            logger.error(ex)
            raise ex
        time.sleep(2)


    #人员管理-人员详情
    def test_204_person_details(self):
        try:
            detail_button=self.driver.find_elements(By.NAME,"detailBtn0")
            detail_button[2].click()
            time.sleep(2)
            detail_name=self.driver.find_elements(By.NAME,"personName")
            self.assertEqual(detail_name[0].get_attribute("value"), "test1", "person detail page has error")
            time.sleep(4)
            self.driver.find_element_by_css_selector(AnalyseXml("person_details_close_button")).click()
            time.sleep(2)
            logger.info("人员详情显示正确")
        except Exception as ex:
            logger.error(ex)
            raise ex
        time.sleep(2)


    # 人员管理-删除人员
    def test_205_delete_person(self):
        try:
            delete_button=self.driver.find_elements(By.NAME,"deleteBtn0")
            delete_button[2].click()
            time.sleep(2)
            self.driver.find_element_by_xpath(AnalyseXml("Person_delete_sure_button")).click()
            time.sleep(2)
            delete_person_list = self.driver.find_elements_by_name("personName0")
            self.assertNotEqual(delete_person_list[1].text, "test1", 'Delete person fail')
            time.sleep(3)
            logger.info("人员删除成功")
        except Exception as ex:
            logger.error(ex)
            raise ex

        # 人员管理-人员信息配置
    def test_206_person_information_config(self):
        try:
            # 定位到人员信息配置button
            self.driver.find_element_by_name("configBtn").click()
            time.sleep(2)
            # 定位密码输入框
            self.driver.find_element_by_name("password").clear()
            time.sleep(1)
            self.driver.find_element_by_name("password").send_keys("1234.com")
            time.sleep(1)
            # 确定按钮
            self.driver.find_element_by_name("submitBtn").click()
            time.sleep(3)
            # 再次打开人员信息配置窗口做判断
            self.driver.find_element_by_name("configBtn").click()
            time.sleep(1)
            self.assertEqual(self.driver.find_element_by_name("password").get_attribute("value"),
                             "1234.com", 'Edit person information fail')
            time.sleep(2)
            self.driver.find_element_by_name("cancelBtn").click()
            time.sleep(1)
            logger.info("人员信息配置成功")
            time.sleep(1)
        except Exception as ex:
            logger.error(ex)
            raise ex

'''
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
'''

