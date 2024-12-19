from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.letskodeit.com/login")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.ID, "email").send_keys("shivanireddykonnegari@gmail.com")
driver.find_element(By.NAME,"password").send_keys("Shiv@ni032002")
driver.find_element(By.XPATH,"html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/form[1]/div[5]/div[1]/button[1]")
time.sleep(9)
