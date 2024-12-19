from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.spicejet.com/")
driver.maximize_window()
time.sleep(5)

driver.execute_script("window.scrollBy(0,5000);")
time.sleep(5)
driver.execute_script("window.scrollBy(0,-5000);")
time.sleep(5)

element = driver.find_element(By.XPATH,"//div[@class='css-76zvg2 r-c20mna r-yy2aun r-1kfrs79 r-1h0z5md r-lgpkq'][normalize-space()='Cargo']")
driver.execute_script("arguments[0].scrollIntoView(true);",element)
time.sleep(5)

driver.find_element(By.XPATH,"/html[1]/body[1]/div[2]/div[1]/div[1]/div[1]/div[13]/div[1]/div[1]/div[1]/div[2]/div[4]/div[1]").click()
time.sleep(5)
