#                                      To Learn Custom xPATH.
# One of the most important way of finding elements is XPATH. It represents path of the web element from
# head to intended element in the DOM structure.
# The complete path is called "Absolute XPATH", which is lengthy and not recommended all the time.
# The Customized XPATH is called as "Relative XPATH", Which provides different options to fetch a element.
#      1. XPATH with "and" & "or" method
#      2. XPATH with xpath using "starts-with" method
#      3. XPATH with "and" & "or" method
#      4. XPATH with text() method.
#      4. XPATH with contains() method.

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome("D:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get('http://automationpractice.com')

#                           xpath with "and" & "or" method.

# '''<input class="search_query form-control ac_input" type="text" id="search_query_top"
# name="search_query" placeholder="Search" value="" autocomplete="off">'''

driver.find_element(By.XPATH, "//input[@id='search_query_top' or @name='search_query']").send_keys("Dress")

# '''<button type="submit" name="submit_search" class="btn btn-default button-search">
# <span>Search</span>	</button>'''
#

driver.find_element(By.XPATH, "//button[@type='submit' and @name='submit_search']").click()

#                                  xpath using "starts-with and contains()"
driver.get('http://automationpractice.com')
driver.find_element(By.XPATH, "//input[contains(@id,'search_query_top')]").send_keys('chiffon')
driver.find_element(By.XPATH, "//button[starts-with(@name, 'submit_search')]").click()

#                                     xpath using "text()"
'''<a href="http://automationpractice.com/index.php?id_category=3&amp;controller=category" 
title="Women" class="sf-with-ul">Women</a>'''

driver.find_element(By.XPATH, "//a[text()='Women']").click()

# close the driver
driver.close()
