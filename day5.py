#               Learning different methods to interact with webelements.
#     Get-methods :
#                 1.Title : To get title of the page.
#                 2.Curr_url: To get the current url of the webpage.
#                 3.Page-source: To fetch the page-source of a webpage.
#     Conditional-methods:
#                 1. is_selected() : To see if a checkbox or radio button was selected.
#                 2. is_enabled()  : To see if a
#                 3. is_displayed()
#     Difference between find_element() and find_elements().
#     Handling No elements in the webpage.
#     Text Vs Get-Attribute
#
#
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome("D:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get('https://opensource-demo.orangehrmlive.com/index.php/auth/login')

# Title
if driver.title == 'OrangeHRM':
    print("Test case Passed")
else:
    print("Test case Failed")

# Current URL
curr_url = driver.current_url
print("Current Website URL is", curr_url)

# Page_Source
page_source = driver.page_source
print("HTML Source Code", page_source)

# BrowserCommand: Close() - close the single instance of browser, which is currently in progress.
driver.close()


#Conditional Commands: is_selected(), is_enabled(), is_displayed()
driver.get('https://opensource-demo.orangehrmlive.com/index.php/auth/login')
userbox = driver.find_element(By.XPATH, "//*[@id='txtUsername']")
passbox = driver.find_element(By.XPATH, "//*[@id='txtPassword']")

#                                      is_displayed command
print("Expected True for Username box", userbox.is_displayed())
print("Expected True for Password box", passbox.is_displayed())

#                                       is_enabled command
print("Expected True for Username box", userbox.is_enabled())
if userbox.is_enabled():
    userbox.send_keys('Admin')

print("Expected True for Password box", passbox.is_displayed())
if passbox.is_enabled():
    passbox.send_keys('admin123')

driver.find_element(By.XPATH, "//*[@id='btnLogin']").click()
driver.find_element(By.XPATH, "//*[@id='menu_pim_viewPimModule']/b").click()


#                                    is_selected
chkBox = driver.find_element(By.XPATH, "//*[@id='ohrmList_chkSelectAll']")
print("Expected False for this condition", chkBox.is_selected())
time.sleep(3)
chkBox.click()

print("Expected True for this condition", chkBox.is_selected())
time.sleep(3)

#                   # Difference between find_element and find_elements

# Locator Matching with Single Element demo.
driver.get('https://demo.nopcommerce.com/')

# # Find element - deals with single element , will return a single web element

driver.find_element(By.XPATH, "//*[@id='small-searchterms']").send_keys("Iphone 7")
driver.find_element(By.XPATH, "//*[@id='small-searchterms']").clear()
searchboxList = driver.find_element(By.XPATH, "//div[@class='footer']//a")
print(searchboxList.text)

#                               Find element with no element in the page
# actual id is small-searchterms
# Since there is no element it will fail the test case with exception " No such elements"

driver.find_element(By.XPATH, "//*[@id='small-searchte']").send_keys("Iphone 7")

# Dealing with Multiple Webelements
# Find elements - will return a list of web elements , we need to index the right the element for processing.
# No exception in case no elements are returned.
searc_elements = driver.find_elements(By.XPATH, "//*[@id='small-searchterms']")
searc_elements[0].send_keys("Nokia 1100")

foot_elements = driver.find_elements(By.XPATH, "//div[@class='footer']//a")
print(len(foot_elements))

for ele in foot_elements:
    print(ele.text)

footer_elements = driver.find_elements(By.XPATH, "//div[@class='foter']//a")
print(len(footer_elements))

#                                            Text Vs Get-Attribute

# Example : <button type="submit" class="button-1 search-box-button">Search</button>
# 'Search' is called as inner text, the values between the tags, here the tag is button.

# Example :<input type="text" class="search-box-text ui-autocomplete-input" id="small-searchterms"
# autocomplete="off" name="q" placeholder="Search store" aria-label="Search store">
# the above html node has not inner text, so we cant use the '.text' method, instead you can use get_attribute(class),it
# will return 'button-1 search-box-button', to get any attribute value we can use it.

cls_attribute = driver.find_element(By.XPATH, "//*[@id='small-searchterms']").get_attribute('class')
print(cls_attribute)

inner_text = driver.find_element(By.XPATH, "//*[@id='small-search-box-form']/button").text
print(inner_text)