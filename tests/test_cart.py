from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from conftest import *
from time import sleep

# Scenario: verifying correct addition and removal of a single item - cart page
def test_cart_add_and_remove_items_flow(driver, logged_in, add_one_item_to_card):
    driver = add_one_item_to_card
    inventory_page = InventoryPage(driver)
    cart_page = inventory_page.go_to_cart_page()
    sleep(2)
    # checking that the shopping cart title, one item, and its name and price are visible
    assert cart_page.get_page_header_name() == 'Your Cart'
    assert cart_page.get_cart_counter() == '1'
    assert cart_page.get_cart_product_count() == 1
    assert cart_page.visible_product_in_cart('Sauce Labs Backpack')
    assert cart_page.visible_prices_in_cart('$29.99')
    # checking that returning to the inventory and reopening the shopping cart does not affect its contents
    cart_page.click_continue_shopping_button()
    sleep(2)
    assert cart_page.get_page_header_name() == 'Products'
    cart_page = inventory_page.go_to_cart_page()
    sleep(2)
    assert cart_page.get_page_header_name() == 'Your Cart'
    assert cart_page.get_cart_counter() == '1'
    assert cart_page.get_cart_product_count() == 1
    assert cart_page.visible_product_in_cart('Sauce Labs Backpack')
    assert cart_page.visible_prices_in_cart('$29.99')
    # verification of product removal from the shopping cart
    pass

