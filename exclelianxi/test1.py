####读取测试用例
import requests

import os,sys
import xlrd
import logging
xlsfile1='testcase.xlsx'####测试用例文件
if not os.path.exists(xlsfile1):
    logging.error('测试用例不存在')
    sys.exit()
book = xlrd.open_workbook(xlsfile1)
api_sheet = book.sheet_by_index(0)
nrows=api_sheet.nrow
for i in range(1,nrows):
    num = api_sheet.cell(i,0)
    password = api_sheet.cell(i,1)
    api_host = api_sheet.cell(i,2)
    request_url=api_sheet.cell(i,3)
    data = api_sheet.cell(i,4)
    headers = api_sheet.cell(i,5)
    cv = num.value
    pv = api_host.value
    sv = request_url.value
    url = pv+sv
    param = data.value
    h=headers.value
    r=requests.get(url,params=param,headers=h)
    if r.status_code == 200:
        logging.info('用例编号' + str(cv) +
                      '执行结果是：' + '成功，返回code是' + str(r.status_code) + ',')
    else:
        logging.info('用例编号'+str(cv) +
                      '执行结果是： ' + '失败！返回code是' + str(r.status_code) + ',')
