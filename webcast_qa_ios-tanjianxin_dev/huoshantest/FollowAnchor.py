# -*- coding: utf8 -*-
"""follow anchor case
"""

from huoshanlib.testcase import HuoshanTest
from huoshanlib.app import HuoshanApp
from huoshanlib.main import MainWindow
import json
import time

class FollowAnchor(HuoshanTest):
    """follow anchor case
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
        num = window.login()
        time.sleep(5)

        self.start_step("enter room")
        window.EnterRoom()
        time.sleep(5)
        #检测是否会有多端登陆问题

        window.checked_more()
        self.assert_("未成功进房", window.EnterRoomSuccess() == 0)
        # window.SwipeToNextRoom()
        # time.sleep(20)
        # window.SwipeToNextRoom()
        # time.sleep(10)

        self.start_step("follow anchor")
        flag = window.FollowAnchor()
        time.sleep(5)
        self.assert_("未成功关注主播", flag == 0)

        self.start_step("quit room")
        window.QuitRoom()
        time.sleep(5)
        self.assert_("未成功退房", window.QuitRoomSuccess() == 0)

        # self.start_step("log out")
        # window.log_out(num)


if __name__ == '__main__':
    FollowAnchor().debug_run()
