from selenium import webdriver
import time

driver = webdriver.Edge()
driver.get("https://www.freecrm.com/")
driver.maximize_window()

time.sleep(8)
actual_title = driver.title
expect_title = "Cogmento Free CRM with AI Customer Relationship Management"

if actual_title == expect_title:
    print("Title is verified")
else:
    print("Title is not verified")
    driver.quit()