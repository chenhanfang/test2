import requests
from requests import Request,Session
import json
########利用session进行请求
s=requests.Session()
url1='http://test.xdaili.cn:10005/ipagent/user/login'
url2='http://test.xdaili.cn:10005/ipagent/user/getUser'
data={'mobile':'18329176957',"password":'e10adc3949ba59abbe56e057f20f883e'}
h={
        "Accept-Encoding": "gzip, deflate, sdch",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Connection": "keep-alive",
        'Host': 'www.xdaili.cn',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',

}

r1=s.post(url1,data)
r2=s.post(url2)#######记住了登录之后的session

# print(r2.status_code)
# print(r2.text.encode('utf-8'))#########encode('utf-8')进行utf-8编码
# print(r2.json())
# pa=r2.json()['obj']
# createtime=pa['createtime']
# print(createtime)
# r2.encoding='ISO-8859-1'######改变编码
# print(r2.text)
# print(r2.status_code == requests.codes.ok)#####requests库自带的内置的状态码查询对象
# print(r2.headers)########打印响应请求头
# print(r2.headers['Date'])#####对字典里的大小写不是很敏感
# print(r2.headers.get('content-type'))
# print(r2.history)

#######搞不清楚什么鬼request.prepare
# s1=Session()
# req=requests.Request('POST',url1,data=data,headers=h)
# prepped=s.prepare_request(req)
# s1.send(req)
# resp=s1.send(prepped)
# print(resp.content)

# ######代理的使用
# proxies={
#         "http":"http://10.10.1.10:3218",
#         "https":"http://10.10.1.10:1080",#########代理ip号
# }
# ######若代理的使用需要使用HTTP Baisic Auth
# proxies1={"http":"http//user:pass@10.10.1.10:3128/",}
# ######若要为某个特定的链接方式或主机设置代理，使用scheme：、、hostname作为key
# proxies3={'http://10.20.1.128':'http://10.10.1.10:5323'}
#
# requests.get('http://xxxx.xxxx.xx',proxies=proxies)
# #######socks代理pip install requests[socks]
# proxies4={'http':'socks5://user:pass@host:port',
#           'http':'socks5://user:pass@host:port'}



