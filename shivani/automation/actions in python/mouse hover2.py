from cffi.cffi_opcode import CLASS_NAME
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.easycalculation.com/")
driver.maximize_window()
time.sleep(5)
element = driver.find_element(By.CLASS_NAME,"lang")
itemToClickLocator = "(//span[contains(.,'Deutschland')])[2]"
try:
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    print("Mouse Handovered on 'Deutschland' element")
    time.sleep(5)
    topLink = driver.find_element(By.XPATH,itemToClickLocator)
    actions.move_to_element(topLink).click().perform()
    print("Item clicked")
except:
    print("Mouse Hover failed on element")