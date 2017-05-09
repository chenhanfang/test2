import requests
import usernames
from login import get_cookie

'''代理池，还有很多其他接口'''
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

###'''简易版获取代理池ip'''orderno还不知道怎么获取
    # r8 = requests.get('http://test.xdaili.cn:10005/ipagent/specialController/batchProxy',
    #                       params={'orderno':orderno,'count':5,'spiderId':spiderid,'returnType':1},headers=h)
    # print(r8.status_code)
    # print(r8.text)

####'''查看代理池订单接口'''
    r9=requests.get('http://test.xdaili.cn:10005/ipagent/specialController/listRechargeBatchProxy',
                    params={"pageNum":'1'},
                    headers=h)
    print(r9.status_code)
    print(r9.text)

#####'''生成使用订单接口type:1-开放，2-独享，3-混拨'''
    # r10 = requests.get('http://test.xdaili.cn:10005/ipagent/recharge/testOrder',
    #                   params={"type": '1'},
    #                   headers=h)
    # print(r10.status_code)
    # print(r10.text)

#####'''支付完成返回订单号'''
    # r11 = requests.get('http://test.xdaili.cn:10005/ipagent/recharge/list',
    #                    params={"sort": 'endtime'},
    #                    headers=h)
    # print(r11.status_code)
    # print(r11.text)

#####'''支付未完成返回交易号'''
    # r12 = requests.get('http://test.xdaili.cn:10005/ipagent/recharge/listNoPay',
    #                    params={"sort": 'endtime'},
    #                    headers=h)
    # print(r12.status_code)
    # print(r12.text)

#####下单接口订单类型1-4：优质订单，5-8混拨订单，10-13独享订单
    r13 = requests.get('http://test.xdaili.cn:10005/ipagent/recharge/buy',
                       params={"type": '1'},
                       headers=h)
    print(r13.status_code)
    print(r13.text)