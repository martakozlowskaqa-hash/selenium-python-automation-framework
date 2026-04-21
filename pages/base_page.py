from selenium.webdriver.common.by import By

class Locators:
    CART_COUNTER = (By.CSS_SELECTOR, '.shopping_cart_badge')

# BasePage class for each page
class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_cart_counter(self):
        return self.driver.find_element(*Locators.CART_COUNTER).text

    def nonvisible_cart_counter(self):
        return len(self.driver.find_elements(*Locators.CART_COUNTER)) > 0