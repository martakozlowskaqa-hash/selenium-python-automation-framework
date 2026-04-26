from selenium import webdriver

class DriverSetup:

    @staticmethod
    def get_driver(browser_name):

        if browser_name == 'chrome':
            driver = webdriver.Chrome()

        elif browser_name == 'firefox':
            driver = webdriver.Firefox()

        else:
            raise ValueError('Unsupported browser')

        driver.maximize_window()
        return driver