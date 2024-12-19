from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://www.automationpractice.pl/index.php?controller=my-account")
driver.maximize_window()
time.sleep(5)

edit_box=driver.find_element(By.ID,"email")
edit_box.send_keys("shivanireddykonnegari@gmail.com")
edit_box.send_keys("Keys.RETURN")

edit_box=driver.find_element(By.NAME, "passwd")
edit_box.send_keys("Shiv@ni032002")
edit_box.send_keys("Keys.RETURN")
time.sleep(9)