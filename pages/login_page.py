from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.inventory_page import InventoryPage

# declare base url - test environment
BASE_URL = "https://www.saucedemo.com/"

# locators used in testing
class Locators:

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message-container.error")

# LoginPage class and the functions used in the tests
class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open(self):
        self.driver.get(BASE_URL)

    def login(self, username, password):
        self.driver.find_element(*Locators.USERNAME_INPUT).send_keys(username)
        self.driver.find_element(*Locators.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*Locators.LOGIN_BUTTON).click()
        return InventoryPage(self.driver)

    def get_error_message(self):
        return self.driver.find_element(*Locators.ERROR_MESSAGE).text