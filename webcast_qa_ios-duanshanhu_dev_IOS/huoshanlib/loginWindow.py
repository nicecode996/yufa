from uibase.controls import Window, ControlList, Control, TextEdit
from uibase.upath import UPath, text_, type_, label_, id_
import time
from webcastlib.mobile_account import MobileRequest
from shoots import logger

class LoginWindow(Window):
    """login window
    """
    window_spec = {"path": UPath(type_ == "HTSLoginCNavigationController")}

    def get_locators(self):
        return {
            "手机号": {"type": TextEdit,
                    "path": UPath(type_ == "UITextField", label_ == "请输入手机号")},
            # "下一步": {"path": UPath(type_ == "UIButton", id_=="(nextButton)",label_ == "下一步")},
            "下一步": {"path": UPath(type_ == "UIButton", label_ == "下一步")},
            "协议勾选": {"path": UPath(id_ == "(approveButton)", label_ == "协议勾选")},
            "验证码": {"type": TextEdit,
                    "path": UPath(type_ == "UITextField", label_ == "请输入验证码")},
            "登录": {"path": UPath(type_ == "UIButton", label_ == "登录")},
        }

    def login(self):

        g = MobileRequest()
        num = g.get_num(tags=1112)
        self.username = num
        self.usercode = "0819"
        logger.info(num)
        time.sleep(5)

        self["手机号"].wait_for_visible()
        self["手机号"].input(self.username)
        if self["协议勾选"].wait_for_visible(raise_error=False):
            self["协议勾选"].click()
        self["下一步"].wait_for_visible()
        self["下一步"].click()
        time.sleep(3)
        self["验证码"].input(self.usercode)

        while self["登录"].wait_for_existing(timeout=10, raise_error=False):
            self["登录"].click()
            time.sleep(5)