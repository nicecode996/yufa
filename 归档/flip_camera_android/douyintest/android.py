# -*- coding: utf-8 -*-
# @Time : 2020/8/3 4:02 下午
# @Author : Zhangfusheng
# @File : android.py
import time
from douyinlib import shoot_move
from douyinlib.testcase import DouyinAndroidTest
from douyinlib.app import *
from douyinlib.android_click import AndroidClick


class AndroidTest(DouyinAndroidTest):
    """demo test case
    """
    timeout = 300
    owner = "zfs"

    def switch_app(self, app_name):
        """切换生成不同的app对象"""
        if app_name == "抖音":
            self.app = DouyinAndroidApps(self.device)
        elif app_name == "西瓜":
            self.app = XiguaAndroidApps(self.device)
        elif app_name == "火山":
            self.app = HuoshanAndroidApps(self.device)
        elif app_name == "皮皮虾":
            self.app = PipixiaAndroidApps(self.device)
        elif app_name == "快手":
            self.app = KuaishouAndroidApps(self.device)
        elif app_name == "斗鱼":
            self.app = DouyuAndroidApps(self.device)
        elif app_name == "YY":
            self.app = YYAndroidApps(self.device)
        elif app_name == "花椒":
            self.app = HuajiaoAndroidApps(self.device)
        elif app_name == "映客":
            self.app = YingkeAndroidApps(self.device)
        else:
            raise ValueError("app名称设置错误")
        return

    def run_test(self):
        shoot_device_id = "9ef47f00"  # 拍摄手机的device ID
        move_device_id = "3ee4c4df"  # 测试手机的device ID
        data_path = "../douyinlib/data/"  # 视频保存的路径
        app_name = "抖音"  # 设置要使用的app，可选 抖音 西瓜 火山 皮皮虾 快手 斗鱼 花椒 YY 映客
        self.start_step("启动被测试手机上的app")
        self.device = self.acquire_device()
        self.switch_app(app_name)  # 生成对应的app对象
        # self.start_step("页面控件")
        # x, y = AndroidClick("页面控件").get_coordinates()
        # self.app.click(x, y)
        time.sleep(30)
        # self.start_step("主入口")
        # AndroidClick(move_device_id, "主入口")
        # time.sleep(3)
        # self.start_step("点击开直播")
        # AndroidClick(move_device_id, "点击开直播")
        self.start_step("拍摄手机来录像")
        shoot_move.start_shoot(shoot_device_id)
        time.sleep(2)
        self.start_step("预览页点击翻转摄像头")
        AndroidClick(move_device_id, "未开播-美化面板")
        time.sleep(3)
        self.start_step("结束拍摄")
        shoot_move.end_shoot(shoot_device_id, data_path)
        '''
        AndroidClick(move_device_id, "null")
        time.sleep(3)
        AndroidClick(move_device_id, "开始视频直播")
        time.sleep(3)
        AndroidClick(move_device_id, "开播-美化面板")
        time.sleep(3)
        AndroidClick(move_device_id, "点开美化按钮")
        time.sleep(3)
        AndroidClick(move_device_id, "直播间美化面板")
        time.sleep(3)
        AndroidClick(move_device_id, "null-2")
        time.sleep(3)
        AndroidClick(move_device_id, "点击美化按钮-1")
        time.sleep(3)
        AndroidClick(move_device_id, "点击道具面板")
        time.sleep(3)
        AndroidClick(move_device_id, "null-3")
        time.sleep(3)
        AndroidClick(move_device_id, "关闭")
        time.sleep(3)
        AndroidClick(move_device_id, "SURE")
        time.sleep(3)
        self.start_step("结束拍摄")
        shoot_move.end_shoot(shoot_device_id, data_path)
        '''


if __name__ == '__main__':
    for i in range(5):
        AndroidTest().debug_run()
