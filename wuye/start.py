# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
binary = FirefoxBinary('D:\\Program Files\Mozilla Firefox\\firefox.exe')

class Start(unittest.TestCase):
    def setUp(self):
        # self.driver = webdriver.Firefox(firefox_binary=binary)
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://manage.test.meidewuye.com/#/login"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_start(self):
        driver = self.driver
        driver.get(self.base_url + "/#/login")
        driver.find_element_by_css_selector("input.el-input__inner").clear()
        driver.find_element_by_css_selector("input.el-input__inner").send_keys("15700087984")
        driver.find_element_by_xpath("//input[@type='password']").clear()
        driver.find_element_by_xpath("//input[@type='password']").send_keys("123456")
        driver.find_element_by_css_selector("button.el-button.el-button--primary").click()
        # driver.find_element_by_css_selector("div.el-notification__closeBtn.el-icon-close").click()
        '''筛选查询'''
        # time.sleep(2)
        # driver.find_element_by_css_selector("input.el-input__inner").clear()
        # driver.find_element_by_css_selector("input.el-input__inner").send_keys(u"1幢5单元210")
        # time.sleep(1)
        # driver.find_element_by_css_selector("button.el-button.el-button--primary").click()
        # time.sleep(1)
        # driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
        # # time.sleep(1)
        # # driver.find_element_by_xpath("(//button[@type='button'])[6]").click()
        # time.sleep(2)



        # driver.find_element_by_css_selector("li.el-select-dropdown__item.hover").click()
        # driver.find_element_by_xpath("//div[@id='app']/div[2]/div/ul/li[6]").click()
        # time.sleep(1)
        # driver.find_element_by_xpath("//div[@id='app']/div[2]/div/ul/li[6]/ul/li[1]").click()

        # time.sleep(1)
        # driver.find_element_by_xpath("(//input[@class='el-checkbox__original'and @type='checkbox'])[11]").click()

        # driver.find_element_by_xpath("//div[@id='app']/div[2]/div/ul/li[6]/ul/li[2]").click()

        # driver.find_element_by_xpath("//div[@id='app']/div[2]/div/ul/li[3]").click()
        '''修改关于我们
       '''
        driver.find_element_by_xpath("//div[@id='app']/div[2]/div/ul/li[9]").click()
        driver.find_element_by_css_selector("textarea.el-textarea__inner").send_keys(Keys.CONTROL,'a')
        driver.find_element_by_css_selector('textarea.el-textarea__inner').send_keys(Keys.BACK_SPACE)
        time.sleep(1)
        driver.find_element_by_css_selector('textarea.el-textarea__inner').send_keys('美德物业叭啦叭叭啦叭')
        driver.find_element_by_css_selector('button.el-button.el-button--primary').click()
        self.assertEqual()

       #
       #  '''添加业主信息
       # '''
       #  driver.find_element_by_xpath("//div[@id='app']/div[2]/div/ul/li[4]").click()
       #  time.sleep(2)
        # driver.find_element_by_xpath("//button[@type='button']").click()
















        time.sleep(10)
    
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
    
    # def tearDown(self):
    #     self.driver.quit()
    #     self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
