# -*- coding: utf8 -*-
"""Follow Anchor
"""
# 2020/07/02 auto generated by shoots

from xigualib.testcase import XiguaTest
from xigualib.app import XiguaApp
from xigualib.main import MainWindow
import time

class FollowAnchor(XiguaTest):
    """Follow Anchor
    """
    owner = "tanjianxin"

    timeout = 1000

    def run_test(self):
        self.start_step("start app")
        self.device = self.acquire_device()
        self.app = XiguaApp(self.device)

        self.start_step("check window")
        window = MainWindow(root=self.app)
        window.wait_for_existing()
        # window.init()
        time.sleep(6)


        self.start_step("log in")
        num = window.log_in(self.device)
        time.sleep(6)


        self.start_step("enter room")
        self.assert_("未成功进房", window.EnterRoom() == 0)
        window.SwipeToNextRoom()
        time.sleep(20)

        self.start_step("follow anchor")
        flag = window.FollowAnchor()
        time.sleep(7)
        self.assert_("未成功关注主播", flag == 0)

        self.start_step("quit room")
        window.QuitRoom()
        time.sleep(6)

        # self.start_step("log out")
        # window.log_out(num,self.device)

if __name__ == '__main__':
    FollowAnchor().debug_run()

