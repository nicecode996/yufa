# -*- coding: utf8 -*-
"""main page
"""

# 2020/03/12 auto generated by shoots


from uibase.controls import Window
from uibase.upath import UPath, type_, visible_, label_, id_
import time
from shoots import logger

# -*- coding: utf-8 -*-
"""alerts definitions
"""

from uibase.controls import Window
from uibase.upath import UPath, label_, type_, id_, text_
from douyinlib.main import MainWindow

class PrivacyAlertPop(Window):

    # window_spec = {"path": UPath(type_ == "HTSAmazingBackgroundView")}
    window_spec = {"path": UPath(label_ == "个人信息保护指引", type_ == "HTSPopoverWindow")}

    def get_locators(self):
        return {
            "好的": {"path": UPath(label_ == "好的",type_=="UILabel")},
            "我知道了": {"path": UPath(label_ == "我知道了", type_ == "UIButton")},
            "同意": {"path": UPath(label_ == "同意", type_ == "UIButton")},
            "关闭": {"path": UPath(label_ == "closelive", type_ == "UIButton")}
        }

    def handle(self):
        if self["同意"].existing and self["同意"].visible:
            return self["同意"].click()
        elif self["好的"].existing and self["好的"].visible:
            return self["好的"].click()
        elif self["我知道了"].existing and self["我知道了"].visible:
            return self["我知道了"].click()

class SwipeTip(Window):
    """
    上下滑引导弹窗
    """
    window_spec = {"path": UPath(label_ == "上下滑动切换内容", visible_ == True)}

    def get_locators(self):
        return{
            "上下滑动切换内容": {"path": UPath(label_ == "上下滑动切换内容", visible_ == True)}
        }

    def handle(self):
        return self['上下滑动切换内容'].click()


class PersonalInformationPopup(Window):

    window_spec = {"path": UPath(type_ == "AWEAccountPrivacyAndUserItemAlertView")}

    def get_locators(self):
        return {
            "个人信息保护指引": {"path": UPath(label_ == "个人信息保护指引")},
            "好的": {"path": UPath(label_ == "好的", type_ == "AWEUIButton")},
        }

    def handle(self):
        return self.好的.click()

class AddressPopup(Window):
    """发现通讯录好友弹窗
    """
    window_spec = {"path": UPath(label_ == "发现通讯录好友", type_ == "HTSStandardPopupView")}

    def get_locators(self):
        return {
            "关闭": {"path": UPath(label_ == "closelive", type_ == "UIButton")}
        }

    def handle(self):
        return self["关闭"].click()

class SwipehighPopup(Window):
    """发现通讯录好友弹窗
    """
    window_spec = {"path": UPath(type_ == "HTSVideoSlideScrollToNextGuideView")}

    def get_locators(self):
        return {
            "精选tab滑动引导动画": {"path": UPath(type_ == "LOTAnimationView")}
        }

    def handle(self):
        if self["精选tab滑动引导动画"].wait_for_visible(timeout=20, raise_error=False):
            logger.info("找到精选tab滑动引导窗口1")
            logger.info(self["精选tab滑动引导动画"].driver.get_element_info(self["精选tab滑动引导动画"].id))
            rect = self["精选tab滑动引导动画"].rect
            to_x = rect.center[0]
            to_y = rect.center[1] - rect.height / 2
            # + 30
            return self["精选tab滑动引导动画"].drag(to_x, to_y, 0, rect.height)

class ChildModePop(Window):
    """
    青少年模式弹窗
    """
    # window_spec = {"path": UPath(type_ == "UIView")}
    window_spec = {"path": UPath(label_ == "青少年弹窗", index=0)}

    def get_locators(self):
        return{
            "我知道了": {"path": UPath(label_ == "我知道了", index=0)}
        }

    def handle(self):
        self['我知道了'].click()
        return True

# class LocalePopup(Window):
#     """允许访问你的位置弹窗
#     """
#     window_spec = {"path": UPath(type_ == "HTSAmazingBackgroundView")}
#
#     def get_locators(self):
#         return {
#             "同意": {"path": UPath(type_ == "HTSModernStandardButton", index=1)}
#         }
#
#     def handle(self):
#         return self["同意"].click()


class BetaTestPop(MainWindow):
    """
    内测弹窗
    """
    window_spec = {"path": UPath(label_ == "内测邀请弹窗")}

    def get_locators(self):
        return {
            "close": {"path": UPath(label_ == "icon tool close")},
            "参与": {"path": UPath(label_ == "立即升级参与")}
        }

    def click_close(self):
        # print(self.is_found_label(self['我知道了']))
        self['close'].refresh()
        self['close'].click()

    def click_ok(self):
        # print(self.is_found_label(self['我知道了']))
        self['参与'].click()


class OuterTestPop(Window):
    window_spec = {"path": UPath(
        label_ == "内测邀请弹窗", type_ == "HTSStandardPopupView")}

    def get_locators(self):
        return {
            "当前版本不再提示": {"path": UPath(label_ == "当前版本不再提示", type_ == "UIButton")},
            "下次再说": {"path": UPath(label_ == "下次再说", type_ == "UIButton")},
        }

    def handle(self):
        print("in handle")
        self["当前版本不再提示"].wait_for_existing()
        print("after wait_for_existing")
        print(self["当前版本不再提示"].clickable)
        self["当前版本不再提示"].click()
        print("after click")
        self["下次再说"].wait_for_existing()
        return self["下次再说"].click()



class FollowGuidePopup(Window):
    """关注按钮
    """
    window_spec = {"path": UPath(type_ == "HTSLiveFollowGuidePopupView")}

    def handle(self):
        # 点击popup外部区域取消弹窗
        from huoshanlib.main import MainWindow
        main = MainWindow(root=self.app)
        return main["直播间a"].click()



#169版本
class SwipePopup(Window):
    """上滑查看更多视频
    """
    window_spec = {"path": UPath(label_ == "上滑查看更多视频")}

    def handle(self):

        self.parent.scroll(distance_y=600)


class CloseLivePopup(Window):
    """上滑查看更多视频
    """
    window_spec = {"path": UPath(label_ == "提示",type_=="UILabel")}

    def get_locators(self):
        return {
            "结束直播": {"path": UPath(label_ == "结束直播", id_=="(结束直播)",type_ == "UIButton")}
        }
    def handle(self):
        self["结束直播"].click()

# # class TimeAlbumPopup(Window):
# #     """时光相册弹窗
# #     """
# #     window_spec = {"path": UPath(
# #         label_ == "打开时光相册记录美好生活", type_ == "HTSStandardPopupView")}
# #
# #     def get_locators(self):
# #         return {
# #             "关闭时光相册": {"path": UPath(label_ == "closelive", type_ == "UIButton")}
# #         }
# #
# #     def handle(self):
# #         return self["关闭时光相册"].click()
# #
#
# # class FlameTaskPopup(Window):
# #     """任务书弹窗
# #     """
# #     window_spec = {"path": UPath(type_ == "HTSFlameTaskBookViewController")}
# #
# #     def get_locators(self):
# #         return {
# #             "关闭": {"path": UPath(label_ == "flame share view close", type_ == "UIButton")}
# #         }
# #
# #     def handle(self):
# #         return self["关闭"].click()
#
#
# class LocalePopup(Window):
#     """允许访问你的位置弹窗
#     """
#     window_spec = {"path": UPath(type_ == "HTSAmazingBackgroundView")}
#
#     def get_locators(self):
#         return {
#             "同意": {"path": UPath(type_ == "HTSModernStandardButton", index=1)}
#         }
#
#     def handle(self):
#         return self["同意"].click()
#
#
#新版本
# class AddressPopup(Window):
#     """发现通讯录好友弹窗
#     """
#     window_spec = {"path": UPath(label_ == "发现通讯录好友", type_ == "HTSStandardPopupView")}
#
#     def get_locators(self):
#         return {
#             "关闭": {"path": UPath(label_ == "closelive", type_ == "UIButton")}
#         }
#
#     def handle(self):
#         return self["关闭"].click()