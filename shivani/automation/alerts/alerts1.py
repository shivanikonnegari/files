from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div[2]/form/div[1]/div[2]/div[2]/div[2]/div/input[2]").click()
time.sleep(5)
driver.switch_to.alert.accept()
time.sleep(5)