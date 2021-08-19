#! usr/bin/env python3
# coding=utf-8


from appium import webdriver

desired_caps = {
    'platformName': 'Android',
    'deviceName': '127.0.0.1:21503',
    'platformVersion': '7.1.2',
    'appPackage': 'com.taobao.taobao',
    'appActivity': 'com.taobao.tao.welcome.Welcome',
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


# driver.find_element.by.id("com.ss.android.ugc.aweme:id/kef")