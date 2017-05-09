import requests
import usernames
import json
from login import get_cookie
from getduor import getduor


i=0
count='3'
for l in usernames.l:
    username=l[0]
    password=l[1]
    spiderid=l[3]
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
    orderno=getduor(h)
    print(orderno)
    r10 = requests.get('http://test.xdaili.cn:10005/ipagent/url/listBatchIp/'+spiderid+'/'+orderno+'/'+count,
                      params={"returnType":1},headers=h)
    print(r10.status_code)
    print(r10.text)
