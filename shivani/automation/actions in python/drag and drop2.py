from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(5)
element = driver.find_element(By.XPATH,"//*[@id='HTML2']/h2")


fromElement =  driver.find_element(By.XPATH,"//*[@id='draggable']/p")
toElement = driver.find_element(By.XPATH,"//*[@id='droppable']")

try:
    actions = ActionChains(driver)
    actions.drag_and_drop(fromElement,toElement).perform()
    print("drag and drop Element successfull")
except:
    print("drag and drop Element failed")
