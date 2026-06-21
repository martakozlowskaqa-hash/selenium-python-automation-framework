from conftest import *
from pages.checkout_page import CheckoutPage
from faker import Faker
from utils.test_data import *

faker = Faker()

# Scenario: verifying that the correct data entered into the form allows the transaction to be completed
def test_correct_data_flow(driver, proceed_to_checkout_page):
    driver = proceed_to_checkout_page
    checkout_page = CheckoutPage(driver)
    checkout_page.is_loaded()
    assert checkout_page.get_page_header_name() == 'Checkout: Your Information'
    # fill in form with correct data
    checkout_page.fill_first_name(faker.first_name())
    checkout_page.fill_last_name(faker.last_name())
    checkout_page.fill_zip_code(faker.postcode())
    checkout_page.click_continue()
    assert checkout_page.get_page_header_name() == 'Checkout: Overview'
    # order confirmation
    assert checkout_page.get_total_price() == CHECKOUT_TOTAL
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
    checkout_page.fill_last_name(faker.last_name())
    checkout_page.fill_zip_code(faker.postcode())
    checkout_page.click_continue()
    # verification of the error message - First Name is required
    assert checkout_page.get_error_checkout_form_message() == CHECKOUT_FIRSTNAME_ERROR

# Scenario: verify that the system does not allow the transaction to be completed if incomplete data is entered into the form (no last name)
def test_missing_last_name_flow(driver, proceed_to_checkout_page):
    driver = proceed_to_checkout_page
    checkout_page = CheckoutPage(driver)
    checkout_page.is_loaded()
    assert checkout_page.get_page_header_name() == 'Checkout: Your Information'
    # fill in form with correct data
    checkout_page.fill_first_name(faker.first_name())
    checkout_page.fill_zip_code(faker.postcode())
    checkout_page.click_continue()
    # verification of the error message - Last Name is required
    assert checkout_page.get_error_checkout_form_message() == CHECKOUT_LASTNAME_ERROR

# Scenario: verify that the system does not allow the transaction to be completed if incomplete data is entered into the form (e.g., no first name)verify that the system does not allow the transaction to be completed if incomplete data is entered into the form (no zip code)
def test_missing_zip_code_flow(driver, proceed_to_checkout_page):
    driver = proceed_to_checkout_page
    checkout_page = CheckoutPage(driver)
    checkout_page.is_loaded()
    assert checkout_page.get_page_header_name() == 'Checkout: Your Information'
    # fill in form with correct data
    checkout_page.fill_first_name(faker.first_name())
    checkout_page.fill_last_name(faker.last_name())
    checkout_page.click_continue()
    # verification of the error message - Postal Code is required
    assert checkout_page.get_error_checkout_form_message() == CHECKOUT_ZIPCODE_ERROR