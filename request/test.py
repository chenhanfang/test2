#coding=utf-8
import requests
import json
import time
url = 'http://127.0.0.1:8000/login/search_guest/'
url2='http://127.0.0.1:8000/login/add_event/'
url3='http://127.0.0.1:8000/login/user_sign/'
url4='http://127.0.0.1:8000/login/get_event_list/'
url5='http://127.0.0.1:8000/login/add_guest'
# r1=requests.get(url,params={'eid':'1','phone':'13511001100'})
payload={'eid':8,'name':'一加4发布会','limit':2000,'address':"深圳宝体",'start_time':'2017-10-10 10:00:00'}
# r=requests.get(url2,params=payload)
# result=r.json()
payload1={'eid':'1','phone':'13511001100'}
# r3=requests.get(url3,params=payload1)
r4=requests.get(url4,params={'eid':'1','name':'红米Pro发布会'})
# payload2={'eid':'1','realname':'红米Pro发布会,','phone':'15859546957','email':'123@123.com','gid':18}
# r5=requests.get(url5,params=payload2)
# print(r1.status_code)
# print(r1.text)
# print(r1.url)
# print(r.status_code)
# print(r.text)
# print(r.url)
# print(r3.status_code)
# print(r3.url)
# print(r3.text)
print(r4.status_code)
print(r4.text)
# print(r5.status_code)
# print(r5.url)
# print(r5.text)
time1 = time.time()
print(time)
url6='http://127.0.0.1:8000/login/sec_get_event_list/'
auth_user=('han','hz970916')
r6=requests.get(url6,auth=auth_user,params={'eid':'1','name':'红米Pro发布会'})
time2= time.time()
print(r6.elapsed.microseconds/1000000)####获取响应时间
t=time2-time1####也是一种获取响应时间
print(t)
print(r6.status_code)
# print(r6.text)

