
import requests
import unittest
from HTMLTestRunner import HTMLTestRunner



if __name__ == '__main__':
    testunit = unittest.TestSuite()
    # testunit.addTest(testloginapi("testloginapi"))
    fp = open('result11.html', 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='讯代理接口测试',
                            description='用例执行情况：')
    discover = unittest.defaultTestLoader.discover('E:\\test2\\exclelianxi\\lianxi\\port', pattern='*test.py')
    runner.run(discover)
    fp.close()