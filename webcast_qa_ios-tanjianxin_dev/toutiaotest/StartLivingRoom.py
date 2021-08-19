# -*- coding: utf8 -*-
"""start living case
"""

from toutiaolib.testcase import ToutiaoTest
from toutiaolib.app import ToutiaoApp
from toutiaolib.main import MainWindow
import json
import time

class StartLivingRoom(ToutiaoTest):
    """Start living case
    """
    #owner = "lijingyu.mogu"
    owner = "tanjianxin"
    timeout = 1000

    def run_test(self):
        self.start_step("start app")
        self.device = self.acquire_device()
        self.app = ToutiaoApp(self.device)

        self.start_step("check window")
        window = MainWindow(root=self.app)
        window.wait_for_existing()
        #window.init()
        time.sleep(6)

        self.start_step("log in")
        num = window.log_in()
        time.sleep(6)

        self.start_step("start living")
        window.StartLiving()
        time.sleep(10)

        self.assert_("未成功开播", window.StartLivingSuccess() == 0)

        self.start_step("close living")
        window.CloseLiving()
        time.sleep(10)
        self.assert_("未成功关播", window.CloseLivingSuccessful() == 0)

        self.start_step("log out")
        window.log_out(num)


if __name__ == '__main__':
    StartLivingRoom().debug_run()