from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/droppable/")
driver.maximize_window()
driver.implicitly_wait(5)

fromElement =  driver.find_element(By.XPATH,"//*[@id='draggable']")
toElement = driver.find_element(By.XPATH,"//*[@id='droppable']")

try:
    actions = ActionChains(driver)
    actions.drag_and_drop(fromElement,toElement).perform()
    print("drag and drop Element successfull")
except:
    print("drag and drop Element failed")