import pytest
from selenium import webdriver

from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

# decorators that provide predictable pre-conditions
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def logged_in(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    return driver

@pytest.fixture
def add_one_item_to_card(driver, logged_in):
    inventory_page = InventoryPage(driver)
    inventory_page.click_add_to_cart_button_backpack()
    return driver

@pytest.fixture
def add_multiple_items_to_cart(driver, logged_in):
    inventory_page = InventoryPage(driver)
    inventory_page.click_add_to_cart_button_backpack()
    inventory_page.click_add_to_cart_button_onesie()
    return driver

@pytest.fixture
def checkout_page(logged_in):
    driver = logged_in
    inventory_page = InventoryPage(driver)
    inventory_page.click_add_to_cart_button_backpack()
    inventory_page.go_to_cart_page()
    cart_page = CartPage(driver)
    cart_page.click_checkout_button()
    return driver