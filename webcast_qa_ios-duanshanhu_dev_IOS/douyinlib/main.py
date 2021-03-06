# -*- coding: utf8 -*-
"""main page
"""
#2020/06/15 auto generated by shoots

from uibase.controls import Window, TextEdit, UIElementBase
from uibase.upath import UPath, text_, type_, label_, id_, visible_
import time
from webcastlib.mobile_account import MobileRequest
from douyinlib.LoginWindow import LoginWindow
from douyinlib.SettingTableView import OkPopup
from shoots import logger


class MainWindow(Window):
    """main window
    """
    window_spec = {"path": UPath(index=0, depth=1)}

    def get_locators(self):
        return {
            "拍摄按钮": {"path": UPath(label_ == "拍摄", id_ == "(btn_home_add_common)")},
            "启用相机访问权限": {"path": UPath(label_ == "启用相机访问权限", type_=="ACCAnimatedButton")},
            "启用麦克风访问权限": {"path": UPath(label_ == "启用麦克风访问权限", type_=="ACCAnimatedButton")},
            "开直播": {"path": UPath(label_ == "开直播", id_ == "(titleLabel)")},
            "影集": {"path": UPath(label_ == "影集", id_ == "(titleLabel)")},
            "开始视频直播":{"path": UPath(type_ == "UIButtonLabel", label_ == "开始视频直播")},
            "直播意外中断了":{"path": UPath(type_ == "UILabel", label_ == "直播意外中断了")},
            "恢复直播": {"path": UPath(type_ == "AWEUIButton", label_ == "恢复直播")},
            "关播按钮": {"path": UPath(label_ == "closeLive")},
            "关播按钮_170": {"path": UPath(label_ == "关闭直播")},
            "确定": {"path": UPath(type_ == "AWEUIButton", label_ == "确定")},
            "关播页关闭按钮": {"path": UPath(type_ == "UIButton", label_ == "close")},
            "关播页关闭按钮_170": {"path": UPath(label_ == "退出关播页面", type_ == "UIButton")},
            "更多按钮": {"path": UPath(label_ == "group", type_ == "HTSLiveToobarItemCell")},
            "更多按钮_170": {"path": UPath(label_ == "更多")},

            "礼物": {"path": UPath(label_ == "礼物", id_ == "(礼物)")},
            "第一个礼物": {"path": UPath(type_ == "IESLiveRoomGiftItemCell", index=0)},
            "礼物面板关闭按钮": {"path": UPath(type_ == "UIButton", id_ == "(closeButton)")},
            "礼物面板关闭按钮_170": {"path": UPath(label_ == "IESLiveGiftPanelCloseButtonAccessID")},

            "我知道了": {"path": UPath(type_ == "AWEUIButton", label_ == "我知道了")},
            "我": {"path": UPath(type_ == "AWETabbarGeneralButton", label_ == "我")},
            "首页": {"path": UPath(type_ == "AWETabbarGeneralButton", label_ == "首页")},
            "跳过": {"path": UPath(type_ == "UIButton", label_ == "跳过")},
            "菜单": {"path": UPath(label_ == "菜单", id_ == "(moreFuncButton)")},
            "设置": {"path": UPath(label_ == "设置")},
            "设置页": {"path": UPath(type_ == "UIViewControllerWrapperView") / UPath(type_ == "UITableView", depth=2)},
            "退出登录": {"path": UPath(type_ =="UILabel", id_=="(titleLabel)",label_=="退出登录",visible_ == True)},
            "上滑查看更多视频": {"path": UPath(label_ == "上滑查看更多视频", id_ == "(mainLabel)")},
            "页面": {"path": UPath(type_ == "UIScrollView")},
            "直播": {"path": UPath(label_ == "直播", id_ == "(liveEntranceView)")},
            "退出直播间": {"path": UPath(label_ == "kHTSLiveToolbarItemClose", visible_ == True)},
            "退出": {"path": UPath(label_ == "退出", id_ == "(cancelButton)")},
            "左滑查看更多直播": {"path": UPath(label_ == "左滑查看更多直播", id_ == "(upGuideLabel)")},
            "引导页面": {"path": UPath(type_ == "HTSLiveGuideView")},
            "关注": {"path": UPath(label_ == "关注", id_ == "(followBtn)")},
            "粉丝团入口": {"path": UPath(id_ == "(fansBtn)")},
            "直播间内页面":{"path": UPath(type_ == "IESLiveFeedCollectionView")},
            "主播id": {"path": UPath(type_ == "UILabel", id_ == "(nameLabel)",index=0)},
            "直播头像": {"path": UPath(label_ == "用户头像")},
            "拍照": {"path": UPath(label_ == "拍摄")},
            "确认": {"path": UPath(label_ == "确认", id_ == "(label)", type_ == "UILabel")},
            "更多直播": {"path": UPath(label_ == "更多直播",type_ == "UILabel")},
        }

    def init(self):
        if self["上滑查看更多视频"].wait_for_visible(raise_error = False):
            self.页面.scroll(distance_x=0, distance_y=600)

    def log_in(self):
        try:
            self["我"].click()
        except:
            self.init()
            time.sleep(4)
            self["我"].click()
        #time.sleep(4)
        Loginpanel = LoginWindow(root=self.app)
        num = Loginpanel.login()
        if num == 0:
            self["首页"].click()
        return num

    def log_out(self, num):
        if self["关播页关闭按钮_170"].wait_for_visible(raise_error=False):
            self["关播页关闭按钮_170"].click()
        elif self["关播页关闭按钮"].wait_for_visible(raise_error=False):
            self["关播页关闭按钮"].click()

        time.sleep(5)

        self["我"].click()
        time.sleep(5)
        self["菜单"].click()

        setting = OkPopup(root=self.app)
        time.sleep(5)
        self["设置"].click()
        time.sleep(4)
        self["设置页"].scroll(distance_x=0, distance_y=500)
        time.sleep(5)

        if self["退出登录"].existing:
           self["退出登录"].click()
        #失败重试
        else:
            time.sleep(4)
            self["设置页"].scroll(distance_x=0, distance_y=500)
            time.sleep(2)
            if self["退出登录"].existing:
                self["退出登录"].click()
        time.sleep(5)
        #确定退出登陆
        setting.logout()
        time.sleep(5)
        g = MobileRequest()
        g.release_num(tags=1128, num=num)


    def StartLiving(self):
        self["拍照"].click()
        self.wait_for_visible()
        if self["启用相机访问权限"].wait_for_visible(timeout=5,raise_error=False):
            self["启用相机访问权限"].click()
        time.sleep(25)
        if self["启用麦克风访问权限"].wait_for_visible(timeout=5,raise_error=False):
            self["启用麦克风访问权限"].click()
        time.sleep(2)

        # 当开直播被遮挡，先点击影集，再点开直播
        if self["影集"].wait_for_visible(raise_error=False):
            self["影集"].click()

        if self["开直播"].wait_for_visible(raise_error=False):
            self["开直播"].click()

        time.sleep(3)
        if self["直播意外中断了"].existing:
            self["恢复直播"].click()
            return
        self["开始视频直播"].wait_for_visible(raise_error=False)
        while self["开始视频直播"].existing:
            self["开始视频直播"].click()
            time.sleep(5)
        if self["直播意外中断了"].existing:
            self["恢复直播"].click()


    def StartLivingSuccess(self):
        if self["关播按钮_170"].wait_for_visible(raise_error=False):
            return 0
        elif self["关播按钮"].wait_for_visible(raise_error=False):
            return 0
        else:
            return 1
    def checked_more(self):
        # 多端登陆看直播前先退出登录
        if self["确定"].wait_for_existing(timeout=6, raise_error=False):
            self["确定"].click()
            time.sleep(3)


    def CloseLiving(self):

        if self["关播按钮_170"].wait_for_visible(raise_error=False):
            time.sleep(3) #等待组件稳定
            print("点击了关播")
            self["关播按钮_170"].click()
        else:
            self["关播按钮"].click()

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


    def SendGift(self):

        time.sleep(4)
        if self["更多按钮_170"].wait_for_visible(timeout=10,raise_error=False):
            time.sleep(2)
            self["更多按钮_170"].click()
        else:
            time.sleep(2)
            self["更多按钮"].click()
        if self["礼物"].wait_for_visible(timeout=10, raise_error = False):
            self["礼物"].click()
        else:
            self["更多按钮_170"].click()
            self["礼物"].click()
        self["第一个礼物"].click()
        time.sleep(1)
        self["第一个礼物"].click()
        time.sleep(5)
        self["第一个礼物"].click()
        time.sleep(1)
        self["第一个礼物"].click()
        if self["礼物面板关闭按钮"].wait_for_existing(timeout=3, raise_error=False):
            self["礼物面板关闭按钮"].click()
        elif self["礼物面板关闭按钮_170"].wait_for_existing(timeout=3, raise_error=False):
            self["礼物面板关闭按钮_170"].click()

    def QuitRoom(self):
        self["退出直播间"].click()
        if self["退出"].wait_for_existing(timeout=3, raise_error = False):
            self["退出"].click()
            self["退出"].wait_for_invisible(timeout=3, raise_error=False)
            time.sleep(2)
            if self["左滑查看更多直播"].wait_for_visible(3, raise_error=False):
                self["引导页面"].click()
        time.sleep(2)
        if self["退出直播间"].existing:
            self["退出直播间"].click()
            if self["退出"].wait_for_existing(3, raise_error=False):
                self["退出"].click()
                self["退出"].wait_for_invisible(3, raise_error=False)
                if self["左滑查看更多直播"].wait_for_visible(3, raise_error=False):
                    self["引导页面"].click()
        time.sleep(4)

    def EnterRoom(self):
        try:
            self["直播"].click()
        except:
            time.sleep(5)
            self.init()
            time.sleep(7)
            self["直播"].click()
        try:
            self["直播"].wait_for_invisible()
        except:
            self["直播"].click()
            self["直播"].wait_for_invisible()
        time.sleep(2)
        # 等待页面加载

    def EnterRoomSuccess(self):
        if self["直播头像"].wait_for_visible(20, raise_error = False):
            return 0
        elif self["更多直播"].wait_for_visible(raise_error=False):
            return 0
        else:
            return 1

    def FollowAnchor(self):
        if self["关注"].visible:
            self["关注"].click()
            time.sleep(4)
            if self["粉丝团入口"].visible:
                return 0
        else:
            self.SwipeToNextRoom()
            while self["粉丝团入口"].visible:
                self.SwipeToNextRoom()
            if self["关注"].visible:
                self["关注"].click()
                time.sleep(2)
                if self["粉丝团入口"].visible:
                    return 0
            else:
                return 1

    def SwipeToNextRoom(self):
        self.更多直播.scroll(distance_x=0, distance_y=600)

    def ScrollToNextRoom(self):

        # 检测是否是媒体直播间  如果是媒体直播间就切换
        while not self["主播id"].wait_for_visible(timeout=6, raise_error=False):
            self.SwipeToNextRoom()
        anchor_a = self.GetAnchorid()
        self.SwipeToNextRoom()
        time.sleep(20)
        self.SwipeToNextRoom()
        time.sleep(20)

        while not self["主播id"].wait_for_visible(timeout=6, raise_error=False):
            self.SwipeToNextRoom()
        anchor_b = self.GetAnchorid()
        if anchor_a == anchor_b:
            return 0 #由于168版本更改了组件导致找不到 暂时去掉检测
        else:
            return 0

    def GetAnchorid(self):
        self["主播id"].refresh()
        Anchorid = self["主播id"].elem_info["label"]
        print(Anchorid)
        return Anchorid