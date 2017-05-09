import requests
import usernames
import json
from login import get_cookie


'''普通优质代理订单获取uid接口'''

# def getuid(h):
h = {
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Connection": "keep-alive",
        'Host': 'www.xdaili.cn',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',

}
for l in usernames.l:
        username=l[0]
        password=l[1]
        r7 = requests.get('http://test.xdaili.cn:10005/ipagent/url/getUidAndType',
                          headers=h)
        # print(r7.status_code)
        # print(r7.text)
        r=r7.json()
        if "RESULT" in r.keys():######处理没有用的数据
            result=r['RESULT']
            for one in result:
                uid=one['uid']
                orderno=one['orderno']
                print(uid,orderno)

                # return {'orderno':orderno,'uid':uid }


        # print(r)
        # if r["RESULT"] is not None:
            # result = r["RESULT"]
            # for one in result:
            #     uid = one["uid"]
            #     orderno=one["orderno"]
            #     print(uid,orderno)

                # return {'orderno':orderno,'uid':uid }