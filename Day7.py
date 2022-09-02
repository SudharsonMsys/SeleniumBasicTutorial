#                             Following are covered here.
#                           1. Handling Checkboxes in webpage.
#                           2. Handling Links in various situation:
#                               1. Internal Link
#                               2. External Link
#                               3. Broken Link
#                           3.  Handling Dropdown.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import requests


driver = webdriver.Chrome("D:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://itera-qa.azurewebsites.net/home/automation")

#                                               Check Box Testings.
# To Select all Weekday check boxes.

# list of check box elements.
chkbox_list = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id, 'day')]")
# To select all the checkboxes.
# Method1:
for chkbox in chkbox_list:
    chkbox.click()

# Method2: Uncheck only the selected box
time.sleep(3)
for chkbox in chkbox_list:
    if chkbox.is_selected():
        chkbox.click()
time.sleep(3)

# Method3: Select only specific date based on conditions
for chkbox in chkbox_list:
    if chkbox.get_attribute('id') == 'monday' or chkbox.get_attribute('id') == 'sunday':
        chkbox.click()

#                   Links Testings: 1.Internal Link , 2. External Link, 3. Broken Link.
#                           Links in page can be collectively get via tag 'a'.

driver.get("https://demo.nopcommerce.com/")
# To click a single  link, use href text, using Link_Text.
driver.find_element(By.LINK_TEXT, "Digital downloads").click()

# using partial link text.
driver.find_element(By.PARTIAL_LINK_TEXT, 'Gift').click()

# To get number of links in the page
link_list = driver.find_elements(By.XPATH, '//a')
print("Number of links in the page", len(link_list))

# To get and handle the broken link
driver.get("http://www.deadlinkcity.com/")
li_list = driver.find_elements(By.XPATH, '//a')
brokenLinkCount = 0
for links in li_list:
    url = links.get_attribute('href')
    try:
        res = requests.head(url)
    except:
        None

    if res.status_code >= 400:
        print("The link is broken", url)
        brokenLinkCount += 1
print("No of broken Link", brokenLinkCount)

#                                           Dropdown Testing
driver.get("https://www.opencart.com/index.php?route=account/register")
dd = Select(driver.find_element(By.ID, 'input-country'))

#                                    # Method1: Using the visible text
dd.select_by_visible_text('Aruba')
time.sleep(3)

#                                     # Method 2, using Index
dd.select_by_index(3)
time.sleep(3)

#                                      # Method 3, using option value
dd.select_by_value('10')
time.sleep(3)
