# -*- coding: utf-8 -*-
# @Time : 2020/7/28 8:47 下午
# @Author : Zhangfusheng
# @File : click_move.py

import os


class AndroidClick:
    def __init__(self, device_id, follow):
        self.device_id = device_id
        """点击关注"""
        self.android_coordinates = {"主入口": [560.5, 1846], "点击开直播": [896, 1851], "未开播-美化面板": [191, 1209],
                                    "null": [120, 530],
                                    "开始视频直播": [329, 1086], "开播-美化面板": [924, 1832],
                                    "点开美化按钮": [483, 1229], "直播间美化面板": [103, 1161], "null-2": [154, 553],
                                    "点击美化按钮-1:[474, 1223]"
                                    "点击道具面板": [276, 1173], "null-3": [529, 552], "关闭": [569, 1229], "SURE": [567, 757]}

    #
    #     self.click(self.android_coordinates[follow])python -m shoots_android install
    '''
    def __init__(self, device_id, name):
        self.device_id = device_id


        """需要维护在测试机上各个app切换前后摄像头的坐标位置"""
        self.android_coordinates = {"抖音": [721, 1830], "西瓜": [735, 1832], "火山": [744, 1854], "皮皮虾": [1008, 1839],
                                    "快手": [990, 1824], "斗鱼": [1001, 1855],
                                    "花椒": [587, 1842], "YY": [1006, 1833], "映客": [631, 1832]}

        self.click(self.android_coordinates[name])
    '''

    def click(self, coordinates):
        """android对应软件在直播预览页切换摄像头点击"""
        os.system('adb -s {} shell input swipe {} {} {} {} 100'.format(self.device_id, coordinates[0], coordinates[1],
                                                                      coordinates[0], coordinates[1]))
        return


if __name__ == '__main__':
    AndroidClick("3ee4c4df")
