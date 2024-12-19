from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='header']/div[2]/div/div/nav/div[1]/a").click()
time.sleep(4)
driver.find_element(By.ID,"email").send_keys("Shivanireddykonnegari@gmail.com")
driver.find_element(By.NAME, "passwd").send_keys("Shiv@ni032002")
driver.find_element(By.XPATH,"//*[@id='SubmitLogin']/span" ).click()
time.sleep(5)

driver.find_element(By.XPATH,"//*[@id='block_top_menu']/ul/li[2]/a" ).click()
driver.find_element(By.XPATH,"//*[@id='columns']/div[1]/span[2]/span[1]/a" ).click()
time.sleep(3)
driver.quit()

