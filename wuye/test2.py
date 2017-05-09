# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Test2(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://manage.test.meidewuye.com/#/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_2(self):
        driver = self.driver
        driver.get(self.base_url + "/#/about")
        driver.find_element_by_css_selector("textarea.el-textarea__inner").clear()
        driver.find_element_by_css_selector("textarea.el-textarea__inner").send_keys(u"2.订单未分配操作：新增的订单管理者查看的同时能对新订单进行指派，指派员工XXX后面的（员工号，电话号）对应数据库里面的字段，统一在一个请求发出；点击发送的同时，弹出是否确认操作的对话框！按着指示来操作；在指派完毕后订单进程的状态变更为“订单处理中”。操作状态更换为“完成”。\n3.订单处理中操作：订单在分配完毕之后，管理者的任务基本就是ok了，但操作里面防止前期员工适应程度的问题，所以加入一个流程闭环操作“完成”，在三天内员工如果不予操作的，或者员工口头通知于管理者等情况；管理者给予流程闭环完成操作状态进入到订单已完成状态。无操作功能。\n详细订单查看：每一条订单可以显示更多的详细信息，根据状态的不同，我划分为四种订单详情：第一种未分配状态，订单下拉显示详细信息（详情请看原型），这种状态的订单是可以操作，通过指派员工，进行订单的处理，（如：选定员工01，对应的信息显示，）下方的发送按键指派之后就可以把这条工单信息指派给对应的员工，订单结束之后显示“操作已完成！”，第二种状态为处理中订单，点击下拉之后，最下方的完成按钮为操作")
        driver.find_element_by_css_selector("button.el-button.el-button--primary").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
