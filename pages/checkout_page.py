from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys

class Locators:
    FIRST_NAME = (By.ID, 'first-name')
    LAST_NAME = (By.ID, 'last-name')
    ZIP_CODE = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')

class CheckoutPage(BasePage):
    def is_loaded(self):
        return 'checkout.html' in self.driver.current_url

    def fill_first_name(self, first_name):
        self.driver.find_element(*Locators.FIRST_NAME).send_keys(first_name)

    def fill_last_name(self, last_name):
        self.driver.find_element(*Locators.LAST_NAME).send_keys(last_name)

    def fill_zip_code(self, zip_code):
        self.driver.find_element(*Locators.ZIP_CODE).send_keys(zip_code)

    def click_continue(self):
        self.driver.find_element(*Locators.CONTINUE_BUTTON).click()

