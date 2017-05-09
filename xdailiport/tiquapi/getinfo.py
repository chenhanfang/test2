import requests
import usernames
import json
from login import get_cookie

'''获取用户信息'''
times=[]
time=0
for l in usernames.l:
    username=l[0]
    password=l[1]
    cookie=str(get_cookie(username,password))
    # data = cookie.split("'")[3].split(";")[0]######分割
    # cookie1=cookie['cookie']
    # print(json.loads(cookie))

    h = {
                    "Accept-Encoding": "gzip, deflate, sdch",
                    "Accept-Language": "zh-CN,zh;q=0.8",
                    "Connection": "keep-alive",
                    'Host': 'www.xdaili.cn',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                    'Cookie':cookie
            }
    r4 = requests.get('http://test.xdaili.cn:10005/ipagent/user/getUser',headers=h)
    print(r4.status_code)
    print(r4.text)
    retime=float(r4.elapsed.microseconds)/1000######获取响应时间，单位是ms
    times.append(retime)

print(times)
for tim in times:
    time+=tim
avetime=float("%.2f"%(time/len(times)))#####保留两位小数
print('avgtime=%s'%avetime)