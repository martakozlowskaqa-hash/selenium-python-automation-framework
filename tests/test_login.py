from pages.login_page import LoginPage
from utils.test_data import *
from time import sleep
from pages.inventory_page import InventoryPage

# Scenario: automated test for valid user login
def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    sleep(3)
    inventory_page = InventoryPage(driver)
    assert inventory_page.is_loaded()

# Scenario: automated test for invalid user login
def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(INVALID_USERNAME, INVALID_PASSWORD)
    sleep(3)
    error_text = login_page.get_error_message()
    assert "Epic sadface: Username and password do not match any user in this service" in error_text