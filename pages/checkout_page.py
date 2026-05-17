from utils.locators import CheckoutPageLocators
from pages.base_page import BasePage

class CheckoutPage(BasePage):

    def fill_information(self, first_name, last_name, postal_code):
        self.type(*CheckoutPageLocators.FIRST_NAME, first_name)
        self.type(*CheckoutPageLocators.LAST_NAME, last_name)
        self.type(*CheckoutPageLocators.POSTAL_CODE, postal_code)

    def continue_checkout(self):
        self.click(*CheckoutPageLocators.CONTINUE_BUTTON)

    def finish_checkout(self):
        self.click(*CheckoutPageLocators.FINISH_BUTTON)

    def get_success_text(self):
        return self.get_text(*CheckoutPageLocators.SUCCESS_TEXT)