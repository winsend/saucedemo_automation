from utils.locators import InventoryPageLocators


class InventoryPage:

    def __init__(self, driver):
        self.driver = driver

    def add_backpack_to_cart(self):
        self.driver.find_element(
            *InventoryPageLocators.ADD_BACKPACK
        ).click()

    def open_cart(self):
        self.driver.find_element(*InventoryPageLocators.CART_ICON).click()