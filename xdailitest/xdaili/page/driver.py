from selenium import webdriver
import time

def browser():
    driver=webdriver.Chrome()
    return driver

if __name__=='__main__':
    dr=browser()
    dr.get('http://10.60.10.71')
    time.sleep(30)