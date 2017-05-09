import requests
import usernames
import json
from login import get_cookie
from getduor import getduor

'''客户端申请独享通道，3分钟内重复返回错误'''
i=0
times=[]
time=0
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
    orderno=getduor(h)
    print(orderno)
    r7 = requests.get('http://test.xdaili.cn:10005/ipagent/privateProxy/getChannel/'+orderno,
                      headers=h)
    print(r7.status_code)
    print(r7.text)
    i=i+1
    retime = float(r7.elapsed.microseconds) / 1000
    times.append(retime)
for tim in times:
    time += tim
avgtime = float('%.2f' % (time / len(times)))
print('avgtime=%s' % avgtime)
print('i=%s'%i)