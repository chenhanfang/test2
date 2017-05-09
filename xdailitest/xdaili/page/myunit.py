from selenium import webdriver
import unittest
import os
from xdailitest.xdaili.page.driver import browser

class mytest(unittest.TestCase ):
    def setUp(self):
        self.driver=browser()
        self.driver.implicitly_wait(20)
        self.driver.set_window_size(1400,1400)


    def tearDown(self):
        print('pass')