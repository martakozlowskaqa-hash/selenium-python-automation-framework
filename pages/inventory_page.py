from pages.base_page import BasePage


class InventoryPage(BasePage):

    def is_loaded(self):
        return "inventory.html" in self.driver.current_url