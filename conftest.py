import pytest
from selenium import webdriver
from pages.login_page import LoginPage

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