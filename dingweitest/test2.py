#coding=utf-8
from selenium import webdriver
import time
driver=webdriver.Chrome()
driver.get('http://www.youdao.com')
driver.add_cookie({'name':'key-aaaaaa','value':'value-bbbb'})#####添加cookie
for cookie in driver.get_cookies():####获取cookies
    print('%s->%s'%(cookie['name'],cookie['value']))
driver.delete_cookie('CookieName')
driver.delete_all_cookies()
time.sleep(1)