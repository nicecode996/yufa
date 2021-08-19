# -*- coding: utf-8 -*-
"""alerts definitions
"""

from uibase.controls import Window
from uibase.upath import UPath, label_, type_, id_ ,visible_,text_
import time


class IknowPopup(Window):

    window_spec = {"path": UPath(label_ == "我知道了", type_ == "UIButton",visible_==True)}
    #
    # def get_locators(self):
    #     return {
    #         "我知道了": {"path": UPath(label_ == "我知道了", type_ == "UIButton",visible_==True)},
    #         "同意": {"path": UPath(label_ == "同意", type_ == "UIButton",visible_==True)}
    #
    #     }
    def handle(self):
        return self["我知道了"].click()

class IagreePopup(Window):
    window_spec = {"path": UPath(label_ == "同意", type_ == "UIButton",visible_==True)}

    def handle(self):
        return self.click()

class UseErrorPopup(Window):
    window_spec = {"path": UPath(type_ == "_UIAlertControllerInterfaceActionGroupView", index=0)}

    def get_locators(self):
        return {
            "确定": {"path": UPath(label_ == "确定", type_ == "_UIAlertControllerActionView")},
        }

    def handle(self):
        return self.确定.click()


class QuitRoom(Window):
    window_spec = {"path": UPath(label_ == "退出", type_ == "UIButton",index=0)}

    def handle(self):
        return self.click()



#多端登陆问题
class Morelogin(Window):

    window_spec = {"path": UPath(label_ == "取消", type_ == "UIButton",index=0)}

    def handle(self):
        return self.click()