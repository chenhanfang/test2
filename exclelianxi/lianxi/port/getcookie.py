import requests
import usernames

'''登录方法获取cookie'''
h = {
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Connection": "keep-alive",
        'Host': 'www.xdaili.cn',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',

}
def get_cookie(username,password):
    # for l in usernames.l:
    #     username = l[0]
    #     password = l[1]
        r = requests.get('http://test.xdaili.cn:10005/ipagent/user/login',
                                  params={'mobile': username,'password': password}, headers=h)

        cookie=r.headers["Set-Cookie"]

        return cookie