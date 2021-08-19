# -*- coding: utf-8 -*-
# @Time : 2020/7/6 5:35 下午
# @Author : Zhangfusheng
# @File : follow.py
import time
from shoots_android.control import Window
from shoots_android.control import Button, Control, ScrollView, LinearLayout, FrameLayout, RelativeLayout
from uibase.upath import UPath, id_, type_, text_, desc_
from android_device import logger


class StartFollowWindow(Window):
    """打开关注页面和好友列表"""
    window_spec = {"activity": "com.ss.android.ugc.aweme.following.ui.FollowRelationTabActivity"}

    def get_locators(self):
        return {
            # "要观看的主播头像": {"type": LinearLayout,
            #              "path": UPath(id_ == "rv_list") / UPath(id_ == "layout_unread_avatar", index=0)},
            # "要观看的主播名": {"type": Control, "path": UPath(id_ == "iv_avatar", index=0)},
            # "要观看的主播名": {"type": Control, "path": UPath(id_ == "layout_unread_avatar", index=0)},
            # "要观看的主播名": {"type": Control, "path": UPath(id_ == "btn_follow_user", index=0)},
            "要观看的主播名": {"type": Control, "path": UPath(id_ == "txt_user_name", index=3)},   # index设置位置不同的主播
            # "搜索": {"type": Control, "path": UPath(id_ == "fl_intput_hint_container")},
            "好友列表": {"type": Control, "path": UPath(id_ == "rv_list")},
            "主播的个人页头像": {"type": FrameLayout, "path": UPath(id_ == "fl_head")},
        }

    def wait_for_loading(self):
        self['主播的个人页头像'].wait_for_visible()

    def open_follow_list_page(self):
        """点击列表内第一个主播头像"""
        self["要观看的主播名"].wait_for_visible()
        self["要观看的主播名"].click()
        time.sleep(2)

    def open_live_page(self):
        self["主播的个人页头像"].click()
