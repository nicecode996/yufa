# -*- coding: utf-8 -*-
# @Time : 2020/10/15 5:30 下午
# @Author : Zhangfusheng
# @File : android_scrool.py
import os


class AndroidScroll:
    def __init__(self, device_id, action):
        self.device_id = device_id
        """需要维护在测试机上各个app切换前后摄像头的坐标位置"""
        self.android_coordinates = {"右滑": [100, 200, 100, 600],
                                    "左滑": [100, 600, 100, 200],
                                    "上滑": [500, 1100, 500, 300],
                                    "下滑": [100, 200, 900, 200], }
        self.click(self.android_coordinates[action])

    def click(self, coordinates):
        """android对应软件在直播预览页切换摄像头点击"""
        os.system('adb -s {} shell input swipe {} {} {} {} 100'.format(self.device_id, coordinates[0], coordinates[1],
                                                                      coordinates[2], coordinates[3]))
        return


if __name__ == '__main__':
    AndroidScroll("f7e9e3d5", "上滑")
