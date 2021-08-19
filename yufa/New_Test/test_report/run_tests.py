#!/usr/bin/env python3
# coding=utf-8

import unittest
import time
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    # 定义测试用例目录为当前目录
    test_dir = './test_case'
    suit = unittest.defaultTestLoader.discover(start_dir=test_dir, pattern='test_*.py')

    # 获取当前日期和时间
    now_time = time.strptime("%Y-%m-%d %H-%M-%S")
    test_report = './test_report/' + now_time + 'result.html'
    with(open(test_report, 'wb')) as fp:
        runner = HTMLTestRunner(stream=fp,
                                title="魅族",
                                )

        runner.run(suit)
