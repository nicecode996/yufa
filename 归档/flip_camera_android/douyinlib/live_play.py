# -*- coding: utf-8 -*-
# @Time : 2020/7/6 8:20 下午
# @Author : Zhangfusheng
# @File : live_play.py
import time
from shoots_android.control import Window
from shoots_android.control import Control
from uibase.upath import UPath, id_
from android_device import logger


class LiveWindow(Window):
    """直播页面的元素"""
    window_spec = {"activity": "com.ss.android.ugc.aweme.live.LivePlayActivity"}

    def get_locators(self):
        return {
            "主播头像和关注按钮": {"type": Control, "path": UPath(id_ == "anchor_info_container")},
            "评论区": {"type": Control, "path": UPath(id_ == "messages_view")},
            "工具栏": {"type": Control, "path": UPath(id_ == "toolbar_container")},
            "编辑区": {"type": Control, "path": UPath(id_ == "edit_btn_audience")},
        }

    def wait_for_loading(self):
        self['评论区'].wait_for_visible(interval=0.01)
        self['工具栏'].wait_for_visible(interval=0.01)
        self['编辑区'].wait_for_visible(interval=0.01)
