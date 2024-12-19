from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://admin:admin@the-internet.herokuapp.com/drag_and_drop")
driver.maximize_window()
time.sleep(5)

fromElement = driver.find_element(By.ID,"column-a")
toElement = driver.find_element(By.ID,"column-b")
time.sleep(5)

try:
    actions = ActionChains(driver)
    actions.drag_and_drop(fromElement,toElement).perform()
    time.sleep(5)
    actions.drag_and_drop(toElement,fromElement).perform()
    time.sleep(5)
    print("drag and drop Element successfull")
except:
    print("drag and drop Element failed")