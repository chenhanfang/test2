import requests
import json
from requests import exceptions
from requests import Request,Session
url='https://developer.github.com/'
url1='https://api.github.com'

def simple_requests():
    response=requests.get(url)
    print(">>>resposes headers")
    print(response.headers)
    print(">>>response body")
    print(response.text)

def build_uri(endpoint):
    return '/'.join([url1,endpoint])

#更好的输出
def better_print(json_str):
    return json.dumps(json.loads(json_str),indent=4)

def requests_method():
    respose1=requests.get(build_uri('users/chenhanfang'))
    print(better_print(respose1.text))
    respose=requests.get(build_uri('user/emails'),auth=('chenhanfang','Chenhan1028'))
    print(better_print(respose.text))

def params_request():
    response=requests.get(build_uri('users'),params={'since':8})
    print(better_print(response.text))
    print(response.request.headers)
    print(response.request.body)
    print(response.status_code)

def json_request():
    # response=requests.patch(build_uri('user'),auth=('chenhanfang','Chenhan1028'),json={'name':'chenhanfang','email':'123@163.com'})
    response=requests.post(build_uri('user/emails'),auth=('chenhanfang','Chenhan1028'),json=['chfan1028@163.com'])
    print(better_print(response .text))
    print(response.request.headers)
    print(response.request.body)
    print(response.status_code)

def timeout_request():
    try:
        response=requests.get(build_uri('user/emails'),timeout=10)
        response.raise_for_status()
    except exceptions.Timeout as e:
        print(e.message)
    except exceptions.HTTPError as e:
        print(e.message)
    else:
        print(response.text)
        print(response.status_code)

def hard_request():
    from requests import Request,Session
    s=Session()
    headers={'User-Agent':'fake1.3.4'}
    req=Request('GET',build_uri('user/emails'),auth=('chenhanfang','Chenhan1028'),headers=headers)
    prepped=req.prepare()
    print(prepped.body)
    print(prepped.headers)

    resp=s.send(prepped,timeout=5)
    print(resp.status_code)
    print(resp.request.headers)
    print(resp.text)



if __name__=='__main__':
    hard_request()