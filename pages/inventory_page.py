from utils.locators import InventoryPageLocators
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from utils.locators import LoginPageLocators


class InventoryPage:
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    def __init__(self, driver):
        self.driver = driver

    def add_backpack_to_cart(self):
        self.driver.find_element(
            *InventoryPageLocators.ADD_BACKPACK
        ).click()

    def open_cart(self):
        self.driver.find_element(*InventoryPageLocators.CART_ICON).click()