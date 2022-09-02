#                                         Tables in Webpage.
#                 1. Fetching data from a Static Table.
#                 2. Fetching data from Dynamic Table.

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("D:\Drivers\chromedriver_win32\chromedriver.exe")
driver.implicitly_wait(30)
driver.get("https://testautomationpractice.blogspot.com/")

#                            # Getting Number of Rows in Book Table
NoOfRows = len(driver.find_elements(By.XPATH, "//table[@name = 'BookTable']//tr"))
print("No of rows in the table", NoOfRows)

#                            # Getting Number of Columns in Book Table
NoOfColumns = len(driver.find_elements(By.XPATH, "//table[@name = 'BookTable']//tr[1]/th"))
print("No of Column in the table", NoOfColumns)

#                            # Getting all data in the Book table
for rNO in range(2, NoOfRows+1):
    for cNO in range(1, NoOfColumns+1):
        data = driver.find_element(By.XPATH, "//table[@name = 'BookTable']//tr["+str(rNO)+"]/td["+str(cNO)+"]").text
        print(data, end="    ")
    print()

# Get Author "Mukesh" Books and its price.
for rNO in range(2, NoOfRows+1):
    # author column number  is # 2
    authorName = driver.find_element(By.XPATH, "//table[@name = 'BookTable']//tr["+str(rNO)+"]/td[2]").text
    Price = driver.find_element(By.XPATH, "//table[@name = 'BookTable']//tr["+str(rNO)+"]/td[4]").text
    BookName = driver.find_element(By.XPATH, "//table[@name = 'BookTable']//tr["+str(rNO)+"]/td[1]").text
    if authorName == 'Mukesh':
        print(authorName, "   ", BookName, "    ", Price)

#                                         Getting data from dynamic table.
driver.implicitly_wait(30)
driver.get("https://opensource-demo.orangehrmlive.com")
driver.maximize_window()
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@type='submit' and normalize-space()='Login']").click()

#                                Navigating Admin-->UserManagement-->Users
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a/span").click()
driver.find_element(By.XPATH, "//span[normalize-space()='User Management']").click()
driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li").click()

#                                         Getting the whole table data
NoOfRows = len(driver.find_elements(By.XPATH, "//*[@class='oxd-table-card']"))
print(NoOfRows)
NoOfColumn = len(driver.find_elements(By.XPATH, "//*[@class='oxd-table-card'][1]/div/div"))
print(NoOfColumn)
rows_data = driver.find_elements(By.XPATH, "//*[@class='oxd-table-card'][1]/div/div[2]")
for r in range(1, NoOfRows+1):
    for c in range(2, NoOfColumn):
        data = driver.find_element(By.XPATH, "//*[@class='oxd-table-card']["+str(r)+"]/div/div["+str(c)+"]").text
        print(data, end='    ')
    print()
count = 0

#                                         To find number of Enabled user
for r in range(1, NoOfRows+1):
    data = driver.find_element(By.XPATH, "//*[@class='oxd-table-card'][" + str(r) + "]/div/div[5]").text
    if data == "Enabled":
        count += 1

print("Total Number of user", NoOfRows)
print("No of enabled users", count)
print("No of Disabled users", NoOfRows-count)






