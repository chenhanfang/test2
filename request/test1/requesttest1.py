import requests
r=requests.get('http://www.xdaili.cn')
r.status_code
print(r.headers['content-type'])
r.encoding
print(r.text)
payload={'key1':'value1','key2':'value2'}
r=requests.get('http://www.xdaili.cn',params=payload)

from io import BytesIO

r.headers