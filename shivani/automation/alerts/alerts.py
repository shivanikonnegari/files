from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
time.sleep(5)
driver.find_element(By.XPATH,"(//button[normalize-space()='Click for JS Alert'])[1]").click()
time.sleep(5)
driver.switch_to.alert.accept()
result = driver.find_element(By.ID, 'result').text
print("value of attribute is: " +result)
assert "you succesfully  clicked:ok" , result
time.sleep(5)

driver.find_element(By.XPATH,"(//button[normalize-space()='Click for JS Confirm'])[1]").click()
time.sleep(5)
driver.switch_to.alert.accept()
result = driver.find_element(By.ID, 'result').text
print("value of attribute is: " +result)
assert "you clicked:ok" , result
time.sleep(5)

driver.find_element(By.XPATH,"(//button[normalize-space()='Click for JS Confirm'])[1]").click()
time.sleep(5)
driver.switch_to.alert.dismiss()
result = driver.find_element(By.ID, 'result').text
print("value of attribute is: " +result)
assert "you clicked:Cancel" , result
time.sleep(5)
driver.find_element(By.XPATH,"(//button[normalize-space()='Click for JS Prompt'])[1]").click()
time.sleep(5)
driver.switch_to.alert.send_keys('hi,hello!')
driver.switch_to.alert.accept()
result = driver.find_element(By.ID, 'result').text
print("value of attribute is: " +result)
assert "You entered: hi,hello!" , result
time.sleep(5)
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth");
value = driver.find_element(By.XPATH,"//p[contains(text(),'Congratulations! You must have the proper credentials.')]").text
time.sleep(5);
print("value of attribute is: " + value)
assert "Congratulations! You must have the proper credentials.", value