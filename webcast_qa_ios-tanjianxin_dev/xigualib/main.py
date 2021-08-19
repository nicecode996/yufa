# -*- coding: utf8 -*-
"""main page
"""
#2020/07/02 auto generated by shoots

from uibase.controls import Window, TextEdit
from uibase.upath import UPath, text_, type_, label_, id_, visible_, value_
import time
from webcastlib.mobile_account import MobileRequest
from shoots import logger
from byted_cv.ocr_helper import find_pic, click_pic
from xigualib.byte_expend import getPath
from settings import PROJECT_ROOT
import os

resoureces_path = PROJECT_ROOT + "/resources/images/"

class MainWindow(Window):
    """main window
    """
    window_spec = {"path": UPath(index=0, depth=1)}
    
    def get_locators(self):
        return {
            #登录相关
            "我的": {"path": UPath(label_ == "我的", type_ == "UITabBarButton")},
            "登录/注册": {"path": UPath(label_ == "登录/注册", type_ == "UILabel", index=0)},
            "其他登录方式": {"path": UPath(label_ == "其他登录方式", type_ == "UIButton")},
            "登录其他账号": {"path": UPath(label_ == "登录其它账号", type_ == "SSThemedButton")},
            "手机号": {"type": TextEdit,
                    "path": UPath(type_ == "SSThemedTextField", index=0)},
            "验证码": {"type": TextEdit,
                    "path": UPath(type_ == "SSThemedTextField", index=1)},
            #"同意": {"path": UPath(label_ == "register agree unchoose")},
            "同意": {"path": UPath(type_ == "UIView",visible_==True)/UPath(type_ == "SSThemedButton",visible_==True,depth=1,index=1)},
            "进入西瓜视频": {"path": UPath(label_ == "进入西瓜视频", type_ == "SSThemedButton")},
            #退登相关
            "页面": {"path": UPath(type_ == "UICollectionView")},
            "设置": {"path": UPath(label_ == "设置", index=0)},
            #"设置1": {"path": UPath(label_ == "设置", type_ == "UILabel",index=1)},
            "帐号管理": {"path": UPath(label_ == "帐号管理", type_ == "SSThemedLabel")},
            "退出登录":  {"path": UPath(label_ == "退出登录", type_ == "SSThemedLabel",index=0)},
            "确定退出": {"path": UPath(label_ == "确定退出", type_ == "_UIAlertControllerActionView")},

            #开播相关
            "开直播": {"path": UPath(label_ == "开直播", type_ == "UILabel")},
            "选择分类": {"path": UPath(label_ == "选择分类", type_ == "UILabel")},
            "选择直播内容": {"path": UPath(label_ == "选择直播内容", type_ == "UILabel")},
            "户外打野": {"path": UPath(label_ == "户外打野", type_ == "UILabel", index=0)},
            "直播标题": {"path": UPath(label_ == "直播标题", type_ == "IESLiveGuideTitleTextField")},
            "开始视频直播": {"path": UPath(label_ == "开始视频直播", type_ == "UIButtonLabel")},
            "直播意外中断了": {"path": UPath(label_ == "直播意外中断了", type_ == "UILabel")},
            "取消": {"path": UPath(label_ == "取消", type_ == "UILabel")},
            #关播相关
            "关播按钮": {"path": UPath(label_ == "closeLive", type_ == "HTSLiveToobarItemCell")},
            "关播按钮_170": {"path": UPath(label_ == "关闭直播")},
            "确定": {"path": UPath(label_ == "确定", type_ == "_UIAlertControllerActionView")},
            "关播页关闭按钮": {"path": UPath(label_ == "close", type_ == "UIButton")},
            "关播页关闭按钮_170": {"path": UPath(label_ == "退出关播页面", type_ == "UIButton")},

            #送礼相关
            "更多按钮": {"path": UPath(label_ == "group", type_ == "HTSLiveToobarItemCell")},
            "更多按钮_170": {"path": UPath(label_ == "更多")},
            "礼物": {"path": UPath(label_ == "礼物", type_ == "UILabel")},
            "礼物a": {"path": UPath(type_ == "IESLiveRoomGiftItemCell", index=0)},
            "礼物面板关闭按钮": {"path": UPath(label_=="IESLiveGiftPanelCloseButtonAccessID")},
            "礼物面板关闭按钮_170": {"path": UPath(type_=="IESLiveGiftPanelCloseCell")},

            #进房相关
            "直播": {"path": UPath(label_ == "直播", type_ == "UITabBarButton")},
            "直播间": {"path": UPath(type_ == "TTLSquareCollectionViewCell_Dynamic_Subclass_TTLSquareElementFeedLiveView", index=0)},
            "关注": {"path": UPath(label_ == "关注", type_ == "UIButton")},
            #退房相关
             "退出直播间": {"path": UPath(label_ == "kHTSLiveToolbarItemClose", visible_ == True)},
            "为你推荐更多主播": {"path": UPath(label_ == "为你推荐更多主播", type_ == "UILabel")},
            "退出": {"path": UPath(label_ == "退出", type_ == "UIButton")},
            "主播id": {"path": UPath(id_ == "anchorName", visible_ == True, index=0)},
            #"主播id": {"path": UPath(type_ == "LiveUserProfileView")/UPath(type_ == "UILabel",visible_==True,depth=2,index=1)},
            "主播头像": {"path": UPath(type_ == "HTSLiveAvatarImageView", id_ == "用户头像")},
            "个人主页": {"path": UPath(type_ == "UILabel", label_=="个人主页")},
            "更多直播": {"path": UPath(type_ == "UILabel", label_=="更多直播")},
        }

    def log_in(self,device):
        self["我的"].click()
        time.sleep(5)
        if not self["登录/注册"].existing:
            logger.warning("已登录")
            #退出登录，避免已登录的账号未实名导致无法进行直播
            self.log_out(0,device)
            logger.warning("已退出登陆")
            # num = 0
            # return num

        g = MobileRequest()
        num = g.get_num(tags=32)
        #临时更改
        self.username = "12341716442"
        self.usercode = "0819"
        logger.info(num)
        time.sleep(8)
        time.sleep(8)
        if self["登录/注册"].wait_for_visible(raise_error=False):
            self["登录/注册"].click()

        if self["其他登录方式"].existing:
            self["其他登录方式"].click()

        if self["登录其他账号"].wait_for_visible(timeout=10,raise_error=False):
            self["登录其他账号"].click()

        time.sleep(5)

        self["手机号"].input(self.username)
        time.sleep(5)
        self["验证码"].input(self.usercode)
        time.sleep(5)
        logger.info(self.username)

        # 判断是否是第一次登陆
        if self["同意"].wait_for_visible(timeout=10,raise_error=False):
            self["同意"].click()

        time.sleep(5)

        if self["进入西瓜视频"].wait_for_visible(timeout=5, raise_error=False):
            logger.warning("点击了进入西瓜视频")
            self["进入西瓜视频"].click()

        if self["个人主页"].wait_for_visible(timeout=5,raise_error=False):
            logger.warning("登录页面找到了个人主页")
            return 0
        #app没有自动点击登录，手动点击登陆
        time.sleep(7)
        if self["进入西瓜视频"].wait_for_visible(timeout=5,raise_error=False):
            logger.warning("第二次点击了进入西瓜视频")
            self["进入西瓜视频"].click()

        time.sleep(5)
        return  0

    def log_out(self, num, device):
        if self["关播页关闭按钮"].existing:
            self["关播页关闭按钮"].click()
        self["我的"].click()
        self["个人主页"].wait_for_visible(timeout=5, raise_error=False)
        self["个人主页"].scroll(distance_x=0, distance_y=600)
        time.sleep(6)
        self["设置"].scroll(distance_x=0, distance_y=600)
        time.sleep(6)

        self["设置"].highlight()
        time.sleep(5)
        #采用byte-cv方式进行点击操作 点击设置按钮
        # if find_pic(driver=device, target_path=os.path.join(resoureces_path, 'setting.png')):
        #     pos = getPath(driver=device, target_path=os.path.join(resoureces_path, 'setting.png'))
        #     if pos!=False:
        #         print(pos[0])
        #         print(pos[1])
        #         self.app.click(pos[0],pos[1])
        #         print("点击无效")
        #     else:
        #         print(pos)
        # # 失败重试
        # else:
        #     time.sleep(5)
        #     if find_pic(driver=device, target_path=os.path.join(resoureces_path, 'setting.png')):
        #         pos = getPath(driver=device, target_path=os.path.join(resoureces_path, 'setting.png'))
        #         self.app.click(pos[0], pos[1])
        #第一次点击
        if self["设置"].wait_for_visible(timeout=20, raise_error=False):
            self["设置"].click()
            time.sleep(5)
            #失败重试
            if self["设置"].existing:
                self["设置"].click()
                time.sleep(3)

        print("没有点击操作了")
        #self["设置1"].click()
        self["帐号管理"].wait_for_visible(timeout=5, raise_error=False)
        if not self["帐号管理"].wait_for_visible(timeout=5, raise_error=False):
            self["设置"].click()
            print("执行了第二次点击")
        self["帐号管理"].click()
        self["退出登录"].wait_for_visible(timeout=5, raise_error=False)
        self["退出登录"].click()
        time.sleep(1)
        self["确定退出"].click()
        g = MobileRequest()
        g.release_num(tags=32, num=num)

    def EnterRoom(self):
        self["直播"].click()
        self["直播间"].wait_for_visible(timeout=60, raise_error=False)
        self["直播间"].click()

        if self["退出直播间"].wait_for_visible(timeout=60, raise_error=False):
            return 0
        else:
            if self["退出直播间"].wait_for_visible(timeout=60, raise_error=False):
                self["直播间"].click()
            self["退出直播间"].wait_for_visible(timeout=60)
            return 0

    def FollowAnchor(self):
        time.sleep(3)
        if self["关注"].wait_for_visible(timeout=5,raise_error=False):
            self["关注"].click()
            time.sleep(4)
            if not self["关注"].visible:
                return 0
        else:
            while not self["关注"].wait_for_visible(timeout=4,raise_error=False):
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

    def ScrollToNextRoom(self):
        # 检测是否是媒体直播间
        while not self["主播id"].wait_for_visible(timeout=6, raise_error=False):
            print("为找到主播ID")
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
        print(anchor_a)
        print(anchor_b)
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
        self["退出直播间"].refresh()
        self["退出直播间"].click()
        self["退出"].wait_for_visible(raise_error=False)
        if self["退出"].existing:
            self["退出"].click()
        time.sleep(4)
        if self["退出直播间"].existing:
            self["退出直播间"].click()
            if self["退出"].existing:
                self["退出"].click()
        time.sleep(2)

    def QuitRoomSuccess(self):

        if self["直播"].wait_for_visible(30, raise_error = False):
            return 0
        else:
            return 1

    def StartLiving(self):
        self["我的"].click()
        time.sleep(5)
        self["开直播"].click()
        time.sleep(5)
        if self["开直播"].existing:
            time.sleep(2)
            self["开直播"].click()
       #判断上次直播是否已经结束
        if self["直播意外中断了"].wait_for_visible(10, raise_error = False):
            self["取消"].click()
            time.sleep(2)
        self["开始视频直播"].wait_for_visible(20, raise_error = False)
        if self["选择分类"].existing:
            self["选择分类"].click()
            time.sleep(2)
            self["户外打野"].click()
            time.sleep(2)
        #1.6.5版本更新
        elif self["选择直播内容"].existing:
            self["选择直播内容"].click()
            time.sleep(2)
            self["户外打野"].click()
            time.sleep(2)

        self["直播标题"].text = "自动化测试测试"
        while self["开始视频直播"].existing:
            self["开始视频直播"].click()
            time.sleep(5)

    def StartLivingSuccess(self):
        if self["关播按钮"].wait_for_visible(raise_error = False):
            return 0
        elif self["关播按钮_170"].wait_for_visible(raise_error = False):
            return 0
        else:
            return 1

    def SendGift(self):
        time.sleep(4)
        if self["更多按钮_170"].wait_for_visible(timeout=20,raise_error = False):
            time.sleep(2)
            self["更多按钮_170"].click()
        else:
            time.sleep(2)
            self["更多按钮"].click()

        while not self["礼物"].wait_for_visible(timeout=20,raise_error = False):
            self["更多按钮_170"].click()
            time.sleep(1)
        else:
            self["礼物"].click()
        time.sleep(3) # 等待礼物资源加载
        self["礼物a"].click()
        self["礼物a"].click()
        time.sleep(3)

        if self["礼物面板关闭按钮_170"].wait_for_visible(timeout=5,raise_error=False):
            self["礼物面板关闭按钮_170"].click()
        elif self["礼物面板关闭按钮"].wait_for_visible(timeout=5,raise_error=False):
            self["礼物面板关闭按钮"].click()

    def checked_more(self):
        # 多端登陆看直播前先退出登录

        if self["确定"].wait_for_existing(timeout=6, raise_error=False):
            self["确定"].click()
            time.sleep(3)

    def CloseLiving(self):

        time.sleep(5)#等待ui稳定
        if self["关播按钮_170"].wait_for_visible(raise_error=False):
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

