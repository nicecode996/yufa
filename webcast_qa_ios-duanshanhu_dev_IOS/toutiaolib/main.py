# -*- coding: utf8 -*-
"""main page
"""
#2020/06/30 auto generated by shoots

from uibase.controls import Window, TextEdit, ControlList, Control
from uibase.upath import UPath, text_, type_, label_, id_, visible_
import time
from webcastlib.mobile_account import MobileRequest
from shoots.retry import Retry
from shoots import logger

class Tab(Control):

    def get_locators(self):
        return {
            "title_elem": {"path": UPath(type_ == "SSThemedLabel")}
        }

    @property
    def title(self):
        return self.title_elem.text

class Tabs(ControlList):
    elem_class = Tab
    elem_path = UPath(type_ == "TTTabBarItem")

    def get_tab(self, name):
        for item in self.items():
            if item.title == name:
                return item

class MainWindow(Window):
    """main window
    """
    window_spec = {"path": UPath(type_ == "UIWindow", index=0, depth=1)}
    
    def get_locators(self):
        return {
            "tabs": {"type": Tabs, "path": UPath(type_ == "TTTabbar")},
            #登录相关
            "未登录": {"path": UPath(label_ == "未登录", type_ == "TTTabBarItem")},
            "登录": {"path": UPath(label_ == "登录", id_ == "(loginButton)")},
            "手机号": {"type": TextEdit,
                    "path": UPath(type_ == "TTAccountLoginV2Textfield", id_ == "(numTextField)")},
            "获取短信验证码": {"path": UPath(id_ == "(nextButton)", label_ == "获取短信验证码")},
            "验证码": {"type": TextEdit,
                    "path": UPath(type_ == "TTAccountLoginV2Textfield", id_ == "(numTextField)")},
            #退登相关
            "我的": {"path": UPath(label_ == "我的", type_ == "TTTabBarItem")},
            "系统设置": {"path": UPath(label_ == "系统设置", type_ == "TTProfileGridItemCell")},
            "退出登录": {"path": UPath(label_ == "退出登录", id_ == "(logoutTitleLabel)")},
            "settings": {"path": UPath(type_ == "SettingView") / UPath(type_ == "SSThemedTableView")},
            "确认退出": {"path": UPath(label_ == "确认退出", type_ == "UIButton")},

            #开播相关
            "发布": {"path": UPath(label_ == "发布", id_ == "(publishButton)")},
            "开直播": {"path": UPath(label_ == "开直播", id_ == "(titleLabel)")},
            #小直播间弹窗入口
            "直播间1": {"path": UPath(type_== "TTLFeedPreviewContainer", id_ == "(previewContentView)",visible_==True,index=0)},
            "直播间2": {"path": UPath(type_== "TTXiguaLivePreviewContainerView", id_ == "(previewContainerView)",visible_==True,index=0)},

            "选择分类": {"path": UPath(label_ == "选择分类", id_ == "(categoryLabel)")},
            "选择直播内容": {"path": UPath(label_ == "选择直播内容", id_ == "(categoryLabel)")},

            "户外打野": {"path": UPath(label_ == "户外打野", id_ == "(mainTitleLabel)", index=0)},
            "开始视频直播": {"path": UPath(label_ == "开始视频直播", id_ == "(开始视频直播)",index=1)},
            #关播相关
            "关播按钮": {"path": UPath(label_ == "closeLive",type_=="HTSLiveToobarItemCell")},
            "关播按钮_170": {"path": UPath(label_ == "关闭直播")},

            "确定": {"path": UPath(label_ == "确定", id_ == "(actionContentView)")},
            "关播页关闭按钮": {"path": UPath(label_ == "close", id_ == "(closeButton)")},
            "关播页关闭按钮_170": {"path": UPath(label_ == "退出关播页面", type_ == "UIButton")},
            #送礼相关
            "更多按钮": {"path": UPath(label_ == "group",type_=="HTSLiveToobarItemCell")},
            "更多按钮_170": {"path": UPath(label_ == "更多")},
            "礼物": {"path": UPath(label_ == "礼物", id_ == "(礼物)")},
            "礼物a": {"path": UPath(type_ == "IESLiveRoomGiftItemCell", index=0)},
            "礼物面板关闭按钮": {"path": UPath(id_ == "(closeButton)")},
            "礼物面板关闭按钮_170": {"path": UPath(label_ == "IESLiveGiftPanelCloseButtonAccessID")},

            #进房相关
            "西瓜视频": {"path": UPath(label_ == "西瓜视频", type_ == "TTTabBarItem")},
            "直播tab": {"path": UPath(label_ == "直播", type_ == "CategorySelectorButton")},
            #"直播间": {"path": UPath(id_ == "(previewContainerView)", type_ == "TTXiguaLivePreviewContainerView", visible_ == True, index=0)},
            "直播中": {"path": UPath(id_ == "(textLabel)",label_== "直播中",visible_ == True, index=0)},
            "主播id": {"path": UPath(id_ == "(nameLabel)",visible_==True,index=0)},
            "主播头像": {"path": UPath(id_ == "(avatarView)",label_=="用户头像")},
            "关注": {"path": UPath(label_ == "关注", id_ == "(followBtn)")},
            "媒体直播间头像": {"path": UPath(id_ == "(avatarImageView)",type_=="UIImageView")},
            "粉丝团入口": {"path": UPath(id_ == "(fansBtn)", type_ == "HTSLiveButton")},
            "直播间内页面": {"path": UPath(type_ == "IESLiveFeedCollectionView")},
            #退房相关
            #"退出直播间": {"path": UPath(label_ == "liveroom ic close white", id_ == "(liveroom_ic_close_white)", visible_ == True)},
            "退出直播间": {"path": UPath(label_ == "kHTSLiveToolbarItemClose",type_=="HTSLiveToobarItemCell",visible_ == True)},
            "退出": {"path": UPath(type_ == "UIButton", label_ == "退出")},
            "直播意外中断了": {"path": UPath(type_ == "UILabel", label_ == "直播意外中断了")},
            "恢复直播": {"path": UPath(type_ == "UIButton", label_ == "恢复直播")},
            "更多直播": {"path": UPath(type_ == "UILabel", id_ == "(titleLabel)", label_ == "更多直播")},
        }

    @property
    def login_tab(self):
        for text in ["未登录", "我的"]:
            for tab in self.tabs.items():
                if tab.title == text:
                    return tab

    def is_logined(self):
        return self.login_tab.title == "我的"

    def log_in(self):
        self.login_tab.click()
        if self.is_logined():
            num = 0
            return num

        g = MobileRequest()
        num = g.get_num(tags=1112)
        self.username = num
        self.usercode = "0 8 1 9"
        logger.info(num)

        self["未登录"].click()
        self["登录"].click()
        time.sleep(2)
        self["手机号"].input(self.username)
        self["获取短信验证码"].refresh()
        self["获取短信验证码"].click()
        time.sleep(2)
        self["验证码"].input(self.usercode)

        return num

    def log_out(self, num):
        if self["关播页关闭按钮"].existing:
            self["关播页关闭按钮"].click()
        self["我的"].click()
        time.sleep(1)  # UITableViewCell reuse
        self.系统设置.click()
        time.sleep(0.5)
        for _ in range(3):
            self.settings.scroll(distance_y=300)
            if self.退出登录.existing and self.退出登录.visible:
                self.退出登录.click()
                self.确认退出.click()
                self.西瓜视频.wait_for_visible()
                break
        g = MobileRequest()
        g.release_num(tags=1112, num=num)

    def EnterRoom(self):
        self["西瓜视频"].click()
        #time.sleep(8)
        self["直播tab"].wait_for_visible(timeout=30, raise_error=False)
        self["直播tab"].click()
        time.sleep(5)
        #进入直播间方式1
        if self["直播中"].wait_for_visible(timeout=30, raise_error=False):
           self["直播中"].click()
           print("通过直播中进入直播间")
        #进入直播间方式2
        elif self["直播间1"].wait_for_visible(timeout=10, raise_error=False):
                self["直播间1"].click()
        else:
           if  self["直播间1"].wait_for_visible(timeout=10, raise_error=False):
                self["直播间1"].click()
        # 检测是否进入直播间
        if self["退出直播间"].wait_for_visible(timeout=30, raise_error=False):
            return 0
        else:
            if self["直播中"].wait_for_visible(timeout=20, raise_error=False):
                self["直播中"].click()

            #如果是媒体直播间则切换直播间，避免后续送礼等操作不成功
            while self["媒体直播间头像"].wait_for_visible(timeout=20,raise_error=False):
                self.更多直播.scroll(distance_x=0, distance_y=600)
            if self["退出直播间"].wait_for_visible(timeout=5,raise_error=False) or self["主播头像"].wait_for_visible(timeout=5,raise_error=False):
                return 0
            else:
                return 1

    def FollowAnchor(self):
        if self["关注"].visible:
            self["关注"].click()
            time.sleep(4)
            if not self["关注"].visible:
                return 0
        else:
            while not self["关注"].visible:
                self.SwipeToNextRoom()
            if self["关注"].visible:
                self["关注"].click()
                time.sleep(2)
                if not self["关注"].visible:
                    return 0
            else:
                return 1

    def SwipeToNextRoom(self):
        self.更多直播.scroll(distance_x=0, distance_y=600)
        # 检测当前直播间是否可以进行关注或者送礼
        while not self["关注"].wait_for_visible(raise_error=False):
            self.更多直播.scroll(distance_x=0, distance_y=600)

    def ScrollToNextRoom(self):
        #检测是否是媒体直播间

        while not self["主播id"].wait_for_visible(timeout=10,raise_error=False):
            print("检测不到id")
            self.SwipeToNextRoom()
        anchor_a = self.GetAnchorid()
        self.SwipeToNextRoom()
        time.sleep(20)
        self.SwipeToNextRoom()
        time.sleep(20)
        # 检测是否是媒体直播间
        while not self["主播id"].wait_for_visible(timeout=6, raise_error=False):
            self.SwipeToNextRoom()

        anchor_b = self.GetAnchorid()
        if anchor_a == anchor_b:
            return 1
        else:
            return 0

    def GetAnchorid(self):
        self["主播id"].refresh()
        Anchorid = self["主播id"].elem_info["label"]
        print(Anchorid)
        return Anchorid

    def QuitRoom(self):
        self.wait_for_visible()
        self["退出直播间"].click()
        time.sleep(4)

        if self["退出"].wait_for_existing(raise_error=False):
            self["退出"].click()
        time.sleep(2)
        if self["退出直播间"].existing:
            self["退出直播间"].click()
            if self["退出"].existing:
                self["退出"].click()

    def QuitRoomSuccess(self):
        if self["西瓜视频"].wait_for_visible(30, raise_error = False):
            return 0
        else:
            return 1

    def StartLiving(self):
        self["西瓜视频"].click()
        time.sleep(5)
        self["发布"].click()
        time.sleep(2)
        self["开直播"].click()
        time.sleep(5)
        if self["开直播"].existing:
            time.sleep(2)
            self["开直播"].click()
        time.sleep(3)

        self["开始视频直播"].wait_for_visible(30, raise_error = False)
        if self["选择分类"].existing:
            self["选择分类"].click()
            time.sleep(2)
            self["户外打野"].click()
            time.sleep(2)
        #165 版本更新直播分类选项
        elif self["选择直播内容"].existing:
            self["选择直播内容"].click()
            time.sleep(2)
            self["户外打野"].click()
            time.sleep(2)

        if self["开始视频直播"].wait_for_visible(30, raise_error = False):
            self["开始视频直播"].click()
            time.sleep(5)

    def StartLivingSuccess(self):
        if self["关播按钮_170"].wait_for_visible(timeout=10,raise_error = False):
            return 0
        elif self["关播按钮"].wait_for_visible(timeout=10,raise_error=False):
            return 0
        else:
            return 1

    def SendGift(self):

        time.sleep(4)
        if self["更多按钮_170"].wait_for_visible(timeout=10, raise_error=False):
            time.sleep(2)
            self["更多按钮_170"].click()
        else:
            self["更多按钮"].click()

        while not self["礼物"].wait_for_visible(raise_error = False):
            self["更多按钮_170"].click()
            time.sleep(1)
        else:
            self["礼物"].click()
        time.sleep(3) # 等待礼物资源加载
        self["礼物a"].click()
        self["礼物a"].click()
        time.sleep(5)

        if self["礼物面板关闭按钮"].wait_for_visible(timeout=10, raise_error=False):
            self["礼物面板关闭按钮"].click()

        elif self["礼物面板关闭按钮_170"].wait_for_visible(timeout=10, raise_error=False):
            self["礼物面板关闭按钮_170"].click()


    def checked_more(self):
        # 多端登陆看直播前先退出登录
        if self["确定"].wait_for_existing(timeout=6, raise_error=False):
            self["确定"].click()
            time.sleep(3)

    def CloseLiving(self):

        time.sleep(3)
        if self["关播按钮_170"].wait_for_visible(raise_error = False):
            self["关播按钮_170"].click()

        else:
            self["关播按钮"].click()
        time.sleep(6)
        if not self["确定"].wait_for_visible(raise_error=False):
            self["关播按钮_170"].click()
        else:
            pass
        self["确定"].click()

    def CloseLivingSuccessful(self):
        if self["关播页关闭按钮_170"].wait_for_visible(raise_error=False):
            return 0
        elif self["关播页关闭按钮"].wait_for_visible(raise_error=False):
            return 0
        else:
            return 1
