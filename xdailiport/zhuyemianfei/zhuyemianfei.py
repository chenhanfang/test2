import requests
import usernames
from login import get_cookie

'''主页免费代理接口'''
i=0
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
    r=requests.get('http://test.xdaili.cn:10005/ipagent/freeip/getFreeIps',params={'page':'1'},headers=h)
    print(r.status_code)
    print(r.text)
    i=i+1
print(i)