#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest,time,re

class Baidu(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.base_url='http://www.baidu.com'
        self.verificationErrors=[]
        self.accept_next_alter = True

    def test_baidu_search(self):
        driver=self.driver
        driver.get(self.base_url+"/")
        try:
            driver.find_element_by_id("kwdd").send_keys('selenium')
        except:
            driver.get_screenshot_as_file("D:\\kw.png")
        driver.find_element_by_id("su").click()
        time.sleep(2)
        driver.close()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)
        print(self.verificationErrors)

if __name__ == '__main__':
    unittest.main()

