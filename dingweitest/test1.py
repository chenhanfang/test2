#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains#######鼠标事件的类
import time
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

driver=webdriver.Remote(desired_capabilities=DesiredCapabilities.CHROME)
driver.get('http://www.baidu.com/')
time.sleep(1)
driver.find_element_by_xpath('//a[@href="http://www.baidu.com/gaoji/preferences.html" and @class="pf"]').click()###设置
driver.find_element_by_xpath('//a[@class="setpref" and @href="javascript:;"]').click()###搜索设置
time.sleep(1)
m=driver.find_element_by_xpath("//select[@name='NR']")####下来框操作
m.find_element_by_xpath("//option[@value='20']").click()
time.sleep(1)
driver.find_element_by_xpath("//a[@class='prefpanelgo']").click()
time.sleep(1)
date=driver.switch_to.alert.text####返回alert/confirm/prompt中的文字信息
print(date)
driver.switch_to.alert.accept()####accept弹出的带有确定按钮的提示框，来接受确认提示框操作
'''dissmiss 点击取消按钮，如果存在取消按钮；send_keys 输入值，这个
alert\confirm没有对话框就不能用了，不然会报错'''
cookie=driver.get_cookies()#获取cookie
print(cookie)

driver.find_element_by_xpath("//input[@id='kw']").send_keys('selenium')
driver.find_element_by_xpath("//input[@id='su']").click()
time.sleep(2)
js="var q=document.documentElement.scrollTop=1000"###将页面滚动条拖到底部
driver.execute_script(js)
time.sleep(2)
# data=driver.find_element_by_xpath('//p[@id="cp"]').text####获取元素的文本信息
# print(data)
# driver.find_element_by_xpath('//a[@name="tj_mp3"]').click()
print(driver.title)####打印浏览器标题
# driver.set_window_size(480,800)
# driver.back()####后退
# time.sleep(2)
# driver.forward()#####前进
'''
qqq=driver.find_element_by_xpath("///")
ActionChains(driver).context_click(qqq).perform()####鼠标右击事件
ActionChains(driver).double_click(qqq).perform()####鼠标双击事件
ppp=driver.find_element_by_xpath("///")
ActionChains(driver).drag_and_drop(qqq,ppp).perform()####鼠标拖地事件,perform()执行所有存储的行为
switch_to_frame()#####框架（frame)或者窗口(window)的定位
switch_to_window()
'''
