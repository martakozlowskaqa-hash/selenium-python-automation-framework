from pages.login_page import LoginPage
from utils.test_data import *
from pages.inventory_page import InventoryPage

# Scenario: automated test for valid user login
def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    inventory_page = InventoryPage(driver)
    assert inventory_page.is_loaded()

# Scenario: automated test for invalid user login
def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(INVALID_USERNAME, INVALID_PASSWORD)
    error_text = login_page.get_error_message()
    assert LOGIN_INVALID_ERROR in error_text
    assert "inventory.html" not in driver.current_url

# Scenario: automated test for lockedout data user login
def test_lockedout_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(LOCKEDOUT_USERNAME, LOCKEDOUT_PASSWORD)
    error_text = login_page.get_error_message()
    assert LOGIN_LOCKED_ERROR in error_text
    assert "inventory.html" not in driver.current_url