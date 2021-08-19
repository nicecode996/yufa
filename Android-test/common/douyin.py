#! usr/bin/env python3
# coding=utf-8

from appium import webdriver

from common import setting

desired_caps = {
    'platformName': 'Android',
    'deviceName': '127.0.0.1:21503',
    'platformVersion': '7.1.2',
    'appPackage': 'com.ss.android.ugc.aweme',
    'appActivity': 'com.ss.android.ugc.aweme.splash.SplashActivity',
    'noReset': True
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# time.sleep(3)
driver.implicitly_wait(25)
# 同意
try:
    driver.find_element_by_id("com.ss.android.ugc.aweme:id/bdb").click()
except:
    driver.find_element_by_id("com.ss.android.ugc.aweme:id/bdb").click()

# 默认上滑动
try:
    setting()
except:
    print("滑动异常")

driver.find_element_by_id("com.ss.android.ugc.aweme:id/gle").click()
