from pages.inventory_page import InventoryPage
from conftest import *
from time import sleep

# Scenario: opening the inventory page and checking the visibility of all products
def test_visibility_of_product(driver, logged_in):
    driver = logged_in
    sleep(3)
    inventory_page = InventoryPage(driver)
    assert inventory_page.is_loaded()
    # verify if 6 products are visible
    assert inventory_page.get_products_count() == 6
    # verify product names and prices - 1 and 4 products as representative samples
    first_product_name = inventory_page.get_first_product_name()
    assert "Sauce Labs Backpack" in first_product_name
    first_product_price = inventory_page.get_first_product_price()
    assert  "29.99" in first_product_price
    fourth_product_name = inventory_page.get_fourth_product_name()
    assert "Sauce Labs Fleece Jacket" in fourth_product_name
    fourth_product_price = inventory_page.get_fourth_product_price()
    assert "49.99" in fourth_product_price

