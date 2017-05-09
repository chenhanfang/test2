from time import sleep
import unittest,random,sys
sys.path.append('./xdaili')
sys.path.append('./xdaili/page')
from xdailitest.xdaili.page import myunit
from xdailitest.xdaili.zhuce import zhuce
from selenium import webdriver

# #注册
# class zhucetest(myunit.mytest ):
#     def user_zhuce_verify(self,username1='',code1='',password1=''):
#         zhuce(self.driver).user_zhuce(username1,code1,password1)
#
#     def test_zhuce(self):
#         self.user_zhuce_verify(username1='15858596957',code1='1234',password1='123456')


if __name__=='__main__':
    unittest.main()
