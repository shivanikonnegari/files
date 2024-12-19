from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.login.hiox.com/login?referrer=easycalculation.com")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.ID, "log_email").send_keys("shivanireddykonnegari@gmail.com")
driver.find_element(By.NAME, "log_password").send_keys("Shivani032002")
driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/form[1]/div[4]/input[1]")
time.sleep(5)