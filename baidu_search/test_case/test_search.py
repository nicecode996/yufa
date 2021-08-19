# coding=utf-8
# !/usr/bin/env python3
# 基础版

import unittest
from time import sleep
from selenium import webdriver
from common import config

'''
class TestBaidu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.base_url = "https://www.baidu.com"

    def test_search_key_maxu(self):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id("kw").send_keys("麻旭")
        sleep(10)
        self.driver.find_element_by_id("su").click()
        sleep(10)
        title = self.driver.title
        self.assertEqual(title, "麻旭_百度搜索")

    def test_search_key_jmeter(self):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id("kw").send_keys("今日头条测试开发面试题")
        sleep(10)
        title = self.driver.title
        self.assertEqual(title, "今日头条测试开发面试题_百度搜索")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()    
'''
# 模块换改进版
class TestBaidu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.base_url = "https://www.baidu.com"

    def baidu_search(self, search_key):
        self.driver.get(self.base_url)
        self.driver.find_element_by_id("kw").send_keys("UI自动化测试")
        self.driver.find_element_by_id("su").click()
        sleep(3)
        print("测试开始")

    def test_search_key_maxu(self):
        search_key = "search_key"
        self.baidu_search("maxu")
        self.assertEqual(self.driver.title, search_key+"_百度搜索")
        print("麻旭搜索完成")

    def test_search_key_jmeter(self):
        search_key = "search_key"
        sleep(5)
        self.baidu_search("jmeter")
        self.assertEqual(self.driver.title, search_key+"_百度搜索")
        print("jmeter搜索完成")

    def test_search_key_niubiclass(self):
        search_key = "search_key"
        self.baidu_search("niubiclass")
        self.assertEqual(self.driver.title, search_key + "_百度搜索")
        print("niu搜索完成")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()