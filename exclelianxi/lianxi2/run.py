import requests
from read import read
read=read()
url=read['url']
print(url)
params=read['params']
print(params)
name=read['name']
print(name)
result=read['result']
print(result)
h1=read['headers']
# h=h1.items()
# print(h)
# h = {
#         "Accept-Encoding": "gzip, deflate, sdch",
#         "Accept-Language": "zh-CN,zh;q=0.8",
#         "Connection": "keep-alive",
#         'Host': 'www.xdaili.cn',
#         'Upgrade-Insecure-Requests': '1',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
# }
r=requests.get(url,params=params,headers=h1)
print(r.text)