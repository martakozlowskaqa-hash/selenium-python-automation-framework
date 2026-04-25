from conftest import *
from time import sleep
from pages.checkout_page import CheckoutPage

# Scenario: verifying that the correct data entered into the form allows the transaction to be completed
def test_correct_data_flow(driver, proceed_to_checkout_page):
    driver = proceed_to_checkout_page
    checkout_page = CheckoutPage(driver)
    checkout_page.is_loaded()
    assert checkout_page.get_page_header_name() == 'Checkout: Your Information'
    checkout_page.fill_first_name('Marta')
    checkout_page.fill_last_name('Nowak')
    checkout_page.fill_zip_code('77-888')
    sleep(3)
    checkout_page.click_continue()
    assert checkout_page.get_page_header_name() == 'Checkout: Overview'


