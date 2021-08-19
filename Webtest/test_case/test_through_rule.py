# -*- coding: utf-8 -*-
# author:caiying

from selenium import webdriver
import time
import os
import unittest
import common.driver as Driver
from common.readconfig import ReadConfig
from common.log import logger


class ThrougnRule(unittest.TestCase):
    # 获取文件夹路径
    proDir = os.getcwd()
    # 找到配置文件
    config = ReadConfig()

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver.get_driver()

    # 新建规则-判断规则是否创建成功
    def test_601_new_rule(self):
        try:
            self.driver.find_element_by_name('rules').click()
            time.sleep( 2 )
            self.driver.find_element_by_xpath( '/html/body/div[1]/div/div/div/div[1]/div/div/ul/li[6]/ul/a[1]/li' ).click()
            time.sleep( 2 )
            self.driver.find_element_by_name( 'createBtn' ).click()
            time.sleep( 2 )
            self.driver.find_element_by_name( 'name' ).send_keys( '测试规则' )
            time.sleep( 1 )
            self.driver.find_element_by_name( 'action' ).click()
            time.sleep( 1 )
            self.driver.find_element_by_name( 'passmode-option-1' ).click()
            time.sleep( 1 )
            self.driver.find_element_by_name( 'newTimeRuleBtn' ).click()
            time.sleep( 2 )
            self.driver.find_element_by_name( 'title' ).send_keys( '111' )
            self.driver.find_element_by_xpath( '//*[@id="addTimeRuleForm"]/div[2]/div/div[1]/label[1]' ).click()
            self.driver.find_element_by_xpath( '//*[@id="addTimeRuleForm"]/div[3]/div/div/label[1]/span[1]/span' ).click()
            self.driver.find_element_by_name( 't' ).click()
            time.sleep( 1 )
            self.driver.find_element_by_css_selector('body > div.el-time-range-picker.el-picker-panel.el-popper > div.el-time-panel__footer > button.el-time-panel__btn.confirm' ).click()
            time.sleep( 1 )
            self.driver.find_element_by_xpath( '//*[@id="addTimeRuleForm"]/div[5]/div/div/div/input' ).click()
            time.sleep( 1 )
            self.driver.find_element_by_name( 'allow-option-1' ).click()
            time.sleep( 1 )
            self.driver.find_element_by_xpath( '//*[@id="addTimeRuleDialog"]/div/div[3]/div/button[2]' ).click()
            time.sleep( 1 )
            self.driver.find_element_by_xpath( '//*[@id="addThroughRuleForm"]/div[5]/div/div/div[1]/input' ).click()
            time.sleep( 1 )
            self.driver.find_element_by_name( 'type-option-1' ).click()
            time.sleep( 1 )
            self.driver.find_element_by_xpath('//*[@id="addThroughRuleForm"]/div[5]/div/div[2]/div[1]/div/div[1]/div/div[2]/div[1]/div/div/span[1]' ).click()
            time.sleep( 1 )
            self.driver.find_element_by_xpath('//*[@id="addThroughRuleForm"]/div[5]/div/div[2]/div[1]/div/div[1]/div/div[2]/div[1]/div/div[4]/label/span/span' ).click()
            time.sleep( 1 )
            self.driver.find_element_by_xpath( '//*[@id="addThroughRuleForm"]/div[5]/div/div[2]/div[3]/button[2]' ).click()
            time.sleep( 1 )
            self.driver.find_element_by_name( 'submitBtn' ).click()
            time.sleep(2)
            self.assertEqual( self.driver.find_element_by_xpath('//*[@id="ruleManage"]/div/div[2]/div/div[3]/table/tbody/tr[1]/td[1]/div').text, u'测试规则')
            logger.info("添加成功！")
        except Exception as ex:
            logger.error('添加失败')
            raise ex


    def test_602_edit_rule(self):
        try:
            self.driver.find_element_by_name('editBtn0').click()
            time.sleep(2)
            self.driver.find_element_by_name('name').send_keys('编辑')
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="addThroughRuleForm"]/div[5]/div/div[2]/div[1]/div/div/div/div[1]/input').send_keys('caiying1')
            time.sleep(3)
            self.driver.find_element_by_xpath('//*[@id="addThroughRuleForm"]/div[5]/div/div[2]/div[1]/div/div/div/div[3]/div/label/span[1]').click()
            time.sleep(2)
            self.driver.find_element_by_xpath('//*[@id="addThroughRuleForm"]/div[5]/div/div[2]/div[3]/button[2]').click()
            time.sleep(2)
            self.driver.find_element_by_name('submitBtn').click()
            time.sleep(2)
            self.assertEqual(self.driver.find_element_by_xpath('//*[@id="ruleManage"]/div/div[2]/div/div[3]/table/tbody/tr[1]/td[1]/div').text,'测试规则编辑')
            logger.info("编辑成功")
        except Exception as ex:
            logger.error('编辑失败')
            raise ex

    def test_603_detail_rule(self):
        try:
            self.driver.find_element_by_name('detailBtn0').click()
            time.sleep(2)
            self.assertEqual(self.driver.find_element_by_xpath('//label[text()="规则名称"]/following-sibling::div//span').text,'测试规则编辑')
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="addThroughRule"]/div/div[1]/button/i').click()
            time.sleep(3)
            logger.info("详情判定成功")
        except Exception as ex:
            logger.error('详情判定失败')
            raise ex



    def test_604_rule_down(self):
        try:
            '''
            self.driver.find_element_by_name( 'rules' ).click()
            time.sleep( 2 )
            '''
            self.driver.find_element_by_name( "ruleapply" ).click()
            time.sleep( 2 )
            self.driver.find_element_by_name('ruleApplyBtn0').click()
            time.sleep( 1 )
            # 选择设备
            self.driver.find_element_by_xpath(
                '//*[@id="applyRuleDialog"]/div/div[2]/form/div[1]/div/div/div[1]/div/div/div[2]/div[4]/div/label/span' ).click()
            self.driver.find_element_by_xpath(
                '//*[@id="applyRuleDialog"]/div/div[2]/form/div[1]/div/div/div[1]/div/div/div[2]/div[3]/div/label/span' ).click()
            time.sleep( 1 )
            #  > 箭头
            self.driver.find_element_by_xpath(
                '//*[@id="applyRuleDialog"]/div/div[2]/form/div[1]/div/div/div[3]/button[2]' ).click()
            time.sleep( 1 )
            self.driver.find_element_by_name( 'submitBtn' ).click()
            time.sleep( 1 )
            # 弹框确认按钮
            self.driver.find_element_by_xpath( '/html/body/div[2]/div/div[3]/button' ).click()
            time.sleep(2)
            self.assertEqual(self.driver.find_element_by_xpath('//*[@id="resultTable"]/div[3]/table/tbody/tr/td[2]/div/a').text,'2')
            time.sleep(1)
            logger.info("下发成功")
        except Exception as ex:
            logger.error('下发失败')
            raise ex

    def test_605_rule_sn(self):
        try:
            self.driver.find_element_by_name('ruleApplyBtn0').click()
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="applyRuleDialog"]/div/div[2]/form/div[1]/div/div/div[2]/div/div/div[1]/input').send_keys('C000100010002')
            time.sleep(2)
            self.assertEqual(self.driver.find_element_by_xpath('//*[@id="applyRuleDialog"]/div/div[2]/form/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/span[2]').text,'测试设备2 C000100010002')
            time.sleep(2)
            self.driver.find_element_by_xpath('//*[@id="applyRuleDialog"]/div/div[2]/form/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/label/span/span').click()
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="applyRuleDialog"]/div/div[2]/form/div[1]/div/div/div[3]/button[1]').click()
            time.sleep(1)
            self.driver.find_element_by_name('submitBtn').click()
            time.sleep(1)
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button').click()
            time.sleep(2)
            logger.info("查询成功，并点击确定")
        except Exception as ex:
            logger.error('查询失败，并点击确定')
            raise ex

    def test_606_rule_delete(self):
        try:
            self.driver.find_element_by_name('rulemanage').click()
            time.sleep(1)
            self.driver.find_element_by_name('delBtn0').click()
            time.sleep(2)
            self.driver.find_element_by_xpath('/html/body/div[2]/div/div[3]/button[2]').click()
            time.sleep(2)
            self.assertNotEqual(self.driver.find_element_by_xpath('//*[@id="ruleManage"]/div/div[2]/div/div[3]/table/tbody/tr[1]/td[1]/div').text,'测试规则编辑')
            logger.info("删除成功")
        except Exception as ex:
            logger.error('删除失败')
            raise ex