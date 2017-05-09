#_*_ coding:utf-8 _*_
import requests
import csv
data=csv.reader(open('test.csv','r'))

def read():
    for port in data:
        name=port[0]
        method=port[1]
        api_url=port[2]
        request_url=port[3]
        params=port[4]
        headers=port[5]
        result=port[6]
        url = api_url+request_url
        return {'name':name,'url':url,'params':params,'result':result,'headers':headers}


