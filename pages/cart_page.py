from utils.locators import CartPageLocators

class CartPage:


    def __init__(self, driver):
        self.driver = driver

    def click_checkout(self):
        self.driver.find_element(*CartPageLocators.CHECKOUT_BUTTON).click()