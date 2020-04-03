#executable path="D:\Python37/chromedriver.exe"
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.common.by import By

from selenium.common.exceptions import TimeoutException,NoSuchElementException

import traceback
from PageObject.Login_Page import *
from Action.Login import *

class RechargePage(object):
    def __init__(self,driver):
        self.driver = driver
        self.parse_config_file = ParsePageObjectRepositoryConfig()
        self.rechage_page_itmes = self.parse_config_file.getItemSestion("hoom_recharge")
        # print("self.rechage_page",self.rechage_page_itmes)


    def rechage_mycount(self):
        locateType,locateExpression = self.rechage_page_itmes['recharge_page.mycount'].split(">")
        print(locateType,locateExpression)
        return getElement(self.driver,locateType,locateExpression)

    def recharge_buttn(self):
        locateType,locateExpression = self.rechage_page_itmes['recharge_page.recharge_button'].split(">")
        print(locateType,locateExpression)
        return getElement(self.driver,locateType,locateExpression)

    def recharge_putt(self):
        locateType,locateExpression = self.rechage_page_itmes['recharge_page.recharge_put'].split(">")
        print(locateType,locateExpression)
        return getElement(self.driver,locateType,locateExpression)

    def recharge_submit(self):
        locateType,locateExpression = self.rechage_page_itmes['recharge_page.recharge_sub'].split(">")
        print(locateType,locateExpression)
        return getElement(self.driver,locateType,locateExpression)

    def recharge_verify(self):
        locateType,locateExpression = self.rechage_page_itmes['recharge_page.verify'].split(">")
        print(locateType,locateExpression)
        return getElement(self.driver,locateType,locateExpression)

    def recharge_do(self):
        rd = RechargePage(driver)
        rd.rechage_mycount().click()
        time.sleep(2)
        rd.recharge_buttn().click()
        rd.recharge_putt().send_keys(200)
        rd.recharge_submit().click()
        rd.recharge_verify().click()




        # try:
        #     wait = WebDriverWait(self.driver,10,0.5) #显示等待
        #     mycount = wait.until(lambda x: x.find_element_by_css_selector('.last-nav a'))
        #     mycount.click()
        #     time.sleep(2)
        #     recharge_button = wait.until(lambda x: x.find_element_by_css_selector('.uc-home-recharge'))
        #     recharge_button.click()
        #
        #     recharge_put = wait.until(lambda x: x.find_element_by_css_selector('#J_quickpay-amount'))
        #     recharge_put.send_keys(100)
        #
        #     recharge_sub = wait.until(lambda x: x.find_element_by_css_selector('#J_quickpay-btn'))
        #     recharge_sub.click()
        #     time.sleep(2)
        #
        #     recharge_verify = wait.until(lambda x: x.find_element_by_css_selector('#J_verifycode'))
        #     recharge_verify.click()
        #     time.sleep(2)
        # except TimeoutException:
        #     # 捕获TimeoutException异常
        #     print(traceback.print_exc())
        #
        # except NoSuchElementException:
        #     # 捕获NoSuchElementException异常
        #     print(traceback.print_exc())
        #
        # except Exception:
        #     # 捕获其他异常
        #     print(traceback.print_exc())

#
# if __name__=="__main__":
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get("http://192.168.1.37:3000")
#     login(driver,"17200010005","1234qwer")
#     recharge_1 = RechargePage(driver)
#     time.sleep(3)
#     recharge_1.rechage_mycount().click()
#     recharge_1.recharge_buttn().click()
#     recharge_1.recharge_putt().send_keys(200)
#     recharge_1.recharge_submit().click()
#     time.sleep(2)
#     recharge_1.recharge_verify().click()
#     time.sleep(3)
#     driver.quit()

