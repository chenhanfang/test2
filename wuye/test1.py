# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Test1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://manage.test.meidewuye.com/#/login"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_1(self):
        driver = self.driver
        driver.get(self.base_url + "/#/login")
        driver.find_element_by_css_selector("input.el-input__inner").clear()
        driver.find_element_by_css_selector("input.el-input__inner").send_keys("15700087984")
        driver.find_element_by_xpath("//input[@type='password']").clear()
        driver.find_element_by_xpath("//input[@type='password']").send_keys("123456")
        driver.find_element_by_css_selector("div.el-notification__closeBtn.el-icon-close").click()
        driver.find_element_by_css_selector("li.el-menu-item.is-active").click()
        driver.find_element_by_xpath("//div[@id='app']/div[2]/div/ul/li[2]").click()
        driver.find_element_by_xpath("//div[@id='app']/div[2]/div/ul/li[3]").click()
        driver.find_element_by_xpath("//div[@id='app']/div[2]/div/ul/li[4]").click()
        driver.find_element_by_xpath("//div[@id='app']/div[2]/div/ul/li[5]").click()
        driver.find_element_by_css_selector("div.el-submenu__title").click()
        driver.find_element_by_css_selector("div.el-submenu__title").click()
        driver.find_element_by_css_selector("li.el-submenu.is-opened > ul.el-menu > li.el-menu-item").click()
        driver.find_element_by_xpath("//div[@id='app']/div[2]/div/ul/li[6]/ul/li[2]").click()
        driver.find_element_by_xpath("//div[@id='app']/div[2]/div/ul/li[7]/div").click()
        driver.find_element_by_xpath("//div[@id='app']/div[2]/div/ul/li[7]/ul/li").click()
        driver.find_element_by_xpath("//div[@id='app']/div[2]/div/ul/li[7]/ul/li[2]").click()
        driver.find_element_by_xpath("//div[@id='app']/div[2]/div/ul/li[7]/ul/li[3]").click()
        driver.find_element_by_xpath("//div[@id='app']/div[2]/div/ul/li[7]/ul/li[4]").click()
        driver.find_element_by_xpath("//div[@id='app']/div[2]/div/ul/li[8]").click()
        driver.find_element_by_xpath("//div[@id='app']/div[2]/div/ul/li[9]").click()
    
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
