from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
    def open(self):
        self.driver.get("https://www.saucedemo.com/")