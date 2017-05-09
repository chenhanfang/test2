######利用request发送请求，利用多线程模拟并发,压力测试
#coding=utf-8
import requests
import datetime
import time
import threading
import usernames
class url_request():
    times=[]
    error=[]
    def req(self,mobile,password,url):
        myreq=url_request()
        headers={"Accept-Encoding": "gzip, deflate, sdch",
                    "Accept-Language": "zh-CN,zh;q=0.8",
                    "Connection": "keep-alive",
                    'Host': 'www.xdaili.cn',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                }
        params={'mobile':mobile,'password':password}
        r=requests.get(url,params=params,headers=headers)
        print(r.text)
        ResponseTime=float(r.elapsed.microseconds)/1000
        myreq.times.append(ResponseTime)######将响应时间写入数组
        if r.status_code != 200:
            myreq.times.append('0')
if __name__ == '__main__':
    myreq=url_request()
    threads=[]
    starttime=datetime.datetime.now()
    print("request start time %s"%starttime)
    nub=1#####设置并发线程数
    ThinkTime=1######设置思考时间
    for i in range(1,nub+1):
        for l in usernames.l:
            mobile=l[0]
            password=l[1]
            t=threading.Thread(target=myreq.req,args=(mobile,
                                                      password,
                                                     'http://test.xdaili.cn:10005/ipagent/user/login'))
            threads.append(t)
    for t in threads:
        time.sleep(ThinkTime)
        t.setDaemon(True)
        t.start()
    t.join()
    endtime=datetime.datetime.now()
    print('request end time %s'%endtime)
    time.sleep(3)
    AverageTime='{:.3f}'.format(float(sum(myreq.times))/float(len(myreq.times)))###计算数组平均值
    print('Average Response Time %s ms'%AverageTime)
    usetime=str(endtime-starttime)
    hour=usetime.split(':').pop(0)####获取时间里的时分秒
    minute=usetime.split(':').pop(1)
    second=usetime.split(':').pop(2)
    totaltime=float(hour)*60*60 + float(minute)*60 + float(second)
    print('Concurrent processing %s'%nub)#####打印并发数
    print('use total time %s s'%(totaltime-float(nub*ThinkTime)))
    print('fail request %s'%myreq.error.count('0'))#####打印错误请求数


