from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class Locators:
    pass

class CartPage(BasePage):
    def is_loaded(self):
        return 'cart.html' in self.driver.current_url