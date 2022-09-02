# To learn the following things as part of selenium.
# use maximize _window() method to maximize the browser windows.
# Next three methods to find web element in webpage.
# 1. Finding element using the LINK_TEXT
# 2. Finding element using  PARTIAL_LINK_TEXT
# 3. Finding element using  CSS_SELECTOR , it has four different Combination to fetch a element.
#      # Note:  Tag is always optional.
#      1. Using Tag and ID, '#' is to represent ID
#      2. Using Tag, Class and Attribute. '.' to represent class, attribute should be provided between '[]'.
#      3. Using Tag and Class
#      4. Using Tag and attribute.


from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome("D:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get('http://automationpractice.com')
# Method to maximize the browser window.
driver.maximize_window()

# get element by link text
driver.find_element(By.LINK_TEXT, 'Contact us')  # Provided full text.

# Full Text is "Sign in"
driver.find_element(By.PARTIAL_LINK_TEXT, 'Sign')  # provided partial text from "Sign In"

# Highlight the logo
driver.find_element(By.CLASS_NAME, 'logo')

# Finding Number of links in the page
links = driver.find_elements(By.TAG_NAME, 'a')
print(len(links))

# CSS Selectors Example:
# Tag and ID
driver.find_element(By.CSS_SELECTOR, 'input#search_query_top').send_keys('Printed Dress')

# Tag class and Attribute
driver.find_element(By.CSS_SELECTOR, "button.btn[type=submit]").click()

# Tag and Class
driver.find_element(By.CSS_SELECTOR, 'select.selectProductSort').click()

# Tag and Attribute
driver.find_element(By.CSS_SELECTOR, "a[rel=nofollow]").click()
driver.close()
