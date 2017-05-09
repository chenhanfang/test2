import requests
import usernames
import json
from login import get_cookie



'''优质按量提取'''

for l in usernames.l:
    username=l[0]
    password=l[1]
    spiderId=l[3]
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

    orderno=[]######还不知道

    r7 = requests.get('http://test.xdaili.cn:10005/ipagent/url/listBatchIp/'+spiderId+'/'+orderno+'/'+10,
                      params={"returnType":'1'},headers=h)
    print(r7.status_code)
    print(r7.text)