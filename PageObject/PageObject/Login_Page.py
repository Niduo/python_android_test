#executable path="D:\Python37/chromedriver.exe"
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.by import By
from Util.ParsePageObjectRepository import * #新加
from Util.ObjectMap import *
from ProjectVar.var import * # 新加
from selenium.common.exceptions import TimeoutException,NoSuchElementException

import traceback
# driver = webdriver.Chrome()
class LoginPage():
    def __init__(self,driver):
        self.driver = driver
        self.parse_config_file = ParsePageObjectRepositoryConfig() #新加，获取配置文件信息
        self.login_page_items = self.parse_config_file.getItemSestion("hoom_login") #新加
        # print("self.login_page_items",self.login_page_items)
        self.wait = WebDriverWait(self.driver,5,0.5)


    # def getLoginButton(self,locateType,locateExpression):
    #     loginbutton = self.wait.until(lambda x: x.find_element(by=locateType,value=locateExpression)) # '.header-reg-btn.header-login'
    #     return loginbutton

    def getLoginButton(self):
        locateType,locateExpression = self.login_page_items['login_page.loginbutton'].split('>')  #css>.header-reg-btn.header-login
        # logbuttun =self.wait.until(lambda x: x.find_element(by=locateType,value=locateExpression)) #css>.header-reg-btn.header-login
        logbuttun = getElement(self.driver,locateType,locateExpression)
        return logbuttun

    # def getUsername(self,locateType,locateExpression):
    #     userName = self.wait.until(lambda x: x.find_element(by=locateType,value=locateExpression))# '#J_username'
    #     return userName


    def getUsername(self):
        locateType, locateExpression = self.login_page_items['login_page.username'].split('>')
        # username = self.wait.until(lambda x:x.find_element(by=locateType,value=locateExpression))
        #使用 元素的方法封装起来后
        username = getElement(self.driver,locateType,locateExpression)
        return username


    # def getPassword(self,locateType,locateExpression):
    #     pwd = self.wait.until(lambda x: x.find_element(by=locateType,value=locateExpression))# '#J_pwd'
    #     return pwd


    def getPassWord(self):
        locateType, locateExpression = self.login_page_items['login_page.password'].split('>')
        # pwd = self.wait.until(lambda x: x.find_element(by=locateType,value=locateExpression))
        #使用 元素的方法封装起来后
        pwd = getElement(self.driver,locateType,locateExpression)
        return pwd


    # def getSubmit(self,locateType,locateExpression):
    #     submit = self.wait.until(lambda x: x.find_element(by=locateType,value=locateExpression))# 'J_submit-login')
    #     return submit
    def getSubmit(self):
        locateType, locateExpression = self.login_page_items['login_page.submit'].split('>')
        # submit = self.wait.until(lambda x: x.find_element(by=locateType,value=locateExpression))
        #使用 元素的方法封装起来后
        submit = getElement(self.driver,locateType,locateExpression)
        return submit

    #查找元素的方法封装起来后（ObjectMap），调用ObjectMap的方法实现各个查找元素的方法，并且对登录动作做个封装
    def login(self):
        self.getLoginButton().click()
        time.sleep(2)
        self.getUsername().send_keys('17200010004')
        self.getPassWord().send_keys('1234qwer')
        self.getSubmit().click()
        # time.sleep(2)
        # driver.quit()


    # def login(self):
        # try:
        #     # driver = webdriver.Chrome()
        #
        #
        #
        #     wait = WebDriverWait(self.driver,10,0.2) #显示等待
        #     # driver.maximize_window()
        #     # driver.get("http://192.168.1.37:3000")
        #     logbuttun = wait.until(lambda x: x.find_element_by_css_selector('.header-reg-btn.header-login'))
        #     logbuttun.click()
        #
        #     name = wait.until(lambda x: x.find_element_by_css_selector('#J_username'))
        #     name.send_keys('17200010004')
        #
        #     password = wait.until(lambda x:x.find_element_by_css_selector('#J_pwd'))
        #     password.send_keys('1234qwer')
        #
        #     submit = wait.until(lambda x:x.find_element_by_id('J_submit-login'))
        #     submit.click()
        #     time.sleep(2)
        #     # assert u"退出" in self.driver.page_source, "no exist in page_source"
        # except TimeoutException:
        #     #捕获TimeoutException异常
        #     print(traceback.print_exc())
        #
        # except NoSuchElementException:
        #     #捕获NoSuchElementException异常
        #     print(traceback.print_exc())
        #
        # except Exception:
        #     # 捕获其他异常
        #     print(traceback.print_exc())


# if __name__=="__main__":
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("http://192.168.1.37:3000")
#     time.sleep(2)
#     login_1 = LoginPage(driver)
#     # login_1.getLoginButton("css", ".header-reg-btn.header-login").click()
#     # time.sleep(2)
#     # login_1.getUsername(By.CSS_SELECTOR, "#J_username").send_keys('17200010004')
#     # login_1.getPassword("css", "#J_pwd").send_keys('1234qwer')
#     # login_1.getSubmit("id", "J_submit-login").click()
#     # time.sleep(2)
#     # mycount = driver.find_element_by_css_selector('.last-nav a')
#     #mycount.click()
# login_1.login()

    # login_1.getLoginButton().click()
    # time.sleep(2)
    # login_1.getUsername().send_keys('17200010004')
    # login_1.getPassWord().send_keys('1234qwer')
    # login_1.getSubmit().click()
    # time.sleep(2)
    #
    # driver.quit()





