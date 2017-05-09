import requests
import usernames
import json
from login import get_cookie
from getuid import getuid
import time


'''普通优质代理提取'''
i=1
for l in usernames.l:
    username=l[0]
    password=l[1]
    cookie=str(get_cookie(username,password))
    h = {
                    "Accept-Encoding": "gzip, deflate, sdch",
                    "Accept-Language": "zh-CN,zh;q=0.8",
                    "Connection": "keep-alive",
                    'Host': 'www.xdaili.cn',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                    'Cookie':cookie
            }
    pm=getuid(h)
    uid=pm['uid']
    print(uid)
    # for i in range(50):
    #     r7 = requests.get('http://test.xdaili.cn:10005/ipagent/url/quality/'+uid,
    #                       params={"returnType":'1',"count":'10'},headers=h,timeout=10)
    #
    #     print(r7.status_code)
    #     print(r7.text)
    #     print(i)
    #     i=i+1
    #     time.sleep(10)


