# -*- coding: utf-8 -*-
# @Time : 2020/7/6 6:18 下午
# @Author : Zhangfusheng
# @File : split_video.py
import cv2
from glob import glob
from pathlib2 import Path
from threading import Thread
import pandas as pd


def SplitFrame(video_names):
    """
    将视频分割为每帧保存，在视频文件对应的位置建立文件夹, 存入图片
    """
    fps_dict = {}
    for name in video_names:
        png_folder = name[:-4]
        Path(png_folder).mkdir(exist_ok=True)
        cap = cv2.VideoCapture(name)
        fps = round(cap.get(cv2.CAP_PROP_FPS), 4)
        fps_dict[name.split("/")[-1]] = fps
        if cap.isOpened():
            ver, frame = cap.read()
            count = 0
            while ver:
                ver, frame = cap.read()
                if ver:
                    cv2.imwrite(png_folder + '/' + str("%06d" % count) + ".png", frame)
                    cv2.waitKey(1)
                    count += 1
                else:
                    break
        df = pd.read_csv("./data/label.csv")
        for key in fps_dict:
            df.at[df["names"]==key, "FPS"] = fps_dict[key]
        df.to_csv("./data/label.csv", index=False, sep=",")


def build_csv(video_names):
    """对所有视频建立CSV文件"""
    names = [i.split("/")[-1] for i in video_names]
    dataFrame = pd.DataFrame(
        {"names": names, "time": [0] * len(names), "start_frame": [0] * len(names), "end_frame": [0] * len(names),
         "FPS": [0] * len(names)})
    dataFrame.to_csv("./data/label.csv", index=False, sep=",")


def run():
    threads_num = 5
    video_names = glob("./data/*.mp4")
    print(video_names)
    build_csv(video_names)
    threadsPool = []
    num = int(len(video_names) / threads_num)
    for i in range(threads_num):
        if i == threads_num - 1:
            task = video_names[i * num:]
        else:
            task = video_names[i * num: (i + 1) * num]
        threadsPool.append(Thread(target=SplitFrame, args=(task,)))

    for thread in threadsPool:
        thread.start()
    for thread in threadsPool:
        thread.join()


if __name__ == '__main__':
    run()
