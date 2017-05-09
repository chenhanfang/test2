import requests
import usernames
import json
from login import get_cookie
from getuid import getuid


'''生成提取普通优质订单的uid的接口'''
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
    orderno=pm['orderno']
    print(orderno)
    if orderno:
        r7 = requests.post('http://test.xdaili.cn:10005/ipagent/url/buildUrl',
                          params={"orderno":orderno,"picknum":'10'},headers=h)
        print(r7.status_code)
        print(r7.text)
        print(i)

        i=i+1