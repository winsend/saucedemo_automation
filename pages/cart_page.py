from utils.locators import CartPageLocators
from pages.base_page import BasePage

class CartPage(BasePage):

    def click_checkout(self):
        self.click(*CartPageLocators.CHECKOUT_BUTTON)