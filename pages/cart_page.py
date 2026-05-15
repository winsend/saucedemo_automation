from utils.locators import CartPageLocators
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from utils.locators import LoginPageLocators


class CartPage:
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    def __init__(self, driver):
        self.driver = driver

    def click_checkout(self):
        self.driver.find_element(*CartPageLocators.CHECKOUT_BUTTON).click()