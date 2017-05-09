import requests,time,json
spiderId='88389195c21711e6a82e000c29f552f01'


headers={'spiderId':spiderId}

r=requests.get('http://api.xdaili.cn/xdaili-api/spider/applyLot',headers=headers)
print(r.status_code)
print(r.content)
print(type(r.content))
