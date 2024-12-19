from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.letskodeit.com/practice")
time.sleep(5)
bmwRadioBtn = driver.find_element(By.ID,"bmwradio")
bmwRadioBtn.click()
time.sleep(5)
benzRadioBtn = driver.find_element(By.ID,"benzradio")
benzRadioBtn.click()
time.sleep(5)
hondaRadioBtn = driver.find_element(By.ID,"hondaradio")
hondaRadioBtn.click()
radio_buttons =driver.find_elements(By.XPATH,"//div[@class='col-md-12']//a")
print(len(radio_buttons))
time.sleep(5)
bmwcheckbox = driver.find_element(By.ID,"bmwcheck")
bmwcheckbox.click()
benzcheckbox = driver.find_element(By.ID,"benzcheck")
benzcheckbox.click()
time.sleep(5)
hondaCheckbox = driver.find_element(By.ID,"hondacheck")
hondaCheckbox.click()
time.sleep(5)

check_boxes =driver.find_elements(By.XPATH,"//div[@class='col-md-12']//a")
print(len(check_boxes))
time.sleep(5)
element = driver.find_element(By.ID,"mousehover")
driver.execute_script("arguments[0].scrollIntoView(true);", element)
time.sleep(5)
driver.execute_script("window.scrollBy(0,-150);")
time.sleep(5)
driver.refresh()
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='name']").send_keys("selenium python")
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='alertbtn']").click()
driver.switch_to.alert.accept()
driver.save_screenshot(".// ok screenshots.png")
driver.find_element(By.XPATH,'//*[@id="confirmbtn"]').click()
driver.switch_to.alert.accept()
driver.save_screenshot(".//confirm screenshots.png")
page_title = driver.title
print(f"Page Title: {page_title}")
page_source = driver.page_source
print(f"Page Source : {page_source}")
actual_title = driver.title
expected_title = "Practice Page"
if actual_title == expected_title:
    print("title matched")
else:
    print("title not matched")
time.sleep(5)
driver.find_element(By.XPATH, '//*[@id="navbar-inverse-collapse"]/div/div/a').click()
driver.back()
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='navbar-inverse-collapse']/div/div/a").click()
time.sleep(5)
text_box=driver.find_element(By.ID,"email")
text_box.send_keys("konnegarishivani03@gmail.com")
text_box=driver.find_element(By.NAME, "password")
text_box.send_keys("Shiv@ni032002")
driver.find_element(By.XPATH,"//button[@id='login']").click()
driver.save_screenshot(".// login screenshots.png")
time.sleep(5)
driver.quit()




