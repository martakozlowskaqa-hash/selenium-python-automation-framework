from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# locators used in testing
class Locators:
    CART_COUNTER = (By.CSS_SELECTOR, '.shopping_cart_badge')
    PAGE_HEADER = (By.CSS_SELECTOR, '.title')

# BasePage class for each page
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_cart_counter(self):
        return self.driver.find_element(*Locators.CART_COUNTER).text

    def nonvisible_cart_counter(self):
        return len(self.driver.find_elements(*Locators.CART_COUNTER)) > 0

    def get_page_header_name(self):
        return self.driver.find_element(*Locators.PAGE_HEADER).text

    def wait_for_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_for_presence(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
