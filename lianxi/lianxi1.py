#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver=webdriver.Remote(command_executor='http://www.baidu.com/wd/hun',
                        desired_capabilities=DesiredCapabilities.CHROME)
driver1=webdriver.Remote (command_executor='http://www.baidu.com',
                          desired_capabilities={'browserName':'htmlunit',
                                                'version':2,
                                                'javascriptEnabled':True})