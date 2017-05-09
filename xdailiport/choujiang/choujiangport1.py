import requests
from threading import Thread



def test_choujiang(number,mobile):
    a90, a80, a70, a60, a50, a20, a10, a0 = 0, 0, 0, 0, 0, 0, 0, 0
    for i in range(int(number)):
        h = {"Accept-Encoding": "gzip, deflate, sdch",
             "Accept-Language": "zh-CN,zh;q=0.8",
             "Connection": "keep-alive",
             'Host': 'www.xdaili.cn',
             'Upgrade-Insecure-Requests': '1',
             'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
             # 'Cookie':cookie
             }
        r = requests.get('http://test.xdaili.cn:10005/ipagent/user/login',
                         params={'mobile': mobile, 'password': 'e10adc3949ba59abbe56e057f20f883e'}, headers=h)

        cookie = r.headers["Set-Cookie"]
        h1 = {"Accept-Encoding": "gzip, deflate, sdch",
              "Accept-Language": "zh-CN,zh;q=0.8",
              "Connection": "keep-alive",
              'Host': 'www.xdaili.cn',
              'Upgrade-Insecure-Requests': '1',
              'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
              'Cookie': cookie
              }
        r4 = requests.get('http://test.xdaili.cn:10005/ipagent//coupon/randomClientCoupon', headers=h1)
        r = r4.json()
        result = r['RESULT']
        print(result)
        if result == 90:
            a90 = a90 + 1
        elif result == 80:
            a80 = a80 + 1
        elif result == 70:
            a70 = a70 + 1
        elif result == 60:
            a60 = a60 + 1
        elif result == 50:
            a50 = a50 + 1
        elif result == 20:
            a20 = a20 + 1
        elif result == 10:
            a10 = a10 + 1
        else:
            a0 = a0 + 1

    print('90的次数：%s' % a90)
    p90 = a90 /int( number)
    print('90的比例：%s' % p90)

    print('80的次数：%s' % a80)
    p80 = a80 /int( number)
    print('80的比例：%s' % p80)

    print('70的次数：%s' % a70)
    p70 = a70 /int( number)
    print('70的比例：%s' % p90)

    print('60的次数：%s' % a60)
    p60 = a60 /int( number)
    print('60的比例：%s' % p60)

    print('50的次数：%s' % a50)
    p50 = a50 / int( number)
    print('50的比例：%s' % p50)

    print('20的次数：%s' % a20)
    p20 = a20 / int( number)
    print('20的比例：%s' % p20)

    print('10的次数：%s' % a10)
    p10 = a10 / int( number)
    print('10的比例：%s' % p10)

    print('0的次数：%s' % a0)
    p0 = a0 / int( number)
    print('0的比例：%s' % p0)
if __name__ == '__main__':
    lists ={'1000':'13712415693','1000':'17681825397'}
    thread = []
    files = range(len(lists))
    for number,mobile in lists.items():
        t=Thread(target=test_choujiang,args=(number,mobile))
        thread.append(t)

    for i in files:
        thread[i].start()
    """
    for i in files:
        thread[i].join()
    """
