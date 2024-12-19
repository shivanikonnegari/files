from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://mybookings.easemytrip.com/MyBooking/MyLogin")
driver.maximize_window()
time.sleep(5)

driver.find_element(By.ID,"txtEmailNew").send_keys("shivanireddykonnegari@gmail.com")
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[4]/input[1]")
time.sleep(9)