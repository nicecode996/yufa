#! usr/bin/env python3
# coding=utf-8

import unittest

import testsuite as testsuite

import HTMLTestRunner-Python3


class demo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setup class")

    @classmethod
    def tearDownClass(cls) -> None:
        print("teardown class")

    def setUp(self) -> None:
        print("setup")

    def tearDown(self) -> None:
        print("teardown")

    def test_case01(self):
        print("testcase01")
        self.assertEqual(2, 2, "判断相等")
        self.assertNotIn('h', 'td')

    def test_case02(self):
        print("testcase02")
        self.assertIs('ac', 'ac', "是相同的")
        self.assertTrue('2==2')

    @unittest.skipIf(2 == 2, "跳过这条用例")
    def test_case03(self):
        print("跳过此条测试用例")
        self.assertTrue(3 == 3, "不是真的")


class demo1(unittest.TestCase):
    def test_demo1_case04(self):
        print("test_demo1_case04")

    def test_demo1_case05(self):
        print("test_demo1_case05")


class demo2(unittest.TestCase):
    def test_demo2_case06(self):
        print("test_demo2_case06")

    def test_demo2_case07(self):
        print("test_demo2_case07")


class HTMLTestrunner3(object):
    pass


if __name__ == '__main__':
    # unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(demo2("test_demo2_case07"))
    # unittest.TextTestRunner().run(suite)

    # suite = unittest.TestLoader().loadTestsFromTestCase(demo)
    # suite1 = unittest.TestLoader().loadTestsFromTestCase(demo1)
    # suiteall = unittest.TestSuite([suite, suite1])
    # unittest.TextTestRunner().run(suiteall)

    report_title = "测试用例报告"
    desc = "展示HTMLTestRunner"
    report_file = './report.html'
    discvoer = unittest.defaultTestLoader.discover("./", 'test*.py')
    unittest.TextTestRunner().run(discvoer)
    with open(report_file, 'wb') as report:
        runner = HTMLTestrunner(stream=report, title=report_title, description=desc)
        runner.run(testsuite)
