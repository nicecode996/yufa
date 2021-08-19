#! usr/bin/env python3
# coding=utf-8
from appium.webdriver.common.touch_action import TouchAction

from common.douyin import driver


class setting():


    '''
        def getSize(self):
            x = self.driver.get_window_size()['width']
            y = self.driver.get_window_size()['height']
            return (x, y)
    '''
# 向上滑动
def move(self):
    TouchAction(driver).press(x=368, y=965).move_to(x=359, y=312).release().perform()


'''
    def I_know(self):
    driver.find_element_by_id("")
'''
