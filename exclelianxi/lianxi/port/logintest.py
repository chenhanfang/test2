from read import readExcel
import requests
import unittest
from HTMLTestRunner import HTMLTestRunner
from getcookie import get_cookie

class testloginapi(unittest.TestCase):
    def testloginapi(self):
        '''登录接口测试'''
        h={
                "Accept-Encoding": "gzip, deflate, sdch",
                "Accept-Language": "zh-CN,zh;q=0.8",
                "Connection": "keep-alive",
                'Host': 'www.xdaili.cn',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',

        }
        excle = readExcel(r'yonglibiao//yongli.xlsx')
        row=excle.getRows
        for i in range(0,row-1):
            name=excle.getName
            data=excle.getData
            url=excle.getUrl
            method=excle.getMethod
            re=excle.getResult
            try:
                if method[i] == 'get':
                    r = requests.get(url[i],params=data[i],headers=h)

                elif method[i] == 'post':
                    r = requests.post(url[i],params=data[i],headers=h)

            except:
                print('failure')
            result = r.text
            print(name[i])
            print('预期输出结果：'+re[i])
            print(' 测试结果：%s' % result)

if __name__=='__main__':
        unittest.main()