#                                       # Handle Date Picker.
#                                   1. selecting date using send_keys() method. 
#                                   2. selecting date using the navigation tab in webpage.
#                                   3. selecting date using send_keys() method.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome("D:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://jqueryui.com/datepicker/")
#                                      # send keys method.
driver.switch_to.frame(0)
driver.find_element(By.ID, "datepicker").send_keys("08/24/2022")

#               #Select with Month and year using navigation button and then selecting date.
driver.switch_to.default_content()
driver.get("https://jqueryui.com/datepicker/")
driver.refresh()
driver.switch_to.frame(0)
driver.find_element(By.ID, "datepicker").click()
Yr = "2023"
Mon = "March"
date = "14"

#                                   # selecting year and Month
#            # Until the intended year and month reached, the code will click the navigation button.

while True:
    year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text
    month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    if year == Yr and month == Mon:
        break
    else:
        driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click()

#                                           selecting date.
dateElements = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']//tr//td")
for ele in dateElements:
    if ele.text == date:
        ele.click()

#                      #select year and month using dropdown and then select date.
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
driver.find_element(By.ID, "dob").click()
month_select = Select(driver.find_element(By.XPATH, "//select[@class='ui-datepicker-month']"))
month_select.select_by_visible_text("Mar")

year_select = Select(driver.find_element(By.XPATH, "//select[@class='ui-datepicker-year']"))
year_select.select_by_value("1991")

date_table = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']//tr/td")

for date in date_table:
    if date.text == '14':
        print(date.text)
        date.click()
        time.sleep(5)
driver.close()
