import requests
import usernames
import json
from login import get_cookie
'''获取用户所有独享订单号'''
def getduor(h):
        r6 = requests.get('http://test.xdaili.cn:10005/ipagent/recharge/listPrivateOrder',headers=h)
        # print(r6.status_code)
        r = r6.json()#######转换成json
        # print(r6.text)
        # r=r6.text
        # print(r, type(r))
        # r = json.loads(r)
        # print(r, type(r))
        result=r["RESULT"]
        for one in result:
            orderno=one["orderno"]
            # print(orderno)
            # return orderno

            return orderno
