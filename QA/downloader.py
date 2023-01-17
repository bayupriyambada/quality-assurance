import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

baseUrl = "https://demoqa.com/"
driverInstall = ChromeDriverManager().install()


class TestLogin(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.browser = webdriver.Chrome(options=options, service=Service(
            driverInstall))
        self.browser.maximize_window()

    def test_success_link(self):
        # steps
        browser = self.browser
        browser.get(baseUrl + "upload-download")
        time.sleep(3)
        browser.find_element(By.ID, "downloadButton").click()
        time.sleep(10)

    def tearDown(self):
        self.browser.close()


if __name__ == "__main__":
    unittest.main()
