# -*- coding: utf8 -*-
"""test plan demo
"""
#2020/06/30 auto generated by shoots

from shoots.plan import TestPlan

class DemoTestPlan(TestPlan):
    """douyin4206 demo plan
    """
    tests = "douyintest.demo.DemoTest"

if __name__ == "__main__":
    DemoTestPlan().debug_run()
