#coding=utf-8
from HTMLTestRunner  import HTMLTestRunner
import smtplib
import unittest
import os,time


if __name__ =='__main__':
    testunit=unittest.TestSuite()
    fp=open('D:\\ceshibaogao\\result9.html','wb')
    runner=HTMLTestRunner (stream=fp,
                           title= '讯代理测试',
                           description= '用例执行情况：')
    discover=unittest.defaultTestLoader.discover('E:\\test2\\xdailitest\\xdaili\\run',pattern='*_sta.py')
    runner.run(discover)
    fp.close()