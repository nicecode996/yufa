# -*- coding: utf8 -*-
"""watching living case
"""

from toutiaolib.testcase import ToutiaoTest
from toutiaolib.app import ToutiaoApp
from toutiaolib.main import MainWindow
import json
import time

class WatchingLivingRoom(ToutiaoTest):
    """watching living case
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

        self.start_step("enter room")
        num  = window.EnterRoom()

        time.sleep(6)
        # 检测是否会有多端登陆问题
        window.checked_more()
        self.assert_("未成功进房", num == 0)

        window.SwipeToNextRoom()
        time.sleep(20)
        window.SwipeToNextRoom()
        time.sleep(20)

        self.start_step("swipe to next room")
        flag = window.ScrollToNextRoom()
        self.assert_("未成功上下滑", flag == 0)


if __name__ == '__main__':
    WatchingLivingRoom().debug_run()