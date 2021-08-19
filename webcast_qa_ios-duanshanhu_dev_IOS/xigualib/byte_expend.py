# -*- coding: UTF-8 -*-
"""
@author:lilingquan
@file:ocr_helper.py
@time:2020/1/209:55 下午
"""

import logging

from byted_cv.core.cv import Template
from byted_cv.core.cv import loop_find
from byted_cv.core.error import TargetNotFoundError


#对byte-cv的扩展方法
def getPath(driver, target_path, timeout=10, **kwargs):
    '''

    :param driver:
    :param target_path: 目标图片路径
    :param timeout: 查找超时时间，默认10s
    :param kwargs: 其他参数，threshold=None, target_pos=TargetPos.MID, record_pos=None, rgb=False
    threshold：门限值，默认0.7
    target_pos：目标图片中区域的位置
    record_pos: 查找图片中的位置
    rgb:识别结果是否使用rgb三通道进行校验
    '''
    v = Template(target_path, **kwargs)
    try:
        pos, screen_resolution = loop_find(driver, v, timeout=timeout)
    except TargetNotFoundError:
        logging.info("{} picture not found".format(dir))
        pos = None
        screen_resolution = None
    if pos is not None:
        return pos
    return False



