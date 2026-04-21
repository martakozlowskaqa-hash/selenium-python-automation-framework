from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class Locators:
    CART_ICON_BUTTON = (By.CSS_SELECTOR, '.shopping_cart_link')
    CART_HEADER = (By.CSS_SELECTOR, '.title')


class CartPage(BasePage):
    def is_loaded(self):
        return 'cart.html' in self.driver.current_url

    def open_cart(self):
        self.driver.find_element(*Locators.CART_ICON_BUTTON).click()

    def get_cart_header_name(self):
        return self.driver.find_element(*Locators.CART_HEADER).text
