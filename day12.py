#           #To learn Keyboard operation in Webpage and document upload using Selenium.
#  With Action chain and perform() method we can utilize the keyboard shortcuts in a webpage.
#  In the below example we did the following steps.
#           1. Input the text "Welcome to Selenium" in first box.
#           2. Select the text using shortcut key (ctrl+a) via selenium.
#           3. Copy the text using shortcut key (ctrl+c) via selenium.
#           4. Press the tab key using shortcut key (TAB) via selenium.
#           5. paste the text using shortcut key (ctrl+v) via selenium in 2nd text box.
#  Upload a document from local to webPage using selenium.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("D:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://text-compare.com/")
#                          # Copy and pasting Text element using keyboar shortcuts.
driver.maximize_window()
txt1 = driver.find_element(By.ID, "inputText1")
txt2 = driver.find_element(By.ID, "inputText2")
txt1.clear()
txt1.send_keys("Welcome to Selenium")
#                               # Intiating the Action Chain.
act = ActionChains(driver)

#                               # ctrl+a, "Select all step"
act.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()

#                               # ctrl+c, "Copy text step"
act.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()

#                               # Tab key, "to press tab key"
act.key_down(Keys.TAB)

#                               # ctrl+v, "To paste the text in text box"
act.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

#                              # Document Upload in webpage.
driver.get("https://www.monsterindia.com/")
driver.find_element(By.XPATH, "//a[@class='btn block resume-btn btn-orange mt20']").click()
time.sleep(3)
driver.find_element(By.ID, "file-upload").send_keys("D:\EmpytDoctoUpload.txt")
