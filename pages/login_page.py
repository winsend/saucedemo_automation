
from utils.locators import LoginPageLocators

class LoginPage:

    URL = "https://www.saucedemo.com/"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.driver.find_element(*LoginPageLocators.USERNAME).send_keys(username)
        self.driver.find_element(*LoginPageLocators.PASSWORD).send_keys(password)
        self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()