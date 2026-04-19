from selenium.webdriver.common.by import By

class BasePage:
    """
    Base Page object for each page
    """
    def __init__(self, driver):
        self.driver = driver