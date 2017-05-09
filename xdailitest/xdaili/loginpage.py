from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
from os import path
from xdailitest.xdaili.page.base import page
from time import sleep
import os

#登录
class login(page):
    url='/'
    def user_login(self,username='username',password='password',code='code',ip='ip'):
        self.open()
        self.driver.find_element_by_class_name('login').click()
        sleep(2)

        js1 = "var sum=document.getElementById('login-phone'); sum.value='" + username + "';"
        self.driver.execute_script(js1)

        js2 = "var sum=document.getElementById('login-pwd'); sum.value='" + password + "';"
        self.driver.execute_script(js2)
        sleep(1)

        self.driver.find_element_by_xpath("//input[@name='code'and @class='form-control']").send_keys(code)
        self.driver.find_element_by_xpath("//button[@class='btn btn-login btn-block']").click()
        sleep(3)
#        file_path = 'file:///' + os.path.abspath('checkbox.html')
#        self.driver.get(file_path)
#        self.driver.find_elements_by_xpath("//input[@class='rem'and @type='checkbox']").click()
#         self.driver.find_element_by_xpath('//html/body/div[1]/div[1]/div[2]/div[8]/span').click()#api提取页面
#         sleep(1)
#         self.driver.find_element_by_xpath(".//*1[@id='ul-header']/li[1]/a").click()
#         sleep(1)
        self.driver.find_element_by_xpath('html/body/div[1]/div[1]/div[2]/div[6]/a').click()
        self.driver.find_element_by_xpath('html/body/div[1]/div[2]/div[2]/div[1]/textarea').send_keys(ip)
        sleep(1)
        self.driver.find_element_by_xpath('html/body/div[1]/div[2]/div[2]/div[2]/button[1]').click()
        sleep(10)



#         self.driver.find_element_by_xpath('//html/body/div[1]/div/div[2]/div[4]/a').click()#购买页面
#         sleep(1)
#         self.driver.find_element_by_xpath ('//html/body/div[1]/div[2]/div[2]/div[1]/section/div[4]/button').click()#优质代理


#找回密码
class mind(page):
    url='/'
    def user_find(self, username2='username2', password2='password2', code2='code2'):
        self.open()
        self.driver.find_element_by_class_name('login').click()
        sleep(2)
        self.driver.find_element_by_xpath("//div[@class='findPwd']").click()
        sleep(2)
        self.driver.find_element_by_xpath("//input[@id='findPwd-phone']").send_keys(username2)
#        self.driver.find_element_by_xpath ("//input[@class='code-file form-control']").send_keys(code2)
        self.driver.find_element_by_xpath("//input[@id='findPwd-pwd']").send_keys(password2)
        self.driver.find_element_by_xpath("//button[@class='btn btn-updatepwd btn-block']").click()
        sleep(3)
