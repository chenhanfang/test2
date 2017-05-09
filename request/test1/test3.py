import requests
url='http://ip.taobao.com/service/getIpInfo.php'
try:
    r=requests.get(url,params={'ip':'8.8.8.8'},timeout=1)
    r.raise_for_status()
except requests.RequestException as e:
    print(e)
else:
    result=r.json()
    print(type(result),result,sep='\n')
