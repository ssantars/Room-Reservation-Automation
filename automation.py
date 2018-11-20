import time
from datetime import date
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

GATEWAY_ROOM_NUM = ["2101", "2102", "2103", "2104", "2105",
                    "2106", "2107", "2110", "2111", "2112",
                    "2113"]
WEEKDAY = ["Monday", "Tuesday", "Wednesday",
           "Thursday", "Friday", "Saturday",
           "Sunday"]
MONTH = ["January", "February", "March", "April", "May",
         "June", "July", "August", "September", "October",
         "November", "December"]


def reservation_date(date):
    weekday = WEEKDAY[my_date.weekday()]
    month = MONTH[my_date.month - 1]

    reservation = weekday + ", " + month + " " + str(date.day) + ", " + str(date.year)
    return reservation


def set_date(des_date):
    if des_date:
        x = des_date.split("-")
        my_date = date(int(x[0]), int(x[1]), int(x[2]))
    else:
        my_date = date.today()

    return my_date


def reservation_time(start, t1, end, t2):
    x = start.split(":")
    start_time = int(x[0] + x[1])

    if t1 == "pm":
        start_time += 1200

    y = end.split(":")
    end_time = int(y[0] + y[1])

    if t2 == "pm":
        end_time += 1200

    res_time = []
    for z in range (start_time, (end_time + 50), 50):
        res_time.append(z)

    return res_time


def time_format(res_time):
    time_interval = []
    for r_time in res_time:
        period = "am"
        if r_time > 1200:
            r_time -= 1200
            period = "pm"
        time_list = list(str(r_time))

        if r_time >= 1000:
            hour = (time_list[0] + time_list[1])
            minutes = int(time_list[2] + time_list[3])
        else:
            hour = (time_list[0])
            minutes = int(time_list[1] + time_list[2])

        if minutes != 0:
            mins = "30"
        else:
            mins = "00"

        time_str = hour + ":" + mins + period
        time_interval.append(time_str)

    return time_interval


def find_reservation(time_interval, reservation, driver):
    test = []
    for x in range(0, len(GATEWAY_ROOM_NUM), 1):
        for y in range(0, 4, 1):
            print(x)
            title = "Gateway " + GATEWAY_ROOM_NUM[x] + ", " + time_interval[y] + " to " + time_interval[y + 1] + ", " \
                    + reservation
            test.append(title)

        res = find_res(test, driver)
        if res:
                for z in res:
                    z.click()
                return True
        else:
            test.clear()
    return False


def find_res(titles, driver):
    elements_list = []
    for x in range(0, 4, 1):
        try:
            reservation = driver.find_element_by_xpath("//a[@title='"+titles[x]+"']")
            elements_list.append(reservation)
        except NoSuchElementException:
            return None

    return elements_list


#start = input("From: ")
#t1 = input("am or pm: ")

#end = input("To: ")
#t2 = input("am or pm: ")

#des_date = input("Choose a date: ")
des_date = "2018-11-21"

start = "3:00"
t1 = "pm"
end = "5:00"
t2 = "pm"



driver = webdriver.Chrome("C:\Program Files\Python37\Selenium\chromedriver.exe")
driver.get("https://spaces.lib.uci.edu/booking/Gateway")

input_month = "10"
input_day = "21"
time_range = [9, 11]
user_name = ""
password = ""

my_date = set_date(des_date)
print(my_date)

reservation = reservation_date(my_date)
res_time = reservation_time(start, t1, end, t2)
time_interval = time_format(res_time)
print(res_time)
print(time_interval)

time.sleep(5)
month = Select(driver.find_element_by_xpath("//select[@class='ui-datepicker-month']"))
month.select_by_value(input_month)

date = driver.find_element_by_xpath("//a[text()='"+input_day+"']")
date.click()

time.sleep(5)
if find_reservation(time_interval, reservation, driver):
    print("IT WORKED")

submit = driver.find_element_by_xpath("//*[@id='s-lc-rm-sub']")
submit.click()


time.sleep(3)
uci_id_login = driver.find_element_by_xpath("//input[@id='ucinetid']")
uci_id_login.send_keys(str(user_name))
time.sleep(1)
uci_pass_login = driver.find_element_by_xpath("//input[@id='password']")
uci_pass_login.send_keys(str(password))

time.sleep(1)
login = driver.find_element_by_xpath("//input[@type='submit' and @value = 'Login']")
login.click()

time.sleep(2)
num_students = driver.find_element_by_xpath("//input[@type='radio' and @value = '6-9']")
num_students.click()

time.sleep(2)
affiliation = driver.find_element_by_xpath("//input[@type='radio' and @value = 'Undergrad']")
affiliation.click()

time.sleep(2)
purpose = driver.find_element_by_xpath("//input[@type='checkbox' and @value = 'Group Work']")
purpose.click()

time.sleep(2)
booking = driver.find_element_by_xpath("//*[@id='s-lc-rm-sub']")
booking.click()