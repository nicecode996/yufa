# -*- coding: utf-8 -*-
"""alerts definitions
"""

from uibase.controls import Window
from uibase.upath import UPath, label_, type_, id_
from douyinlib.main import MainWindow

class IknowPopup(Window):
    window_spec = {"path": UPath(label_ == "我知道了", type_ == "AWEUIButton")}

    def handle(self):
        return self.click()


class PersonalInformationPopup(Window):
    window_spec = {"path": UPath(type_ == "AWEAccountPrivacyAndUserItemAlertView")}

    def get_locators(self):
        return {
            "个人信息保护指引": {"path": UPath(label_ == "个人信息保护指引")},
            "好的": {"path": UPath(label_ == "好的", type_ == "AWEUIButton")},
        }

    def handle(self):
        return self.好的.click()

class FindFriendsPopup(Window):
    window_spec = {"path": UPath(type_ == "AWEUploadContactAlertView")}

    def get_locators(self):
        return {
            "发现通讯录好友": {"path": UPath(label_ == "发现通讯录好友")},
            "取消": {"path": UPath(label_ == "取消", type_ == "AWEUIButton")},
        }

    def handle(self):
        return self.取消.click()


class LocationPopup(Window):
    window_spec = {"path": UPath(label_ == "暂不", type_ == "AWEUIButton")}

    def handle(self):
        return self.click()

class MoreLivePopup(Window):
    window_spec = {"path": UPath(label_ == "左滑查看更多直播", id_ == "(upGuideLabel)")}

    def handle(self):
        return self.click()

