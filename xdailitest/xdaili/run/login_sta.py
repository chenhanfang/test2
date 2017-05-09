from time import sleep
import unittest,random,sys
sys.path.append('./xdaili')
sys.path.append('./xdaili/page')
from xdailitest.xdaili.page import myunit
from xdailitest.xdaili.loginpage import login,mind
from selenium import webdriver

#登录

class logintest(myunit.mytest ):
    def user_login_verify(self,username='',password='',code='',ip=''):
        login(self.driver).user_login(username,password,code,ip)

    def test_login1(self):
        self.user_login_verify(username='18329176957',password='123456',code='1111',ip='113.225.193.192:12151\n124.15.56.293:27329')
        print('pass')
        # t=self.driver.find
        # self.assertEqual('登录成功',t.text)

#    def test_login2(self):
#        self.user_login_verify(username='15858585954',password='123456',code='8888')
# # 找回密码
# class mindtest(myunit.mytest):
#     def user_find_verify(self, username2='', code2='', password2=''):
#         mind(self.driver).user_find(username2, code2, password2)
#
#     def test_find1(self):
#         self.user_find_verify(username2='18329176957',code2='1234',password2='123456')

if __name__=='__main__':
    unittest.main()
