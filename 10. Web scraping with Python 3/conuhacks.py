#! https://www.browserstack.com/guide/python-selenium-to-run-web-automation-
#https://www.guru99.com/accessing-forms-in-webdriver.html
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


from selenium.webdriver.remote.webelement import WebElement

driver=webdriver.Chrome(executable_path=r"D:\Personnel\Other learning\Programming\_1_Computer Science\0. Python3\2. Cool Projects\10. Web scraping with Python 3\chromedriver_win32\chromedriver.exe")

driver.get("https://conuhacks.io/challenges/6378")
# get_status(driver)
# WebElement answer = driver.findElement(By.name("answer"))
WebElement element = driver.findElement(By.name("answer"))

# for i in range(0,6378):
    # element.sendKeys(str(i))
