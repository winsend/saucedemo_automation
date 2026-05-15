from utils.locators import CheckoutPageLocators
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from utils.locators import LoginPageLocators

class CheckoutPage:
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    
    def __init__(self, driver):
        self.driver = driver

    def fill_information(self, first_name, last_name, postal_code):
        self.driver.find_element(
            *CheckoutPageLocators.FIRST_NAME
        ).send_keys(first_name)

        self.driver.find_element(
            *CheckoutPageLocators.LAST_NAME
        ).send_keys(last_name)

        self.driver.find_element(
            *CheckoutPageLocators.POSTAL_CODE
        ).send_keys(postal_code)

    def continue_checkout(self):
        self.driver.find_element(
            *CheckoutPageLocators.CONTINUE_BUTTON
        ).click()

    def finish_checkout(self):
        self.driver.find_element(
            *CheckoutPageLocators.FINISH_BUTTON
        ).click()

    def get_success_text(self):
        return self.driver.find_element(
            *CheckoutPageLocators.SUCCESS_TEXT
        ).text