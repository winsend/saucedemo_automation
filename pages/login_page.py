from pages.base_page import BasePage
from utils.locators import LoginPageLocators

class LoginPage(BasePage):

    URL = "https://www.saucedemo.com/"

    def open_login_page(self):
        self.open(self.URL)

    def login(self, username, password):
        self.type(LoginPageLocators.USERNAME, username)
        self.type(LoginPageLocators.PASSWORD, password)
        self.click(LoginPageLocators.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(LoginPageLocators.ERROR_MESSAGE)