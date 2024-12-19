from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://auth.hollandandbarrett.com/u/login")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.ID, "username").send_keys("shivanireddykonnegari@gmail.com")
driver.find_element(By.NAME,"password").send_keys("Shiv@ni032002")
time.sleep(5)
