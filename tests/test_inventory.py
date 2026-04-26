from pages.inventory_page import InventoryPage
from conftest import *

# Scenario: opening the inventory page and checking the visibility of all products
def test_visibility_of_product(driver, logged_in):
    driver = logged_in
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

# Scenario: verification of the number of 'Add to cart' buttons and their behavior after interaction
def test_add_to_cart_buttons(driver, logged_in):
    driver = logged_in
    inventory_page = InventoryPage(driver)
    assert inventory_page.is_loaded()
    # verify if 6 buttons 'Add to cart' are visible
    assert inventory_page.get_buttons_add_to_cart_count() == 6
    # verifying whether clicking the first 'Add to cart' button adds the product to the cart and changes the button text to 'Remove'
    inventory_page.click_add_to_cart_button_onesie()
    assert inventory_page.get_onesie_remove_button_name() == 'Remove'
    assert inventory_page.get_cart_counter() == '1'
    inventory_page.click_remove_button_onesie()
    assert inventory_page.get_onesie_add_button_name() == 'Add to cart'
    assert not inventory_page.nonvisible_cart_counter()