from xdailitest.xdaili.page.base import page
from time import sleep


#注册
class zhuce(page):
    url='/'
    def user_zhuce(self,username1='username1',code1='code1',password1='password1'):
        self.open()
        self.driver.find_element_by_class_name('register').click()
        sleep(2)

        self.driver.find_element_by_id('register-phone').send_keys(username1)
        sleep(2)
#        self.driver.find_element_by_xpath("//input[@class='code_field form-control']").send_keys(code1)
        self.driver.find_element_by_id('register-pwd').send_keys(password1)
        self.driver.find_element_by_xpath("//button[@class='btn btn-register btn-block']").click()
        sleep(3)
