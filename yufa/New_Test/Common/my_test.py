#!usr/bin/env python3
# coding=utf-8
from os.path import dirname, abspath

import os
import unittest

from appium import webdriver
import sys

from test_report.app_config import CAPS

BASE_PATH = dirname(dirname(abspath(__file__)))
sys.path.append(BASE_PATH)


class MyTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Remote("hhttp://localhost:4723/wd/hub", CAPS)
        cls.driver.find_element_by_name("允许").click()
        cls.driver.implicitly_wait(10)
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
