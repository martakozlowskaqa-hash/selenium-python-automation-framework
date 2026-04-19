from pages.login_page import LoginPage

def test_valid_login(driver):
    page = LoginPage(driver)
    page.open()