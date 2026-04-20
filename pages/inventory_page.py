from pages.base_page import BasePage
from selenium.webdriver.common.by import By

# locators used in testing
class Locators:
    INVENTORY_PRODUCTS = (By.CLASS_NAME, 'inventory_item')
    NAME_FIRST_PRODUCT = (By.XPATH, "(//*[@data-test='inventory-item-name'])[1]")
    PRICE_FIRST_PRODUCT = (By.XPATH, "(//*[@data-test='inventory-item-price'])[1]")
    NAME_FOURTH_PRODUCT = (By.XPATH, "(//*[@data-test='inventory-item-name'])[4]")
    PRICE_FOURTH_PRODUCT = (By.XPATH, "(//*[@data-test='inventory-item-price'])[4]")
    ADD_TO_CART_BUTTONS = (By.XPATH, "//button[text()='Add to cart']")
    ONESIE_ADD_TO_CART_BUTTON = (By.ID, 'add-to-cart-sauce-labs-onesie')
    ONESIE_REMOVE_BUTTON = (By.ID, 'remove-sauce-labs-onesie')
    CART_COUNTER = (By.CSS_SELECTOR, '.shopping_cart_badge')

# InventoryPage class and the functions used in the tests
class InventoryPage(BasePage):
    def is_loaded(self):
        return 'inventory.html' in self.driver.current_url

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

    def get_buttons_add_to_cart_count(self):
        return len(self.driver.find_elements(*Locators.ADD_TO_CART_BUTTONS))

    def click_add_to_cart_button_onesie(self):
        return self.driver.find_element(*Locators.ONESIE_ADD_TO_CART_BUTTON).click()

    def get_onesie_remove_button_name(self):
        return self.driver.find_element(*Locators.ONESIE_REMOVE_BUTTON).text

    def get_cart_counter(self):
        return self.driver.find_element(*Locators.CART_COUNTER).text

    def click_remove_button_onesie(self):
        return self.driver.find_element(*Locators.ONESIE_REMOVE_BUTTON).click()

    def nonvisible_cart_counter(self):
        return len(self.driver.find_elements(*Locators.CART_COUNTER)) > 0

    def get_onesie_add_button_name(self):
        return self.driver.find_element(*Locators.ONESIE_ADD_TO_CART_BUTTON).text