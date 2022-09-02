# Wait mechanism used in selenium.
# Python way - time.sleep(10s) - ADV: Easy to use
# Dis ADV: 1. Poor Performance of script, 2. If ele not within time frame it still throw exception.

# Implicit Wait: Adv : 1. Single Statement, 2. High Performance, will move to next statement if it find the ele before
# timeout.   DisAdv: Need explicit error handling if the ele not found even after the timeout.

# Explicit Wait: Adv: 1. Highly effective , allow polling inbetween timeout, handled exceptions by default.
# DisAdv: 1. Complex in usage, 2. Need to declare in more than place(Implicit is single declaration)


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

# simple Time sleep in python way
time.sleep(10)  # sleeps for 10s, allow time for the element to load, use in anywhere in the code.

#                                                    Implicit wait
driver = webdriver.Chrome("D:\Drivers\chromedriver_win32\chromedriver.exe")
driver.implicitly_wait(10)
# It will wait for 10 sec wherever we got any delay in finding the element.
driver.get("https://www.google.com")
search_element = driver.find_element(By.NAME, 'q')
search_element.send_keys("selenium")
search_element.submit()

# The single statement will run whenever there is delay in loading the element,Timeout = 10s.
driver.implicitly_wait(10)

#           Explicit wait:  we need to declared as many as time we needed, we can poll and handle exceptions.
mywait = WebDriverWait(driver, 10)

#                                    To add poll and Default Exceptions
mywait = WebDriverWait(driver, 10, ignored_exceptions=[NotImplementedError, OverflowError], poll_frequency=2)
# if we need a explicit wait inbetween code, use the below.
# newElement = mywait.until(EC.presence_of_element_located("xpath of a element"))
# newElement.click() # with the web element we can continue our process.

#                                               To use Explicit wait
sel_ele = mywait.until(EC.presence_of_element_located((By.XPATH, "//h3[text() = 'Selenium']")))



