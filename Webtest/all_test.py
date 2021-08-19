# -*- coding: utf-8 -*-
#author:jiayanzi

import unittest
import os

import common.login as login
import common.driver as Driver
from test_case.test_home_page import HomePage
from test_case.test_person_manager import PersonManager
from test_case.test_device_manager import DeviceManager
from test_case.test_device_grouping import DeviceGroup
from test_case.test_device_administrator import Administrator
from test_case.test_configuration_management import ConfigManager
from test_case.test_command_sent_down_record import CommandRecord
from test_case.test_authority_allocation import AuthorityAllocation
from test_case.test_passage_records import PassageRecord
from test_case.test_through_rule import ThrougnRule
from test_case.test_wechat_authorization import Wechatapps
from test_case.test_system import System
from test_case.test_Profile import Profile
from test_case.test_English import English_tab
from HTMLTestRunner import HTMLTestRunner
from common.readconfig import ReadConfig



#获取文件夹路径
proDir = os.getcwd()
#定义读取配置文件的一个对象
config=ReadConfig()

#创建一个新的chrome session
driver=login.auth(config)
Driver.set_driver(driver)

#取测试结果路径
result_dir=os.path.join(proDir,"test_result")

#加载测试类及方法
HomePage_tests=unittest.TestLoader().loadTestsFromTestCase(HomePage)
PersonManager_tests=unittest.TestLoader().loadTestsFromTestCase(PersonManager)
DeviceManager_tests=unittest.TestLoader().loadTestsFromTestCase(DeviceManager)
DeviceGroup_tests=unittest.TestLoader().loadTestsFromTestCase(DeviceGroup)
Administrator_tests=unittest.TestLoader().loadTestsFromTestCase(Administrator)
ConfigManager_tests=unittest.TestLoader().loadTestsFromTestCase(ConfigManager)
CommandRecord_tests=unittest.TestLoader().loadTestsFromTestCase(CommandRecord)
AuthorityAllocation_test=unittest.TestLoader().loadTestsFromTestCase(AuthorityAllocation)
PassageRecord_tests=unittest.TestLoader().loadTestsFromTestCase(PassageRecord)
ThrougnRule_tests=unittest.TestLoader().loadTestsFromTestCase(ThrougnRule)
Wechatapps_tests=unittest.TestLoader().loadTestsFromTestCase(Wechatapps)
System_tests=unittest.TestLoader().loadTestsFromTestCase(System)
Profile_tests=unittest.TestLoader().loadTestsFromTestCase(Profile)
English_tab_tests=unittest.TestLoader().loadTestsFromTestCase(English_tab)


#smoke测试需要加的testcase都写在此
smoke_tests=unittest.TestSuite([HomePage_tests,PersonManager_tests,DeviceManager_tests,DeviceGroup_tests,\
                                Administrator_tests,ConfigManager_tests,CommandRecord_tests,AuthorityAllocation_test,\
                                PassageRecord_tests,ThrougnRule_tests,Wechatapps_tests,System_tests,Profile_tests, \
                                English_tab_tests])

#把smoke测试结果写入文件中
outfile=open(result_dir+"\SmokeTestReport.html","wb")
runner = HTMLTestRunner(stream=outfile,
                        title='Web Test Report',
                        verbosity=2,
                        description='Smoke Tests'
                         )
runner.run(smoke_tests)
