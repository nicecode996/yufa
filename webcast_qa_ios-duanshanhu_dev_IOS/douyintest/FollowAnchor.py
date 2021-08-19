# -*- coding: utf8 -*-
"""follow anchor case
"""

from douyinlib.testcase import DouyinTest
from douyinlib.app import DouyinApp
from douyinlib.main import MainWindow
import json
import time

class FollowAnchor(DouyinTest):
    """follow anchor case
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
        time.sleep(3)
        window.init()
        time.sleep(3)

        self.start_step("log in")
        num = window.log_in()
        time.sleep(5)
        self.start_step("enter room")
        window.EnterRoom()
        time.sleep(5)
        self.assert_("未成功进房", window.EnterRoomSuccess() == 0)
        window.SwipeToNextRoom()
        time.sleep(20)
        window.SwipeToNextRoom()
        time.sleep(20)

        self.start_step("follow anchor")
        flag = window.FollowAnchor()
        self.assert_("未成功关注主播",flag == 0)
        time.sleep(5)

        self.start_step("quit room")
        window.QuitRoom()
        time.sleep(5)

        self.start_step("log out")
        window.log_out(num)


if __name__ == '__main__':
    FollowAnchor().debug_run()
