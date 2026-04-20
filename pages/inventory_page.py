from pages.base_page import BasePage
from selenium.webdriver.common.by import By

# locators used in testing
class Locators:
    INVENTORY_PRODUCTS = (By.CLASS_NAME, "inventory_item")
    NAME_FIRST_PRODUCT = (By.XPATH, "(//*[@data-test='inventory-item-name'])[1]")
    PRICE_FIRST_PRODUCT = (By.XPATH, "(//*[@data-test='inventory-item-price'])[1]")
    NAME_FOURTH_PRODUCT = (By.XPATH, "(//*[@data-test='inventory-item-name'])[4]")
    PRICE_FOURTH_PRODUCT = (By.XPATH, "(//*[@data-test='inventory-item-price'])[4]")

# InventoryPage class and the functions used in the tests
class InventoryPage(BasePage):
    def is_loaded(self):
        return "inventory.html" in self.driver.current_url

    def get_products_count(self):
        return len(self.driver.find_elements(*Locators.INVENTORY_PRODUCTS))

    def get_first_product_name(self):
        return self.driver.find_element(*Locators.NAME_FIRST_PRODUCT).text

    def get_first_product_price(self):
        return self.driver.find_element(*Locators.PRICE_FIRST_PRODUCT).text

    def get_fourth_product_name(self):
        return self.driver.find_element(*Locators.NAME_FOURTH_PRODUCT).text

    def get_fourth_product_price(self):
        return self.driver.find_element(*Locators.PRICE_FOURTH_PRODUCT).text