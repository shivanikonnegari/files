from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://demo-opencart.com/index.php?route=account/login&language=en-gb")
driver.maximize_window()
driver.minimize_window()
time.sleep(8)
actual_title = driver.title
expect_title = "Account Login"

if actual_title == expect_title:
    print("Title is matched")
else:
    print("Title is not matched")
    driver.quit()