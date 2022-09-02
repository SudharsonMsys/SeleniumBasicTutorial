#  To learn handling alerts in a webpage.
#        1. Alert1 : using accept() method.
#        2. Alert2 : using accept() or dismiss() method.
#        3. Alert3 : Text prompt using accept() or dismiss() method.
#  To handle server level authentication pop-up. Not normal login test.
#  To handle Frames:
#            1. Handling single frame.
#            2. Switching between different frames in a webpage. (Inner frames and Outer Frames)
#               Note: In case of layer of frames, everytime we need to traverse to outer frame to
#                     switch to another frame. Directly move between diff inner frames.
#  To handle Multiple browser instances.
#            1. Using Browser Ids.
#            2. Using Browser Title.

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome("D:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

#                                      #  Alert1: Only Accept.
driver.find_element(By.XPATH, "//button[@onclick='jsAlert()']").click()
myalert = driver.switch_to.alert
print(myalert.text)
myalert.accept()

#                                       Alert2: Either Accept or Dismiss
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']").click()
myalert2 = driver.switch_to.alert
print(myalert2.text)
#                                             # accepting the alert.
myalert2.accept()
#
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']").click()
myalert2 = driver.switch_to.alert
#                                             # dismissing the alert.
myalert2.dismiss()

#                               Alert3: Text prompt with accept and Dismiss
#                                       Accepting with text.
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']").click()
myalert3 = driver.switch_to.alert
myalert.send_keys("Welcome")
myalert.accept()
#                                        Dismissing the alert.
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(By.XPATH, "//button[@onclick='jsPrompt()']").click()
myalert3 = driver.switch_to.alert
myalert3.dismiss()

#                                         Authentication POP up.
driver.get("https://the-internet.herokuapp.com/basic_auth")
#                                   Injecting username and password.
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")

#                                #Switching between Multiple Frames
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
driver.switch_to.frame("packageListFrame")
driver.find_element(By.LINK_TEXT, "org.openqa.selenium").click()
driver.switch_to.default_content()

driver.switch_to.frame("packageFrame")
driver.find_element(By.LINK_TEXT, "WebDriver").click()
driver.switch_to.default_content()

driver.switch_to.frame("classFrame")
driver.find_element(By.XPATH, "/html/body/header/nav/div[1]/div[1]/ul/li[8]").click()

#                          #Dealing with Inner frames and Outer Frames
driver.get("https://demo.automationtesting.in/Frames.html")
driver.find_element(By.XPATH, "/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[2]/a").click()
outerFrame = driver.find_element(By.XPATH, "//*[@id='Multiple']/iframe")
driver.switch_to.frame(outerFrame)
innerFrame = driver.find_element(By.XPATH, "/html/body/section/div/div/iframe")
driver.switch_to.frame(innerFrame)
driver.find_element(By.XPATH, "//input[@type='text']").send_keys("End of Frames")

#                              #Switch between Multiple Browser Windows
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(30)
secElement = driver.find_element(By.XPATH, "//a[normalize-space()='OrangeHRM, Inc']").click()
#                               # To get list of Browser Ids
ListOfBrowserIDs = driver.window_handles

#     Switch between browsers using ids and close desired browsers by comparing with title of the pages.
for ids in ListOfBrowserIDs:
    driver.switch_to.window(ids)
    if driver.title == "OrangeHRM":
        driver.close()
time.sleep(5)
print("Reached here")
