from pages.base_page import BasePage
from selenium.webdriver.common.by import By

# from pages.inventory_page import InventoryPage


class Locators:
    CART_ICON_BUTTON = (By.CSS_SELECTOR, '.shopping_cart_link')
    CART_PRODUCT_COUNT = (By.CLASS_NAME, 'cart_item')
    CART_PRODUCT_NAMES = (By.CLASS_NAME, 'inventory_item_name')
    CART_PRODUCT_PRICE = (By.CLASS_NAME, 'inventory_item_price')
    CONTINUE_SHOPPING_BUTTON = (By.ID, 'continue-shopping')
    REMOVE_BACKPACK_BUTTON = (By.ID, 'remove-sauce-labs-backpack')

class CartPage(BasePage):
    def is_loaded(self):
        return 'cart.html' in self.driver.current_url

    def open_cart(self):
        self.driver.find_element(*Locators.CART_ICON_BUTTON).click()

    def get_cart_product_count(self):
        return len(self.driver.find_elements(*Locators.CART_PRODUCT_COUNT))

    def get_cart_product_names(self):
        elements = self.driver.find_elements(*Locators.CART_PRODUCT_NAMES)
        return [element.text for element in elements]

    def visible_product_in_cart(self, product_name):
        return product_name in self.get_cart_product_names()

    def get_cart_product_price(self):
        elements = self.driver.find_elements(*Locators.CART_PRODUCT_PRICE)
        return [element.text for element in elements]

    def visible_prices_in_cart(self,price):
        return price in self.get_cart_product_price()

    def click_continue_shopping_button(self):
        from pages.inventory_page import InventoryPage
        self.driver.find_element(*Locators.CONTINUE_SHOPPING_BUTTON).click()
        return InventoryPage(self.driver)

    def click_remove_backpack_button(self):
        self.driver.find_element(*Locators.REMOVE_BACKPACK_BUTTON).click()


