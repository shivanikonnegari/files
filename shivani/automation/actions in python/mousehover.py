from cffi.cffi_opcode import CLASS_NAME
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.rajasthanroyals.com/login")
driver.maximize_window()
time.sleep(5)
element = driver.find_element(By.CLASS_NAME,"nav-anchor")
itemToClickLocator = "//span[@class='nav-text'][contains(.,'Squad')]"

try:
    actions = ActionChains(driver)
    actions.move_to_element(element).perform()
    print("Mouse Handovered on 'squad' element")
    time.sleep(5)
    topLink = driver.find_element(By.XPATH,itemToClickLocator)
    actions.move_to_element(topLink).click().perform()
    
    print("Item clicked")
except:
    print("Mouse Hover failed on element")


