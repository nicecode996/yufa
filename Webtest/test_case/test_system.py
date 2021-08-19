# -*- coding: utf-8 -*-
# author:caiying

from selenium import webdriver
import time
import os
import unittest
import common.driver as Driver
from common.readconfig import ReadConfig
from common.log import logger


class System(unittest.TestCase):
    # 获取文件夹路径
    proDir = os.getcwd()
    # 找到配置文件
    config = ReadConfig()

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver.get_driver()


    def test_801_Organizational_update(self):
        try:
            self.driver.find_element_by_name('system').click()
            time.sleep(1)
            self.driver.find_element_by_name('organization').click()
            time.sleep(1)
            self.driver.find_element_by_name('createBtn').click()
            time.sleep(1)
            self.driver.find_element_by_name( 'name' ).send_keys(u'测试一组')
            time.sleep(1)
            self.driver.find_element_by_name('submitBtn').click()
            time.sleep(5)
            self.assertEqual(self.driver.find_element_by_xpath('//*[@id="organization"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div[1]/div[2]/div[3]/div/span[2]/span').text,'测试一组')
            logger.info("新建组织成功")
        except Exception as ex:
            logger.error('新建组织失败')
            raise ex

    def test_802_Organizational_edit(self):
        try:
            self.driver.find_element_by_xpath('//*[@id="organization"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div[1]/div[2]/div[3]/div/span[2]/span' ).click()
            time.sleep( 1 )
            self.driver.find_element_by_name( 'editBtn' ).click()
            time.sleep( 1 )
            self.driver.find_element_by_name( 'name' ).send_keys( u'二' )
            time.sleep( 1 )
            self.driver.find_element_by_name( 'submitBtn' ).click()
            time.sleep( 5 )
            self.assertEqual(self.driver.find_element_by_xpath('//*[@id="organization"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div[1]/div[2]/div[3]/div/span[2]/span').text,'测试一组二')
            logger.info("编辑成功")
        except Exception as ex:
            logger.error('编辑失败')
            raise ex


    def test_803_Organizational_delete(self):
        try:
            self.driver.find_element_by_xpath('//*[@id="organization"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div/div[1]/div[2]/div[3]/div/span[2]/span' ).click()
            time.sleep( 1 )
            self.driver.find_element_by_name( 'delBtn' ).click()
            time.sleep( 1 )
            self.driver.find_element_by_xpath( '/html/body/div[2]/div/div[3]/button[2]' ).click()
            time.sleep(5)
            self.assertNotEqual(self.driver.find_element_by_xpath('//*[@id="organization"]/div[1]/div/div[1]/div').text,'测试一组二')
            logger.info("删除成功")
        except Exception as ex:
            logger.error('删除失败')
            raise ex
