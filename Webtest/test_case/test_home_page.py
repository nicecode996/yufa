__author__ = 'Administrator'
import time
import unittest
import common.driver as Driver
from common.log import logger

class HomePage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver.get_driver()

    # 进入个人资料页
    def test_101_click_profile(self):
        try:
            self.driver.find_element_by_name("dashboard").click()
            time.sleep(5)
            self.driver.find_element_by_name("home").click()
            time.sleep(5)
            self.driver.find_element_by_xpath('//ul[@class="card-content personIntro"]').click()
            time.sleep(5)
            key_word=self.driver.find_element_by_xpath('//div[text()="个人资料"]')
            self.assertEqual(key_word.text, "个人资料")
            time.sleep(5)
            logger.info("进入个人资料页成功")
        except Exception as ex:
            logger.error(ex)
            raise ex
        time.sleep(2)


    #进入设备预警页
    def test_102_click_device_alarm(self):
        try:
            self.driver.find_element_by_name("home").click()
            time.sleep(5)
            self.driver.find_element_by_xpath('//ul[@class="card-content device"]').click()
            time.sleep(5)
            key_word=self.driver.find_element_by_xpath('//div[text()="终端预警"]')
            self.assertEqual(key_word.text, "终端预警")
            time.sleep(5)
            logger.info("进入设备预警页成功")
        except Exception as ex:
            logger.error(ex)
            raise ex
        time.sleep(2)

    # 进入操作日志页
    def test_103_click_operation_log(self):
        try:
            self.driver.find_element_by_name("home").click()
            time.sleep(5)
            self.driver.find_element_by_id('moreBtn').click()
            time.sleep(5)
            key_word = self.driver.find_element_by_xpath('//span[text()="操作日志"]')
            self.assertEqual(key_word.text, "操作日志")
            time.sleep(5)
            logger.info("进入操作日志页成功")
        except Exception as ex:
            logger.error(ex)
            raise ex
        time.sleep(2)

    # 进入业务管理页
    def test_104_click_business_management(self):
        try:
            self.driver.find_element_by_name("home").click()
            time.sleep(5)
            self.driver.find_element_by_xpath('//div[contains(text(),"业务管理")]').click()
            time.sleep(5)
            key_word = self.driver.find_element_by_xpath('//span[@class="el-breadcrumb__inner is-link" and text()="业务管理"]')
            self.assertEqual(key_word.text, "业务管理")
            time.sleep(5)
            logger.info("进入业务管理页成功")
        except Exception as ex:
            logger.error(ex)
            raise ex
        time.sleep(2)

    # 进入访客系统
    def test_105_click_base_application(self):
        try:
            self.driver.find_element_by_name("dashboard").click()
            time.sleep(5)
            self.driver.find_element_by_name("home").click()
            time.sleep(5)
            self.driver.find_element_by_xpath('//div[contains(text(),"访客应用")]').click()
            time.sleep(5)
            key_word = self.driver.find_element_by_name("dashboard")
            self.assertNotEqual(key_word.text, "访客管理系统")
            time.sleep(5)
            logger.info("进入访客管理系统成功")
        except Exception as ex:
            logger.error(ex)
            raise ex
        time.sleep(2)

'''
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
'''


