from pages.base_page import BasePage

# InventoryPage class and the functions used in the tests
class InventoryPage(BasePage):
    def is_loaded(self):
        return "inventory.html" in self.driver.current_url