__author__ = 'Administrator'
import time
import unittest
from selenium.webdriver.common.by import By
import common.driver as Driver
from common.log import logger


class AuthorityAllocation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver.get_driver()

    # 权限分配-新增账号
    def test_405_create_account(self):
        try:
            self.driver.find_element_by_name("permission").click()
            time.sleep(3)
            self.driver.find_element_by_name("accountmanage").click()
            time.sleep(3)
            self.driver.find_element_by_name("createBtn").click()
            time.sleep(3)
            self.driver.find_element_by_xpath('//input[@placeholder="支持大小写英文、数字"]').send_keys('test001')
            time.sleep(1)
            self.driver.find_element_by_name("password").send_keys('123456')
            time.sleep(1)
            self.driver.find_element_by_name("email").send_keys('test001@163.com')
            time.sleep(1)
            self.driver.find_element_by_name("submitBtn").click()
            time.sleep(0.5)
            key_word = self.driver.find_element_by_name("loginName1")
            self.assertEqual(key_word.text,"test001")
            time.sleep(2)
            logger.info("新增账号成功")
        except Exception as ex:
            logger.error(ex)
            raise ex
        time.sleep(2)


    #权限分配-账号详情
    def test_406_account_detail(self):
        try:
            detail_button=self.driver.find_elements_by_name("detailBtn1")
            detail_button[1].click()
            time.sleep(4)
            detail_name = self.driver.find_element_by_xpath('//div[text()="邮箱"]/following-sibling::div[contains(@class,"el-col el-col-16")]')
            self.assertEqual(detail_name.text, "test001@163.com")
            time.sleep(3)
            logger.info("角色详情显示正确")
        except Exception as ex:
            logger.error(ex)
            raise ex
        finally:
            self.driver.find_element_by_class_name("el-dialog__headerbtn").click()
            time.sleep(3)


    #权限分配-删除账号
    def test_407_delete_account(self):
        try:
            delete_button = self.driver.find_elements(By.NAME, "delBtn1")
            delete_button[1].click()
            time.sleep(3)
            self.driver.find_element_by_xpath('//span[contains(text(),"确 定")]').click()
            time.sleep(1)
            key_word = self.driver.find_element_by_xpath('//p[text()="成功"]')
            self.assertEqual(key_word.text, "成功")
            time.sleep(2)
            logger.info("角色删除成功")
        except Exception as ex:
            logger.error(ex)
            raise ex

'''
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
'''