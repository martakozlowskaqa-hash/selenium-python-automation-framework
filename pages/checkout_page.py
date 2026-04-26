from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys

# locators used in testing
class Locators:
    FIRST_NAME = (By.ID, 'first-name')
    LAST_NAME = (By.ID, 'last-name')
    ZIP_CODE = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')
    TOTAL_PRICE = (By.CSS_SELECTOR, "[data-test='total-label']")
    FINISH_BUTTON = (By.ID, 'finish')
    COMPLETE_MESSAGE = (By.CLASS_NAME, 'complete-header')
    CHECKOUT_ERROR_MESSAGE = (By.CSS_SELECTOR, '.error-message-container.error')

# CheckoutPage class and the functions used in the tests
class CheckoutPage(BasePage):
    def is_loaded(self):
        return 'checkout.html' in self.driver.current_url

    def fill_first_name(self, first_name):
        self.wait_for_visible(Locators.FIRST_NAME).send_keys(first_name)

    def fill_last_name(self, last_name):
        self.wait_for_visible(Locators.LAST_NAME).send_keys(last_name)

    def fill_zip_code(self, zip_code):
        self.wait_for_visible(Locators.ZIP_CODE).send_keys(zip_code)

    def click_continue(self):
        self.wait_for_clickable(Locators.CONTINUE_BUTTON).click()

    def get_total_price(self):
        text = self.wait_for_visible(Locators.TOTAL_PRICE).text
        return text.replace("Total: ", "")

    def click_finish_button(self):
        self.wait_for_clickable(Locators.FINISH_BUTTON).click()

    def get_finish_message(self):
        return self.wait_for_visible(Locators.COMPLETE_MESSAGE).text

    def get_error_checkout_form_message(self):
        return self.wait_for_visible(Locators.CHECKOUT_ERROR_MESSAGE).text