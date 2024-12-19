from behave import *
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

@given('User should open Edge browser')
def LaunchBrowser(context):
    context.driver =webdriver.Edge()


@when('User should Enter Url in Browser')
def EnterURL(context):
    context.driver.get("https://www.hollandandbarrett.com/")
    context.driver.maximize_window()


@when('User should Navigate Login Page')
def LoginPage(context):
    context.driver.get("https://auth.hollandandbarrett.com/u/login")
    time.sleep(3)


@when('Enter UserName and Password in Edit Box')
def EneterValues(context):
    context.driver.find_element(By.ID,"username").send_keys("shivanireddykonnegari@gmail.com")
    context.driver.find_element(By.NAME,"password").send_keys("Shiv@ni032002")



@when('Click on Login Button')
def ClickSignButton(context):
    context.driver.implicitly_wait(5)
    context.driver.find_element(By.XPATH,"//button[normalize-space()='Sign In']").click()



@then('Message displayed Login Successfully')
def step_impl(context):
    status=context.driver.title
    expect_title ="Sign in - to your account, for the best experience"
    assert status == expect_title


@then('User should Close Browser')
def CloseBrowser(context):
    context.driver.quit()
