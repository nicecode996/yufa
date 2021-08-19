# -*- coding: utf-8 -*-
# @Time : 2020/7/6 6:39 下午
# @Author : Zhangfusheng
# @File : shoot_move.py

import os
import time


def start_shoot(device_id):
    """使用另一只手机开始拍摄画面"""
    os.system('adb -s {} shell am start -a android.media.action.VIDEO_CAPTURE'.format(device_id))  # 打开录像
    time.sleep(2)
    # os.system('adb -s {} shell am start -a android.media.action.FOCUS_MODE_AUTO'.format(device_id))   # 自动对焦
    os.system('adb -s {} shell input tap 565 1731'.format(device_id))  # 拍摄按钮的位置需要实验前调试确定
    return


def end_shoot(device_id, data_path):
    """停止拍摄然后保存文件到工程目录"""
    time.sleep(1.5)
    os.system('adb -s {} shell input tap 565 1731'.format(device_id))  # 再次点击按钮结束拍摄
    time.sleep(2)
    os.system('adb -s {} shell input tap 535 1672'.format(device_id))  # 保存视频按钮的位置需要在实验前调试确定
    time.sleep(1)
    # os.system('adb -s {} shell input tap 827 205'.format(device_id))  # 退出相机
    time.sleep(2)
    video_path = os.popen('adb -s {} shell ls /sdcard/DCIM/Camera/*.mp4'.format(device_id)).readlines()
    for i in video_path:
        os.system('adb -s {} pull {} {}'.format(device_id, i.replace("\n", ""), data_path))  # 保存视频到工程目录
        time.sleep(5)
        os.system('adb -s {} shell rm {}'.format(device_id, i.replace("\n", "")))
    return


if __name__ == '__main__':
    start_shoot("9ef47f00")
    end_shoot("9ef47f00")
