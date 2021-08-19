# -*- coding: utf-8 -*-
#author:jiayanzi

import time
from selenium import webdriver
from common.readconfig import ReadConfig
from common.analysexml import AnalyseXml


def auth(self):

    http_config=ReadConfig()
    # 加启动配置
    option = webdriver.ChromeOptions()
    option.add_argument('disable-infobars')

    driver=webdriver.Chrome(chrome_options=option)
    driver.maximize_window()
    loginurl=http_config.get_http('url')
    driver.get(loginurl)

    driver.find_element_by_name("uname").send_keys(http_config.get_http('username'))
    driver.find_element_by_name("pass").send_keys(http_config.get_http('password'))
    time.sleep(1)
    driver.find_element_by_xpath(AnalyseXml("Home_login_button")).click()
    time.sleep(2)
    return driver

