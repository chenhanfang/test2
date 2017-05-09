import re
# str1='imooc python'
# str1.startswith('imooc')
import urllib.request#python3中引入urllib2.urlopen()
req=urllib.request.urlopen('http://www.imooc.com/course/list')
# req=urllib.request.urlopen('http://10.60.10.71/freeproxy.html')

buf=req.read()

i=0
print(buf)
# list=re.findall(r'\d.\d.\d.\d',buf.decode('utf-8'))
# for li in list:
#     print(li)

listurl=re.findall(r'http:.+\.jpg',buf.decode('utf-8'))
for imgurl in listurl:
    print(imgurl)
    # f=open(str(i)+ '.jpg','wb+')#没有指定存储路径
    f=open('D:\\zhuaqushuju\\%s.jpg' %str(i),'wb+')#指定存储路径
    req1=urllib.request.urlopen(imgurl)
    buf1=req1.read()
    f.write(buf1)
    i=i+1







