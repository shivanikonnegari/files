import time
from unittest import TestCase

from selenium import webdriver
import unittest
from Login_Page import LoginPage

class LoginTests(unittest.TestCase):

    def test_validateLogin(self):
        driver = webdriver.Chrome()
        driver.get("https://auth.hollandandbarrett.com/u/login")

        driver.maximize_window()
        time.sleep(5)

        lp = LoginPage(driver)
        lp.login( "shivanireddykonnegari@gmail.com", "Shiv@ni032002")

        actual_title = driver.title
        expect_title = "Sign in - to your account, for the best experience"

        if actual_title == expect_title:
            print("Login is succesful ...... well done python")

        else:
            print("Login Unsuccesful ..... very good my boy")