from selenium import webdriver
import time

driver = webdriver.Edge()
driver.get("hhttps://www.bing.com/")
driver.maximize_window()
driver.minimize_window()
time.sleep(8)
actual_title = driver.title
expect_title = "Bing"

if actual_title == expect_title:
    print("Title is verified")
else:
    print("Title is not verified")
driver.quit()