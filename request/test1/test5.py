import requests
r2=requests.get('http://www.xdaili.cn',timeout=1)
print(r2.content)
r=requests.get('http://www.xdaili.cn/ipagent/sendMsg/register',timeout=1)
print(r.text)
print(r.url)
print(r.encoding)
r1=requests.post('http://www.xdaili.cn/ipagent/user/login',params={'mobile':'18329176957','passowrd':'123456','code':'8888'},timeout=5)
print(r1.text)
print(r1.status_code)