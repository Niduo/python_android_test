import time
from datetime import timedelta,date

# def date_time_chinese():
#     print(u"returns the current time string,format for YYYY年mm月dd日HH时MM分SS秒")
#     return time.strftime("%Y 年 %m 月 %d 日 %H时%M分%S秒", time.localtime())
#
# def date_chinese():
#     print(u"returns the current time string, format for YYYY年mm月dd日")
#     return time.strftime("%Y年%m月%d日", time.localtime())
# def time_chinese():
#     print(u"returns the current time string,format for HH时 MM分 SS秒")
#     return time.strftime("%H时%M分%S秒", time.localtime())
def date_time():
    print("returns the current time string, format for YYYY-mm-dd HH:MM:SS")
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
def date_time_slash():
    print("returns the current time string,format for YYYY/mm/dd HH:MM:SS")
    return time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())
def dates():
    print("returns the current time string,format for YYYY-mm-dd")
    return time.strftime("%Y-%m-%d", time.localtime())
def date_slash():
    print("returns the current time string,format for YYYY/mm/dd")
    return time.strftime("%Y/%m/%d", time.localtime())
def times():
    print("returns the current time string, format for HH:MM:SS")
    return time.strftime("%H:%M:%S", time.localtime())
def year():
    print("returns the current time string,format for year")
    return time.strftime("%Y", time.localtime())
def month():
    print("returns the current time string,format for month")
    return time.strftime("%m", time.localtime())
def day():
    print("returns the current time string,format for day")
    return time.strftime("%d", time.localtime())
def hour():
    print("returns the current time string, format for Hour")
    return time.strftime("%H", time.localtime())
def minute():
    print("returns the current time string,format for minute")
    return time.strftime("%M", time.localtime())
def seconds():
    print("return the current time string,format for seconds")
    return time.strftime("%S", time.localtime())

def str_to_tuple(stime):
    print("returns the string variable into time tuples")
    return time.strptime(stime, "%Y-%m-%d %H:%M:%S")

def add_date(day_num):
    today = date.today()
    print("returns the current date-%s and a time interval-%s" % (today, day_num))
    timess = today + timedelta(days=day_num)
    return timess


def sub_date(day_num):
    today = date.today()
    print("returns the current date-%s minus one time interval-%s" % (today, day_num))
    timess = today - timedelta(days=day_num)
    return timess

if __name__ == '__main__':
    # 测试代码

    # print(date_time_chinese())
    # print(date_chinese())
    # print(time_chinese())
    print(date_time())
    print(date_time_slash())
    print(dates())
    print(date_slash())
    print(times())
    print(year())
    print(month())
    print(day())
    print(hour())
    print(minute())
    print(seconds())
    time1 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(str_to_tuple(time1))
    print(add_date(2))
    print(sub_date(2))
