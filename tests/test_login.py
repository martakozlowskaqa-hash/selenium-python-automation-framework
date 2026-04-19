from pages.login_page import LoginPage
from utils.test_data import *
from time import sleep

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(VALID_USERNAME, VALID_PASSWORD)
    sleep(6)