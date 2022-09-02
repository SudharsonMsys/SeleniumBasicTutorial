#                                    To Learn XPATH AXES.
# From a selective node we can traverse to intended element using the following axex.
#  Self ==> intended node to reach. Below is the AXES traverse used for reaching a web element from hierarchy.
#
#                                      1. Ancestor
#                                            |
#                                            |
#                          ----------------------------------------
#                          |                 |                    |
#                    2. Preceding             3.Parent           4. Following
#       ----------------------------------------------------------------------------------
#       |         | 6.Preceeding Sibling     |              | 7. Following Sibling        |
#    5. Preceeding Sibiling                "Self"                                    Following Sibling.
#                                            |
#       -----------------------------------------------------------------------------------
#       |                      |             |                         |                  |
#       9. Child           10.Child        11.Child               12. Child            13. Child
#                              |             |                                             |
#                     -----------------    16. Descendant                         ------------------
#                     |               |                                           |                 |
#                    14. Descendant  15. Descendant                              17. Descendant   18. Descendant
#
#
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome("D:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get('https://www.orangehrm.com/')
driver.refresh()  # To refresh the web page. Shortcut to avoid notifications before page load.
driver.maximize_window()

# Self Value
self_value = driver.find_element(By.XPATH, "//button[contains(text(),'Try it for Free') and @id='linkadd']/self::button").text
print(self_value)

# Parent Value
parent_value = driver.find_element(By.XPATH, "//button[contains(text(),'Try it for Free') and @id='linkadd']/parent::div").text
print(parent_value)

# Ancestor Value
noOfChild = driver.find_elements(By.XPATH,"//button[contains(text(),'Try it for Free') and @id='linkadd']/self::button/ancestor::form/child::div")
print(len(noOfChild))
val = driver.find_element(By.XPATH,"//button[contains(text(),'Try it for Free') and @id='linkadd']/ancestor::form").text
print(val)

# Descendant
driver.get('https://opensource-demo.orangehrmlive.com/index.php/auth/login')
desc_count = driver.find_elements(By.XPATH, "//*[@id='txtUsername']/ancestor::form/descendant::*")
print(len(desc_count))

# Following
driver.get('https://opensource-demo.orangehrmlive.com/index.php/auth/login')
Fol_count = driver.find_elements(By.XPATH, "//*[@id='txtUsername']/ancestor::form/following::*")
print(len(Fol_count))

# Preceding
driver.get('https://opensource-demo.orangehrmlive.com/index.php/auth/login')
prd_count = driver.find_elements(By.XPATH, "//*[@id='txtUsername']/ancestor::form/following::*")
print(len(prd_count))