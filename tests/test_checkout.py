from conftest import *
from time import sleep
from pages.checkout_page import CheckoutPage

# Scenario: verifying that the correct data entered into the form allows the transaction to be completed
def test_correct_data_flow(driver, proceed_to_checkout_page):
    driver = proceed_to_checkout_page
    checkout_page = CheckoutPage(driver)
    checkout_page.is_loaded()
    assert checkout_page.get_page_header_name() == 'Checkout: Your Information'
    # fill in form with correct data
    checkout_page.fill_first_name('Marta')
    checkout_page.fill_last_name('Nowak')
    checkout_page.fill_zip_code('77-888')
    sleep(3)
    checkout_page.click_continue()
    assert checkout_page.get_page_header_name() == 'Checkout: Overview'
    sleep(4)
    # order confirmation
    assert checkout_page.get_total_price() == "$32.39"
    checkout_page.click_finish_button()
    assert checkout_page.get_page_header_name() == 'Checkout: Complete!'
    # verify finish message
    assert checkout_page.get_finish_message() == 'Thank you for your order!'

# Scenario: verify that the system does not allow the transaction to be completed if incomplete data is entered into the form (no first name)
def test_missing_first_name_flow(driver, proceed_to_checkout_page):
    driver = proceed_to_checkout_page
    checkout_page = CheckoutPage(driver)
    checkout_page.is_loaded()
    assert checkout_page.get_page_header_name() == 'Checkout: Your Information'
    # fill in form with correct data
    checkout_page.fill_last_name('Nowak')
    checkout_page.fill_zip_code('77-888')
    sleep(3)
    checkout_page.click_continue()
    # verification of the error message - First Name is required
    assert checkout_page.get_error_checkout_form_message() == 'Error: First Name is required'

# Scenario: verify that the system does not allow the transaction to be completed if incomplete data is entered into the form (no last name)
def test_missing_last_name_flow(driver, proceed_to_checkout_page):
    driver = proceed_to_checkout_page
    checkout_page = CheckoutPage(driver)
    checkout_page.is_loaded()
    assert checkout_page.get_page_header_name() == 'Checkout: Your Information'
    # fill in form with correct data
    checkout_page.fill_first_name('Marta')
    checkout_page.fill_zip_code('77-888')
    sleep(3)
    checkout_page.click_continue()
    # verification of the error message - Last Name is required
    assert checkout_page.get_error_checkout_form_message() == 'Error: Last Name is required'

# Scenario: verify that the system does not allow the transaction to be completed if incomplete data is entered into the form (e.g., no first name)verify that the system does not allow the transaction to be completed if incomplete data is entered into the form (no zip code)
def test_missing_zip_code_flow(driver, proceed_to_checkout_page):
    driver = proceed_to_checkout_page
    checkout_page = CheckoutPage(driver)
    checkout_page.is_loaded()
    assert checkout_page.get_page_header_name() == 'Checkout: Your Information'
    # fill in form with correct data
    checkout_page.fill_first_name('Marta')
    checkout_page.fill_last_name('Nowak')
    sleep(3)
    checkout_page.click_continue()
    # verification of the error message - Postal Code is required
    assert checkout_page.get_error_checkout_form_message() == 'Error: Postal Code is required'