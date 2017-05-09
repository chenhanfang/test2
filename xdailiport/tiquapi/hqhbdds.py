import requests
import usernames
import json
from login import get_cookie
from getduor import getduor

'''获取可用混拨订单数接口'''
times=[]
time=0
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


    r6 = requests.get('http://test.xdaili.cn:10005/ipagent/privateProxy/maxOrderNum',
                          headers=h)
    print(r6.status_code)
    print(r6.text)
    retime=float(r6.elapsed.microseconds)/1000
    times.append(retime)
for tim in times:
    time+=tim
avgtime=float('%.2f'%(time/len(times)))
print(avgtime)
