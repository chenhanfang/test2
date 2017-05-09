import requests
import usernames
from login import get_cookie

'''根据优惠券类型查询接口，不包括已过期的和使用过的'''
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
    r=requests.get('http://test.xdaili.cn:10005/ipagent/coupon/listCouponsBetweenType',
                   params={'minType':'0','maxType':'16'},headers=h)
    print(r.status_code)
    print(r.text)