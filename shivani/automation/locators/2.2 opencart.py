from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.opencart.com/index.php?route=account/login")
driver.maximize_window()
time.sleep(20)

edit_box=driver.find_element(By.ID,"input-email")
edit_box.send_keys("shivanireddykonnegari@gmail.com")
edit_box.send_keys("Keys.RETURN")

edit_box=driver.find_element(By.NAME,"password")
edit_box.send_keys("Shiv@ni032002")
edit_box.send_keys("Keys.RETURN")
time.sleep(9)
