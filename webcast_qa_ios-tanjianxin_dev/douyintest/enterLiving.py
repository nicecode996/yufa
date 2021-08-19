]

# -*- coding: utf8 -*-
"""watch living case
"""

from douyinlib.testcase import DouyinTest
from douyinlib.app import DouyinApp
from douyinlib.main import MainWindow
import json
import time

"""
登录的情况下，进入直播间：
操作步骤：
1. 启动app并处理弹窗
2. 登录
3. 进入直播间

"""


class WatchingLivingRoom(DouyinTest):
    """enter living(logined)
    """

    owner = "tanjianxin"
    timeout = 1000

    def run_test(self):
        self.start_step("start app")
        self.device = self.acquire_device()
        self.app = DouyinApp(self.device)

        self.start_step("check window")
        window = MainWindow(root=self.app)
        window.wait_for_existing()
        # window.init()
        time.sleep(5)

        self.start_step("login in")
        num = window.log_in()
        time.sleep(5)

        self.start_step("enter room")
        window.EnterRoom()
        # 检测是否多端登陆并正在直播
        window.checked_more()
        self.assert_("未成功进房", window.EnterRoomSuccess() == 0)
        window.SwipeToNextRoom()
        time.sleep(8)


if __name__ == '__main__':
    WatchingLivingRoom().debug_run()
