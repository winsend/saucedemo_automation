from pages.base_page import BasePage
from utils.locators import InventoryPageLocators


class InventoryPage(BasePage):

    def add_backpack_to_cart(self):
        self.click(InventoryPageLocators.ADD_BACKPACK)

    def open_cart(self):
        self.click(InventoryPageLocators.CART_ICON)