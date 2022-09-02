# Following are to be learnt in selenium.
#     1. Handling different type of Dropdown without using select method.
#     2. To take screenshot of a webpage.
#     3. Regarding New tab and New windows in browser.
#             1. opening URL in new Tab and switch .
#             2. opening URL in new Window and switch
#     4. To handle the cookies.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
driver = webdriver.Chrome("D:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

#                             #Handling different type of dropdown.
driver.find_element(By.XPATH, "//span[@id='select2-billing_country-container']").click()
countryListElements = driver.find_elements(By.XPATH, "//span[@class='select2-results']//li")
countriesCount = len(countryListElements)
print(countriesCount)

# To select a specific country (India).
for ele in countryListElements:
    if ele.text  == "India":
        ele.click()
        break

#                                       To take screenshot of a page
driver.get("https://demo.nopcommerce.com/")
driver.save_screenshot(os.getcwd()+"//sample.png")
driver.find_element(By.XPATH, "//ul[@class='top-menu notmobile']//a[normalize-space()='Digital downloads']").click()
driver.get_screenshot_as_file(os.getcwd()+"//sample1.png")

#                              # Open url in separate browser
driver.get("https://demo.nopcommerce.com/")
keyCombination1 = Keys.CONTROL+Keys.RETURN
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//a[@class='ico-register']").send_keys(keyCombination1)

#                               # Opening to newTab and switch
driver.get("https://demo.nopcommerce.com/")
driver.switch_to.new_window('tab')
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

#                              # Opening to new-window and switch
driver.get("https://demo.nopcommerce.com/")
driver.switch_to.new_window('window')
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

#                              # Working on cookies of a website.
driver.get("https://demo.nopcommerce.com/")
cookiesDetails = driver.get_cookies()
print("Length of cookies", len(cookiesDetails))
for cook in cookiesDetails:
    print(cook)

driver.add_cookie({"name": "shiva", "value": "31"})
cookiesDetails = driver.get_cookies()
for cook in cookiesDetails:
    print(cook)
print("Length of cookies after addition", len(cookiesDetails))

driver.delete_cookie('shiva')
cookiesDetails = driver.get_cookies()
print("Length of cookies after deletion", len(cookiesDetails))

driver.delete_all_cookies()
cookiesDetails = driver.get_cookies()
print("Length of cookies after deletion", len(cookiesDetails))
