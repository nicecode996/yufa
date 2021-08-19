# -*- coding: utf-8 -*-
"""alerts definitions
"""

from uibase.controls import Window
from uibase.upath import UPath, label_, type_, id_

# class PrivacyAlert(Window):
#     window_spec = {"path": UPath(type_ == "PrivacyAlertView")}
#
#     def get_locators(self):
#         return {"got_it": {"path": UPath(label_ == "我知道了", type_ == "UIButton")}}
#
#     def handle(self):
#         if self.got_it.wait_for_visible(1, raise_error=False):
#             return self.got_it.click()
#         return True
class GotIt(Window):
    window_spec = {"path": UPath(label_ == "我知道了", type_ == "UIButton")}

    def handle(self):
        return self.click()

#关闭恢复之前的直播间
class Closeling(Window):
    window_spec = {"path": UPath(type_ == "_UIInterfaceActionRepresentationsSequenceView")}

    def get_locators(self):
        return {
            "直播意外中断了": {"path": UPath(label_=="直播意外中断了",id_== "(titleLabel)")},
            "取消": {"path": UPath(label_ == "取消",id_=="(label)")}
        }
    def handle(self):
        return self["取消"].click()


class TTAppUpdateTipView(Window):
    window_spec = {"path": UPath(type_ == "TTAppUpdateTipView")}

    def get_locators(self):
        return {
            "download_new_ipa": {"path": UPath(label_ == "优先体验", type_ == "UIButton")},
            "app_update_close_icon": {"path": UPath(label_ == "app update close icon", type_ == "UIButton")}
        }

    def handle(self):
        if self.download_new_ipa.wait_for_visible(3, raise_error=False):
            return self.app_update_close_icon.click()
        return True


class PushPopup(Window):
    window_spec = {"path": UPath(type_ == "SettingAppUpdateView")}

    def get_locators(self):
        return {"close_button": {"path": UPath(id_ == "(closeButton)")}}

    def handle(self):
        return self.close_button.click()



#1650版本之后新加的弹窗处理



# class TTAppUpdateTipView(Window):
#     window_spec = {"path": UPath(type_ == "TTAppUpdateTipView")}
#
#     def get_locators(self):
#         return {
#             "download_new_ipa": {"path": UPath(label_ == "优先体验", type_ == "UIButton")},
#             "app_update_close_icon": {"path": UPath(label_ == "app update close icon", type_ == "UIButton")}
#         }
#
#     def handle(self):
#         if self.download_new_ipa.wait_for_visible(3, raise_error=False):
#             return self.app_update_close_icon.click()
#         return True

class NewPagePopup(Window):

    window_spec = {"path": UPath(id_=="(closeButton)")}

    def get_locators(self):
        return {

                }

    def handle(self):
        return self.click()


class PushPopupNew(Window):
    window_spec = {"path": UPath(type_ == "TTAuthorizePushCustomDialog")}

    def get_locators(self):
        return {
            "close_button": {"path": UPath(label_ == "以后再说", type_ == 'UIButton')},
            "allow_button": {"path": UPath(label_ == "获取通知", type_ == 'UIButton')},
                }

    def handle(self):
        return self.close_button.click()


class TestGudiePopup(Window):
    window_spec = {"path": UPath(type_ == "TTOuterTestUserGuideDialog")}

    def get_locators(self):
        return {
            "close_button": {"path": UPath(label_ == "取消", type_ == 'UIButton')},
        }

    def handle(self):
        return self.close_button.click()
