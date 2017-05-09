import requests
import json
import time

r=requests.get('http://47.92.30.145:8585/huadan/login',
               params={'account':'17681825397','password':'970916','provider':'中国联通','province':'浙江','idCardNum':'342921199308140328','realName':'陈含芳'})
retime = float(r.elapsed.microseconds) / 1000
print(retime)
print(r.status_code)
print(r.text)

print(type(r.text))
r1=r.json()
print(type(r1))
print(r1)
print(r1['token'])

token=r1['token']
print(token)

r2=requests.get('http://47.92.30.145:8585/huadan/getCode',params={'token':token})
print(r2.status_code)
print(r2.text)
print(r2.json())

r3=requests.get('http://47.92.30.145:8585/huadan/sendSMS',params={'token':token})
print(r3.status_code)
print(r3.text)
print(r3.json())