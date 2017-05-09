#coding=utf-8
import ast
import xlrd
import requests
import json
import unittest
from HTMLTestRunner import HTMLTestRunner

headers={
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Connection": "keep-alive",
        'Host': 'www.xdaili.cn',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',

}
class tets(unittest.TestCase):######下面的中文显示在结果表上
    '''接口测试'''
    def test(self):
        '''登录接口测试:HTMLTestRunner'''
        xls_data = xlrd.open_workbook(r"yongli.xlsx")  ######读取excel文件数据
        print("Get data type:", type(xls_data))
        table = xls_data.sheets()[0]
        row = table.nrows
        print(row)
        for i in range(1,row):
            xuhao=table.cell(i,0).value
            apiurl=table.cell(i,1).value
            requesturl=table.cell(i,2).value
            url=apiurl+requesturl
            params=ast.literal_eval(table.cell(i,3).value)########将excel里的字符串数据转换成数据字典
            result=table.cell(i,5).value
            # print(result)
            r=requests.get(url,params=params,headers=headers)
            print('%s测试结果：'%xuhao)
            print(r.text)
            # res=r.json()['jsonMsg']['msg']
            # print(res)
            # try:
            #     assert(result == res),'failure!'
            # except AssertionError as msg:
            #     print(msg)
            # else:
            #     print('pass')

if __name__ == '__main__':
    testunit=unittest.TestSuite()
    testunit.addTest(tets("test"))
    fp = open('D:\\ceshibaogao\\result11.html', 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='讯代理接口测试',
                            description='用例执行情况：')
    runner.run(testunit)
    fp.close()
