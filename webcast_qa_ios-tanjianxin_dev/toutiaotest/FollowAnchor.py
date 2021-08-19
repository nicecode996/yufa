# -*- coding: utf8 -*-
"""follow anchor case
"""

from toutiaolib.testcase import ToutiaoTest
from toutiaolib.app import ToutiaoApp
from toutiaolib.main import MainWindow
import json
import time

class FollowAnchor(ToutiaoTest):
    """follow anchor
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

        self.start_step("enter room")
        self.assert_("未成功进房", window.EnterRoom() == 0)
        window.SwipeToNextRoom()
        time.sleep(20)
        window.SwipeToNextRoom()
        time.sleep(20)

        self.start_step("follow anchor")
        flag = window.FollowAnchor()
        self.assert_("未成功关注主播", flag == 0)
        time.sleep(6)

        self.start_step("quit room")
        window.QuitRoom()
        self.assert_("未成功退房", window.QuitRoomSuccess() == 0)

        time.sleep(6)

        self.start_step("log out")
        window.log_out(num)

if __name__ == '__main__':
    FollowAnchor().debug_run()