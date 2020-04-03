from PageObject.Login_Page import *
from selenium import webdriver

def login(driver,username,password):
    lp = LoginPage(driver)
    lp.getLoginButton().click()
    lp.getUsername().send_keys(username)
    lp.getPassWord().send_keys(password)
    lp.getSubmit().click()
# if __name__=='__main__':
#
#     #测试代码
#
#     driver=webdriver.Chrome()
#
#     driver.get("http://192.168.1.37:3000")
#
#     login(driver,"17200010005","1234qwer")