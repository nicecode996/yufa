# -*- coding: utf8 -*-
"""scroll to next room
"""

from douyinlib.testcase import DouyinTest
from douyinlib.app import DouyinApp
from douyinlib.main import MainWindow
import json
import time

class ScrollToNextRoom(DouyinTest):
    """scroll to next room
    """
    #owner = "lijingyu.mogu"
    owner = "tanjianxin"
    timeout = 1000

    def run_test(self):
        self.start_step("start app")
        self.device = self.acquire_device()
        self.app = DouyinApp(self.device)

        self.start_step("check window")
        window = MainWindow(root=self.app)
        window.wait_for_existing()
        window.init()
        time.sleep(5)

        self.start_step("enter room")
        window.EnterRoom()
        time.sleep(5)

        self.assert_("未成功进房", window.EnterRoomSuccess() == 0)
        window.SwipeToNextRoom()
        time.sleep(20)

        self.start_step("swipe to next room")
        flag = window.ScrollToNextRoom()
        self.assert_("未成功上下滑", flag == 0)


if __name__ == '__main__':
    ScrollToNextRoom().debug_run()