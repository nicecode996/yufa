# -*- coding: utf8 -*-
"""demo test case
"""
#2020/06/15 auto generated by shoots

from douyinlib.testcase import DouyinTest
from douyinlib.app import DouyinApp
from douyinlib.main import MainWindow
import json

class DemoTest(DouyinTest):
    """demo test case
    """
    #owner = "lijingyu.mogu"
    owner = "tanjianxin"
    timeout = 300

    def run_test(self):
        self.start_step("start app")
        self.device = self.acquire_device()
        self.app = DouyinApp(self.device)

        self.start_step("check window")
        window = MainWindow(root=self.app)
        window.wait_for_existing()
        with open("tree.json", "w") as fd:
            fd.write(json.dumps(window.ui_tree, indent=2))

if __name__ == '__main__':
    DemoTest().debug_run()

