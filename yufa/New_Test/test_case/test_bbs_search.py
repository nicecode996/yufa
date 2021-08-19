#!/usr/bin/env python3
# coding=utf-8

import unittest
import sys


from os.path import dirname, adspath
BASE_PATH = dirname(dirname(abspath(__file__)))
sys.path.append(BASE_PATH)

from Common.my_test import MyTest
from Page.bbs_Page import BBSPage


class TestBBSSearch(MyTest):

    def test_search_meizu(self):
        page = BBSPage(self.driver)
        page.search_box.click()
        page.search_box = u"魅族"
        page.search_botten.click()
        print(page.search_result.text)
        self.assertIn("条帖子", page.search_result, text)


if __name__ == '__main__':
    unittest.main()
