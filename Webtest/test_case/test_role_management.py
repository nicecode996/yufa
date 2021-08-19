__author__ = 'Administrator'
import time
import unittest
import common.driver as Driver
from common.log import logger

class RoleManagement(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = Driver.get_driver()

    # 角色管理-新增角色
    def test_401_create_role(self):
        try:
            self.driver.find_element_by_name("permission").click()
            time.sleep(3)
            self.driver.find_element_by_name("rolemanage").click()
            time.sleep(3)
            self.driver.find_element_by_name("createBtn").click()
            time.sleep(3)
            self.driver.find_element_by_name("name").send_keys('test')
            time.sleep(1)
            self.driver.find_element_by_name("submitBtn").click()
            time.sleep(0.5)
            key_word = self.driver.find_element_by_xpath('//p[contains(text(),"添加成功")]')
            self.assertEqual(key_word.text,"添加成功！")
            time.sleep(2)
            logger.info("新增角色成功")
        except Exception as ex:
            logger.error(ex)
            raise ex
        time.sleep(2)

    # 角色管理-角色详情
    def test_402_role_detail(self):
        try:
            self.driver.find_element_by_name("detailBtn1").click()
            time.sleep(4)
            key_word=self.driver.find_element_by_name("roleManageDetailName")
            self.assertEqual(key_word.text,"test")
            time.sleep(3)
            logger.info("角色详情显示正确")
        except Exception as ex:
            logger.error(ex)
            raise ex
        finally:
            self.driver.find_element_by_class_name("el-dialog__headerbtn").click()
        time.sleep(3)

    # 角色管理-编辑角色名称
    def test_403_edit_role_name(self):
        try:
            self.driver.find_element_by_name("editBtn1").click()
            time.sleep(1)
            self.driver.find_element_by_name("name").clear()
            time.sleep(1)
            self.driver.find_element_by_name("name").send_keys("test1")
            time.sleep(1)
            self.driver.find_element_by_name("submitBtn").click()
            time.sleep(2)
            edit_person_list = self.driver.find_element_by_name("roleManageName1")
            self.assertEqual(edit_person_list.text,"test1")
            logger.info("编辑角色成功")
        except Exception as ex:
            logger.error("编辑角色失败")
            raise ex
        time.sleep(2)

    # 角色管理-删除角色
    def test_404_delete_role(self):
        try:
            self.driver.find_element_by_name("deleteBtn1").click()
            time.sleep(3)
            self.driver.find_element_by_xpath('//span[contains(text(),"确 定")]').click()
            time.sleep(1)
            key_word = self.driver.find_element_by_xpath('//p[text()="删除角色成功"]')
            self.assertEqual(key_word.text, "删除角色成功")
            time.sleep(2)
            logger.info("角色删除成功")
        except Exception as ex:
            logger.error(ex)
            raise ex

    '''
        @classmethod
        def tearDownClass(cls):
            cls.driver.quit()
    '''
