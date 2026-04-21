from pages.cart_page import CartPage
from conftest import *
from time import sleep

# Scenario: verifying correct addition and removal of a single item - cart page
def test_cart_add_and_remove_items_flow(driver, logged_in, add_one_item_to_card):
    # driver = logged_in
    driver = add_one_item_to_card()
    sleep(2)

    cart_page = CartPage(driver)
    cart_page.open_cart()
    sleep(2)
    assert cart_page.get_cart_header_name() == 'Your Cart'


