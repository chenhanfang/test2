#coding=utf-8
import os
from threading import Thread
from time import ctime,sleep
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

binary = FirefoxBinary('D:\\Program Files\Mozilla Firefox\\firefox.exe')

def testbaidu(browser,search):
    print('start:%s' %ctime())
    print('browser:%s'%browser)
    if browser =='ie':
        driver=webdriver.Ie()
    elif browser =='chrome':
        driver=webdriver.Chrome()
    elif browser =='firefox':
        driver=webdriver.Firefox(firefox_binary=binary )
    else:
        print('browser参数有误，只能为ie,chrome,firefox')
    driver.get("http://www.baidu.com")
    sleep(2)
    driver.find_element_by_id('kw').send_keys(search )
    driver.find_element_by_id('su').click()


if __name__=='__main__':
    lists={'chrome':'threading','ie':'hello','firefox':'python'}
    threads=[]
    files=range(len(lists))

    for browser,search in lists.items() :
        t=Thread(target=testbaidu,args=(browser ,search ))
        threads.append(t)

    for t in files:
        threads[t].start()
    for t in files:
        threads[t].join()

    print('end:%s'%ctime())
