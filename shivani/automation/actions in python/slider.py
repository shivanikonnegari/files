from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://jqueryui.com/slider/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.switch_to.frame(0)
element = driver.find_element(By.XPATH,"//*[@id='slider']/span")
try:
    actions = ActionChains(driver)
    actions.drag_and_drop_by_offset(element, "400" ,"0").perform()
    print("sliding element is successfull")
except:
    print("sliding element is failed")