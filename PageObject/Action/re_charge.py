from PageObject.Recharge_Page import *
from selenium import webdriver

def re_charge(driver,amount):
    rd = RechargePage(driver)
    rd.rechage_mycount().click()
    time.sleep(2)
    rd.recharge_buttn().click()
    rd.recharge_putt().send_keys(amount)
    rd.recharge_submit().click()
    rd.recharge_verify().click()

if __name__=='__main__':
    driver =webdriver.Chrome()
    driver.maximize_window()
    driver.get("http:192.168.1.37:3000")
    login(driver,"17200010005","1234qwer")
    time.sleep(2)
    re_charge(driver,200)
    time.sleep(2)
    driver.quit()
