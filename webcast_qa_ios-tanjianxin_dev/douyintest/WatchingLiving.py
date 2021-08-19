# -*- coding: utf8 -*-
"""watch living case
"""

from douyinlib.testcase import DouyinTest
from douyinlib.app import DouyinApp
from douyinlib.main import MainWindow
import json
import time

class WatchingLivingRoom(DouyinTest):
    """watch living case
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
        #window.init()
        time.sleep(5)

        self.start_step("enter room")
        window.EnterRoom()
        #检测是否多端登陆并正在直播
        window.checked_more()
        self.assert_("未成功进房", window.EnterRoomSuccess() == 0)
        window.SwipeToNextRoom()
        time.sleep(20)

        self.start_step("quit room")
        window.QuitRoom()


if __name__ == '__main__':
    WatchingLivingRoom().debug_run()
