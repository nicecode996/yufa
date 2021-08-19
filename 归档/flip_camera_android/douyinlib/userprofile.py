# -*- coding: utf-8 -*-
# @Time : 2020/7/6 6:00 下午
# @Author : Zhangfusheng
# @File : userprofile.py
import time
from shoots_android.control import Window
from shoots_android.control import Button, Control, ScrollView, LinearLayout, FrameLayout, RelativeLayout
from uibase.upath import UPath, id_, type_, text_, desc_
from android_device import logger


class StartLiveWindow(Window):
    """从个人主页打开直播"""
    window_spec = {"activity": "com.ss.android.ugc.aweme.profile.ui.UserProfileActivity"}

    def get_locators(self):
        return {
            "主播的个人页头像": {"type": FrameLayout, "path": UPath(id_ == "dark_avatar_mask")},
        }

    def open_live_page(self):
        self["主播的个人页头像"].wait_for_visible()
        self["主播的个人页头像"].click()
