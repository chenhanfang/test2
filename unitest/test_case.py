#coding=utf-8
import os
caselist=os.listdir('E:\\test2\\unitest\\thread')
print("caselist: %s" % caselist)
for a in caselist:
    if a != "__pycache__":
        s=a.split('.')[1]
    if s=='py':
        os.system("python E:\\test2\\unitest\\thread\\%s >>log.txt 2>&1"%a)#重定向输出
        #os.system("python %s >>log.txt 2>&1" % a)