import requests
payload={'mobile':'18329176957','password':'e10adc3949ba59abbe56e057f20f883e','code':'8888'}
r=requests.get('http://www.xdaili.cn/ipagent/user/login',params=payload)
print(r.url)
r.raw
r.raw.read(10)
