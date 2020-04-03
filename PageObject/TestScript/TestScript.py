#executable path="D:\Python37/chromedriver.exe"
# from selenium.webdriver.common.by import By
from Action.re_charge import *
from Action.Login import *
from Util.Excel import *
from Util.FormatTime import *

dr = webdriver.Chrome()  #不能小写！！！！
dr.maximize_window()
dr.get("http://192.168.1.37:3000")
pe = parseExcel("E:\\PYwork\\PageObject\\TestData\\hoomtest.xlsx")
# time.sleep(2)
pe.set_sheet_by_index(0)
print(pe.get_default_sheet())

rows = pe.get_all_rows()[1:]
for id ,row in enumerate(rows):
    if row[3].value  == 'y':
        username = row[1].value
        password = row[2].value
        print(username,password)
        try:
            login(dr,username,password)
            pe.write_cell_content(id + 2, 5, "pass")
            pe.set_sheet_by_name(u"充值金额")
            rows1 = pe.get_all_rows()[1:]
            # print("rows1:", rows1)
            test_data_pass_flag =True  #结果表示，用于最后写入excel结果

            for id1, row in enumerate(rows1):
                if row[2].value == 'y':
                    try:
                        # print row[1].value,row[2].value,row[3].value,row[4].value,row[5].value
                        # print "execute1"
                        re_charge(dr,row[1].value)

                        pe.write_cell_content(id1+2,9,"pass")
                        pe.write_cell_content(id1+2,11,date_time())
                    except Exception as e1:
                        pe.write_cell_content(id1+2,10,"fail")
                        test_data_pass_flag = False  # 代码走到这里，说明有异常，测试失败
                        pe.write_cell_content(id1+2,9,date_time())
                else:
                    pe.write_cell_content(id1+2,10,u"忽略1")
                    continue
        except Exception as e2:
            pe.set_sheet_by_index(0)
            pe.write_cell_content(id+2,5,"fail")
            time.sleep(2)
            dr.quit()
    else:
        pe.set_sheet_by_index(0)
        pe.write_cell_content(id+2,5,u"忽略2")
        continue


# login(dr, "17200010005", "1234qwer")
# re_charge(dr,300)
# # time.sleep(2)
# dr.quit()








#
# # lp = LoginPage(dr)
# wait = WebDriverWait(dr, 10, 0.5)  # 显示等待
#
# try:
#     lp = LoginPage(dr)
#     lp.login()
#     ab = RechargePage(dr)
#     ab.rechage()
#     # log_in = wait.until(lambda x: x.find_element_by_css_selector('.header-reg-btn.header-login'))
#     # log_in.click()
#     # nam = wait.until(lambda x:x.find_element_by_css_selector('#J_username'))
#     # nam.send_keys('17200010005')
#     # pwd = wait.until(lambda x: x.find_element_by_css_selector('#J_pwd'))
#     # pwd.send_keys('1234qwer')
#     # sub = wait.until(lambda x: x.find_element_by_id('J_submit-login'))
#     # sub.click()
#     # time.sleep(2)
#     # mycount = wait.until(lambda x:x.find_element_by_css_selector('.last-nav>a'))
#     # mycount.click()
#     # time.sleep(2)
#     # recharge_button = wait.until(lambda x:x.find_element_by_css_selector('.uc-home-recharge'))
#     # recharge_button.click()
#     #
#     # recharge_put =  wait.until(lambda x: x.find_element_by_css_selector('#J_quickpay-amount'))
#     # recharge_put.send_keys(100)
#     #
#     # recharge_sub = wait.until(lambda x:x.find_element_by_css_selector('#J_quickpay-btn'))
#     # recharge_sub.click()
#     # time.sleep(2)
#     #
#     # recharge_verify = wait.until(lambda x: x.find_element_by_css_selector('#J_verifycode'))
#     # recharge_verify.click()
#     # time.sleep(2)
#
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
# finally:
#     dr.quit()