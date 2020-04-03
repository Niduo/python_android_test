from selenium.webdriver.support.ui import WebDriverWait


#获取单个元素对象
def getElement(driver,locateType,locateExpression):
    try:
        element = WebDriverWait(driver,5).until(lambda x: x.find_element(by= locateType,value=locateExpression))
        return element
    except Exception:
        raise
def getElements(driver,locateType,locateExpression):
    try:
        elements = WebDriverWait(driver,5).until(lambda x: x.find_elements(by=locateType,value=locateExpression))
        return elements
    except Exception:
        raise

if __name__=="__main__":
    #测试代码
    from selenium import webdriver
    import time
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http:www.baidu.com")
    searchBox = getElement(driver,"css","#kw")
    searchBox.send_keys("红小宝")
    time.sleep(2)
    driver.quit()