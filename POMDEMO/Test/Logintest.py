from selenium import webdriver
import time
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__),"..",".."))
from POMDEMO.Pages.Loginpage import LoginPage
from POMDEMO.Pages.HomePage import  HomePage
import HtmlTestRunner


class loginTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path="C:/Users/Sarbajit/PycharmProjects/Selenium/Driver/chromedriver.exe")
        cls.driver.implicitly_wait(10)

    def test_serach_1(self):
        driver = self.driver
        self.driver.get("https://opensource-demo.orangehrmlive.com/")

        login =  LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()

    @ classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("Test completed")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/Sarbajit/PycharmProjects/Selenium/Output'), verbosity=2)
