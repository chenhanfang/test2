import requests
url='http://www.xdaili.cn/ipagent/sendMsg/forget'
result=requests.get(url,timeout=1)
print('http status code: %s\n'% result.status_code)
print(result.content)
text=result.content.decode()
print(text)
print('http texttype:%s\n'%type(text))
#print(result.text)
print(result.encoding)
result.request.headers