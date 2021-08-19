# -*- coding: utf8 -*-
"""anchor send gift
"""

from toutiaolib.testcase import ToutiaoTest
from toutiaolib.app import ToutiaoApp
from toutiaolib.main import MainWindow
import json
import time

class AnchorSendGift(ToutiaoTest):
    """anchor send gift
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

        self.start_step("log in")
        num = window.log_in()
        time.sleep(8)


        self.start_step("start living")
        window.StartLiving()
        time.sleep(10)

        self.assert_("未成功开播", window.StartLivingSuccess() == 0)
        self.start_step("送礼")
        window.SendGift()
        time.sleep(8)

        self.start_step("close living")
        window.CloseLiving()
        self.assert_("未成功关播", window.CloseLivingSuccessful() == 0)
        time.sleep(6)

        self.start_step("log out")
        window.log_out(num)


if __name__ == '__main__':
    AnchorSendGift().debug_run()