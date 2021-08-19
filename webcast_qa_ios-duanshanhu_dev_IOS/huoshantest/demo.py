# -*- coding: utf8 -*-
"""demo test case
"""
#2020/06/28 auto generated by shoots

from huoshanlib.testcase import HuoshanTest
from huoshanlib.app import HuoshanApp
from huoshanlib.main import MainWindow

class DemoTest(HuoshanTest):
    """demo test case
    """
    #owner = "lijingyu.mogu"
    owner = "tanjianxin"
    timeout = 300
    
    def run_test(self):
        self.start_step("start app")
        self.device = self.acquire_device()
        self.app = HuoshanApp(self.device)
        
        self.start_step("check window")
        window = MainWindow(root=self.app)
        window.wait_for_existing()
        
    
if __name__ == '__main__':
    DemoTest().debug_run()

