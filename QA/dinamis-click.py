import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options=options, service=Service(
#     ChromeDriverManager().install()))
# driver.maximize_window()
# driver.get("https://www.saucedemo.com/")
# driver.find_element(
#     By.NAME, "user-name").send_keys("standard_user")
# time.sleep(1)
# driver.find_element(
#     By.NAME, "password").send_keys("secret_sauce")
# time.sleep(1)
# driver.find_element(By.ID, "login-button").click()
# # driver.close()


class TestLogin(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(options=options, service=Service(
            ChromeDriverManager().install()))
        self.browser.maximize_window()

    def test_success_login(self):
        # steps
        browser = self.browser
        browser.get("https://www.saucedemo.com/")  # buka situs
        time.sleep(3)
        browser.find_element(
            By.NAME, "user-name").send_keys("standard_user")
        time.sleep(1)
        browser.find_element(
            By.NAME, "password").send_keys("secret_sauce")
        time.sleep(1)
        browser.find_element(By.ID, "login-button").click()
        time.sleep(1)


if __name__ == "__main__":
    unittest.main()
