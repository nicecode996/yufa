# -*- coding: utf8 -*-
"""watching living case
"""

from huoshanlib.testcase import HuoshanTest
from huoshanlib.app import HuoshanApp
from huoshanlib.main import MainWindow
from huoshanlib.popup import PrivacyAlertPop
import json
import time

class WatchingLivingRoom(HuoshanTest):
    """watching living case
    """
    owner = "tanjianxin"
    timeout = 1000

    def run_test(self):
        self.start_step("start app")
        self.device = self.acquire_device()
        self.app = HuoshanApp(self.device)

        self.start_step("check window")
        window = MainWindow(root=self.app)
        window.wait_for_existing()
        #点击首页去除弹窗
        window.init()
        time.sleep(5)

        self.start_step("enter room")
        window.EnterRoom()
        #检测是否会有多端登陆问题

        window.checked_more()
        self.assert_("未成功进房", window.EnterRoomSuccess() == 0)
        window.SwipeToNextRoom()
        time.sleep(20)
        window.SwipeToNextRoom()
        time.sleep(20)

        self.start_step("quit room")
        window.QuitRoom()
        time.sleep(5)
        self.assert_("未成功退房", window.QuitRoomSuccess() == 0)


if __name__ == '__main__':
    WatchingLivingRoom().debug_run()
