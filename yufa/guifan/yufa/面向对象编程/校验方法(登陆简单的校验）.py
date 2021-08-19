# coding=utf-8
# !/usr/bin/env python3

class MIS(object):
    def _verify_usr(self, p_user):
        if len(p_user)>=8 and len(p_user)<=20:
            return True
        else:
            return False
    def _verify_pwd(self, p_pwd):
         if len(p_pwd)>=5 and len(p_pwd)<10:
             return True
         else:
             return False

    def login(self, p_usr, p_pwd):

        if self._verify_usr(p_usr) and self._verify_pwd(p_pwd):
            print("登陆成功")
        else:
            print("登陆失败")

m=MIS()
m.login('11','12345')
