# -*- coding: utf8 -*-
"""close living case
"""

from huoshanlib.testcase import HuoshanTest
from huoshanlib.app import HuoshanApp
from huoshanlib.main import MainWindow
import json
import time

class AnchorSendGift(HuoshanTest):
    """close living case
    """
    #owner = "lijingyu.mogu"
    owner = "tanjianxin"
    timeout = 1000

    def run_test(self):
        self.start_step("start app")
        self.device = self.acquire_device()
        self.app = HuoshanApp(self.device)

        self.start_step("check window")
        window = MainWindow(root=self.app)
        window.wait_for_existing()
        window.init()
        time.sleep(5)
        self.start_step("log in")
        window.login()
        time.sleep(5)

        self.start_step("start living")
        window.StartLiving()
        time.sleep(5)
        self.assert_("未成功开播", window.StartLivingSuccess() == 0)

        self.start_step("close living")
        window.CloseLiving()
        time.sleep(5)
        self.assert_("未成功关播", window.CloseLivingSuccessful() == 0)

        # self.start_step("log out")
        # window.log_out(num)


if __name__ == '__main__':
    AnchorSendGift().debug_run()
