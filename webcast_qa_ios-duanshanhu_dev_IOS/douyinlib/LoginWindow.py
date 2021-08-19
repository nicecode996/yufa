# -*- coding: utf8 -*-
"""login page
"""

from uibase.controls import Window, ControlList, Control, TextEdit
from uibase.upath import UPath, text_, type_, label_, id_
import time
from webcastlib.mobile_account import MobileRequest
from shoots import logger

class LoginWindow(Window):
    """login window
    """
    window_spec = {"path": UPath(type_ == "AWELoginWindow")}

    def get_locators(self):
        return {
            "一键登录": {"path": UPath(type_ == "DYLoginNextActionButton", label_ == "一键登录")},
            "以其他帐号 登录": {"path": UPath(id_ == "(titleView)", label_ == "以其他帐号 登录")},
            "手机号":{"type": TextEdit, "path": UPath(type_ == "DYPhoneNumberInputView", id_ == "(phoneNumberInputView)")},
            "获取短信验证码":{"path": UPath(label_ == "loginButton", id_ == "(loginButton)")},
            "网络请求失败，请重试":{"path": UPath(label_ == "网络请求失败，请重试", id_ == "(errorTipLabel)")},
            "验证码":{"type": TextEdit, "path": UPath(type_ == "DYVerificationCodeInputView", id_ == "(codeInputView)")},
            "同意":{"path": UPath(label_ == "selectButton", id_ == "(selectButton)")},
            "登录": {"path": UPath(label_ == "登录", id_ == "(loginButton)")},
            "跳过": {"path": UPath(type_ == "UIButton", label_ == "跳过")},

        }

    def login(self):
        if self["以其他帐号 登录"].wait_for_visible(5, raise_error=False):
            self["以其他帐号 登录"].click()
        # self["手机号"].click()
        # self["手机号"].send_keys(self.username)

        if not self["手机号"].existing:
            logger.info("已登录")
            return 0

        g = MobileRequest()
        num = g.get_num(tags=1128)
        self.username = num
        self.usercode = "0819"
        logger.info(num)

        self["手机号"].input(self.username)
        time.sleep(2)
        self["获取短信验证码"].click()
        time.sleep(2)
        if self["验证码"].visible:
            self["验证码"].input(self.usercode)
        else:
            if self["获取短信验证码"].wait_for_visible():
                self["获取短信验证码"].click()
            time.sleep(2)
            self["验证码"].input(self.usercode)

        if self["同意"].visible:
            self["同意"].click()
        time.sleep(5)
        while self["登录"].existing:
            self["登录"].click()
            time.sleep(5)

        if self["跳过"].wait_for_visible(30, raise_error=False):
            self["跳过"].click()
        time.sleep(3)
        return num
