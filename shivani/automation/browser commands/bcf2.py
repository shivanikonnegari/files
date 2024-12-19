from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://demo.opencart.com/")
page_title = driver.title
title_length = len(page_title)
print(f"Page Title: {page_title}")
print(f"Title Length: {title_length}")

current_url = driver.current_url
if current_url == "https://demo.opencart.com/":
    print("URL is correct.")
else:
    print("URL is incorrect.")

page_source = driver.page_source
source_length = len(page_source)

print(f"Page Source Length: {source_length}")
driver.quit()