
class LoginPageLocators:
    USERNAME = ("xpath", "//input[@id='user-name']")
    PASSWORD = ("xpath", "//input[@id='password']")
    LOGIN_BUTTON = ("xpath", "//input[@id='login-button']")


class InventoryPageLocators:
    ADD_BACKPACK = ("xpath", "//button[@id='add-to-cart-sauce-labs-backpack']")
    CART_ICON = ("xpath", "//a[@class='shopping_cart_link']")


class CartPageLocators:
    CHECKOUT_BUTTON = ("xpath", "//button[@id='checkout']")


class CheckoutPageLocators:
    FIRST_NAME = ("xpath", "//input[@id='first-name']")
    LAST_NAME = ("xpath", "//input[@id='last-name']")
    POSTAL_CODE = ("xpath", "//input[@id='postal-code']")
    CONTINUE_BUTTON = ("xpath", "//input[@id='continue']")
    FINISH_BUTTON = ("xpath", "//button[@id='finish']")
    SUCCESS_TEXT = ("xpath", "//h2[text()='Thank you for your order!']")