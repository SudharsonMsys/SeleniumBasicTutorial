# This source code is to get familiar with Basic method to find the elements and interacting.
# 1. Id
# 2. Name
# 3. XPath
# 4. driver.title to verify title of the webpage.
# 5. send_keys method to send input.
# 6. click method to click buttons, checkbox & radio buttons.
# 7. clear() method to clear any pre-written text box to avoid over-writings.

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome("D:\Drivers\chromedriver_win32\chromedriver.exe")

                                        # OrangeHRMCode:

# Use Get method to open the expected URL.
driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")

# Find element using Id, and sending inputs through send_keys method.
driver.find_element(By.ID, "txtUsername").send_keys("Admin")

# Find element using Name
driver.find_element(By.NAME, "txtPassword").send_keys("admin123")

# Find element using Xpath, and click the intended button using click() method.
driver.find_element(By.XPATH, "//*[@id='btnLogin']").click()

# verifying whether the intended page got loaded, using the title of the web page.

# Method to verify the title of given page.
if driver.title == "OrangeHRM":
    print("Test case Passed")
else:
    print("Test Case Failed")

# To close the current browser instance.
driver.close()

                                         # AdminYourStore Code:
# Example using above tutorial.
driver.get("https://admin-demo.nopcommerce.com/login")

# Method to clear the hint text, in text box.
driver.find_element(By.ID, 'Email').clear()
driver.find_element(By.ID, 'Email').send_keys('admin@yourstore.com')
driver.find_element(By.NAME, 'Password').clear()
driver.find_element(By.NAME, 'Password').send_keys('admin')
driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button').click()

driver.close()
