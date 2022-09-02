# To Learn Mouse handling in selenium using Action chains.
#     1. Mouse operations:
#              1. Hover option
#              2. Right-Click option
#              3. Double-Click option.
#              4. Drag and drop option.
#     2. Using the sliders in webpage. (x-axes)
#     3. Using the scroll pane in webpage.
#           ~ Top navigation
#           ~ Bottom navigation.
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("D:\Drivers\chromedriver_win32\chromedriver.exe")
act = ActionChains(driver)

#                           #Mouse Hover demonstration over cart page.
driver.get("http://automationpractice.com/index.php")
driver.find_element(By.XPATH, "//span[text()='Add to cart']").click()
time.sleep(3)
cart = driver.find_element(By.XPATH, "//a[@title='View my shopping cart']")
act.move_to_element(cart).click().perform()

#                                  #Implementing Right click option
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
button = driver.find_element(By.XPATH, "//span[text()= 'right click me']")
act.context_click(button).perform()
driver.find_element(By.XPATH, "//li[@class='context-menu-item context-menu-icon context-menu-icon-quit']").click()
driver.switch_to.alert.accept()

#                                  #Implementing Double click option
driver.get("https://mousetester.com/")
click_element = driver.find_element(By.ID, "clickMe")
act.double_click(click_element).perform()
act.double_click(click_element).perform()
act.double_click(click_element).perform()
NoOfDoubleClicks = driver.find_element(By.XPATH, "//span[@id='button_0_double']").text
print(NoOfDoubleClicks)

#                                #Mouse: Drag and drop Implementation.
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
capital_list = ['Rome', 'Oslo', 'Madrid', 'Stockholm', 'Washington', 'Copenhagen', 'Seoul']
Country_list = ['Italy', 'Norway', 'Spain', 'Sweden', 'United States', 'Denmark', 'South Korea']

for ind in range(0, len(capital_list)):
    cap = capital_list[ind]
    coun = Country_list[ind]
    sourceEle = driver.find_element(By.XPATH, "//*[text()='"+cap+"' ][2]")
    TargetEle = driver.find_element(By.XPATH, "//*[text()='"+coun+"' ]")
    act.drag_and_drop(sourceEle, TargetEle).perform()
    time.sleep(2)
driver.close()

#                                      # Implement x-axis slider access.
driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")
start = driver.find_element(By.XPATH, "//*[@id='slider-range']/span[1]")
end = driver.find_element(By.XPATH, "//*[@id='slider-range']/span[2]")
print(start.location)
print(end.location)
act.drag_and_drop_by_offset(start, 100, 0).perform()
time.sleep(3)
act.drag_and_drop_by_offset(end, -112, 0).perform()
time.sleep(3)
print(start.location)
print(end.location)

#                             # Implementing Scroll option in webpage
driver.get('https://www.countries-ofthe-world.com/flags-of-the-world.html')
driver.maximize_window()
#                                # Scroll in yaxis with given pixel
driver.execute_script("window.scrollBy(0,3000)", "")
value = driver.execute_script("return window.pageYOffset;")
print(value)

#                     # Implementing Scroll until getting the desired element
indFlag = driver.find_element(By.XPATH, "//img[@alt= 'Flag of India']")
driver.execute_script("arguments[0].scrollIntoView();", indFlag)
value = driver.execute_script("return window.pageYOffset;")
print(value)
time.sleep(3)

#                          # Implementing scroll until end of page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset")
print(value)
time.sleep(3)

#                          # Implementing scroll to top of page
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset")
print(value)
