#                         # This tutorial concludes the data driven way of automating a scene.
#   As a part of the Scenario we are doing the following steps.
#   1. Opening a XL book with Simple Instruction calculation details.
#   2. Using selenium input that data into online SI calculator.
#   3. Store the result in book and compare with benchmark values.
#   4. If the comparission passed, pass the test case and highlight the cell in green color.
#   4. If the comparission failed, fail the test case and highlight the cell in red color.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from PyXlUtil import *
import time

file = "D:\SeleniumVideosCode\TextXLBook.xlsx"
writeFile = "D:\SeleniumVideosCode\WriteFile.xlsx"
#                                      # To open a XL sheet.
workbook = openpyxl.load_workbook(file)
writeworkbook = openpyxl.load_workbook(writeFile)
#                                      # To switch to correct Page in the workbook.
sheet = workbook['Sheet1']
writesheet = writeworkbook['Sheet1']

#                                # Get number of rows in XL sheet.
NoOfRows = sheet.max_row
#                                # Get number of column in XL sheet.
NoOfColumns = sheet.max_column

for i in range(1, NoOfRows+1):
    for j in range(1, NoOfColumns+1):
        print(sheet.cell(i, j).value, end='  ')
#                                             # writing data into a cell
        writesheet.cell(i, j).value = sheet.cell(i, j).value
    writeworkbook.save(writeFile)
    print()

driver = webdriver.Chrome("D:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/"
           + "fixed-deposit-calculator-SBI-BSB001.html?classic=true")
driver.maximize_window()
driver.refresh()
time.sleep(3)

file = "D:\SeleniumVideosCode\TextXLBook.xlsx"
workbook = openpyxl.load_workbook(file)
sheet = 'Sheet1'

noofrows = rowcount(file, sheet)
noofcolumns = columncount(file, sheet)


for row in range(2, noofrows+1):
    # read from Excel file.
    principle = readdata(file, sheet, row, 1)
    ROI = readdata(file, sheet, row, 2)
    duration = readdata(file, sheet, row, 3)
    frequency = readdata(file, sheet, row, 4)
    term = readdata(file, sheet, row, 5)
    maturity = readdata(file, sheet, row, 6)
    print()

    # Enter data in the calc.
    driver.find_element(By.XPATH, "//input[@id='principal']").send_keys(principle)
    driver.find_element(By.XPATH, "//input[@id='interest']").send_keys(ROI)
    driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(duration)
    ymddropdown = Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']"))
    ymddropdown.select_by_visible_text(frequency)
    frequencydropdown = Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
    frequencydropdown.select_by_visible_text(term)
    driver.find_element(By.XPATH, "//div[@class='CTR PT15']//img").click()

    #  Update the xl sheet with result.
    result = driver.find_element(By.XPATH, "//span[@class='gL_27']/strong").text
    if float(maturity) == float(result):
        writedata(file, sheet, row, 8, "Passed")
        fillgreencolor(file, sheet, row, 8)
    else:
        writedata(file, sheet, row, 8, "Failed")
        fillredcolor(file, sheet, row, 8)
    driver.find_element(By.XPATH, "//img[@class='PL5']").click()

# To close the browser instance.
driver.quit()
