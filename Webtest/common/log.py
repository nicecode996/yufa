# -*- coding: utf-8 -*-
# author:jiayanzi

import logging
import os
import time
from logging import Logger


class Log:

    def __init__(self):
        global proDir, ResultPath, LogPath
        proDir = os.getcwd()
        ResultPath = os.path.join(proDir, "test_result")
        # create log file if it doesn't exists
        LogPath = os.path.join(ResultPath, str(time.strftime('%Y-%m-%d', time.localtime(time.time()))))
        if not os.path.exists(LogPath):
            os.mkdir(LogPath)
        # defined logger
        self.logger = logging.getLogger(__name__)
        # define logger level
        self.logger.setLevel(level=logging.INFO)

        # 定义日志输出文件
        handler = logging.FileHandler(os.path.join(LogPath, "output.txt"),encoding="UTF-8")
        # 定义日志输出级别
        handler.setLevel(logging.INFO)
        # 定义日志输出格式
        formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        # add logger
        self.logger.addHandler(handler)

    def get_logger(self):
        return self.logger


logger = Log().get_logger()
